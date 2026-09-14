#!/usr/bin/env python3
# Adds the six niche landers to sitemap.xml and links them from google-ads.html
import os, re, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = "2026-09-14"

NICHES = [
 ("heating-engineers", "Heating engineers", "Boiler and heat pump installations, not ninety pound callouts."),
 ("builders", "Builders", "Extension and loft conversion enquiries from homeowners with a budget."),
 ("roofers", "Roofers", "Re-roofs and storm repairs, exclusive to you rather than sold on by a directory."),
 ("kitchen-fitters", "Kitchen fitters", "Survey-ready homeowners rather than people still collecting ideas."),
 ("dentists", "Dentists", "Implants, Invisalign and cosmetic consultations, with NHS searches filtered out."),
 ("bathroom-fitters", "Bathroom fitters", "Full bathroom and wet room installations, not tap replacements."),
]

# ---- sitemap -------------------------------------------------------------
sm_path = os.path.join(ROOT, "sitemap.xml")
sm = open(sm_path, encoding="utf-8").read()
block = []
for slug, _, _ in NICHES:
    url = "https://alamex.com/google-ads/%s/" % slug
    if url in sm:
        continue
    block.append("  <url>\n    <loc>%s</loc>\n    <lastmod>%s</lastmod>\n"
                 "    <changefreq>monthly</changefreq>\n    <priority>0.8</priority>\n  </url>" % (url, TODAY))
if block:
    sm = sm.replace("</urlset>", "\n".join(block) + "\n</urlset>")
    open(sm_path, "w", encoding="utf-8").write(sm)
    print("sitemap.xml: added %d urls" % len(block))
else:
    print("sitemap.xml: already current")

# ---- google-ads.html industries block ------------------------------------
ga_path = os.path.join(ROOT, "google-ads.html")
ga = open(ga_path, encoding="utf-8").read()
if "id=\"industries\"" in ga:
    print("google-ads.html: industries block already present")
else:
    cards = "\n".join(
      '        <div class="card">\n'
      '          <h3><a href="google-ads/%s/">%s</a></h3>\n'
      '          <p>%s</p>\n'
      '        </div>' % (slug, name, blurb) for slug, name, blurb in NICHES)
    section = ('  <!-- Industries -->\n'
      '  <section class="section" id="industries">\n'
      '    <div class="container">\n'
      '      <div class="section-header text-center">\n'
      '        <h2>Industries we work with</h2>\n'
      '        <p>Fixed packs, plain pricing and a weekly written update. These pages set out exactly what you get and what it costs.</p>\n'
      '      </div>\n'
      '      <div class="card-grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));">\n'
      + cards + '\n      </div>\n    </div>\n  </section>\n\n')
    marker = '  <!-- CTA -->'
    assert marker in ga, "CTA marker not found in google-ads.html"
    ga = ga.replace(marker, section + marker, 1)
    open(ga_path, "w", encoding="utf-8").write(ga)
    print("google-ads.html: industries block inserted")
