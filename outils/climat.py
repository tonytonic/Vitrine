# -*- coding: utf-8 -*-
# Met à jour les températures mois par mois de toutes les destinations (outils/dests.json)
# à partir de NASA POWER : moyennes climatiques sur 30 ans, données publiques, sans clé.
#   python3 outils/climat.py            → met à jour les températures (colonne 13)
#   python3 outils/climat.py --mois     → et recalcule aussi les meilleurs mois (colonne 7)
# Lancé tout seul depuis GitHub : onglet Actions → « Climat des destinations » → Run workflow.
import json, os, sys, time, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
F = os.path.join(HERE, 'dests.json')
MO = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
JOURS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
URL = ('https://power.larc.nasa.gov/api/temporal/climatology/point?parameters=T2M_MAX,PRECTOTCORR'
       '&community=RE&longitude={lng:.3f}&latitude={lat:.3f}&format=JSON')


def climat(lat, lng):
    with urllib.request.urlopen(URL.format(lat=lat, lng=lng), timeout=60) as r:
        p = json.load(r)['properties']['parameter']
    t = [round(p['T2M_MAX'][m]) for m in MO]
    w = [round(p['PRECTOTCORR'][m] * JOURS[i]) for i, m in enumerate(MO)]
    if any(x < -90 for x in t):
        raise ValueError('valeur manquante')
    return t, w


def meilleurs(t, w):
    # même règle que l’appli : 18 à 31 °C l’après-midi et moins de 150 mm de pluie dans le mois
    ok = [i + 1 for i in range(12) if 18 <= t[i] <= 31 and w[i] < 150]
    if ok:
        return ok
    sc = sorted(range(12), key=lambda i: abs(t[i] - 26) + max(0, (w[i] - 90) / 25))
    return sorted(i + 1 for i in sc[:4])


def main():
    mois = '--mois' in sys.argv
    D = json.load(open(F, encoding='utf-8'))
    n = 0
    for x in D:
        try:
            t, w = climat(x[3], x[4])
        except Exception as e:  # une destination en erreur ne bloque pas les autres
            print('⚠️', x[0], e)
            continue
        if t != x[12] or (mois and meilleurs(t, w) != x[6]):
            n += 1
        x[12] = t
        if mois:
            x[6] = meilleurs(t, w)
        print('✓', x[0], t)
        time.sleep(1)  # on reste poli avec le service de la NASA
    open(F, 'w', encoding='utf-8').write(json.dumps(D, ensure_ascii=False))
    print(f'{n} destination(s) mise(s) à jour sur {len(D)}')


if __name__ == '__main__':
    main()
