# -*- coding: utf-8 -*-
# Pages générées à partir des données de destinations de l'appli (outils/dests.json, extrait de l'appli Vezoria) :
# une page par destination, une page par mois (« Où partir en mars »), une page par thème, la table des prises électriques.
import json, os, re, unicodedata
HERE = os.path.dirname(__file__)
D = json.load(open(os.path.join(HERE, 'dests.json'), encoding='utf-8'))
# [nom, pays, cc, lat, lng, tags, meilleurs mois, €/jour/pers (confort), [durée min,max], itinéraire [[ville,nuits]], conseil, formalités, temp. max (jan→déc), article Wikipédia]
MOIS = ['janvier','février','mars','avril','mai','juin','juillet','août','septembre','octobre','novembre','décembre']
MOIS_C = ['janv.','févr.','mars','avr.','mai','juin','juil.','août','sept.','oct.','nov.','déc.']
VISA = {'UE':'Carte d’identité ou passeport en cours de validité suffisent pour un voyageur de l’Union européenne.',
        'FR':'Comme en France : la carte d’identité suffit pour un voyageur français.',
        'P':'Passeport demandé (souvent valable plusieurs mois après le retour).',
        'E':'Passeport et autorisation de voyage électronique à demander en ligne avant le départ (par exemple ESTA, ETA…).',
        'V':'Passeport et visa (souvent en ligne ou à l’arrivée).'}
EU_CEAM = set('AT BE BG CH CY CZ DE DK EE ES FI FR GR HR HU IE IS IT LI LT LU LV MT NL NO PL PT RO SE SI SK'.split())
FRT = {'FR', 'RE', 'GP', 'MQ', 'PF', 'NC'}
PLUG = {'OM':'G','TZ':'D/G','NA':'D/M','ZW':'D/G','GT':'A/B','PA':'A/B','BO':'A/C','CL':'L','KH':'A/C/G','LA':'A/B','PF':'A/B','DO':'A/B','GB':'G','IE':'G','MT':'G','CY':'G','HK':'G','SG':'G','MY':'G','AE':'G','QA':'G','KE':'G','US':'A/B','CA':'A/B','MX':'A/B','JP':'A/B','CO':'A/B','CU':'A/B','DO':'A/B','PH':'A/B','TW':'A/B',
        'AU':'I','NZ':'I','CN':'I/A','AR':'I','FJ':'I','CH':'J','LI':'J','IT':'L','BR':'N','IN':'D/M','ZA':'M/N','IL':'H','TH':'A/B/O','LK':'D/G','NP':'D','MV':'G','MU':'G','SC':'G','JM':'A/B','CR':'A/B','PE':'A/C','EC':'A/B','VN':'A/C','ID':'C/F'}
PAYS = {'OM':'Oman','TZ':'Tanzanie','NA':'Namibie','ZW':'Zimbabwe','GT':'Guatemala','PA':'Panama','BO':'Bolivie','CL':'Chili','KH':'Cambodge','LA':'Laos','PF':'Polynésie française','GB':'Royaume-Uni','IE':'Irlande','MT':'Malte','CY':'Chypre','HK':'Hong Kong','SG':'Singapour','MY':'Malaisie','AE':'Émirats arabes unis','QA':'Qatar','KE':'Kenya','US':'États-Unis','CA':'Canada','MX':'Mexique','JP':'Japon','CO':'Colombie','CU':'Cuba','DO':'République dominicaine','PH':'Philippines','TW':'Taïwan',
        'AU':'Australie','NZ':'Nouvelle-Zélande','CN':'Chine','AR':'Argentine','FJ':'Fidji','CH':'Suisse','LI':'Liechtenstein','IT':'Italie','BR':'Brésil','IN':'Inde','ZA':'Afrique du Sud','IL':'Israël','TH':'Thaïlande','LK':'Sri Lanka','NP':'Népal','MV':'Maldives','MU':'Maurice','SC':'Seychelles','JM':'Jamaïque','CR':'Costa Rica','PE':'Pérou','EC':'Équateur','VN':'Vietnam','ID':'Indonésie'}
REGION = {'Europe du Sud':'PT ES IT GR MT HR SI CY','France':'FR','Europe du Nord et de l’Ouest':'GB IE NL BE DE CZ AT HU IS NO FI DK SE LV CH','Europe centrale et Balkans':'PL RO BG ME AL BA MK RS','Méditerranée orientale, Moyen-Orient et Afrique du Nord':'TR MA EG JO TN OM AE GE AM','Afrique':'TZ KE ZA NA MG SN ZW','Amériques':'US CA MX CR CU DO GT PA PE BO CL AR BR CO EC','Asie':'JP TH VN ID LK UZ IN NP PH MY SG KH LA KR TW CN HK MN','Océanie':'AU NZ','Îles lointaines':'RE GP MQ PF NC CV MV MU SC'}
REG = {cc: r for r, ccs in REGION.items() for cc in ccs.split()}
THEMES = {'plage':('Destinations plage', 'Sable, mer et soleil : les destinations où la plage est au cœur du voyage.'),
          'ville':('City trips', 'Les grandes villes à découvrir le temps d’un week-end ou de quelques jours.'),
          'nature':('Destinations nature', 'Paysages, parcs et grands espaces : les voyages au grand air.'),
          'randonnée':('Destinations randonnée', 'Sentiers, montagnes et volcans : les voyages à faire à pied.'),
          'gastronomie':('Destinations gastronomiques', 'Les voyages où l’on vient d’abord pour bien manger.'),
          'culture':('Destinations culture', 'Musées, monuments, architecture : les voyages pour découvrir et comprendre.'),
          'fête':('Destinations festives', 'Les villes et les îles où les soirées comptent autant que les journées.'),
          'romantique':('Destinations romantiques', 'Les voyages à deux, pour un anniversaire, une lune de miel ou une escapade.'),
          'aventure':('Destinations aventure', 'Désert, volcans, pistes : les voyages qui sortent de l’ordinaire.'),
          'détente':('Destinations détente', 'Les voyages pour souffler, loin de tout.'),
          'histoire':('Destinations histoire', 'Les voyages au cœur de l’histoire, des ruines antiques aux vieilles villes.')}
TAGW = {'ville':'ville','culture':'culture','gastronomie':'gastronomie','mer':'mer','plage':'plage','nature':'nature','randonnée':'randonnée','aventure':'aventure','détente':'détente','histoire':'histoire','fête':'fête','romantique':'romantique','musées':'musées','montagne':'montagne','désert':'désert','vin':'vin','noel':'Noël','plongée':'plongée','shopping':'shopping','bateau':'bateau','aurores':'aurores boréales','faune':'faune','château':'châteaux','musique':'musique','bains':'bains','lac':'lacs','croisière':'croisière','neige':'neige','roadtrip':'road trip','parcs':'parcs nationaux','volcan':'volcans'}

def slugify(s):
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-z0-9]+', '-', s.replace('&', ' ')).strip('-')

def dslug(x): return 'voyage-' + slugify(x[0])
def r10(v): return int(round(v / 10.0) * 10)
def months_txt(ms):
    ms = sorted(ms)
    # regroupe les mois consécutifs : « avril à juin, septembre et octobre »
    runs, cur = [], [ms[0]]
    for m in ms[1:]:
        if m == cur[-1] + 1: cur.append(m)
        else: runs.append(cur); cur = [m]
    runs.append(cur)
    if len(runs) > 1 and runs[0][0] == 1 and runs[-1][-1] == 12: runs = [runs[-1] + runs[0]] + runs[1:-1]   # « de novembre à mars » passe le cap de l’année
    parts = [MOIS[r[0]-1] if len(r) == 1 else (MOIS[r[0]-1] + '-' + MOIS[r[-1]-1] if len(r) == 2 else 'de ' + MOIS[r[0]-1] + ' à ' + MOIS[r[-1]-1]) for r in runs]
    return parts[0] if len(parts) == 1 else ', '.join(parts[:-1]) + ' et ' + parts[-1]
def plug(cc):
    if cc in PLUG: return f'Type {PLUG[cc]} : un adaptateur est nécessaire avec des appareils français.'
    if cc in EU_CEAM or cc in FRT: return 'Les mêmes prises qu’en France (types C et E/F) : pas d’adaptateur nécessaire.'
    return ''
def tags_of(x): return x[5].split()
def mo_slug(m): return 'ou-partir-en-' + slugify(MOIS[m-1])
def th_slug(t): return 'destinations-' + slugify(t)
BY = {dslug(x): x for x in D}

def dest_page(x, E):
    nom, pays, cc, la, lo, tags, best, eur, dur, it, tip, visa, tmp, wk = x
    n_it = sum(n for _, n in it); best_s = months_txt(best)
    hot = max(range(12), key=lambda i: tmp[i]); cold = min(range(12), key=lambda i: tmp[i])
    lo_b, hi_b = r10(eur * dur[0]), r10(eur * dur[1])
    idea = ', '.join(TAGW.get(t, t) for t in tags.split()[:4])
    bars = ''.join(f'<div class="mb{" on" if (i+1) in best else ""}"><i style="height:{max(6, min(100, (tmp[i]+5)*2.6)):.0f}%"></i><b>{tmp[i]}°</b><small>{MOIS_C[i]}</small></div>' for i in range(12))
    days, d = [], 1
    for k, (v, nn) in enumerate(it):
        days.append(f'<li><b>{"J1" if d == 1 else "J" + str(d)}{"–J" + str(d + nn - 1) if nn > 1 else ""}</b> · {E(v)} <small>{nn} nuit{"s" if nn > 1 else ""}</small></li>'); d += nn
    eu_note = '<li>Carte européenne d’assurance maladie (CEAM) pour les soins.</li>' if cc in EU_CEAM else ('<li>Assurance voyage couvrant les frais médicaux et le rapatriement, vivement conseillée.</li>' if cc not in FRT else '')
    sections = [
      ('Quand partir ?', f'<p>Les meilleures périodes pour {E(nom)} : <b>{best_s}</b>. Les températures maximales moyennes vont d’environ {tmp[cold]} °C en {MOIS[cold]} à {tmp[hot]} °C en {MOIS[hot]}.</p><div class="months">{bars}</div><p class="small">Températures maximales moyennes en °C, mois par mois. En couleur : les meilleures périodes.</p>'),
      ('Combien de jours ?', f'<p>Compter <b>{dur[0]} à {dur[1]} jours</b> pour en profiter sans courir. Voici un itinéraire type de {n_it} nuits :</p><ol class="itin">{"".join(days)}</ol>'),
      ('Quel budget ?', f'<p>Sur place, en voyage « confort », compter environ <b>{eur} € par jour et par personne</b> (hébergement, repas, transports locaux et visites), soit environ <b>{lo_b} à {hi_b} €</b> par personne pour {dur[0]} à {dur[1]} jours, hors trajet aller-retour.</p><ul><li>En version économique : environ {r10(eur*0.7)} € par jour.</li><li>En version petit luxe : environ {r10(eur*1.8)} € par jour.</li></ul><p class="small">Ordres de grandeur pour comparer les destinations : les prix réels dépendent de la saison et des réservations.</p>'),
      ('Papiers et formalités', f'<ul><li>{VISA[visa]}</li>{eu_note}' + (f'<li>Prises électriques : {plug(cc)}</li>' if plug(cc) else '') + '</ul><p class="note">Règles générales pour un court séjour touristique, pour un voyageur français. Vérifiez toujours avant de partir sur diplomatie.gouv.fr (Conseils aux voyageurs) ou le site officiel du pays.</p>'),
      ('Le conseil', f'<p>{E(tip)}</p>'),
      ('Préparer ce voyage dans Vezoria', f'<p>Dans Vezoria, « Je ne sais pas encore où aller » propose {E(nom)} quand la destination correspond à tes dates, ton budget et tes envies, avec cet itinéraire type. « Créer tel quel » prépare tout le voyage d’un coup : le programme jour par jour, un hébergement par étape et les trajets. Il ne reste qu’à réserver, à plusieurs.</p>'),
    ]
    faq = [(f'Quelle est la meilleure période pour partir à {nom} ?', f'Les meilleures périodes sont {best_s}.'),
           (f'Combien de jours faut-il pour {nom} ?', f'Compter {dur[0]} à {dur[1]} jours.'),
           (f'Quel budget prévoir pour {nom} ?', f'Environ {eur} € par jour et par personne sur place en voyage confort, hors trajet aller-retour (ordre de grandeur).'),
           (f'Quels papiers pour {nom} ?', VISA[visa] + ' À vérifier sur diplomatie.gouv.fr avant le départ.')]
    sim = sorted([y for y in D if y is not x], key=lambda y: (-(y[2] == cc) - len(set(tags_of(y)) & set(tags.split())) * .3))[:3]
    return dict(slug=dslug(x), cat='Destinations', title=f'Voyage {nom} : quand partir, combien de jours, budget'[:70],
                desc=((f'Préparer un voyage {nom} ({pays}) :' if pays not in nom else f'Préparer un voyage {nom} :') + f' meilleures périodes ({best_s}), {dur[0]} à {dur[1]} jours, budget ≈ {eur} €/jour, itinéraire type et formalités.')[:158],
                h1=f'{nom} : préparer son voyage', lead=(f'{nom}, {pays}. ' if pays not in nom else f'{nom}. ') + f'Idéal pour : {idea}. À faire en {dur[0]} à {dur[1]} jours, de préférence {best_s}.',
                sections=sections, faq=faq, sim=sim, best=best, tags=tags.split(), flag=cc, eur=eur, dur=dur)

def month_page(m, E):
    L = sorted([x for x in D if m in x[6]], key=lambda x: -x[12][m-1])
    rows = ''.join(f'<a class="dl" href="{dslug(x)}"><b>{E(x[0])}</b><span>{E(x[1])}</span><span class="t">{x[12][m-1]} °C</span><span>≈ {x[7]} €/jour</span><span>{x[8][0]}–{x[8][1]} j</span></a>' for x in L)
    warm = [x for x in L if x[12][m-1] >= 25]; mild = [x for x in L if x[12][m-1] < 25]
    txt = f'<p>En {MOIS[m-1]}, {len(L)} destinations sont dans leur meilleure période{(", dont " + str(len(warm)) + " où il fait 25 °C ou plus l’après-midi") if warm else ""}.</p>'
    return dict(slug=mo_slug(m), cat='Destinations', title=f'Où partir en {MOIS[m-1]} ? {len(L)} destinations idéales',
                desc=f'Où partir en vacances en {MOIS[m-1]} : {len(L)} destinations dans leur meilleure période, avec température, budget par jour et durée idéale.'[:158],
                h1=f'Où partir en {MOIS[m-1]} ?', lead=f'Les destinations dans leur meilleure période en {MOIS[m-1]}, des plus chaudes aux plus fraîches.',
                body=txt + f'<div class="dlist"><div class="dh"><b>Destination</b><span>Pays</span><span>Max</span><span>Budget</span><span>Durée</span></div>{rows}</div>', count=len(L))

def theme_page(t, E):
    name, intro = THEMES[t]
    L = sorted([x for x in D if t in tags_of(x)], key=lambda x: x[0])
    cards = ''.join(f'<a class="pc" href="{dslug(x)}"><span class="pc-cat">{E(x[1])}</span><b>{E(x[0])}</b><small>Idéal {months_txt(x[6])} · {x[8][0]}–{x[8][1]} jours · ≈ {x[7]} €/jour</small><i class="stamp">→</i></a>' for x in L)
    return dict(slug=th_slug(t), cat='Destinations', title=f'{name} : {len(L)} idées de voyage', desc=f'{intro} {len(L)} destinations avec la meilleure période, la durée idéale et le budget par jour.'[:158],
                h1=name, lead=intro, body=f'<div class="cards">{cards}</div>', count=len(L))

def plug_page(E):
    rows = sorted(PLUG.items(), key=lambda kv: PAYS[kv[0]])
    t = ''.join(f'<tr><td>{E(PAYS[c])}</td><td><b>{p}</b></td></tr>' for c, p in rows)
    return dict(slug='adaptateur-prise-electrique-pays', cat='Checklists', title='Adaptateur de prise : quel type selon le pays ?',
                desc='Quel adaptateur de prise électrique emporter en voyage ? Le type de prise pays par pays (G, A/B, I, L…) pour un voyageur venant de France.',
                h1='Quel adaptateur de prise selon le pays ?', lead='En France, les prises sont de type C et E. Dans beaucoup de pays, il faut un adaptateur : voici lesquels.',
                body=f'<section class="block"><h2>Pas d’adaptateur nécessaire</h2><p>Dans la plupart des pays de l’Union européenne et en Islande, en Norvège, dans les territoires français d’outre-mer : les prises sont les mêmes qu’en France. Exceptions en Europe : Royaume-Uni, Irlande, Malte et Chypre (type G), Suisse (type J), Italie (type L, mais les prises C passent le plus souvent).</p></section><section class="block"><h2>Le type de prise par pays</h2><table class="tbl"><thead><tr><th>Pays</th><th>Type de prise</th></tr></thead><tbody>{t}</tbody></table><p class="note">Vérifie aussi la tension : 230 V en France, 100 à 127 V dans certains pays (Amériques, Japon). La plupart des chargeurs de téléphone et d’ordinateur acceptent les deux.</p></section><section class="block"><h2>Dans Vezoria</h2><p>La valise intelligente ajoute l’adaptateur du bon type selon les pays visités.</p></section>')
