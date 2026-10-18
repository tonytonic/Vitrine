# Vezoria · site vitrine (référencement Google)

Pages statiques pensées pour Google : chacune répond à une recherche précise (« organiser un voyage entre amis », « partager les dépenses d’un voyage »…) et renvoie vers l’appli (Play Store pour Android, Safari pour iPhone).

Ce ne sont pas des écrans de l’appli : ce sont des panneaux sur la route qui mènent à Vezoria.

## Ce qu’il y a dedans
- `index.html` : l’accueil (présentation, 8 points forts, destinations, guides, questions fréquentes).
- 51 guides écrits (`organiser-voyage-entre-amis.html`, `partager-depenses-voyage.html`, …) en 9 rubriques : Découvrir, Préparer, Types de voyage, Budget, Checklists, Partager, Voyager, Se souvenir, L’appli. Avec de vraies captures de l’appli.
- 56 pages destinations (`voyage-japon.html`, …), 12 pages « Où partir en … » et 11 pages par envie (`destinations-plage.html`, …) : générées à partir des données de destinations de l’appli (meilleures périodes, températures mois par mois, durée, itinéraire type, budget, formalités).
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
4. Le site s’ouvre sur `https://vezoria-site.pages.dev`.

## Faire connaître le site à Google
1. Google Search Console → Ajouter une propriété → l’adresse du site.
2. Valider la propriété (balise HTML : donne-la-moi, je l’ajoute dans les pages).
3. Sitemaps → envoyer `sitemap.xml`.

## Changer l’adresse du site (nom de domaine)
L’adresse est écrite dans `outils/generer.py` (ligne `SITE = …`) puis recopiée dans toutes les pages. Donne le nouveau domaine : tout le site est régénéré d’un coup.

## Ajouter ou modifier un guide
Tout le texte est dans `outils/pages.py`, puis `python3 outils/generer.py`.
