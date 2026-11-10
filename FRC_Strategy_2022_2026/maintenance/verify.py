"""Check the delivered index can restore its full corpus and preserve source coverage."""
from pathlib import Path
import json
import sqlite3
import subprocess
import sys
import tempfile

from launcher import restore

target = Path(__file__).resolve().parent.parent/'delivery/index.html'
with tempfile.TemporaryDirectory(prefix='workbench-check-') as path:
    root = restore(target, Path(path))
    coverage = json.loads((root/'data/dossier_review_coverage.json').read_text())
    reviews = {
        row['robot_id']: row
        for row in map(json.loads, (root/'data/dossier_research_reviews.jsonl').read_text().splitlines())
    }
    assert len(reviews) == coverage['reviewed']
    assert len(coverage['pending']) + len(reviews) == coverage['roster'] == 143
    assert not set(reviews) & set(coverage['pending'])
    assert len(list((root/'agent/robot_packets').glob('*.json'))) == 143
    for rid, review in reviews.items():
        packet = json.loads((root/'agent/robot_packets'/f'{rid}.json').read_text())
        assert packet['source_review'] == review
    with sqlite3.connect(root/'agent/retrieval.sqlite') as index:
        count = index.execute("select count(*) from units where kind='dossier_review'").fetchone()[0]
        assert count == len(reviews)
        count = index.execute("select count(*) from units where kind='reviewed_subsystem'").fetchone()[0]
        assert count == sum(len(row['subsystems']) for row in reviews.values())
        count = index.execute("select count(*) from units where kind='event_benchmark'").fetchone()[0]
        assert count == 292
        assert index.execute("select count(*) from units where id='image:7bc3e516e03f77f970'").fetchone()[0] == 0
    check = subprocess.check_output([sys.executable, str(root/'workbench/research.py'),
                                    'packet','2018-254','--section','source_review'],text=True)
    assert json.loads(check)['robot_id'] == '2018-254'
    print(f"PASS: restored {len(reviews)} reviews, 143 robot packets, 292 event benchmarks")
