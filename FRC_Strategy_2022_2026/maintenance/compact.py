from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from PIL import Image
import base64,io,json
r=Path(__file__).resolve().parent
base=r.parent/'FRC_Strategy_2022_2026_Database/FRC_Strategy_2022_2026'
records=[json.loads(l) for l in (base/'data/mechanism_images.jsonl').read_text().splitlines()]
def compact(im):
    p=base/im['path']
    if not p.exists():return None
    pic=Image.open(p).convert('RGB')
    pic.thumbnail((1350,1350))
    stream=io.BytesIO()
    pic.save(stream,format='WEBP',quality=76,method=4)
    return im['id'],dict(mime='image/webp',base64=base64.b64encode(stream.getvalue()).decode())
with ThreadPoolExecutor(8) as pool:
    data=dict(v for v in pool.map(compact,records) if v)
p=r/'asset_cache.json'
p.write_text(json.dumps(data,separators=(',',':')))
print(len(data),p.stat().st_size)
