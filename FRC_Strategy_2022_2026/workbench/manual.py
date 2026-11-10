"""Render an uploaded manual page inside its isolated run for visual inspection."""
import argparse,json,pathlib,shutil,subprocess
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--run',type=pathlib.Path,required=True);p.add_argument('--page',type=int,required=True);a=p.parse_args();run=a.run.resolve();m=json.loads((run/'manual-manifest.json').read_text())
if not 1<=a.page<=m['page_count']:p.error('Page outside this manual')
source=run/m['filename']
if source.suffix.lower()!='.pdf':p.error('This manual is text; there are no PDF pages to render.')
out=run/'manual-figures';out.mkdir(exist_ok=True);target=out/f'page-{a.page:04}.png'
try:
 import fitz
 with fitz.open(source) as doc:doc[a.page-1].get_pixmap(matrix=fitz.Matrix(1.7,1.7),alpha=False).save(target)
except ImportError:
 tool=shutil.which('pdftoppm')
 if not tool:raise SystemExit('PDF rendering needs PyMuPDF or pdftoppm. Install python -m pip install pymupdf, then retry. Do not claim visual inspection without opening an image.')
 subprocess.run([tool,'-f',str(a.page),'-l',str(a.page),'-scale-to','1800','-singlefile','-png',str(source),str(target.with_suffix(''))],check=True)
print(json.dumps({'page':a.page,'image':str(target),'next_step':'Open the image with an image-capable tool. Rendering alone is not inspection.'},indent=2))
