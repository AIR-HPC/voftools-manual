"""Check generated HTML files, local links, anchors and image references."""
from pathlib import Path
from urllib.parse import urlsplit,unquote
from html.parser import HTMLParser
import sys,json
class Page(HTMLParser):
 def __init__(self,path):
  super().__init__(); self.ids=set(); self.links=[]; self.images=0; self.errors=[]
  self.feed(path.read_text())
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:
   if a['id'] in self.ids:self.errors.append('duplicate id '+a['id'])
   self.ids.add(a['id'])
  if tag=='a' and 'href' in a:self.links.append(a['href'])
  if tag in ('img','script') and 'src' in a:self.links.append(a['src'])
  if tag=='link' and 'href' in a:self.links.append(a['href'])
  if tag=='img':self.images+=1
root=Path(sys.argv[1] if len(sys.argv)>1 else '_build/html').resolve()
pages={p:Page(p) for p in root.rglob('*.html')};errors=[];checked=0
for path,page in pages.items():
 errors.extend(str(path.relative_to(root))+': '+e for e in page.errors)
 for link in page.links:
  u=urlsplit(link)
  if u.scheme or u.netloc or not link:continue
  dest=(path.parent/unquote(u.path)).resolve() if u.path else path
  if dest.is_dir():dest=dest/'index.html'
  checked+=1
  if not dest.exists():errors.append(f'{path.relative_to(root)}: missing {link}')
  elif u.fragment and dest in pages and unquote(u.fragment) not in pages[dest].ids:
   errors.append(f'{path.relative_to(root)}: missing anchor {link}')
print(json.dumps({'html_pages':len(pages),'local_links_checked':checked,'errors':errors},indent=2))
sys.exit(bool(errors))
