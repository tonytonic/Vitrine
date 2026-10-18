# -*- coding: utf-8 -*-
# Génère toutes les pages HTML du site à partir de outils/pages.py
#   python3 outils/generer.py
# Adresse du site, liens de l'appli : à changer ici (une seule fois).
import html, json, os, sys, datetime
sys.path.insert(0, os.path.dirname(__file__))
from pages import PAGES, FAQ_HOME
import pages2  # noqa : ajoute les guides supplémentaires
import destinations as DST

SITE   = 'https://vezoria-site.pages.dev'          # ← l'adresse du site (sans / à la fin)
APP    = 'https://vezoria.pages.dev/'                # l'appli (iPhone : à ajouter à l'écran d'accueil)
PLAY   = 'https://play.google.com/store/apps/details?id=fr.vezoria.app'
LEGAL  = 'mentions-legales'                          # pages du site (l’appli a les siennes)
PRIV   = 'confidentialite'
APP_LEGAL = 'https://vezoria.pages.dev/mentions-legales.html'
APP_PRIV  = 'https://vezoria.pages.dev/privacy.html'
CONTACT = 'appareils.treves6g@icloud.com'
MAJ = '18 octobre 2026'
TODAY  = datetime.date.today().isoformat()
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
<link rel="canonical" href="{url}">
<meta property="og:type" content="{og_type}"><meta property="og:site_name" content="Vezoria">
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/assets/img/og.jpg"><meta property="og:locale" content="fr_FR">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#2A1238">
<link rel="icon" href="assets/img/icon-192.png"><link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="preload" href="assets/fonts/outfit-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/site.css?v=3">
{ld}
</head><body>'''

def topbar():
    return f'''<header class="top"><a class="brand" href="./"><img src="assets/img/logo-vezoria.png" alt="" width="34" height="34"><span>Vezoria</span></a>
<nav><a href="./#guides">Guides</a><a href="guide-utilisateur">Mode d’emploi</a><a class="cta-mini" href="{PLAY}" data-store>Installer</a></nav></header>'''

def cta(label='Installer Vezoria gratuitement'):
    return f'''<div class="cta"><a class="btn and" href="{PLAY}" rel="noopener">🤖 Android · Play Store</a><a class="btn ios" href="{APP}" rel="noopener">🍏 iPhone · ouvrir dans Safari</a>
<small>{E(label)} · sans pub · sans compte</small></div>'''

def footer():
    cols = ''.join(f'<div><b>{E(c)}</b>' + ''.join(f'<a href="{p["slug"]}">{E(p["h1"])}</a>' for p in [q for q in PAGES if q['cat'] == c][:5]) + f'<a class="more" href="guides#{slug_cat(c)}">Tous les guides « {E(c)} » →</a></div>' for c in CATS if any(p['cat'] == c for p in PAGES))
    dst = '<div><b>Destinations</b><a href="destinations">Toutes les destinations</a>' + ''.join(f'<a href="{DST.th_slug(t)}">{E(DST.THEMES[t][0])}</a>' for t in ['plage', 'ville', 'nature', 'romantique']) + ''.join(f'<a href="{DST.mo_slug(m)}">Où partir en {DST.MOIS[m-1]}</a>' for m in NEXT3) + '</div>'
    return f'''<footer class="foot"><div class="air"></div><div class="wrap"><div class="fcols">{dst}{cols}</div>
<div class="fbot"><span>Vezoria · le carnet de voyage qu’on remplit à plusieurs</span><span><a href="guides">Tous les guides</a> · <a href="guide-utilisateur">Mode d’emploi</a> · <a href="{LEGAL}">Mentions légales</a> · <a href="{PRIV}">Confidentialité</a></span></div></div></footer>
<script src="assets/site.js?v=3" defer></script></body></html>'''

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
          'offers': {'@type': 'Offer', 'price': '0', 'priceCurrency': 'EUR'}, 'downloadUrl': PLAY, 'image': SITE + '/assets/img/og.jpg'}

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
    out = head(p['title'], p['desc'], p['slug'], 'article', lds) + topbar() + f'''
<div class="hero"><div class="wrap"><nav class="crumbs"><a href="./">Vezoria</a> › <span>{E(p["cat"])}</span></nav>
<h1>{E(p["h1"])}</h1><p class="lead">{E(p["lead"])}</p>{cta()}</div><div class="air"></div></div>
<main class="wrap">{body}{faq_html(p["faq"]) if p.get("faq") else ""}
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
home = head('Vezoria · carnet de voyage partagé, gratuit et sans pub', 'Vezoria : le carnet de voyage qu’on remplit à plusieurs. Programme jour par jour, réservations, budget partagé, checklist et souvenirs. Gratuit, sans pub, sans compte.', '', 'website', [APP_LD, faq_ld(FAQ_HOME)]) + topbar() + f'''
<div class="hero home"><div class="wrap hgrid"><div><p class="kick">Carnet de voyage partagé</p><h1>Le carnet de voyage qu’on remplit <em>à plusieurs</em></h1>
<p class="lead">Programme jour par jour, réservations, budget partagé, valise, souvenirs : tout le voyage dans une seule appli, pour tous ceux qui partent avec toi.</p>{cta()}</div>
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
def legal_page(slug, title, desc, h1, body):
    p = {'slug': slug, 'cat': 'Informations', 'title': title, 'desc': desc, 'h1': h1}
    return head(title, desc, slug, 'website', [crumbs_ld(p)]) + topbar() + f"""
<div class="hero"><div class="wrap"><nav class="crumbs"><a href="./">Vezoria</a> › <span>{E(h1)}</span></nav><h1>{E(h1)}</h1><p class="lead">Site d’information de Vezoria · dernière mise à jour : {MAJ}</p></div><div class="air"></div></div>
<main class="wrap legal">{body}</main>""" + footer()

write('mentions-legales.html', legal_page('mentions-legales', 'Mentions légales du site Vezoria', 'Mentions légales du site d’information Vezoria : éditeur, hébergement, propriété intellectuelle, responsabilité.', 'Mentions légales', f"""
<section class="block"><p>Conformément aux articles 6-III et 19 de la loi n° 2004-575 du 21 juin 2004 pour la confiance dans l’économie numérique (LCEN), voici les mentions légales du présent site d’information consacré à Vezoria (ci-après « le Site »). L’application Vezoria a ses propres <a href="{APP_LEGAL}" rel="noopener">mentions légales</a>.</p></section>
<section class="block"><h2>1. Éditeur</h2><p>Le Site est édité par un particulier, à titre personnel et non professionnel :</p><ul><li><b>Nom :</b> Anthony Chauvel</li><li><b>Qualité :</b> personne physique, éditeur non professionnel</li><li><b>Contact :</b> <a href="mailto:{CONTACT}">{CONTACT}</a></li></ul><p>Conformément à l’article 6-III-2 de la LCEN, l’éditeur non professionnel peut ne tenir à disposition du public que les éléments permettant de le contacter, son identité complète étant communiquée à l’hébergeur.</p></section>
<section class="block"><h2>2. Directeur de la publication</h2><p>Anthony Chauvel.</p></section>
<section class="block"><h2>3. Hébergement</h2><p>Le Site est hébergé par <b>GitHub Pages</b> : GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis (github.com).</p></section>
<section class="block"><h2>4. Objet du Site</h2><p>Le Site présente l’application gratuite Vezoria et propose des guides pratiques pour préparer un voyage à plusieurs. Il ne vend rien, ne contient aucune publicité et ne demande aucune inscription.</p></section>
<section class="block"><h2>5. Informations indicatives</h2><p>Les informations des guides (périodes conseillées, températures moyennes, durées, budgets, formalités, règles de voyage) sont données <b>à titre indicatif</b>, comme ordres de grandeur et règles générales. Elles peuvent évoluer et ne remplacent pas les sources officielles (diplomatie.gouv.fr, service-public.fr, sites officiels des pays, des transporteurs et des prestataires), qu’il appartient à chacun de consulter avant de partir ou de réserver.</p></section>
<section class="block"><h2>6. Responsabilité</h2><p>Le Site est fourni « en l’état ». L’éditeur ne saurait être tenu responsable d’une erreur ou d’une omission dans les informations publiées, d’une décision prise sur leur base, ni du contenu des sites externes vers lesquels le Site renvoie. Le Site est indépendant : il n’est ni affilié, ni partenaire, ni rémunéré par les sites mentionnés.</p></section>
<section class="block"><h2>7. Propriété intellectuelle</h2><p>Les textes, captures d’écran de l’application, illustrations, le nom et le logo Vezoria sont la propriété de l’éditeur. Toute reproduction sans autorisation est interdite, sauf courte citation avec un lien vers le Site. Les captures montrent le voyage de démo de l’application : les personnes et les voyages y sont fictifs.</p></section>
<section class="block"><h2>8. Données personnelles</h2><p>Le Site ne dépose aucun cookie et ne collecte aucune donnée personnelle : voir la <a href="confidentialite">politique de confidentialité</a>.</p></section>
<section class="block"><h2>9. Droit applicable</h2><p>Les présentes mentions sont soumises au droit français.</p></section>"""))

write('confidentialite.html', legal_page('confidentialite', 'Politique de confidentialité du site Vezoria', 'Le site Vezoria ne dépose aucun cookie, n’utilise aucun outil de mesure d’audience et ne collecte aucune donnée personnelle.', 'Politique de confidentialité', f"""
<section class="block"><p>Cette politique concerne le présent site d’information. L’application Vezoria a sa propre <a href="{APP_PRIV}" rel="noopener">politique de confidentialité</a>.</p>
<div class="feats"><div class="feat"><i>🍪</i><b>Aucun cookie</b><span>Ni cookie, ni traceur, ni stockage dans ton navigateur.</span></div><div class="feat"><i>📊</i><b>Aucune statistique</b><span>Pas de mesure d’audience, pas de Google Analytics.</span></div><div class="feat"><i>📢</i><b>Aucune publicité</b><span>Aucune régie, aucun réseau social intégré.</span></div><div class="feat"><i>📝</i><b>Aucun formulaire</b><span>Rien à remplir, aucun compte.</span></div></div></section>
<section class="block"><h2>1. Responsable</h2><p>Anthony Chauvel, éditeur non professionnel — <a href="mailto:{CONTACT}">{CONTACT}</a>.</p></section>
<section class="block"><h2>2. Ce que le Site ne fait pas</h2><ul><li>Il ne dépose <b>aucun cookie</b> et n’utilise <b>aucun stockage</b> dans ton navigateur.</li><li>Il n’utilise <b>aucun outil de mesure d’audience</b> ni de publicité.</li><li>Il ne charge <b>aucun service extérieur</b> : polices, images et scripts sont hébergés sur le Site lui-même.</li><li>Il ne contient <b>aucun formulaire</b> et ne demande aucune information.</li></ul></section>
<section class="block"><h2>3. Le petit script du Site</h2><p>Un script affiche le bon bouton d’installation (iPhone ou Android) et les boutons Retour, Menu et Haut de page. Pour savoir quel téléphone tu utilises, il lit le type de navigateur <b>directement dans ton navigateur</b> : rien n’est envoyé ni enregistré.</p></section>
<section class="block"><h2>4. L’hébergeur</h2><p>Comme tout hébergeur, GitHub (GitHub Pages) reçoit des données techniques au moment où une page est demandée (notamment l’adresse IP), pour acheminer la page et assurer la sécurité du service. Ces données sont traitées par GitHub selon sa propre déclaration de confidentialité ; l’éditeur n’y a pas accès.</p></section>
<section class="block"><h2>5. Liens vers d’autres sites</h2><p>En touchant un lien vers Google Play, l’application Vezoria ou un site officiel, tu quittes le Site : la politique de confidentialité de ce site s’applique alors.</p></section>
<section class="block"><h2>6. Tes droits</h2><p>Le Site ne conservant aucune donnée personnelle, il n’y a rien à consulter, rectifier ou effacer. Pour toute question : <a href="mailto:{CONTACT}">{CONTACT}</a>. Tu peux aussi adresser une réclamation à la CNIL (cnil.fr).</p></section>"""))

# ── sitemap, robots ──
urls = [('', '1.0', 'weekly'), ('guides', '0.9', 'weekly'), ('destinations', '0.9', 'weekly'), ('guide-utilisateur', '0.8', 'monthly')] + [(p['slug'], '0.8', 'monthly') for p in PAGES] + [(p['slug'], '0.7', 'monthly') for p in DPAGES + MPAGES + TPAGES + [PLUGP]] + [('mentions-legales', '0.2', 'yearly'), ('confidentialite', '0.2', 'yearly')]
write('sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>{SITE}/{u}</loc><lastmod>{TODAY}</lastmod><changefreq>{f}</changefreq><priority>{pr}</priority></url>\n' for u, pr, f in urls) + '</urlset>\n')
write('robots.txt', f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')
print(len(urls) + 1, 'pages générées')
