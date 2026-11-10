"""Retrieve candidate publisher thumbnails for otherwise unillustrated dossiers."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from PIL import Image, ImageDraw
import urllib.request, re, json, base64, io

R=Path(__file__).resolve().parent
corpus=R.parent/'FRC_Strategy_2022_2026_Database/FRC_Strategy_2022_2026'
original=[json.loads(l) for l in (corpus/'data/mechanism_images.jsonl').read_text().splitlines()]
skip={17,18,29,43,75,79,80,100,101,106,115,129,136,137,138,140,222,281,330,331,332,335,339,364,389,395,396,407,416,445,515,563,*range(576,597)}
illustrated={im['robot_id'] for n,im in enumerate(original) if n not in skip}
robots=[json.loads(l) for l in (corpus/'data/robot_dossiers.jsonl').read_text().splitlines()]
def download(r):
    for u in r['primary']:
        m=re.search(r'(?:youtu\.be/|[?&]v=)([A-Za-z0-9_-]{11})',u)
        if not m:continue
        for variant in ['maxresdefault','hqdefault']:
            url=f'https://i.ytimg.com/vi/{m[1]}/{variant}.jpg'
            try:
                raw=urllib.request.urlopen(url,timeout=10).read()
                pic=Image.open(io.BytesIO(raw)).convert('RGB')
                if pic.width<320:continue
                pic.thumbnail((950,950))
                dst=io.BytesIO()
                pic.save(dst,format='WEBP',quality=78)
                return dict(robot_id=r['id'],source_url=u,image_url=url,image=base64.b64encode(dst.getvalue()).decode())
            except Exception:pass
with ThreadPoolExecutor(12) as pool:
    rows=[v for v in pool.map(download,[r for r in robots if r['id'] not in illustrated]) if v]
(R/'overview_candidates.json').write_text(json.dumps(rows,separators=(',',':')))
for start in range(0,len(rows),16):
    sheet=Image.new('RGB',(1280,800),'white')
    draw=ImageDraw.Draw(sheet)
    for j,r in enumerate(rows[start:start+16]):
        pic=Image.open(io.BytesIO(base64.b64decode(r['image'])))
        pic.thumbnail((314,173))
        x=j%4*320
        y=j//4*200
        sheet.paste(pic,(x,y))
        draw.text((x+4,y+175),str(start+j)+' '+r['robot_id'],fill='black')
    sheet.save(R/('overview_'+str(start//16)+'.jpg'))
print('Candidates',len(rows))
