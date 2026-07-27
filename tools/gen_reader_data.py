#!/usr/bin/env python3
"""Generate reader/data/issue-NN.json from issues/issue-NN/script.md (lettering text per panel)."""
import re,json,glob,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for sp in sorted(glob.glob(f"{ROOT}/issues/issue-*/script.md")):
    nn=re.search(r"issue-(\d+)",sp).group(1)
    txt=open(sp).read()
    title=re.match(r"# ISSUE \d+ \u2014 (.+)",txt).group(1).strip()
    pages=[]
    for m in re.finditer(r"### PAGE (\d+)[^\n]*\n(.*?)(?=\n### PAGE |\n---\n\n## BACK|\Z)",txt,re.S):
        n=int(m.group(1)); body=m.group(2); panels=[]; cur=None
        for line in body.split("\n"):
            if line.startswith("**PANEL"):
                if cur is not None: panels.append(cur)
                cur=[]
            elif line.startswith("> ") and cur is not None:
                l=line[2:].strip()
                mm=re.match(r"(CAPTION|FOOTNOTE|GNOM\u0112|END PLATE)(?:\s*\([^)]*\))?:\s*(.*)",l)
                if mm:
                    kind={"GNOM\u0112":"GNOME","END PLATE":"PLATE"}.get(mm.group(1),mm.group(1))
                    cur.append([kind,None,mm.group(2)])
                else:
                    mm=re.match(r"([A-Z][A-Z \-'\u2019]+?)(?:\s*\([^)]*\))?:\s*(.*)",l)
                    if mm: cur.append(["DLG",mm.group(1).title(),mm.group(2)])
        if cur is not None: panels.append(cur)
        pages.append({"n":n,"panels":[{"pn":i+1,"items":p} for i,p in enumerate(panels)]})
    out={"issue":int(nn),"title":title,"pages":pages}
    open(f"{ROOT}/reader/data/issue-{nn}.json","w").write(json.dumps(out,ensure_ascii=False))
    print(f"issue-{nn}: {len(pages)} pages, title: {title}")
