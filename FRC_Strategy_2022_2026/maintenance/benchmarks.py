from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import collections, hashlib, json, math, statistics, urllib.request

BASE = 'https://api.statbotics.io/v3'
CACHE = Path(__file__).parent / 'event_cache'
CACHE.mkdir(exist_ok=True)
YEARS = (2018, 2019, 2022, 2023, 2024, 2025, 2026)
TYPES = {'regional', 'district', 'district_cmp', 'district_cmp_div', 'champs_div', 'champs', 'einstein'}

def fetch(path):
    url = BASE + path
    local = CACHE / (hashlib.sha256(url.encode()).hexdigest() + '.json')
    if not local.exists():
        for attempt in range(3):
            try:
                raw = urllib.request.urlopen(url, timeout=25).read()
                json.loads(raw)
                local.write_bytes(raw)
                break
            except Exception:
                if attempt == 2:
                    raise
    raw = local.read_bytes()
    return json.loads(raw), hashlib.sha256(raw).hexdigest()

def select(year):
    events, digest = fetch(f'/events?year={year}&limit=1000')
    groups = collections.defaultdict(list)
    selected = set()
    for event in events:
        kind = event['type']
        if kind not in TYPES or event['status'] != 'Completed':
            continue
        key = event['key']
        groups[(kind, event['week'])].append(key)
        if event.get('district') == 'pch' or kind in {'champs_div','champs','einstein'}:
            selected.add(key)
    for group in groups.values():
        selected.update((min(group), max(group)))
    return sorted(selected)

def dist(values):
    v = sorted(x for x in values if type(x) in (int,float) and math.isfinite(x))
    def quantile(q):
        if not v: return None
        k = (len(v)-1)*q
        j = int(k)
        return round(v[j]+(v[math.ceil(k)]-v[j])*(k-j),3)
    return dict(n=len(v),min=quantile(0),p25=quantile(.25),median=quantile(.5),p75=quantile(.75),p90=quantile(.9),p95=quantile(.95),max=quantile(1))

def event(key):
    bundle, digest = fetch('/site/event/'+key)
    e = bundle['event']
    row = {k:e.get(k) for k in ['year','name','type','week','start_date','end_date']}
    row.update(event=key, source_url='https://www.statbotics.io/event/'+key, data_url=BASE+'/site/event/'+key, tba_url='https://www.thebluealliance.com/event/'+key, response_sha256=digest, alliance_populations={})
    matches = [m for m in bundle['matches'] if m.get('status')=='Completed']
    for stage in ('qualification','playoff'):
        sample = [m for m in matches if bool(m.get('elim'))==(stage=='playoff')]
        rows, dq, missing = [], 0, 0
        for m in sample:
            for c in ('red','blue'):
                if m['alliances'][c].get('dq_team_keys'):
                    dq += 1
                    continue
                scores = {k[len(c)+1:]:v for k,v in (m.get('result') or {}).items() if k.startswith(c+'_') and type(v) in (int,float,bool)}
                clean = scores.get('no_foul')
                if type(clean) not in (int,float) or not math.isfinite(clean) or clean<0:
                    missing += 1
                    continue
                rows.append(scores)
        fields = sorted(set().union(*(r.keys() for r in rows)))
        rp = [k for k in fields if k.endswith('_rp') or k.startswith('rp_')]
        row['alliance_populations'][stage] = dict(completed_matches=len(sample),alliance_observations=len(rows),excluded_dq=dq,missing_score=missing, metrics={k:dist(r.get(k) for r in rows) for k in fields if k not in rp}, ranking_points={k:dict(observed=sum(type(r.get(k)) is bool for r in rows),achieved=sum(r.get(k) is True for r in rows)) for k in rp})
    epa = [t.get('epa',{}) for t in bundle['team_events']]
    start = [t.get('stats',{}).get('pre_elim') for t in epa]
    valid = sorted((n for n in start if type(n) in (float,int)),reverse=True)
    row.update(individual_epa=dict(pre_elimination=dist(start),event_end=dist(t.get('total_points') for t in epa)),pre_elim_epa_8th=valid[7] if len(valid)>7 else None,pre_elim_epa_top=valid[0] if valid else None)
    row['notes'] = 'Clean score uses the source no_foul field. EPA is an individual model estimate. Qualification and playoff populations are separate. 2019 auto points represent Sandstorm. 2026 endgame points include late fuel, so use the tower field for climbing.'
    return row

def work(key):
    try: return event(key)
    except Exception as exc:
        print(key,str(exc),flush=True)
        return None

if __name__=='__main__':
    with ThreadPoolExecutor(8) as pool:
        keys = sorted(set().union(*pool.map(select,YEARS)))
        out = Path(__file__).parent/'benchmarks.jsonl'
        with out.open('w') as f:
            for row in pool.map(work,keys):
                if row:
                    f.write(json.dumps(row,separators=(',',':'))+'\n')
                    f.flush()
    print('Selected',len(keys),'written',len(out.read_text().splitlines()),flush=True)
