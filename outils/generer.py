# -*- coding: utf-8 -*-
# Génère toutes les pages HTML du site à partir de outils/pages.py
#   python3 outils/generer.py
# Adresse du site, liens de l'appli : à changer ici (une seule fois).
import html, json, os, sys, datetime
sys.path.insert(0, os.path.dirname(__file__))
from pages import PAGES, FAQ_HOME
import pages2  # noqa : ajoute les guides supplémentaires
import destinations as DST

SITE   = 'https://vezoria.fr'                       # ← l'adresse du site (sans / à la fin)
# 🚀 AVANT LE LANCEMENT : boutons d'installation masqués, remplacés par l'annonce du lancement.
#    Le jour J : mettre PRELAUNCH = False puis relancer  python3 outils/generer.py
PRELAUNCH = True
LAUNCH    = 'novembre 2026'
APP    = 'https://vezoria.pages.dev/'                # l'appli (iPhone : à ajouter à l'écran d'accueil)
PLAY   = 'https://play.google.com/store/apps/details?id=fr.vezoria.app'
LEGAL  = 'mentions-legales'                          # pages du site (l’appli a les siennes)
PRIV   = 'confidentialite'
APP_LEGAL = 'https://vezoria.pages.dev/mentions-legales.html'
APP_PRIV  = 'https://vezoria.pages.dev/privacy.html'
CONTACT = 'contact.vezoria@icloud.com'   # adresse de contact (boîte iCloud)
TODAY  = datetime.date.today().isoformat()
# 🔗 LIENS PARTENAIRES — pour l’instant de simples liens directs : aucune commission.
#    🗓️ LE 1er NOVEMBRE 2026 (début de la micro-entreprise) : mettre AFFIL = True, directement sur GitHub.
#    Le robot régénère tout le site. AFFIL = True allume d’un coup :
#      · Drive (Travelpayouts), qui transforme les liens de réservation en liens partenaires,
#        mais SEULEMENT après l’accord du visiteur (bandeau « Accepter / Refuser » les cookies) ;
#      · la mention « liens partenaires », rel="sponsored", et un lien « Cookies » en bas de page ;
#      · les mentions légales et la confidentialité version micro-entreprise (éditeur pro, cookies, commissions) ;
#      · l’autorisation du script Travelpayouts dans la sécurité du site (fichier _headers).
AFFIL = False
DRIVE = '592113'          # numéro du projet « Vezoria » (site) chez Travelpayouts ; '' = ne jamais charger Drive
# 🏢 L’ÉDITEUR PROFESSIONNEL, affiché quand AFFIL = True (la loi LCEN demande ces informations à un pro)
ENTREPRISE = 'CELMAR APPS'
SIRET   = ''              # vide = « en cours d’attribution » ; à remplir dès réception
ADRESSE = ''              # ⚠️ OBLIGATOIRE pour un pro : adresse postale (ou adresse de domiciliation)
TEL     = ''              # ⚠️ OBLIGATOIRE pour un pro : numéro de téléphone
MAJ = '1er novembre 2026' if AFFIL else '21 octobre 2026'
if AFFIL and not (ADRESSE and TEL): print('⚠️  AFFIL = True : remplis ADRESSE et TEL dans outils/generer.py (mentions légales)')
from urllib.parse import quote
# Marques choisies parmi les programmes DÉJÀ DISPONIBLES pour le projet Vezoria chez Travelpayouts (Drive ne convertit
# que celles-là) : Kiwi.com, Tiqets, Economybookings, Airalo, AirHelp. Booking.com reste en attente d'acceptation
# (programme « à débloquer ») : son lien est converti automatiquement le jour où il est accepté.
PARTNERS = {
    'kiwi':        ('✈️', 'Kiwi.com',      lambda c: 'https://www.kiwi.com/fr/'),
    'booking':     ('🛏️', 'Booking.com',   lambda c: 'https://www.booking.com/searchresults.fr.html?ss=' + quote(c) if c else 'https://www.booking.com/index.fr.html'),
    'tiqets':      ('🎟️', 'Tiqets',        lambda c: 'https://www.tiqets.com/fr/'),
    'trainline':   ('🚆', 'Trainline',     lambda c: 'https://www.thetrainline.com/fr'),
    'economy':     ('🚙', 'Economybookings', lambda c: 'https://www.economybookings.com/'),
    'airhelp':     ('🧾', 'AirHelp',       lambda c: 'https://www.airhelp.com/fr/'),
    'airalo':      ('📶', 'Airalo',        lambda c: 'https://www.airalo.com/fr'),
    'chapka':      ('🛡️', 'Chapka',        lambda c: 'https://www.chapkadirect.fr/'),
    'safetywing':  ('🛡️', 'SafetyWing',    lambda c: 'https://safetywing.com/'),
    'wise':        ('💳', 'Wise',          lambda c: 'https://wise.com/fr/'),
}
def bk_a(k, what, ctx=''):
    ic, name, url = PARTNERS[k]
    rel = 'sponsored noopener' if AFFIL else 'noopener'
    return f'<a href="{E(url(ctx))}" target="_blank" rel="{rel}">{E(what)}</a>'
# un seul lien, seulement dans les guides où il rend vraiment service
GUIDE_BK = {
    'voyager-hors-ligne':               ('airalo',      'une eSIM Airalo', 'pour avoir Internet dès l’atterrissage hors d’Europe'),
    'depenses-voyage-plusieurs-devises':('wise',        'une carte Wise', 'pour payer en devise locale sans frais de change'),
    'papiers-voyage-formalites':        ('chapka',      'Chapka', 'pour une assurance voyage hors Europe'),
    'voyage-en-train-europe':           ('trainline',   'Trainline', 'pour comparer les billets de train en Europe'),
    'road-trip-plusieurs-villes':       ('economy',     'Economybookings', 'pour comparer les locations de voiture'),
    'retard-annulation-vol-droits':     ('airhelp',     'AirHelp', 'pour faire valoir tes droits sans avancer de frais si tu ne veux pas t’en occuper toi-même'),
}
BK_NOTE = ' <small>(liens partenaires)</small>' if AFFIL else ''
def bk_box(slug):
    if slug not in GUIDE_BK: return ''
    k, what, why = GUIDE_BK[slug]
    return f'<p class="bk-l">🔗 Bon à savoir : {bk_a(k, what)} {E(why)}.{BK_NOTE}</p>'
def bk_dest(x):
    nom, it = x[0], x[9]
    city = it[0][0] if it else nom
    return f'<p class="bk-l">🔗 Pour réserver : {bk_a("kiwi", "les vols (Kiwi.com)", city)} · {bk_a("booking", "un hébergement à " + city, city)} · {bk_a("tiqets", "musées et visites (Tiqets)", city)}{BK_NOTE}</p>'
ROOT   = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E = html.escape
BY = {p['slug']: p for p in PAGES}
CATS = ['Découvrir', 'Préparer', 'Types de voyage', 'Budget', 'Checklists', 'Partager', 'Voyager', 'Se souvenir', 'L’appli']

def head(title, desc, path, og_type='article', extra_ld=()):
    url = SITE + ('/' + path if path else '/')
    ld = ''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in extra_ld)
    return f'''<!DOCTYPE html>
<html lang="fr"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="fr" href="{url}"><link rel="alternate" hreflang="x-default" href="{url}">
<meta property="og:type" content="{og_type}"><meta property="og:site_name" content="Vezoria">
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/assets/img/og.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="Vezoria, le carnet de voyage qu’on remplit à plusieurs"><meta property="og:locale" content="fr_FR">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{E(title)}"><meta name="twitter:description" content="{E(desc)}"><meta name="twitter:image" content="{SITE}/assets/img/og.jpg">
<meta name="theme-color" content="#2A1238">
<link rel="icon" href="assets/img/icon-192.png"><link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="preload" href="assets/fonts/outfit-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/site.css?v=7">
{ld}
</head><body>'''

def topbar():
    act = f'<a class="cta-mini tz-mini" href="./#lancement">🚀 {E(LAUNCH.split()[0].capitalize())}</a>' if PRELAUNCH else f'<a class="cta-mini" href="{PLAY}" data-store>Installer</a>'
    return f'''<header class="top"><a class="brand" href="./"><img src="assets/img/logo-vezoria.png" alt="" width="34" height="34"><span>Vezoria</span></a>
<nav><a href="./#guides">Guides</a><a href="guide-utilisateur">Mode d’emploi</a>{act}</nav></header>'''

TZN = [0]
def teaser(home=False, src='site'):
    TZN[0] += 1; n = TZN[0]
    return f'''<div class="cta teaser"{' id="lancement"' if home else ''}><div class="tz"><span class="tz-dot"></span><b>Lancement courant {E(LAUNCH)}</b></div>
<p>Vezoria arrive très bientôt sur Android et iPhone. En attendant, prépare ton prochain voyage avec les guides.</p>
<form class="wl" method="post" action="/api/waitlist" data-wl>
<label class="wl-l" for="wl-e{n}">Sois prévenu·e le jour du lancement</label>
<div class="wl-r"><input id="wl-e{n}" type="email" name="email" required maxlength="190" autocomplete="email" inputmode="email" placeholder="ton@email.fr"><button class="btn tz1" type="submit">Me prévenir</button></div>
<select name="interest" aria-label="Tu voyages plutôt"><option value="">Tu voyages plutôt… (facultatif)</option><option value="amis">Entre amis</option><option value="famille">En famille</option><option value="couple">En couple</option><option value="solo">En solo</option><option value="groupe">En groupe / association</option></select>
<label class="wl-c"><input type="checkbox" name="consent" value="1" required><span>J’accepte de recevoir un e-mail au lancement de Vezoria (et c’est tout). <a href="confidentialite#liste">En savoir plus</a></span></label>
<input type="text" name="site" class="wl-hp" tabindex="-1" autocomplete="off" aria-hidden="true"><input type="hidden" name="source" value="{src}">
<p class="wl-msg" role="status" aria-live="polite"></p></form>
<div class="tz-b"><a class="btn tz2" href="./#guides">📚 Lire les guides</a><a class="btn tz2" href="destinations">🌍 Trouver une destination</a></div>
<small>Gratuit · sans pub · sans compte · voyages chiffrés</small></div>'''

def cta(label='Installer Vezoria gratuitement', home=False):
    if PRELAUNCH: return teaser(home)
    return f'''<div class="cta"><a class="btn and" href="{PLAY}" rel="noopener">🤖 Android · Play Store</a><a class="btn ios" href="{APP}" rel="noopener">🍏 iPhone · ouvrir dans Safari</a>
<small>{E(label)} · sans pub · sans compte</small></div>'''

def footer():
    cols = ''.join(f'<div><b>{E(c)}</b>' + ''.join(f'<a href="{p["slug"]}">{E(p["h1"])}</a>' for p in [q for q in PAGES if q['cat'] == c][:5]) + f'<a class="more" href="guides#{slug_cat(c)}">Tous les guides « {E(c)} » →</a></div>' for c in CATS if any(p['cat'] == c for p in PAGES))
    dst = '<div><b>Destinations</b><a href="destinations">Toutes les destinations</a>' + ''.join(f'<a href="{DST.th_slug(t)}">{E(DST.THEMES[t][0])}</a>' for t in ['plage', 'ville', 'nature', 'romantique']) + ''.join(f'<a href="{DST.mo_slug(m)}">Où partir en {DST.MOIS[m-1]}</a>' for m in NEXT3) + '</div>'
    return f'''<footer class="foot"><div class="air"></div><div class="wrap"><div class="fcols">{dst}{cols}</div>
<div class="fbot"><span>Vezoria · le carnet de voyage qu’on remplit à plusieurs</span><span><a href="guides">Tous les guides</a> · <a href="guide-utilisateur">Mode d’emploi</a> · <a href="{LEGAL}">Mentions légales</a> · <a href="{PRIV}">Confidentialité</a>{CK_LINK}</span></div></div></footer>
<script src="assets/site.js?v=5" defer></script>{DRIVE_JS}</body></html>'''

ON_DRIVE = bool(AFFIL and DRIVE)
CK_LINK  = f' · <a href="{PRIV}#cookies" data-ck>Cookies</a>' if ON_DRIVE else ''
# Avant AFFIL = True, drive.js est quand même présent mais ne fait RIEN, sauf sur le téléphone de l'éditeur
# passé une fois par https://vezoria.fr/?drive=test (mode test ; ?drive=off pour l'arrêter).
DRIVE_JS = f'\n<script src="assets/drive.js?v=3" data-tp="{E(DRIVE)}" data-on="{1 if ON_DRIVE else 0}" defer></script>' if DRIVE else ''

def slug_cat(c): return DST.slugify(c)
ICON = {'Découvrir':'✨','Préparer':'🧭','Types de voyage':'🧳','Budget':'💸','Checklists':'✅','Partager':'👀','Voyager':'📍','Se souvenir':'📸','L’appli':'📱','Destinations':'🌍'}
def acc(title, inner, n=None, icon='', id_='', open_=False):
    return f'<details class="acc"{" id=" + chr(34) + id_ + chr(34) if id_ else ""}{" open" if open_ else ""}><summary><span class="ai">{icon}</span>{E(title)}</summary><div class="acc-in">{inner}</div></details>'
NEXT3 = [((datetime.date.today().month - 1 + k) % 12) + 1 for k in range(1, 4)]

def phone(img, alt):
    return f'<figure class="ph"><img src="assets/img/{img}.webp" alt="{E(alt)}" width="280" height="606" loading="lazy" decoding="async"><figcaption>{E(alt)}</figcaption></figure>'

def card(p):
    return f'<a class="pc" href="{p["slug"]}"><span class="pc-cat">{E(p["cat"])}</span><b>{E(p["h1"])}</b><small>{E(p["desc"][:110])}…</small><i class="stamp">→</i></a>'

def faq_ld(faq):
    return {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in faq]}

def crumbs_ld(p):
    return {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': 'Vezoria', 'item': SITE + '/'},
        {'@type': 'ListItem', 'position': 2, 'name': p['h1'], 'item': SITE + '/' + p['slug']}]}

APP_LD = {'@context': 'https://schema.org', '@type': 'SoftwareApplication', 'name': 'Vezoria', 'operatingSystem': 'Android, iOS',
          'applicationCategory': 'TravelApplication', 'inLanguage': 'fr', 'url': SITE + '/',
          'description': 'Carnet de voyage partagé : programme jour par jour, réservations, budget partagé, checklist, souvenirs. Gratuit, sans publicité, sans compte.',
          'offers': {'@type': 'Offer', 'price': '0', 'priceCurrency': 'EUR'}, 'image': SITE + '/assets/img/og.jpg', **({} if PRELAUNCH else {'downloadUrl': PLAY})}
ORG_LD = {'@context': 'https://schema.org', '@type': 'Organization', 'name': 'Vezoria', 'url': SITE + '/', 'logo': SITE + '/assets/img/logo-vezoria.png', 'email': CONTACT}
SITE_LD = {'@context': 'https://schema.org', '@type': 'WebSite', 'name': 'Vezoria', 'alternateName': 'Vezoria, carnet de voyage partagé', 'url': SITE + '/', 'inLanguage': 'fr'}

def faq_html(faq):
    return '<section class="block"><h2>Questions fréquentes</h2>' + ''.join(f'<details class="q"><summary>{E(q)}</summary><p>{E(a)}</p></details>' for q, a in faq) + '</section>'

def write(name, s):
    open(os.path.join(ROOT, name), 'w', encoding='utf-8').write(s)


# ── pages générées depuis les données de l'appli ──
DPAGES = [DST.dest_page(x, E) for x in DST.D]
MPAGES = [DST.month_page(m, E) for m in range(1, 13)]
TPAGES = [DST.theme_page(t, E) for t in DST.THEMES]
PLUGP = DST.plug_page(E)
for g in DPAGES + MPAGES + TPAGES + [PLUGP]: BY[g['slug']] = g
BY['destinations'] = {'slug': 'destinations', 'cat': 'Destinations', 'h1': 'Toutes les destinations', 'desc': f'{len(DST.D)} destinations avec la meilleure période, la durée idéale, le budget par jour et les formalités, pour préparer ton voyage.'}
BY['guides'] = {'slug': 'guides', 'cat': 'Découvrir', 'h1': 'Tous les guides', 'desc': 'Tous les guides pour préparer, vivre et garder un voyage à plusieurs : budget, checklists, types de voyage, l’appli.'}
BY['guide-utilisateur'] = {'slug': 'guide-utilisateur', 'cat': 'L’appli', 'h1': 'Le mode d’emploi de Vezoria', 'desc': 'Le mode d’emploi complet de Vezoria : 81 pages illustrées, chaque bouton expliqué, de l’installation aux souvenirs.'}

def simple_page(p, body, lds=(), with_cta=True):
    return head(p['title'], p['desc'], p['slug'], 'article', [crumbs_ld(p), *lds]) + topbar() + f'''
<div class="hero"><div class="wrap"><nav class="crumbs"><a href="./">Vezoria</a> › <a href="destinations">Destinations</a></nav>
<h1>{E(p["h1"])}</h1><p class="lead">{E(p["lead"])}</p>{cta() if with_cta else ""}</div><div class="air"></div></div>
<main class="wrap">{body}</main>''' + footer()

for p in DPAGES:
    x = DST.BY[p['slug']]
    body = ''.join(f'<section class="block"><h2>{E(h)}</h2>{t}</section>' + (cta('Préparer ce voyage à plusieurs') if i == 2 else '') for i, (h, t) in enumerate(p['sections']))
    body += f'<section class="block withph">{phone("idees", "Les idées de destinations dans Vezoria")}<div class="txt"><h2>Partir à plusieurs ?</h2><p>Programme jour par jour, réservations, comptes partagés, valise et souvenirs : prépare {E(x[0])} avec tes compagnons dans un seul carnet.</p><ul><li><a href="organiser-voyage-entre-amis">Organiser un voyage entre amis</a></li><li><a href="partager-depenses-voyage">Partager les dépenses</a></li><li><a href="checklist-valise-voyage">La checklist valise</a></li></ul></div></section>'
    body += bk_dest(x)
    body += faq_html(p['faq'])
    links = ''.join(f'<a class="chip" href="{DST.mo_slug(m)}">Où partir en {DST.MOIS[m-1]}</a>' for m in sorted(p['best'])) + ''.join(f'<a class="chip" href="{DST.th_slug(t)}">{E(DST.THEMES[t][0])}</a>' for t in p['tags'] if t in DST.THEMES)
    body += f'<section class="block"><h2>Autres idées</h2><div class="cards">{"".join(card(BY[DST.dslug(y)]) for y in p["sim"])}</div><div class="chips">{links}</div></section>'
    pl = {'@context': 'https://schema.org', '@type': 'TouristDestination', 'name': x[0], 'description': p['desc'], 'geo': {'@type': 'GeoCoordinates', 'latitude': x[3], 'longitude': x[4]}, 'containedInPlace': {'@type': 'Country', 'name': x[1]}}
    write(p['slug'] + '.html', simple_page(p, body, [faq_ld(p['faq']), pl]))

for p in MPAGES + TPAGES:
    other = ''.join(f'<a class="chip" href="{q["slug"]}">{E(q["h1"])}</a>' for q in (MPAGES if p in MPAGES else TPAGES) if q is not p)
    write(p['slug'] + '.html', simple_page(p, f'<section class="block">{p["body"]}</section>{cta("Prépare ton prochain voyage à plusieurs")}<section class="block"><h2>Voir aussi</h2><div class="chips">{other}</div></section>'))

write(PLUGP['slug'] + '.html', simple_page(dict(PLUGP), PLUGP['body'] + cta() + '<section class="block"><h2>À lire aussi</h2><div class="cards">' + ''.join(card(BY[s]) for s in ['checklist-valise-voyage', 'valise-intelligente', 'papiers-voyage-formalites']) + '</div></section>'))

# hub destinations
reg = ''
for r in DST.REGION:
    L = [x for x in DST.D if DST.REG.get(x[2]) == r]
    if L: reg += acc(r, '<div class="cards">' + ''.join(card(BY[DST.dslug(x)]) for x in sorted(L, key=lambda x: x[0])) + '</div>', len(L), '🌍', DST.slugify(r))
hub = {'slug': 'destinations', 'cat': 'Destinations', 'title': f'Où partir ? {len(DST.D)} destinations : période, durée, budget', 'desc': BY['destinations']['desc'], 'h1': 'Où partir ? Toutes les destinations', 'lead': 'Pour chaque destination : la meilleure période, la météo mois par mois, la durée idéale, un itinéraire type, le budget par jour et les formalités.'}
mo = ''.join(f'<a class="chip" href="{q["slug"]}">{E(DST.MOIS[i].capitalize())} </a>' for i, q in enumerate(MPAGES))
th = ''.join(f'<a class="chip" href="{q["slug"]}">{E(q["h1"])} </a>' for q in TPAGES)
write('destinations.html', simple_page(hub, f'<section class="block"><h2>Par mois</h2><div class="chips">{mo}</div></section><section class="block"><h2>Par envie</h2><div class="chips">{th}</div></section><section class="block"><h2>Par région</h2>{reg}</section>'))

# hub guides
gall = ''.join(acc(c, '<div class="cards">' + ''.join(card(p) for p in PAGES if p['cat'] == c) + '</div>', len([p for p in PAGES if p['cat'] == c]), ICON.get(c, ''), slug_cat(c)) for c in CATS if any(p['cat'] == c for p in PAGES))
gh = {'slug': 'guides', 'cat': 'Découvrir', 'title': 'Tous les guides pour voyager à plusieurs · Vezoria', 'desc': BY['guides']['desc'], 'h1': 'Tous les guides', 'lead': 'Préparer, voyager, partager, se souvenir : tous les guides pour réussir un voyage à plusieurs.'}
write('guides.html', simple_page(gh, f'<section class="block">{gall}</section><section class="block"><h2>Destinations</h2><div class="cards">{card(BY["destinations"])}{card(PLUGP)}</div></section>'))

# ── pages de contenu ──
for p in PAGES:
    art = {'@context': 'https://schema.org', '@type': 'Article', 'headline': p['h1'], 'description': p['desc'], 'inLanguage': 'fr',
           'dateModified': TODAY, 'image': SITE + '/assets/img/og.jpg', 'mainEntityOfPage': SITE + '/' + p['slug'],
           'author': {'@type': 'Organization', 'name': 'Vezoria'}, 'publisher': {'@type': 'Organization', 'name': 'Vezoria', 'logo': {'@type': 'ImageObject', 'url': SITE + '/assets/img/logo-vezoria.png'}}}
    lds = [art, crumbs_ld(p)] + ([faq_ld(p['faq'])] if p.get('faq') else [])
    shots = p.get('shots', [])
    body = ''
    for i, (h2, txt) in enumerate(p['sections']):
        fig = phone(*shots[i // 2]) if i % 2 == 0 and i // 2 < len(shots) else ''
        body += f'<section class="block{" withph" if fig else ""}{" alt" if (i // 2) % 2 else ""}">{fig}<div class="txt"><h2>{E(h2)}</h2>{txt}</div></section>'
        if i == 1: body += cta()
    rel = ''.join(card(BY[s]) for s in p.get('rel', []) if s in BY)
    soon = f'<div class="tz-note">🚀 Vezoria sera disponible courant {E(LAUNCH)} : cette page t’explique comment l’installer dès le lancement.</div>' if PRELAUNCH and p['slug'].startswith('installer-') else ''
    out = head(p['title'], p['desc'], p['slug'], 'article', lds) + topbar() + f'''
<div class="hero"><div class="wrap"><nav class="crumbs"><a href="./">Vezoria</a> › <span>{E(p["cat"])}</span></nav>
<h1>{E(p["h1"])}</h1><p class="lead">{E(p["lead"])}</p>{cta()}</div><div class="air"></div></div>
<main class="wrap">{soon}{body}{bk_box(p["slug"])}{faq_html(p["faq"]) if p.get("faq") else ""}
<section class="block"><h2>À lire aussi</h2><div class="cards">{rel}</div></section></main>''' + footer()
    write(p['slug'] + '.html', out)

# ── accueil ──
groups = ''.join(acc(c, '<div class="cards">' + ''.join(card(p) for p in PAGES if p['cat'] == c) + '</div>', len([p for p in PAGES if p['cat'] == c]), ICON.get(c, ''), slug_cat(c)) for c in CATS if any(p['cat'] == c for p in PAGES))
dhome = ''.join(card(BY[DST.dslug(x)]) for x in sorted(DST.D, key=lambda x: -x[12][NEXT3[0]-1])[:0]) + ''.join(f'<a class="chip" href="{q["slug"]}">{E(q["h1"])}</a>' for q in MPAGES) + ''.join(f'<a class="chip" href="{q["slug"]}">{E(q["h1"])}</a>' for q in TPAGES)
feat = [('🗓️', 'Le programme jour par jour', 'Étapes, hôtels, trajets et visites rangés au bon jour, pour tout le groupe.'),
        ('🎫', 'Toutes les réservations', 'Importe le mail ou la capture : la fiche se remplit, le billet reste lisible sans réseau.'),
        ('💸', 'Les comptes sans calcul', 'Qui a payé, pour qui : l’appli dit qui doit combien à qui.'),
        ('✅', 'La valise et les papiers', 'Une checklist partagée et une valise intelligente selon la météo et les pays.'),
        ('📍', 'Pendant le voyage', 'La prochaine étape, les billets, la météo, les dépenses du jour en un geste.'),
        ('📸', 'Les souvenirs', 'Photos et récits jour par jour, puis bilan, film, album et carte du monde.'),
        ('👀', 'La famille suit le voyage', 'Un simple lien, sans installer d’appli. Tu choisis ce qui est publié.'),
        ('🔒', 'Gratuit, sans pub, sans compte', 'Aucun pistage. Tes voyages partagés ne sont visibles que par tes invités.')]
fhtml = ''.join(f'<div class="feat"><i>{a}</i><b>{E(b)}</b><span>{E(c)}</span></div>' for a, b, c in feat)
home = head('Vezoria · carnet de voyage partagé, gratuit et sans pub', 'Vezoria : le carnet de voyage qu’on remplit à plusieurs. Programme jour par jour, réservations, budget partagé, checklist et souvenirs. Gratuit, sans pub, sans compte.', '', 'website', [APP_LD, ORG_LD, SITE_LD, faq_ld(FAQ_HOME)]) + topbar() + f'''
<div class="hero home"><div class="wrap hgrid"><div><p class="kick">Carnet de voyage partagé</p><h1>Le carnet de voyage qu’on remplit <em>à plusieurs</em></h1>
<p class="lead">Programme jour par jour, réservations, budget partagé, valise, souvenirs : tout le voyage dans une seule appli, pour tous ceux qui partent avec toi.</p>{cta(home=True)}</div>
<div class="hph">{phone("mes-voyages", "La liste des voyages dans Vezoria")}{phone("accueil", "L’écran principal d’un voyage")}</div></div><div class="air"></div></div>
<main class="wrap"><section class="block"><h2>Tout le voyage, au même endroit</h2><div class="feats">{fhtml}</div></section>
<section class="block three"><div><span class="ph3">🧳</span><b>Avant</b><p>On prépare ensemble : étapes, hôtels, trajets, budget, valise.</p></div><div><span class="ph3">📍</span><b>Pendant</b><p>Les billets en un geste, les dépenses notées, la journée racontée.</p></div><div><span class="ph3">🗺️</span><b>Après</b><p>Les souvenirs, le bilan, le film et l’album du voyage.</p></div></section>
<section class="block"><h2>Où partir ?</h2><p>{len(DST.D)} destinations avec la meilleure période, la météo mois par mois, la durée idéale, le budget et les formalités.</p>
{acc('Où partir selon le mois', '<div class="chips">' + ''.join(f'<a class="chip" href="{q["slug"]}">{E(DST.MOIS[i].capitalize())} </a>' for i, q in enumerate(MPAGES)) + '</div>', 12, '📅')}
{acc('Où partir selon ses envies', '<div class="chips">' + ''.join(f'<a class="chip" href="{q["slug"]}">{E(q["h1"])} </a>' for q in TPAGES) + '</div>', len(TPAGES), '💡')}
{"".join(acc(r, '<div class="cards">' + "".join(card(BY[DST.dslug(x)]) for x in sorted([x for x in DST.D if DST.REG.get(x[2]) == r], key=lambda x: x[0])) + '</div>', len([x for x in DST.D if DST.REG.get(x[2]) == r]), '🌍') for r in DST.REGION if any(DST.REG.get(x[2]) == r for x in DST.D))}
</section>
<section class="block" id="guides"><h2>Les guides</h2><p>Touche une rubrique pour l’ouvrir.</p>{groups}</section>
<section class="block guide-b"><div><h2>Le mode d’emploi complet</h2><p>81 pages illustrées, chaque bouton expliqué, de l’installation aux souvenirs.</p><a class="btn and" href="guide-utilisateur">Voir le mode d’emploi</a></div><img src="assets/img/bilan.webp" alt="Le bilan d’un voyage dans Vezoria" width="200" height="433" loading="lazy"></section>
{faq_html(FAQ_HOME)}</main>''' + footer()
write('index.html', home)

# ── mode d'emploi ──
chap = ['Bienvenue', 'Premiers pas', 'L’écran du voyage', 'Mes voyages', 'Créer un voyage', 'Le programme jour par jour', 'Les réservations', 'Le budget', 'Bagages et papiers', 'Voyager à plusieurs', 'Qui voit quoi ?', 'Les abonnés', 'Pendant le voyage', 'Souvenirs et bilan', 'Envies, notes et outils', 'Réglages et sécurité', 'Questions fréquentes']
gp = {'slug': 'guide-utilisateur', 'h1': 'Mode d’emploi de Vezoria'}
guide = head('Mode d’emploi de Vezoria (PDF illustré, 81 pages)', 'Le mode d’emploi complet de Vezoria : 81 pages illustrées, chaque bouton expliqué, de l’installation aux souvenirs. Téléchargement gratuit en PDF.', 'guide-utilisateur', 'article', [crumbs_ld(gp)]) + topbar() + f'''
<div class="hero"><div class="wrap"><nav class="crumbs"><a href="./">Vezoria</a> › <span>Mode d’emploi</span></nav><h1>Le mode d’emploi de Vezoria</h1>
<p class="lead">81 pages illustrées avec de vraies captures de l’appli : chaque bouton est expliqué dans une bulle, de l’installation aux souvenirs.</p>
<div class="cta"><a class="btn and" href="assets/vezoria-guide-utilisateur.pdf" download>📥 Télécharger le PDF (14 Mo)</a></div></div><div class="air"></div></div>
<main class="wrap"><section class="block"><h2>Au sommaire</h2><ol class="toc">{"".join(f"<li>{E(c)}</li>" for c in chap)}</ol></section>
<section class="block withph">{phone("assistant", "L’assistant de création de voyage")}<div class="txt"><h2>Pour qui ?</h2><p>Pour tous : ceux qui découvrent l’appli, ceux qui veulent tout savoir, et ceux qui veulent aider un proche à s’en servir. Le guide utilise le voyage de démo de l’appli (trois semaines au Japon avec Léo, Inès et Camille) : tu peux le charger dans l’appli et suivre les pages en même temps.</p></div></section>
{cta()}</main>''' + footer()
write('guide-utilisateur.html', guide)

# ── 404 ──
write('404.html', head('Page introuvable · Vezoria', 'Cette page n’existe pas.', '404', 'website') + topbar() + '<div class="hero"><div class="wrap"><h1>Page introuvable</h1><p class="lead">Cette page a dû partir en voyage. Retour à <a href="./" style="color:#fff">l’accueil</a>.</p></div><div class="air"></div></div><main class="wrap"><section class="block"><div class="cards">' + ''.join(card(p) for p in PAGES[:6]) + '</div></section></main>' + footer())


# ── mentions légales et confidentialité DU SITE ──
if AFFIL:
    ED_BLOCK = f'''<section class="block"><h2>1. Éditeur</h2><p>Le Site est édité par une entreprise individuelle (micro-entreprise) :</p><ul><li><b>Entrepreneur :</b> Anthony Chauvel, entrepreneur individuel (EI)</li><li><b>Nom commercial :</b> {E(ENTREPRISE)}</li><li><b>SIRET :</b> {E(SIRET) if SIRET else "en cours d’attribution"}</li>{f"<li><b>Adresse :</b> {E(ADRESSE)}</li>" if ADRESSE else ""}{f"<li><b>Téléphone :</b> {E(TEL)}</li>" if TEL else ""}<li><b>Contact :</b> <a href="mailto:{CONTACT}">{CONTACT}</a></li></ul></section>'''
    AFFIL_RESP = 'Certains liens vers des sites de réservation sont des <b>liens partenaires</b> (affiliation, via la plateforme Travelpayouts) : si tu réserves après avoir touché l’un d’eux, l’éditeur peut percevoir une commission, <b>sans aucun surcoût pour toi</b>. Ces liens sont signalés par la mention « liens partenaires ». Ils ne changent ni le contenu des guides ni le choix des sites cités, qui restent indépendants.'
else:
    ED_BLOCK = f'''<section class="block"><h2>1. Éditeur</h2><p>Le Site est édité par un particulier, à titre personnel et non professionnel :</p><ul><li><b>Nom :</b> Anthony Chauvel</li><li><b>Qualité :</b> personne physique, éditeur non professionnel</li><li><b>Contact :</b> <a href="mailto:{CONTACT}">{CONTACT}</a></li></ul><p>Conformément à l’article 6-III-2 de la LCEN, l’éditeur non professionnel peut ne tenir à disposition du public que les éléments permettant de le contacter, son identité complète étant communiquée à l’hébergeur.</p></section>'''
    AFFIL_RESP = 'Le Site est indépendant : il n’est ni affilié, ni partenaire, ni rémunéré par les sites mentionnés.'

def legal_page(slug, title, desc, h1, body):
    p = {'slug': slug, 'cat': 'Informations', 'title': title, 'desc': desc, 'h1': h1}
    return head(title, desc, slug, 'website', [crumbs_ld(p)]) + topbar() + f"""
<div class="hero"><div class="wrap"><nav class="crumbs"><a href="./">Vezoria</a> › <span>{E(h1)}</span></nav><h1>{E(h1)}</h1><p class="lead">Site d’information de Vezoria · dernière mise à jour : {MAJ}</p></div><div class="air"></div></div>
<main class="wrap legal">{body}</main>""" + footer()

write('mentions-legales.html', legal_page('mentions-legales', 'Mentions légales du site Vezoria', 'Mentions légales du site d’information Vezoria : éditeur, hébergement, propriété intellectuelle, responsabilité.', 'Mentions légales', f"""
<section class="block"><p>Conformément aux articles 6-III et 19 de la loi n° 2004-575 du 21 juin 2004 pour la confiance dans l’économie numérique (LCEN), voici les mentions légales du présent site d’information consacré à Vezoria (ci-après « le Site »). L’application Vezoria a ses propres <a href="{APP_LEGAL}" rel="noopener">mentions légales</a>.</p></section>
{ED_BLOCK}
<section class="block"><h2>2. Directeur de la publication</h2><p>Anthony Chauvel.</p></section>
<section class="block"><h2>3. Hébergement</h2><p>Le Site est hébergé par <b>Cloudflare Pages</b> : Cloudflare, Inc., 101 Townsend Street, San Francisco, CA 94107, États-Unis, tél. +1 650 319 8930 (cloudflare.com). Le nom de domaine vezoria.fr est enregistré auprès d’OVH SAS, 2 rue Kellermann, 59100 Roubaix, France.</p></section>
<section class="block"><h2>4. Objet du Site</h2><p>Le Site présente l’application gratuite Vezoria et propose des guides pratiques pour préparer un voyage à plusieurs. Il ne vend rien, ne contient aucune publicité et ne demande aucune inscription.{" Certains liens vers des sites de réservation sont des liens partenaires (voir l’article 6)." if AFFIL else ""}</p></section>
<section class="block"><h2>5. Informations indicatives</h2><p>Les informations des guides (périodes conseillées, températures moyennes, durées, budgets, formalités, règles de voyage) sont données <b>à titre indicatif</b>, comme ordres de grandeur et règles générales. Elles peuvent évoluer et ne remplacent pas les sources officielles (diplomatie.gouv.fr, service-public.fr, sites officiels des pays, des transporteurs et des prestataires), qu’il appartient à chacun de consulter avant de partir ou de réserver.</p></section>
<section class="block"><h2>6. Responsabilité</h2><p>Le Site est fourni « en l’état ». L’éditeur ne saurait être tenu responsable d’une erreur ou d’une omission dans les informations publiées, d’une décision prise sur leur base, ni du contenu des sites externes vers lesquels le Site renvoie. {AFFIL_RESP}</p></section>
<section class="block"><h2>7. Propriété intellectuelle</h2><p>Les textes, captures d’écran de l’application, illustrations, le nom et le logo Vezoria sont la propriété de l’éditeur. Toute reproduction sans autorisation est interdite, sauf courte citation avec un lien vers le Site. Les captures montrent le voyage de démo de l’application : les personnes et les voyages y sont fictifs.</p></section>
<section class="block"><h2>8. Données personnelles</h2><p>{"Le Site ne dépose aucun cookie sans ton accord : les cookies des liens partenaires ne sont déposés que si tu les acceptes." if ON_DRIVE else "Le Site ne dépose aucun cookie."} La seule donnée personnelle collectée est l’adresse e-mail que tu choisis de laisser pour être prévenu·e du lancement : voir la <a href="confidentialite">politique de confidentialité</a>.</p></section>
<section class="block"><h2>9. Droit applicable</h2><p>Les présentes mentions sont soumises au droit français.</p></section>"""))

if ON_DRIVE:
    PRIV_NOT = '''<section class="block"><h2>2. Ce que le Site ne fait pas</h2><ul><li>Il ne dépose <b>aucun cookie sans ton accord</b> : seuls les cookies des liens partenaires (article 8), si tu les acceptes.</li><li>Il n’utilise <b>aucun outil de mesure d’audience</b> ni de publicité.</li><li>Polices, images et scripts sont hébergés sur le Site lui-même ; le seul service extérieur est celui des liens partenaires, chargé <b>uniquement si tu l’acceptes</b>.</li></ul></section>'''
    PRIV_CK = '''
<section class="block" id="cookies"><h2>8. Liens partenaires et cookies</h2>
<ul><li><b>Le principe :</b> certains liens vers des sites de réservation (vols, hébergement, activités, eSIM, assurance…) sont des liens partenaires. Si tu réserves après en avoir touché un, l’éditeur peut percevoir une commission, <b>sans surcoût pour toi</b>.</li>
<li><b>Qui :</b> ces liens passent par la plateforme d’affiliation <b>Travelpayouts</b>, exploitée par Go Travel Un Limited (4007 Central Plaza, 18 Harbour Road, Wanchai, Hong Kong), puis par le site partenaire.</li>
<li><b>Les cookies :</b> pour savoir qu’une réservation vient de Vezoria, Travelpayouts et le site partenaire déposent des cookies et reçoivent des données techniques (adresse IP, navigateur, page d’origine). Ces données peuvent être traitées hors de l’Union européenne. Leurs propres politiques de confidentialité s’appliquent.</li>
<li><b>Seulement si tu acceptes :</b> au premier passage, un bandeau te laisse le choix « Accepter » ou « Refuser ». Tant que tu n’as pas accepté, rien n’est chargé depuis Travelpayouts et les liens restent de simples liens directs. Refuser ne change rien d’autre : tout le Site reste accessible.</li>
<li><b>Ton choix</b> est retenu dans ton navigateur (stockage local, sans cookie) : 6 mois si tu refuses, 13 mois si tu acceptes, puis la question t’est reposée.</li>
<li><b>Changer d’avis :</b> à tout moment avec le lien « Cookies » en bas de chaque page. Les cookies déjà déposés peuvent être effacés dans les réglages de ton navigateur.</li></ul></section>'''
else:
    PRIV_NOT = '''<section class="block"><h2>2. Ce que le Site ne fait pas</h2><ul><li>Il ne dépose <b>aucun cookie</b> et n’utilise <b>aucun stockage</b> dans ton navigateur.</li><li>Il n’utilise <b>aucun outil de mesure d’audience</b> ni de publicité.</li><li>Il ne charge <b>aucun service extérieur</b> : polices, images et scripts sont hébergés sur le Site lui-même.</li></ul></section>'''
    PRIV_CK = ''

write('confidentialite.html', legal_page('confidentialite', 'Politique de confidentialité du site Vezoria', ('Le site Vezoria n’utilise aucune mesure d’audience et ne dépose aucun cookie sans ton accord. Les cookies des liens partenaires ne sont déposés que si tu les acceptes.' if ON_DRIVE else 'Le site Vezoria ne dépose aucun cookie et n’utilise aucune mesure d’audience. Seule l’adresse e-mail laissée pour être prévenu du lancement est conservée.'), 'Politique de confidentialité', f"""
<section class="block"><p>Cette politique concerne le présent site d’information. L’application Vezoria a sa propre <a href="{APP_PRIV}" rel="noopener">politique de confidentialité</a>.</p>
<div class="feats">{'<div class="feat"><i>🍪</i><b>Aucun cookie sans ton accord</b><span>Seulement ceux des liens partenaires, et seulement si tu dis oui.</span></div>' if ON_DRIVE else '<div class="feat"><i>🍪</i><b>Aucun cookie</b><span>Ni cookie, ni traceur, ni stockage dans ton navigateur.</span></div>'}<div class="feat"><i>📊</i><b>Aucune statistique</b><span>Pas de mesure d’audience, pas de Google Analytics.</span></div><div class="feat"><i>📢</i><b>Aucune publicité</b><span>Aucune régie, aucun réseau social intégré.</span></div><div class="feat"><i>✉️</i><b>Un seul formulaire, facultatif</b><span>Ton e-mail, seulement si tu veux être prévenu·e du lancement.</span></div></div></section>
<section class="block"><h2>1. Responsable</h2><p>Anthony Chauvel, {f"entrepreneur individuel ({E(ENTREPRISE)})" if AFFIL else "éditeur non professionnel"} — <a href="mailto:{CONTACT}">{CONTACT}</a>.</p></section>
{PRIV_NOT}
<section class="block" id="liste"><h2>3. La liste « Me prévenir du lancement »</h2>
<ul><li><b>Ce qui est enregistré :</b> ton adresse e-mail, la date d’inscription, la page depuis laquelle tu t’es inscrit·e et, si tu le choisis, ta façon de voyager (entre amis, en famille…). Une empreinte chiffrée et non réversible de ton adresse IP sert seulement à bloquer les inscriptions en rafale (anti-robots) : elle est effacée automatiquement une heure après ton inscription (au prochain passage du Site) et ne permet pas de te retrouver.</li>
<li><b>Pourquoi :</b> t’envoyer <b>un seul e-mail</b> pour t’annoncer le lancement de Vezoria. Aucune lettre d’information, aucune revente, aucun partage.</li>
<li><b>Sur quelle base :</b> ton consentement (case à cocher), que tu peux retirer à tout moment.</li>
<li><b>Combien de temps :</b> jusqu’à l’envoi de l’e-mail de lancement, puis la liste est effacée, et au plus tard le 31 mars 2027.</li>
<li><b>Où :</b> dans une base de données Cloudflare D1 rattachée au Site, accessible uniquement par l’éditeur.</li>
<li><b>Te désinscrire :</b> écris à <a href="mailto:{CONTACT}">{CONTACT}</a> ; ton adresse est supprimée. L’e-mail de lancement contiendra aussi un lien de désinscription.</li></ul></section>
<section class="block"><h2>4. Le petit script du Site</h2><p>Un script affiche {"les boutons Retour, Menu et Haut de page, et envoie le formulaire « Me prévenir » sans recharger la page (et, après le lancement, le bon bouton d’installation selon ton téléphone)" if PRELAUNCH else "le bon bouton d’installation (iPhone ou Android) et les boutons Retour, Menu et Haut de page"}. Il ne lit ni n’enregistre rien d’autre.</p></section>
<section class="block"><h2>5. L’hébergeur</h2><p>Comme tout hébergeur, Cloudflare (Cloudflare Pages) reçoit des données techniques au moment où une page est demandée (notamment l’adresse IP), pour acheminer la page et assurer la sécurité du service. Ces données sont traitées par Cloudflare selon sa propre politique de confidentialité ; l’éditeur n’y a pas accès. Cloudflare peut traiter des données hors de l’Union européenne, dans le cadre des clauses contractuelles types et du cadre de protection des données UE–États-Unis.</p></section>
<section class="block"><h2>6. Liens vers d’autres sites</h2><p>En touchant un lien vers Google Play, l’application Vezoria, un site officiel ou un site de réservation (vols, hébergement, activités, eSIM, assurance…), tu quittes le Site : la politique de confidentialité de ce site s’applique alors. {"" if not AFFIL else "Certains de ces liens sont des liens partenaires (affiliation) : ils permettent au site partenaire de savoir que tu viens de Vezoria ; l’éditeur peut percevoir une commission, sans surcoût pour toi. Voir aussi l’article 8."}</p></section>
<section class="block"><h2>7. Tes droits</h2><p>Tu peux accéder à ton adresse, la faire corriger ou effacer, et retirer ton consentement : <a href="mailto:{CONTACT}">{CONTACT}</a>. Tu peux aussi adresser une réclamation à la CNIL (cnil.fr).</p></section>{PRIV_CK}"""))

# page « merci » (après le formulaire), non référencée
write('merci.html', head('Merci · Vezoria', 'Inscription à l’annonce du lancement de Vezoria.', 'merci', 'website').replace('index,follow,max-image-preview:large,max-snippet:-1', 'noindex,follow') + topbar() + f"""
<div class="hero"><div class="wrap"><h1 id="mr-t">Merci !</h1><p class="lead" id="mr-p">C’est noté : tu recevras un seul e-mail, le jour du lancement de Vezoria (courant {E(LAUNCH)}).</p>
<div class="tz-b" style="justify-content:flex-start"><a class="btn tz1" href="./#guides">📚 Lire les guides</a><a class="btn tz2" href="destinations">🌍 Trouver une destination</a></div></div><div class="air"></div></div>
<main class="wrap"><section class="block"><div class="cards">""" + ''.join(card(p) for p in PAGES[:6]) + '</div></section></main>' + footer())

# ── sitemap, robots ──
urls = [('', '1.0', 'weekly'), ('guides', '0.9', 'weekly'), ('destinations', '0.9', 'weekly'), ('guide-utilisateur', '0.8', 'monthly')] + [(p['slug'], '0.8', 'monthly') for p in PAGES] + [(p['slug'], '0.7', 'monthly') for p in DPAGES + MPAGES + TPAGES + [PLUGP]] + [('mentions-legales', '0.2', 'yearly'), ('confidentialite', '0.2', 'yearly')]
write('sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>{SITE}/{u}</loc><lastmod>{TODAY}</lastmod><changefreq>{f}</changefreq><priority>{pr}</priority></url>\n' for u, pr, f in urls) + '</urlset>\n')
CSP = ("default-src 'self'; script-src 'self' https:; style-src 'self' 'unsafe-inline'; img-src 'self' data: https:; font-src 'self'; connect-src 'self' https:; frame-src https:; object-src 'none'; base-uri 'self'; form-action 'self'; frame-ancestors 'self'; upgrade-insecure-requests"
       if DRIVE else "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'self'; object-src 'none'; base-uri 'self'; form-action 'self'; frame-ancestors 'self'; upgrade-insecure-requests")
write('_headers', f'''/*
  X-Content-Type-Options: nosniff
  X-Frame-Options: SAMEORIGIN
  Referrer-Policy: strict-origin-when-cross-origin
  Strict-Transport-Security: max-age=31536000
  Content-Security-Policy: {CSP}
  Permissions-Policy: camera=(), microphone=(), geolocation=(), payment=(), browsing-topics=()
/assets/*
  Cache-Control: public, max-age=2592000
''')
write('robots.txt', f'User-agent: *\nAllow: /\nDisallow: /api/\nDisallow: /merci\n\nSitemap: {SITE}/sitemap.xml\n')
print(len(urls) + 1, 'pages générées')
