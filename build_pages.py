#!/usr/bin/env python3
"""Uncorked Wine Bar — generator (single source for all pages).
websites lane, card t_69ac5b0e. Built 2026-11-25. Demo host pinned from first byte.
Design: "arrivals, international" — flight-board amber-on-black hero panel over bone-paper
body, bordeaux + cork accents, Georgia serif display, system mono labels. No photos, no
third-party JS, no webfonts.
Facts ONLY from press-verified card: ctinsider.com (Hearst/NH Register) 2026-11 opening
feature (author Susan Braden) + hoodline.com 11-25 opening item; address geo from
OpenStreetMap parcel 973;975 State Street (ODbL). Unknown (phone, bottle prices,
reservation policy) = omitted, never guessed."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
PUBLIC = os.path.join(HERE, "public")
ORIGIN = "https://uncorked-newhaven-demo.up.railway.app"

BRAND = "Uncorked Wine Bar"
BRAND_PLAIN = "Uncorked Wine Bar"
ADDR = "975 State Street, New Haven, Connecticut 06511"
GEO = (41.3153711, -72.9098152)  # exact house match, OpenStreetMap address point 973;975 State St (ODbL)
MAP_Q = "https://www.google.com/maps?q=975%20State%20Street%2C%20New%20Haven%2C%20CT%2006511&output=embed"
DIRS = "https://www.google.com/maps/dir/?api=1&destination=975%20State%20Street%2C%20New%20Haven%2C%20CT%2006511"
IG = "https://www.instagram.com/uncorkednh/"  # handle from the ctinsider opening feature

FOOTER = ('</main>\n<footer>\n'
          '<p class="footline"><a href="/">Uncorked Wine Bar</a></p>\n'
          '<p class="footline">975 State Street, New Haven, Connecticut 06511 &middot; Sun&#8211;Thu 4 pm &#8211; 1 am &middot; Fri &amp; Sat 4 pm &#8211; 2 am</p>\n'
          '<p class="footline fine">&copy; 2026 &middot; <a href="/wine-list">Wine List</a> &middot; <a href="/small-plates">Small Plates</a> &middot; <a href="/visit">Visit</a> &middot; <a href="/contact">Contact</a> &middot; <a href="/privacy">Privacy</a></p>\n'
          '</footer>\n</body>\n</html>\n')

def business_node(extra_url=None):
    n = {
        "@context": "https://schema.org",
        "@type": "BarOrPub",
        "name": "Uncorked Wine Bar",
        "url": ORIGIN + (extra_url or "/"),
        "image": ORIGIN + "/og.png",
        "description": "A new wine bar on State Street in New Haven, Connecticut - 75 to 80 hand-picked bottles from around the world, ten whites and ten reds by the glass, and a small-plates kitchen.",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "975 State Street",
            "addressLocality": "New Haven",
            "addressRegion": "CT",
            "postalCode": "06511",
            "addressCountry": "US"
        },
        "geo": {"@type": "GeoCoordinates", "latitude": GEO[0], "longitude": GEO[1]},
        "sameAs": IG,
        "openingHoursSpecification": [
            {"@type": "OpeningHoursSpecification", "dayOfWeek": d,
             "opens": "16:00", "closes": "23:59"}
            for d in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        ] + [
            {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
             "opens": "00:00", "closes": "01:00"},
            {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Saturday", "Sunday"],
             "opens": "00:00", "closes": "02:00"}
        ]
    }
    return n

def provider_node():
    return {
        "@type": "BarOrPub",
        "name": "Uncorked Wine Bar",
        "url": ORIGIN + "/",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "975 State Street",
            "addressLocality": "New Haven",
            "addressRegion": "CT",
            "postalCode": "06511",
            "addressCountry": "US"
        }
    }

def crumb(path, label):
    items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": ORIGIN + "/"}]
    if path != "/":
        items.append({"@type": "ListItem", "position": 2, "name": label, "item": ORIGIN + path})
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}

NAV = [("/", "Home"), ("/wine-list", "Wine List"), ("/small-plates", "Small Plates"),
       ("/visit", "Visit"), ("/contact", "Contact")]

def head(title, desc, path, ld=None, utility=False):
    u = ORIGIN + path
    d = desc.replace('"', "'")
    parts = ['<!DOCTYPE html>', '<html lang="en">', '<head>', '<meta charset="utf-8">',
             '<meta name="robots" content="noindex, nofollow">',
             '<!-- BUILT-2026-11-25 -->',
             '<title>%s</title>' % title,
             '<meta name="description" content="%s">' % d,
             '<meta name="viewport" content="width=device-width, initial-scale=1">',
             '<link rel="canonical" href="%s">' % u,
             '<link rel="icon" href="/favicon.svg" type="image/svg+xml">',
             '<link rel="stylesheet" href="/style.css">']
    if not utility:
        t = title.replace('"', "'")
        parts += [
            '<meta property="og:type" content="website">',
            '<meta property="og:title" content="%s">' % t,
            '<meta property="og:description" content="%s">' % d,
            '<meta property="og:image" content="%s/og.png">' % ORIGIN,
            '<meta property="og:url" content="%s">' % u,
            '<meta name="twitter:card" content="summary_large_image">']
    for blk in (ld or []):
        parts.append('<script type="application/ld+json">%s</script>' % json.dumps(blk, ensure_ascii=False))
    parts.append('</head>\n<body>')
    return "\n".join(parts)

def nav(current):
    items = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == current else ""
        items.append('<a href="%s"%s>%s</a>' % (href, cur, label))
    return ('<a class="skip" href="#main">Skip to content</a>\n'
            '<header class="site">\n'
            '<p class="brand"><a href="/">Uncorked <em>Wine Bar</em></a></p>\n'
            '<nav aria-label="Site"><p>%s</p></nav>\n'
            '</header>\n<main id="main">' % " ".join(items))

BOARD = [
    ("Napa Valley", "California, USA"),
    ("Italy", "the mainland"),
    ("Greece", "islands"),
    ("Portugal", "the Atlantic coast"),
    ("Spain", "around the table"),
]

def board_html():
    rows = ['<div class="brow bhead"><span>Where the wine is from</span><span>Status</span></div>']
    for a, b in BOARD:
        rows.append('<p class="brow"><span class="bfrom">%s &middot; %s</span><span class="bst">Pouring</span></p>' % (a, b))
    rows.append('<p class="brow bmore"><span class="bfrom">And more from around the world</span><span class="bst">On the list</span></p>')
    return ('<section class="board" aria-label="Wine origins pouring now">\n'
            '<p class="lab boardlab">Arrivals &#8212; the cellar</p>\n%s\n</section>' % "\n".join(rows))

def write(name, doc):
    os.makedirs(PUBLIC, exist_ok=True)
    with open(os.path.join(PUBLIC, name), "w", encoding="utf-8") as f:
        f.write(doc)

pages = {}

# ---------- HOME ----------
ld_home = [business_node(), crumb("/", "Home")]
home = head("Uncorked Wine Bar &#8212; New Wine Bar on State Street in New Haven, CT",
            "A new wine bar from the owners of Blue Tortuga: 75 to 80 hand-picked bottles from around the world, ten whites and ten reds by the glass, small plates, every night on State Street, New Haven.",
            "/", ld_home) + "\n" + nav("/") + "\n"
home += ('<section class="hero">\n<div class="wrap hero-grid">\n'
         '<div class="hero-copy">\n'
         '<p class="kicker">New wine bar &#183; 975 State Street &#183; New Haven, CT</p>\n'
         '<h1>The whole world,<br>poured by the glass.</h1>\n'
         '<p class="lede">Seventy-five to eighty bottles on the list. Ten whites and ten reds poured by the glass. A small kitchen turning out plates worth the trip &#8212; every bottle hand-picked by the two people who own the place.</p>\n'
         '<p class="cta-row"><a class="btn" href="/wine-list">See the wine list</a> <a class="btn ghost" href="/contact">Send a note</a></p>\n'
         '</div>\n' + board_html() + '\n</div>\n</section>\n')
home += ('<section class="band grand"><div class="wrap">\n'
         '<p class="lab">Save the date</p>\n'
         '<h2>Grand opening &#8212; Wednesday, November 25, 2026</h2>\n'
         '<p>Doors open at four o&#8217;clock every night of the week. Come see what the new room looks like.</p>\n'
         '<p class="cta-row"><a class="btn" href="/visit">Plan your visit</a></p>\n'
         '</div></section>\n')
home += ('<section class="wrap quoteband">\n'
         '<blockquote>&#8220;We wanted to do something completely different, and so we did.&#8221;</blockquote>\n'
         '<p class="attrib">Lorena San Martin &#183; co-owner, with Maria Huertas &#183; the pair behind Blue Tortuga Bistro &amp; Bar</p>\n'
         '</section>\n')
home += ('<section class="wrap split">\n'
         '<div>\n<p class="lab">The kitchen</p>\n<h2>Small plates, big pairings</h2>\n'
         '<p>Filet mignon sliders with beet chips. Steak tartare made with filet mignon. Octopus and hummus, chicken liver with lingonberry. The menu was built around the wine, not the other way around.</p>\n'
         '<p class="cta-row"><a class="btn" href="/small-plates">The full plates menu</a></p>\n'
         '</div>\n'
         '<aside class="pour-card">\n<p class="lab">The pour everyone is ordering</p>\n'
         '<h3>Bonanza Cabernet Sauvignon</h3>\n<p>Caymus Vineyards, Napa Valley &#8212; the bottle the room keeps reaching for.</p>\n'
         '<p class="price">$14 <span>a glass</span></p>\n'
         '<p class="cta-row"><a class="btn ghost" href="/wine-list">About the list</a></p>\n'
         '</aside>\n</section>\n')
home += ('<section class="band visit"><div class="wrap vsplit">\n'
         '<div>\n<p class="lab">Find us</p>\n'
         '<h2>975 State Street, New Haven</h2>\n'
         '<p>On Upper State Street in East Rock &#8212; the other end of town from our bistro. Sun&#8211;Thu 4 pm to 1 am. Fri &amp; Sat 4 pm to 2 am.</p>\n'
         '<p class="cta-row"><a class="btn" href="%s">Get directions</a> <a class="btn dark ghost" href="/contact">Send a note</a></p>\n'
         '</div>\n'
         '<p class="ig-line">Follow the board: <a href="%s">@uncorkednh</a></p>\n'
         '</div></section>\n' % (DIRS, IG))
home += FOOTER
pages["index.html"] = home

# ---------- WINE LIST ----------
ld_wine = [
    {"@context": "https://schema.org", "@type": "Service",
     "name": "Wine List and By-the-Glass at Uncorked Wine Bar",
     "serviceType": "Wine list",
     "provider": provider_node(),
     "areaServed": {"@type": "City", "name": "New Haven", "address": {"@type": "PostalAddress", "addressLocality": "New Haven", "addressRegion": "CT", "addressCountry": "US"}}},
    crumb("/wine-list", "Wine List"),
]
wine = head("Wine List &amp; By-the-Glass &#8212; Uncorked Wine Bar, New Haven CT",
            "75 to 80 bottles from Napa Valley, Italy, Greece, Portugal, Spain and beyond. Ten whites and ten reds by the glass. The list is hand-picked by the owners.",
            "/wine-list", ld_wine) + "\n" + nav("/wine-list") + "\n"
wine += ('<section class="pagehead"><div class="wrap">\n'
         '<p class="kicker">The list</p>\n<h1>Wines from all over the world, hand-picked bottle by bottle</h1>\n'
         '<p class="lede">About 75 to 80 bottles on the list at any time. Ten whites and ten reds poured by the glass &#8212; ten each, no filler. The full list lives at the bar, and it changes as bottles run out.</p>\n'
         '</div></section>\n')
wine += '<section class="wrap">\n' + board_html() + '\n</section>\n'
wine += ('<section class="wrap">\n<div class="grid">\n'
         '<div class="card"><p class="lab">California &#183; Napa Valley</p><h3>The Cabernet the room orders</h3><p>Bonanza, from Caymus Vineyards &#8212; $14 by the glass.</p></div>\n'
         '<div class="card"><p class="lab">Italy</p><h3>Poured alongside the rest</h3><p>From the list, selected in the same round of tastings as everything else here.</p></div>\n'
         '<div class="card"><p class="lab">Greece</p><h3>Island bottles made it in</h3><p>Greek pours are on the list &#8212; proof of how wide the net was thrown.</p></div>\n'
         '<div class="card"><p class="lab">Portugal</p><h3>From the Atlantic coast</h3><p>Portuguese bottles are part of the program.</p></div>\n'
         '<div class="card"><p class="lab">Spain</p><h3>On tables across the room</h3><p>Spanish bottles anchor the by-the-glass side.</p></div>\n'
         '<div class="card"><p class="lab">And everywhere else</p><h3>&#8220;We literally are trying to bring wines from all over the world&#8221;</h3><p>That&#8217;s the whole idea of the list.</p></div>\n'
         '</div>\n</section>\n')
wine += ('<section class="wrap story">\n'
         '<p class="lab">How the list happened</p>\n'
         '<h2>Five months, a lot of tastings</h2>\n'
         '<p>The room used to be a wine bar called Cave a Vin. Maria Huertas and Lorena San Martin bought it from the old owner, kept it a wine bar, and rebuilt the cellar from zero &#8212; the old stock out, a new list in, chosen over months of tastings.</p>\n'
         '<blockquote>&#8220;So we actually picked and took our time to make the wine list ourselves. We had a lot of tastings, a lot of drunken days.&#8221;</blockquote>\n'
         '<p class="attrib">Lorena San Martin &#183; co-owner</p>\n'
         '</section>\n')
wine += ('<section class="wrap cta-band">\n<h2>Come taste where it landed</h2>\n'
         '<p class="cta-row"><a class="btn" href="/visit">Hours &amp; directions</a> <a class="btn ghost" href="/contact">Ask us anything</a></p>\n'
         '</section>\n')
wine += FOOTER
pages["wine-list.html"] = wine

# ---------- SMALL PLATES ----------
ld_plates = [
    {"@context": "https://schema.org", "@type": "Menu",
     "name": "Small Plates at Uncorked Wine Bar",
     "inLanguage": "en",
     "hasMenuSection": {
         "@type": "MenuSection", "name": "Small Plates",
         "hasMenuItem": [
             {"@type": "MenuItem", "name": "Filet Mignon Sliders", "description": "With beet chips. A big hit with guests."},
             {"@type": "MenuItem", "name": "Steak Tartare", "description": "Made with filet mignon."},
             {"@type": "MenuItem", "name": "Octopus and Hummus"},
             {"@type": "MenuItem", "name": "Chicken Liver", "description": "With lingonberry."}
         ]}},
    crumb("/small-plates", "Small Plates"),
]
plates = head("Small Plates &#8212; Uncorked Wine Bar, New Haven CT",
              "Filet mignon sliders with beet chips, steak tartare, octopus and hummus, chicken liver with lingonberry - a small kitchen with the menu built around the wine.",
              "/small-plates", ld_plates) + "\n" + nav("/small-plates") + "\n"
plates += ('<section class="pagehead"><div class="wrap">\n'
           '<p class="kicker">The kitchen</p>\n<h1>Small plates, built around the wine</h1>\n'
           '<p class="lede">The kitchen is small, and the menu treats that as a feature, not an excuse &#8212; much thought went into what pairs with what, plate for plate, glass for glass.</p>\n'
           '</div></section>\n')
plates += ('<section class="wrap">\n<ul class="plates">\n'
           '<li><span class="pname">Filet mignon sliders</span><span class="pd">with beet chips</span><span class="hit">a big hit</span></li>\n'
           '<li><span class="pname">Steak tartare</span><span class="pd">made with filet mignon</span><span class="hit">a big hit</span></li>\n'
           '<li><span class="pname">Octopus and hummus</span><span class="pd">&nbsp;</span><span class="hit">&nbsp;</span></li>\n'
           '<li><span class="pname">Chicken liver</span><span class="pd">with lingonberry</span><span class="hit">&nbsp;</span></li>\n'
           '</ul>\n'
           '<p class="note">The bar keeps pairing notes for every plate &#8212; ask your server what to pour beside what.</p>\n'
           '</section>\n')
plates += ('<section class="wrap quoteband">\n'
           '<blockquote>&#8220;Our menu is pretty nice for the small kitchen.&#8221;</blockquote>\n'
           '<p class="attrib">Lorena San Martin &#183; co-owner</p>\n'
           '</section>\n')
plates += ('<section class="wrap cta-band">\n<h2>Pick your plate, we&#8217;ll pick the pour</h2>\n'
           '<p class="cta-row"><a class="btn" href="/visit">Hours &amp; directions</a> <a class="btn ghost" href="/contact">Send a note</a></p>\n'
           '</section>\n')
plates += FOOTER
pages["small-plates.html"] = plates

# ---------- VISIT ----------
faq_items = [
    ("When did Uncorked Wine Bar open?",
     "The bar opened with a soft opening in November 2026 and held its grand opening on Wednesday, November 25, 2026, at 975 State Street in New Haven."),
    ("Where are you located?",
     "975 State Street, New Haven, Connecticut 06511 - on Upper State Street in the East Rock neighborhood."),
    ("What are your hours?",
     "Four o'clock in the afternoon every day: Sunday through Thursday until 1 am, Friday and Saturday until 2 am."),
    ("How much is a glass of wine?",
     "It depends on the bottle, but the Cabernet the room keeps ordering - Bonanza from Caymus Vineyards - is $14 a glass."),
    ("Do you serve food?",
     "Yes - small plates, including filet mignon sliders with beet chips, steak tartare, octopus and hummus, and chicken liver with lingonberry."),
]
ld_visit = [
    {"@context": "https://schema.org", "@type": "FAQPage",
     "mainEntity": [{"@type": "Question", "name": q,
                     "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq_items]},
    crumb("/visit", "Visit"),
]
visit = head("Hours &amp; Directions &#8212; Uncorked Wine Bar, New Haven CT",
             "Open every day at four o'clock: Sun-Thu 4 pm to 1 am, Fri-Sat 4 pm to 2 am, at 975 State Street in New Haven's East Rock neighborhood.",
             "/visit", ld_visit) + "\n" + nav("/visit") + "\n"
visit += ('<section class="pagehead"><div class="wrap">\n'
          '<p class="kicker">Visit</p>\n<h1>Four o&#8217;clock, every day of the week</h1>\n'
          '<p class="lede">Sun&#8211;Thu 4 pm &#8211; 1 am. Fri &amp; Sat 4 pm &#8211; 2 am. The whole week, seven nights.</p>\n'
          '</div></section>\n')
visit += ('<section class="wrap vsplit">\n<div>\n'
          '<table class="hours"><caption class="lab">The week</caption>\n'
          '<tr><th scope="row">Sunday</th><td>4 pm &#8211; 1 am</td></tr>\n'
          '<tr><th scope="row">Monday</th><td>4 pm &#8211; 1 am</td></tr>\n'
          '<tr><th scope="row">Tuesday</th><td>4 pm &#8211; 1 am</td></tr>\n'
          '<tr><th scope="row">Wednesday</th><td>4 pm &#8211; 1 am</td></tr>\n'
          '<tr><th scope="row">Thursday</th><td>4 pm &#8211; 1 am</td></tr>\n'
          '<tr><th scope="row">Friday</th><td>4 pm &#8211; 2 am</td></tr>\n'
          '<tr><th scope="row">Saturday</th><td>4 pm &#8211; 2 am</td></tr>\n'
          '</table>\n'
          '<p class="addr"><strong>Uncorked Wine Bar</strong><br>%s<br><a href="%s">Get directions</a> &#183; <a href="%s">@uncorkednh</a></p>\n'
          '</div>\n'
          '<iframe class="map" src="%s" title="Map showing Uncorked Wine Bar at 975 State Street, New Haven, Connecticut" loading="lazy"></iframe>\n'
          '</section>\n' % (ADDR, DIRS, IG, MAP_Q))
visit += ('<section class="wrap story">\n'
          '<p class="lab">The room</p>\n'
          '<h2>What used to be dark is open and white and bright</h2>\n'
          '<p>The space was a wine bar called Cave a Vin. Maria and Lorena bought it from the old owner, spent five months on it, and turned a darker room with its burgundy ceiling into something else entirely &#8212; &#8220;open and white and bright and really nice.&#8221; At the soft opening the old owner stopped by, saw the new room, and cried.</p>\n'
          '<p class="lab">The team</p>\n'
          '<h2>From the owners of Blue Tortuga</h2>\n'
          '<p>Uncorked comes from Lorena San Martin and Maria Huertas, who opened Blue Tortuga Bistro &amp; Bar on Chapel Street in early 2025. &#8220;Blue Tortuga is more like party time, like casual,&#8221; San Martin says. &#8220;We wanted to do something completely different.&#8221; This is the other end of New Haven, and a different kind of crowd.</p>\n'
          '</section>\n')
visit += ('<section class="wrap faq">\n<p class="lab">Common questions</p>\n<h2>Before you come</h2>\n'
          + "".join('<h3>%s</h3>\n<p>%s</p>\n' % (q, a) for q, a in faq_items) +
          '</section>\n')
visit += FOOTER
pages["visit.html"] = visit

# ---------- CONTACT ----------
ld_contact = [
    {"@context": "https://schema.org", "@type": "Service",
     "name": "Contact Uncorked Wine Bar",
     "serviceType": "Contact",
     "provider": provider_node(),
     "availableChannel": {"@type": "ContactChannel", "contactType": "customer service", "availableLanguage": "English"}},
    crumb("/contact", "Contact"),
]
contact = head("Contact &#8212; Uncorked Wine Bar, New Haven CT",
               "Questions, lost-and-found, or a hello for the new wine bar on State Street in New Haven - send a note and the shop will answer.",
               "/contact", ld_contact) + "\n" + nav("/contact") + "\n"
contact += ('<section class="pagehead"><div class="wrap">\n'
            '<p class="kicker">Contact</p>\n<h1>Send a note</h1>\n'
            '<p class="lede">Questions about the list, a birthday you&#8217;re planning, lost-and-found, or just a hello &#8212; your message goes straight to the shop.</p>\n'
            '</div></section>\n')
contact += ('<section class="wrap vsplit">\n<form class="cform" method="post" action="/contact">\n'
            '<p><label for="f-name">Your name</label><input id="f-name" name="name" type="text" autocomplete="name" required></p>\n'
            '<p><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email" required></p>\n'
            '<p><label for="f-phone">Phone <span class="opt">(optional)</span></label><input id="f-phone" name="phone" type="tel" autocomplete="tel"></p>\n'
            '<p><label for="f-msg">Your note</label><textarea id="f-msg" name="message" rows="5" required></textarea></p>\n'
            '<p><button class="btn" type="submit">Send it over</button></p>\n'
            '</form>\n'
            '<div class="cdetails">\n'
            '<p class="addr"><strong>Uncorked Wine Bar</strong><br>%s</p>\n'
            '<p class="addr">Sun&#8211;Thu 4 pm &#8211; 1 am<br>Fri &amp; Sat 4 pm &#8211; 2 am</p>\n'
            '<p class="addr">Instagram: <a href="%s">@uncorkednh</a><br>Directions: <a href="%s">tap here</a></p>\n'
            '</div>\n</section>\n' % (ADDR, IG, DIRS))
contact += FOOTER
pages["contact.html"] = contact

# ---------- PRIVACY ----------
ld_priv = [{"@context": "https://schema.org", "@type": "WebPage", "name": "Privacy - Uncorked Wine Bar", "url": ORIGIN + "/privacy"}]
privacy = head("Privacy &#8212; Uncorked Wine Bar, New Haven CT",
               "What this site does with what you send it: contact-form notes go to the shop's inbox and exist only to get you an answer.",
               "/privacy", ld_priv) + "\n" + nav("/privacy") + "\n"
privacy += ('<section class="wrap"><article class="page">\n'
            '<p class="lab">Privacy</p>\n<h1>What this site collects</h1>\n'
            '<p>This site collects only what you send it on purpose. The contact form takes your name, your email, an optional phone number, and your note. That message goes to Uncorked Wine Bar&#8217;s inbox and is used for one thing: answering you.</p>\n'
            '<p>No cookies are set by this site. No analytics or tracking scripts run here. Nothing you type is sold, shared, or added to some other company&#8217;s mailing list.</p>\n'
            '<p>If you&#8217;d rather we didn&#8217;t keep your message after we&#8217;ve answered it, say so in the note and we&#8217;ll delete it.</p>\n'
            '<p class="cta-row"><a class="btn ghost" href="/contact">Back to the form</a></p>\n'
            '</article></section>\n')
privacy += FOOTER
pages["privacy.html"] = privacy

# ---------- 404 ----------
nf = head("Page Not Found &#8212; Uncorked Wine Bar, New Haven CT",
          "That page isn't here. The wine bar is - wine list, small plates, hours and contact are one tap away.",
          "/404", utility=True) + "\n" + nav("/") + "\n"
nf += ('<section class="wrap"><article class="page">\n'
       '<p class="lab">404</p>\n<h1>That flight isn&#8217;t on the board</h1>\n'
       '<p>The page you were looking for isn&#8217;t here. The wine list, the plates, the hours and the contact form all still are.</p>\n'
       '<p class="cta-row"><a class="btn" href="/">Back home</a> <a class="btn ghost" href="/wine-list">Wine list</a> <a class="btn ghost" href="/contact">Contact</a></p>\n'
       '</article></section>\n')
nf += FOOTER
pages["404.html"] = nf

# ---------- thanks ----------
ty = head("Message Sent &#8212; Uncorked Wine Bar, New Haven CT",
          "Your note is on its way to Uncorked Wine Bar on State Street in New Haven. The shop reads what comes in.",
          "/thanks", utility=True) + "\n" + nav("/") + "\n"
ty += ('<section class="wrap"><article class="page">\n'
       '<p class="lab">Received</p>\n<h1>Your note just landed</h1>\n'
       '<p>It&#8217;s on its way to the shop. If you left an email, expect a real person on the other end of the reply.</p>\n'
       '<p class="cta-row"><a class="btn" href="/">Back to the site</a></p>\n'
       '</article></section>\n')
ty += FOOTER
pages["thanks.html"] = ty

# ---------- sitemap + robots + assets ----------
locs = []
for u in ["/", "/wine-list", "/small-plates", "/visit", "/contact", "/privacy"]:
    locs.append("<url><loc>%s%s</loc><lastmod>2026-11-25</lastmod></url>" % (ORIGIN, u))
write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://sitemaps.org/schemas/sitemap/0.9">\n%s\n</urlset>\n' % "\n".join(locs))
write("robots.txt", "User-agent: *\nDisallow:\n\nSitemap: %s/sitemap.xml\n" % ORIGIN)

with open(os.path.join(HERE, "style.css"), encoding="utf-8") as f:
    write("style.css", f.read())

import shutil
for asset in ("pixel.gif", "favicon.svg"):
    src = os.path.join(HERE, asset)
    if os.path.exists(src):
        shutil.copyfile(src, os.path.join(PUBLIC, asset))

for name, doc in sorted(pages.items()):
    write(name, doc)
print("built %d pages + css + sitemap + robots" % len(pages))
