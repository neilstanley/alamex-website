#!/usr/bin/env python3
# Alamex niche Google Ads landers - generator
# Builds /google-ads/<slug>/index.html from one shared template + a content map.
# Run:  python3 _build/build_niche_landers.py   (from the repo root)

import os, json
from string import Template

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------- shared copy

CASE_STUDY = ("A UK services business came to us with a Search account that looked busy and "
              "converted badly. We rebuilt the campaign structure, cleared out the search terms "
              "that were never going to buy, and moved the reporting on to booked jobs instead of "
              "clicks. The weekly update said what had changed and why, and we only interrupted "
              "them when something needed a decision.")

PACKS = [
    ("Starter", "&pound;750", "&pound;750 / month", "up to &pound;1.5k a month",
     "One campaign type, built properly. The right fit if you are starting from nothing or your current account is a mess."),
    ("Growth", "&pound;1,250", "&pound;1,250 / month", "&pound;1.5k to &pound;5k a month",
     "More campaigns, more search terms to keep on top of, and tighter budget pacing across them."),
    ("Scale", "&pound;2,000", "&pound;2,000 / month or 12% of spend", "typically &pound;5k or more a month",
     "For accounts where the spend is large enough that half a percentage point of waste matters."),
]

PROCESS = [
    ("1. Book the &pound;99 call", "&pound;99 including VAT, half an hour on your account, your market and the jobs you actually want. You get the plan whether or not you go ahead, and we will tell you if paid search is the wrong tool for you."),
    ("2. Start Starter", "If it makes sense, you pay &pound;750 setup plus the first &pound;750 month and your &pound;99 comes off the setup fee. No proposal ping-pong, no three-week sales process."),
    ("3. Live in about 7 to 10 days", "A short kickoff checklist from us (access, conversion tracking, service areas, the jobs you want and the ones you do not), then we build the campaigns, set the negatives and turn it on."),
    ("4. Weekly written update", "Every week you get a plain-English update: what happened, what we changed, what we are doing next. A human steps in when something breaks."),
]

FAQS = [
    ("Can I cancel?",
     "Yes. Thirty days' notice, any time, no minimum term beyond that notice period. We do not use twelve-month lock-ins."),
    ("Is my Google spend included?",
     "No. You pay Google directly with your own card, so the ad budget is yours and stays visible to you. Alamex bills the setup fee and the monthly management fee only."),
    ("Do I pay VAT on top?",
     "The &pound;99 strategy call is the one price on this page that already includes VAT, so &pound;99 is what you pay. Everything else is ex-VAT: Alamex Ltd is VAT registered, so VAT at the prevailing UK rate is added at checkout, and Starter is &pound;750 setup plus VAT and &pound;750 a month plus VAT. If you are VAT registered yourself you reclaim it in the normal way. Your Google ad spend is billed to you by Google, not by us."),
    ("What is the difference between Starter and Growth?",
     "Scope and attention. Starter is one campaign type built and managed properly, for accounts spending up to about &pound;1.5k a month. Growth covers a wider account with more campaigns and more search term work, for roughly &pound;1.5k to &pound;5k a month of spend."),
    ("What do you mean by AI-written updates?",
     "The weekly performance update is drafted by our own reporting system straight from the account data, so it goes out on time and the numbers are not massaged. A human reviews anything unusual and contacts you directly when there is a decision to make or something has gone wrong."),
    ("What happens to the &pound;99 strategy call fee if I sign up?",
     "The &pound;99 includes VAT, and it comes off your setup fee if you buy a pack within fourteen days of the call. If you do not, you keep the notes and the plan and owe us nothing further. You pay for the call when you book it, and we email you within one working day with times."),
]

INCLUDED_LEFT = [
    ("Account build and conversion tracking",
     "Campaigns built from scratch or rebuilt, with conversion tracking that counts enquiries and booked work rather than page views."),
    ("Search architecture",
     "Clean campaign and ad group structure so that budget follows intent, with ad copy written against the search that triggered it."),
    ("Negative keywords",
     "A starting negative list on day one and an ongoing search term review, so you stop paying for the searches that were never going to become a job."),
]

INCLUDED_RIGHT = [
    ("Bid and budget management",
     "Bids and budgets managed against cost per enquiry, not left on autopilot. Budget moves to the campaigns doing the work."),
    ("Weekly AI-written performance update",
     "A written update every week, generated from the account data. Human intervention on exceptions, which is when it actually matters."),
    ("Monitoring",
     "Spend, disapprovals, tracking breakages and sudden drops watched between reports, so problems get caught in days rather than at month end."),
]

# ---------------------------------------------------------------- niche map

NICHES = [
 {
  "slug": "heating-engineers",
  "title": "Google Ads for Heating Engineers &mdash; Install Leads | Alamex",
  "og_title": "Google Ads for Heating Engineers | Alamex",
  "desc": "Google Ads management for heating engineers who want boiler and heat pump installations, not &pound;90 callouts. Packs from &pound;750 setup and &pound;750 a month.",
  "desc_plain": "Google Ads management for heating engineers who want boiler and heat pump installations, not GBP 90 callouts. Packs from GBP 750 setup and GBP 750 a month.",
  "h1": "Google Ads for heating engineers",
  "lede": "Campaigns built for boiler and heat pump installations from homeowners who are ready to replace a system, not for emergency callouts at ninety pounds a time.",
  "service_name": "Google Ads Management for Heating Engineers",
  "service_desc": "Google Ads campaign build and management for heating and plumbing firms selling boiler replacements and heat pump installations across the UK.",
  "for": [
   "You install boiler replacements, system upgrades or heat pumps, and that is the work you want more of",
   "You already spend on Google, or you know you should be spending around &pound;1.5k a month or more",
   "You have the capacity to survey and quote the enquiries when they arrive",
   "You want booked surveys measured, not clicks",
  ],
  "notfor": [
   "One-van emergency callout work, where Local Services Ads usually wins on economics and we will say so",
   "Landlord gas safety certificates as the main line of business",
   "Budgets well under &pound;1.5k a month with Google, where there is not enough room to learn anything",
  ],
 },
 {
  "slug": "builders",
  "title": "Google Ads for Builders &mdash; Extension &amp; Loft Leads | Alamex",
  "og_title": "Google Ads for Builders | Alamex",
  "desc": "Google Ads management for builders chasing extension and loft conversion work. Campaigns aimed at homeowners with a budget. From &pound;750 setup and &pound;750 a month.",
  "desc_plain": "Google Ads management for builders chasing extension and loft conversion work. Campaigns aimed at homeowners with a budget. From GBP 750 setup and GBP 750 a month.",
  "h1": "Google Ads for builders",
  "lede": "Extension and loft conversion enquiries from homeowners who have a property, a budget and a timescale, rather than people pricing an idea for some day.",
  "service_name": "Google Ads Management for Builders",
  "service_desc": "Google Ads campaign build and management for building firms selling extensions, loft conversions and renovation projects across the UK.",
  "for": [
   "Extensions, loft conversions and full renovations are the projects you want to fill the diary with",
   "You already spend on Google, or you should be spending around &pound;1.5k a month or more",
   "You can respond to an enquiry inside a day, which is what decides who wins the job",
   "You want to measure site visits booked, not form fills of any kind",
  ],
  "notfor": [
   "Small repairs and odd jobs, where the ticket will not carry a click price",
   "Firms with a full order book for the next year who cannot take on more",
   "Budgets well under &pound;1.5k a month with Google",
  ],
 },
 {
  "slug": "roofers",
  "title": "Google Ads for Roofers &mdash; Re-roofs &amp; Storm Repairs | Alamex",
  "og_title": "Google Ads for Roofers | Alamex",
  "desc": "Google Ads management for roofers. Exclusive re-roof and storm repair enquiries that come to you, not a lead sold to three rivals. From &pound;750 a month.",
  "desc_plain": "Google Ads management for roofers. Exclusive re-roof and storm repair enquiries that come straight to you, not a directory lead sold to three rivals. From GBP 750 a month.",
  "h1": "Google Ads for roofers",
  "lede": "Re-roofs and storm damage work, with the enquiry coming straight to you instead of to a directory that sells the same lead to three of your competitors.",
  "service_name": "Google Ads Management for Roofers",
  "service_desc": "Google Ads campaign build and management for roofing contractors selling re-roofs, flat roof replacements and storm damage repairs across the UK.",
  "for": [
   "Re-roofs, flat roof replacements and storm damage work are what you want the phone ringing about",
   "You are tired of buying shared leads and being one of four quotes by lunchtime",
   "You already spend on Google, or you should be spending around &pound;1.5k a month or more",
   "You can get someone up a ladder for a survey quickly when the weather has just turned",
  ],
  "notfor": [
   "Gutter clearing and small maintenance as the main line of business",
   "Firms who want to keep buying shared directory leads and run ads on top without changing anything",
   "Budgets well under &pound;1.5k a month with Google",
  ],
 },
 {
  "slug": "kitchen-fitters",
  "title": "Google Ads for Kitchen Fitters &mdash; Survey-Ready Leads | Alamex",
  "og_title": "Google Ads for Kitchen Fitters | Alamex",
  "desc": "Google Ads management for kitchen fitters and showrooms. Campaigns tuned for survey-ready homeowners, not ideas browsers. From &pound;750 setup and &pound;750 a month.",
  "desc_plain": "Google Ads management for kitchen fitters and showrooms. Campaigns tuned for survey-ready homeowners, not ideas browsers. From GBP 750 setup and GBP 750 a month.",
  "h1": "Google Ads for kitchen fitters",
  "lede": "Enquiries from homeowners who are ready for a survey and a quote, rather than from people who are three years away from a decision and collecting pictures.",
  "service_name": "Google Ads Management for Kitchen Fitters",
  "service_desc": "Google Ads campaign build and management for kitchen fitting firms and showrooms selling supply-and-fit kitchen installations across the UK.",
  "for": [
   "Supply-and-fit kitchen installations are the work you want, and you survey before you quote",
   "You already spend on Google, or you should be spending around &pound;1.5k a month or more",
   "You have a showroom or a portfolio that stands up when someone checks you out",
   "You want to count booked surveys rather than brochure downloads",
  ],
  "notfor": [
   "Worktop swaps and door replacements alone, where the ticket is too small for paid search",
   "Trade-only suppliers with no consumer-facing offer",
   "Budgets well under &pound;1.5k a month with Google",
  ],
 },
 {
  "slug": "dentists",
  "title": "Google Ads for Dentists &mdash; Implants &amp; Invisalign | Alamex",
  "og_title": "Google Ads for Dentists | Alamex",
  "desc": "Google Ads management for private dental practices: implants, Invisalign and cosmetic consultations, with NHS searches filtered out. From &pound;750 a month.",
  "desc_plain": "Google Ads management for private dental practices. Campaigns for implants, Invisalign and cosmetic consultations, with NHS searches filtered out. From GBP 750 a month.",
  "h1": "Google Ads for dentists",
  "lede": "Private treatment enquiries for implants, Invisalign and cosmetic work, with NHS and emergency searches filtered out before they spend your budget for you.",
  "service_name": "Google Ads Management for Dental Practices",
  "service_desc": "Google Ads campaign build and management for private dental practices marketing implants, Invisalign and cosmetic dentistry consultations across the UK.",
  "for": [
   "Implants, Invisalign, veneers and cosmetic consultations are the treatments you want to fill",
   "You have the chair time and the treatment coordinator to follow up an enquiry properly",
   "You already spend on Google, or you should be spending around &pound;1.5k a month or more",
   "You want consultations booked and attended counted, not enquiry forms",
  ],
  "notfor": [
   "NHS lists and routine check-ups, which we filter out rather than advertise against",
   "Emergency dentist searches as the main aim",
   "Practices that cannot follow up an enquiry the same day, where paid search leaks badly",
  ],
 },
 {
  "slug": "bathroom-fitters",
  "title": "Google Ads for Bathroom Fitters &mdash; Wet Room Leads | Alamex",
  "og_title": "Google Ads for Bathroom Fitters | Alamex",
  "desc": "Google Ads management for bathroom and wet room installers. Built for full installation enquiries, not tap replacements. From &pound;750 setup and &pound;750 a month.",
  "desc_plain": "Google Ads management for bathroom and wet room installers. Built for full installation enquiries, not tap replacements. From GBP 750 setup and GBP 750 a month.",
  "h1": "Google Ads for bathroom fitters",
  "lede": "Full bathroom and wet room installation enquiries from homeowners ready to book a survey, not from someone looking for a plumber to swap a tap.",
  "service_name": "Google Ads Management for Bathroom Fitters",
  "service_desc": "Google Ads campaign build and management for bathroom and wet room installation firms selling full fitted bathrooms across the UK.",
  "for": [
   "Full bathroom and wet room installations are the work you want, ideally supply and fit",
   "Accessible and mobility wet rooms are a line you want to grow",
   "You already spend on Google, or you should be spending around &pound;1.5k a month or more",
   "You survey before you quote and want surveys counted as the conversion",
  ],
  "notfor": [
   "Emergency plumbing and small repairs, which is different economics and a different campaign",
   "Supply-only retailers with no fitting offer",
   "Budgets well under &pound;1.5k a month with Google",
  ],
 },
]

# ---------------------------------------------------------------- template

TEMPLATE = Template(r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <!-- Favicons -->
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
  <link rel="icon" type="image/png" sizes="192x192" href="/favicon-192.png">
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
  <link rel="manifest" href="/site.webmanifest">
  <meta name="theme-color" content="#0f1b2d">
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-K8MTETS33F"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-K8MTETS33F');
  </script>
  <title>$title</title>
  <meta name="description" content="$desc">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://alamex.com/google-ads/$slug/">

  <meta property="og:title" content="$og_title">
  <meta property="og:description" content="$desc">
  <meta property="og:url" content="https://alamex.com/google-ads/$slug/">
  <meta property="og:type" content="website">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../../css/style.css">

  <script type="application/ld+json">
$service_jsonld
  </script>
  <script type="application/ld+json">
$faq_jsonld
  </script>
</head>
<body>

  <!-- Header -->
  <header class="header" id="header">
    <div class="container header__inner">
      <a href="../../index.html" class="logo">Alamex<span>.</span></a>
      <nav class="nav" id="nav" aria-label="Main navigation">
        <a href="../../index.html" class="nav__link">Home</a>
        <a href="../../about.html" class="nav__link">About</a>
        <a href="../../seo-services.html" class="nav__link">SEO/AEO</a>
        <a href="../../google-ads/" class="nav__link nav__link--active">Google Ads</a>
        <a href="../../use-ai-in-my-business/" class="nav__link">AI for Business</a>
        <a href="/apps-by-alamex/" class="nav__link">Apps</a>
        <a href="../../contact.html" class="btn btn--primary btn--sm">Get in Touch</a>
      </nav>
      <button class="nav-toggle" id="nav-toggle" aria-label="Toggle navigation" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>

  <!-- 1. Hero -->
  <section class="page-header">
    <div class="container">
      <h1>$h1</h1>
      <p>$lede</p>
      <div style="display: flex; flex-wrap: wrap; gap: var(--space-md); margin-top: var(--space-xl);">
        <!-- Stripe payment link, plink alamex_agency=call. 99 ex-VAT, VAT added at checkout. -->
        <a href="https://buy.stripe.com/00w28r76jgtU2rv1us1ck02" target="_blank" rel="noopener" class="btn btn--white btn--lg" data-cta="strategy_call" data-cta-position="hero">Book a &pound;99 strategy call</a>
        <a href="#packs" class="btn btn--outline btn--lg" style="border-color: rgba(255,255,255,0.35); color: #fff;" data-cta="view_packs" data-cta-position="hero">See the packs</a>
      </div>
      <p style="font-size: 0.95rem; color: #cbd5e1; margin-top: var(--space-lg); max-width: 640px;"><strong style="color: #fff;">What happens next:</strong> the call is &pound;99 including VAT and takes half an hour. If it makes sense, the next stage is Starter at &pound;750 setup plus &pound;750 a month, and your &pound;99 comes off the setup fee.</p>
      <p style="font-size: 0.9rem; color: #94a3b8; margin-top: var(--space-md);">The call is &pound;99 including VAT. Pack prices are ex-VAT, with VAT added at checkout. You pay Google directly for the ad spend. Thirty days' notice to cancel, any time.</p>
    </div>
  </section>

  <!-- 2. Proof -->
  <section class="section">
    <div class="container">
      <div class="stats">
        <div>
          <div class="stat__number">&pound;5m</div>
          <div class="stat__label">Of our own money spent on Google Ads</div>
        </div>
        <div>
          <div class="stat__number">10+</div>
          <div class="stat__label">Years in Search Marketing</div>
        </div>
        <div>
          <div class="stat__number">200+</div>
          <div class="stat__label">Campaigns Managed</div>
        </div>
        <div>
          <div class="stat__number">95%</div>
          <div class="stat__label">Client Retention Rate</div>
        </div>
        <div>
          <div class="stat__number">3.2x</div>
          <div class="stat__label">Average ROAS Improvement</div>
        </div>
      </div>
      <p class="text-center mt-xl" style="max-width: 760px; margin-left: auto; margin-right: auto; color: var(--text-light);">We are not only spending other people's money. Alamex runs its own portfolio of websites and apps, and we have put nearly &pound;5 million of our own budget through Google Ads. Everything we do on a client account, we have already paid to learn on our own.</p>
      <div class="testimonial mt-xl">
        <blockquote>&ldquo;$case_study&rdquo;</blockquote>
        <cite>Anonymised client account, UK services business</cite>
      </div>
    </div>
  </section>

  <!-- 3. Who it is for -->
  <section class="section section--alt">
    <div class="container">
      <div class="section-header text-center">
        <h2>Who this is for</h2>
        <p>You already spend on Google, or you should be spending around &pound;1.5k a month or more. We do not replace Local Services Ads for one-van callout work, and we will tell you if that is the better route.</p>
      </div>
      <div class="card-grid" style="grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));">
        <div class="card">
          <h3>A good fit if</h3>
          <ul class="feature-list">
$for_items
          </ul>
        </div>
        <div class="card">
          <h3>Not a good fit if</h3>
          <ul class="feature-list">
$notfor_items
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- 4. Packs -->
  <section class="section" id="packs" style="scroll-margin-top: 88px;">
    <div class="container">
      <div class="section-header text-center">
        <h2>Three packs, no proposals</h2>
        <p>Setup fee plus a monthly management fee. All prices are ex-VAT and VAT is added at checkout. Your Google spend is separate and paid by you, directly to Google. Most people take the &pound;99 call first and put it towards the setup fee, but if you already know what you want you can start today.</p>
      </div>
      <div class="card-grid">
$pack_cards
      </div>
      <p class="text-center mt-xl" style="color: var(--text-light);">Cancel with thirty days' notice at any time. No minimum term beyond the notice period.</p>
    </div>
  </section>

  <!-- 5. What is included -->
  <section class="section section--alt">
    <div class="container">
      <div class="section-header text-center">
        <h2>What is included</h2>
        <p>The same work on every pack. The difference between packs is how much account there is to do it to.</p>
      </div>
      <div class="service-detail">
        <div>
          <h3>Build</h3>
          <ul class="feature-list">
$included_left
          </ul>
        </div>
        <div>
          <h3>Run</h3>
          <ul class="feature-list">
$included_right
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- 6. How it works -->
  <section class="section">
    <div class="container">
      <div class="section-header text-center">
        <h2>How it works</h2>
        <p>From the first call to live campaigns in about a fortnight.</p>
      </div>
      <div class="process">
$process_steps
      </div>
    </div>
  </section>

  <!-- 7. FAQ -->
  <section class="section section--alt">
    <div class="container container--narrow">
      <div class="section-header text-center">
        <h2>Questions</h2>
      </div>
$faq_items
    </div>
  </section>

  <!-- 8. Bottom CTA -->
  <section class="cta-banner">
    <div class="container">
      <h2>$cta_heading</h2>
      <p>Book the &pound;99 call, including VAT, and we will tell you honestly whether paid search is worth it for you. If it is, the next stage is Starter at &pound;750 setup plus &pound;750 a month, and your &pound;99 comes off the setup fee. If it is not, we will say so and you will have the plan anyway.</p>
      <div style="display: flex; flex-wrap: wrap; gap: var(--space-md); justify-content: center; margin-top: var(--space-xl);">
        <!-- Stripe payment link, plink alamex_agency=call. 99 ex-VAT, VAT added at checkout. -->
        <a href="https://buy.stripe.com/00w28r76jgtU2rv1us1ck02" target="_blank" rel="noopener" class="btn btn--white btn--lg" data-cta="strategy_call" data-cta-position="footer">Book a &pound;99 strategy call</a>
        <!-- Stripe payment link, plink alamex_agency=starter. 750 setup + 750/mo, both ex-VAT. -->
        <a href="https://buy.stripe.com/9B67sLaivb9A2rvfli1ck01" target="_blank" rel="noopener" class="btn btn--outline btn--lg" style="border-color: rgba(255,255,255,0.35); color: #fff;" data-cta="start_starter" data-cta-position="footer">Or start Starter &mdash; &pound;750 setup</a>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="footer">
    <div class="container">
      <div class="footer__grid">
        <div class="footer__brand">
          <a href="../../index.html" class="logo" style="color: #fff;">Alamex<span>.</span></a>
          <p>Specialist SEO and Google Ads agency based in Bath, UK. Helping businesses grow through the power of search.</p>
        </div>
        <div>
          <h4>Services</h4>
          <ul class="footer__links">
            <li><a href="../../seo-services.html">SEO/AEO</a></li>
            <li><a href="../../google-ads/">Google Ads</a></li>
            <li><a href="../../use-ai-in-my-business/">AI for Business</a></li>
          </ul>
        </div>
        <div>
          <h4>Company</h4>
          <ul class="footer__links">
            <li><a href="../../about.html">About Us</a></li>
            <li><a href="../../contact.html">Contact</a></li>
            <li><a href="../../apps-by-alamex/">Apps by Alamex</a></li>
          </ul>
        </div>
        <div>
          <h4>Contact</h4>
          <ul class="footer__links">
            <li><a href="mailto:hello@alamex.com">hello@alamex.com</a></li>
            <li>11 Laura Place</li>
            <li>Bath, BA2 4BL</li>
            <li>United Kingdom</li>
          </ul>
        </div>
      </div>
      <div class="footer__legal">Alamex Digital is a trading name of Alamex Ltd, a company registered in England and Wales, company number 06332689. Registered office: 11 Laura Place, Bath, BA2 4BL.</div>
      <div class="footer__bottom">
        <span>&copy; 2026 Alamex Digital. All rights reserved.</span>
        <span>
          <a href="../../privacy.html">Privacy Policy</a> &nbsp;&middot;&nbsp;
          <a href="../../terms.html">Terms of Service</a>
        </span>
      </div>
    </div>
  </footer>

  <script src="../../js/main.js"></script>
</body>
</html>
""")

# ---------------------------------------------------------------- helpers

def unescape(s):
    return (s.replace("&pound;", "£").replace("&mdash;", "—")
             .replace("&ndash;", "–").replace("&amp;", "&")
             .replace("&ldquo;", "“").replace("&rdquo;", "”"))

def li(text):
    return ('            <li><span class="feature-list__check">&check;</span>\n'
            '              <div>%s</div>\n            </li>' % text)

def li_pair(title, body):
    return li("<strong>%s</strong>: %s" % (title, body))

def pack_cards():
    out = []
    for name, setup, monthly, spend, blurb in PACKS:
        out.append(
 '        <div class="card">\n'
 '          <h3>%s</h3>\n'
 '          <div class="stat__number" style="font-size: 2rem; margin-bottom: var(--space-xs);">%s</div>\n'
 '          <div class="stat__label" style="margin-bottom: var(--space-lg);">setup, one-off, plus VAT</div>\n'
 '          <p style="font-weight: 600; color: var(--navy); margin-bottom: var(--space-sm);">%s management, plus VAT</p>\n'
 '          <p style="font-size: 0.9rem; color: var(--text-light); margin-bottom: var(--space-md);">For clients spending %s directly with Google.</p>\n'
 '          <p>%s</p>\n'
 '        </div>' % (name, setup, monthly, spend, blurb))
    return "\n".join(out)

def process_steps():
    return "\n".join(
 '        <div class="process__step">\n          <h4>%s</h4>\n          <p>%s</p>\n        </div>' % (h, b)
        for h, b in PROCESS)

def faq_items():
    return "\n".join(
 '      <div class="card" style="margin-bottom: var(--space-lg);">\n'
 '        <h3>%s</h3>\n        <p>%s</p>\n      </div>' % (q, a) for q, a in FAQS)

def faq_jsonld():
    data = {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": unescape(q),
                            "acceptedAnswer": {"@type": "Answer", "text": unescape(a)}}
                           for q, a in FAQS]}
    return json.dumps(data, indent=2, ensure_ascii=False)

def service_jsonld(n):
    data = {"@context": "https://schema.org", "@type": "Service",
            "name": unescape(n["service_name"]),
            "provider": {"@type": "ProfessionalService", "name": "Alamex Digital",
                         "url": "https://alamex.com"},
            "description": unescape(n["service_desc"]),
            "areaServed": "GB",
            "serviceType": "Google Ads Management",
            "url": "https://alamex.com/google-ads/%s/" % n["slug"]}
    return json.dumps(data, indent=2, ensure_ascii=False)

CTA_HEADINGS = {
 "heating-engineers": "Fill the diary with installs, not callouts",
 "builders": "Get in front of homeowners with a budget",
 "roofers": "Stop buying leads three rivals already have",
 "kitchen-fitters": "Book surveys, not brochure requests",
 "dentists": "Fill the private treatment diary",
 "bathroom-fitters": "Book bathroom surveys, not tap repairs",
}

def build():
    for n in NICHES:
        html = TEMPLATE.substitute(
            title=n["title"], og_title=n["og_title"], desc=n["desc"], slug=n["slug"],
            h1=n["h1"], lede=n["lede"], case_study=CASE_STUDY,
            for_items="\n".join(li(x) for x in n["for"]),
            notfor_items="\n".join(li(x) for x in n["notfor"]),
            pack_cards=pack_cards(),
            included_left="\n".join(li_pair(t, b) for t, b in INCLUDED_LEFT),
            included_right="\n".join(li_pair(t, b) for t, b in INCLUDED_RIGHT),
            process_steps=process_steps(),
            faq_items=faq_items(),
            faq_jsonld=faq_jsonld(),
            service_jsonld=service_jsonld(n),
            cta_heading=CTA_HEADINGS[n["slug"]],
        )
        d = os.path.join(ROOT, "google-ads", n["slug"])
        os.makedirs(d, exist_ok=True)
        p = os.path.join(d, "index.html")
        with open(p, "w", encoding="utf-8") as f:
            f.write(html)
        print("wrote %s (%d bytes)" % (p.replace(ROOT + "/", ""), len(html)))

if __name__ == "__main__":
    build()
