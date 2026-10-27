# Vezoria · site vitrine (référencement Google)

Pages statiques pensées pour Google : chacune répond à une recherche précise (« organiser un voyage entre amis », « partager les dépenses d’un voyage »…) et renvoie vers l’appli (Play Store pour Android, Safari pour iPhone).

Ce ne sont pas des écrans de l’appli : ce sont des panneaux sur la route qui mènent à Vezoria.

## Ce qu’il y a dedans
- `index.html` : l’accueil (présentation, 8 points forts, destinations, guides, questions fréquentes).
- 51 guides écrits (`organiser-voyage-entre-amis.html`, `partager-depenses-voyage.html`, …) en 9 rubriques : Découvrir, Préparer, Types de voyage, Budget, Checklists, Partager, Voyager, Se souvenir, L’appli. Avec de vraies captures de l’appli.
- 176 pages destinations (`voyage-japon.html`, …), 12 pages « Où partir en … » et 11 pages par envie (`destinations-plage.html`, …) : générées depuis `outils/dests.json` (mêmes données que l’appli).
- `adaptateur-prise-electrique-pays.html` : le type de prise pays par pays.
- `guides.html` et `destinations.html` : les sommaires.
- `guide-utilisateur.html` + `assets/vezoria-guide-utilisateur.pdf` : le mode d’emploi complet à télécharger.
- `sitemap.xml`, `robots.txt`, `404.html`, `_headers` (sécurité + cache).
- Chaque page a son titre, sa description, son adresse officielle (canonical), son image de partage (réseaux sociaux) et des données structurées pour Google (article, fil d’Ariane, questions fréquentes ; l’accueil déclare une appli gratuite).
- Aucun cookie, aucune statistique, aucun service extérieur : polices et images sont dans `assets/`.

## Mettre en ligne (Cloudflare Pages)
1. GitHub → nouveau dépôt `vezoria-site` → déposer tout le contenu du zip à la racine.
2. Cloudflare → Workers & Pages → Créer → Pages → connecter le dépôt.
3. Préréglage : *Aucun*. Commande de build : *vide*. Dossier de sortie : `/`.
4. Le site s’ouvre sur `https://vezoria-site.pages.dev`, puis sur **https://vezoria.fr** une fois le domaine branché (Custom domains).

## Faire connaître le site à Google
1. Google Search Console → Ajouter une propriété → l’adresse du site.
2. Valider la propriété (balise HTML : donne-la-moi, je l’ajoute dans les pages).
3. Sitemaps → envoyer `sitemap.xml`.

## Changer l’adresse du site (nom de domaine)
L’adresse est écrite dans `outils/generer.py` (ligne `SITE = …`) puis recopiée dans toutes les pages. Donne le nouveau domaine : tout le site est régénéré d’un coup.

## Ajouter ou modifier un guide
Tout le texte est dans `outils/pages.py`, puis `python3 outils/generer.py`.

## Avant le lancement (novembre 2026)
Dans `outils/generer.py`, `PRELAUNCH = True` : les boutons d’installation (Play Store, iPhone) sont remplacés partout par l’annonce « Lancement courant novembre 2026 ».
Le jour du lancement : `PRELAUNCH = False`, puis `python3 outils/generer.py` : tous les boutons reviennent d’un coup.

## Liste « Me prévenir du lancement » et contact
- Formulaire sur toutes les pages (avant le lancement) → `functions/api/waitlist.js` (Cloudflare Pages Function) → base Cloudflare D1 liée sous le nom `DB`.
- Export CSV des inscrits : `https://vezoria.fr/api/waitlist-export?key=ADMIN_KEY` (secret `ADMIN_KEY` dans les réglages du projet Pages).
- Adresse de contact : `contact.vezoria@icloud.com`.
- Marche à suivre complète : fichier `MARCHE-A-SUIVRE.html` livré à part (pas dans le dépôt).


## Automatique (GitHub Actions)
- **Régénérer le site** : dès qu’un fichier de `outils/` change (par exemple une destination ajoutée dans `outils/dests.json` depuis l’iPhone), toutes les pages sont régénérées et enregistrées ; Cloudflare Pages publie tout seul. Lancement manuel possible : onglet Actions → « Régénérer le site » → Run workflow.
- **Climat des destinations** : onglet Actions → « Climat des destinations » → Run workflow. Met à jour les températures mois par mois de toutes les destinations avec NASA POWER (moyennes sur 30 ans, données publiques), et, si la case est cochée, recalcule aussi les meilleurs mois. Script : `outils/climat.py`.
- Les deux ont besoin, une fois : Settings → Actions → General → Workflow permissions → « Read and write permissions ».
