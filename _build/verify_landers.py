#!/usr/bin/env python3
import os, re, json, glob, sys
from html.parser import HTMLParser
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import html as htmlmod

VOID = {"area","base","br","col","embed","hr","img","input","link","meta","param","source","track","wbr"}
class Checker(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True); self.stack=[]; self.errs=[]
    def handle_starttag(self,tag,attrs):
        if tag not in VOID: self.stack.append(tag)
    def handle_endtag(self,tag):
        if tag in VOID: return
        if not self.stack: self.errs.append("stray </%s>"%tag); return
        if self.stack[-1]==tag: self.stack.pop()
        else: self.errs.append("expected </%s> got </%s>"%(self.stack[-1],tag))

fail=0
for p in sorted(glob.glob(os.path.join(ROOT,"google-ads","*","index.html"))):
    rel=p.replace(ROOT+"/","")
    s=open(p,encoding="utf-8").read()
    probs=[]
    c=Checker(); c.feed(s)
    if c.errs: probs.append("unbalanced tags: %s"%c.errs[:3])
    if c.stack: probs.append("unclosed: %s"%c.stack)
    t=htmlmod.unescape(re.search(r"<title>(.*?)</title>",s,re.S).group(1))
    d=htmlmod.unescape(re.search(r'<meta name="description" content="(.*?)">',s,re.S).group(1))
    if not (45<=len(t)<=65): probs.append("title %d chars: %s"%(len(t),t))
    if not (140<=len(d)<=165): probs.append("desc %d chars"%len(d))
    for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>',s,re.S):
        try: json.loads(m)
        except Exception as e: probs.append("bad JSON-LD: %s"%e)
    for need in ['class="page-header"','class="cta-banner"','class="footer"','js/main.js',
                 '../../css/style.css','id="nav-toggle"','&pound;750','&pound;1,250','&pound;2,000',
                 'thirty days','directly to Google','Anonymised client account','robots" content="index, follow']:
        if need not in s: probs.append("missing: %s"%need)
    if s.count("<h1")!=1: probs.append("h1 count %d"%s.count("<h1"))
    if s.count("<h2")<6: probs.append("only %d h2 sections"%s.count("<h2"))
    if "Amalulu" in s or "amalulu" in s: probs.append("CLIENT NAME LEAKED")
    for bad in ["Lorem","TODO:</","{{","$slug","$title"]:
        if bad in s: probs.append("placeholder left: %s"%bad)
    # invented numbers guard: list every number-ish token for eyeball
    nums=set(re.findall(r'(?<![\w&#])\d[\d,\.]*\s*(?:%|x|k\b)?',htmlmod.unescape(s)))
    print("%-46s %s  h2=%d  title=%d desc=%d" % (rel, "OK " if not probs else "FAIL", s.count("<h2"), len(t), len(d)))
    for x in probs: print("      - %s"%x); 
    if probs: fail=1
print("\nnumbers used across pages:", sorted(n.strip() for n in nums if n.strip()))
sys.exit(fail)
