# -*- coding: utf-8 -*-
# Guides supplémentaires : types de voyage, pratique, checklists, l'appli
from pages import page

# ───────────── Types de voyage ─────────────
page(slug='week-end-entre-amis', cat='Types de voyage',
  title='Organiser un week-end entre amis : la checklist express',
  desc='Organiser un week-end entre amis en quelques jours : choisir la date, le logement, le programme et partager les frais sans calculs. Méthode simple.',
  h1='Organiser un week-end entre amis, en un éclair',
  lead='Un week-end se prépare vite… à condition de ne pas passer trois semaines à trouver une date. Voici la méthode en quatre étapes.',
  sections=[
   ('Trouver la date', '<p>Proposez deux ou trois dates et laissez chacun répondre. Le premier week-end où tout le monde est libre gagne. Dans Vezoria, un sondage permet de voter directement dans le voyage.</p>'),
   ('Un logement pour tous', '<p>Pour un groupe, un appartement ou une maison est souvent moins cher que plusieurs chambres d’hôtel, et plus convivial. Notez le prix global : l’appli le divise entre tous.</p>'),
   ('Un programme léger', '<p>Deux jours passent vite : un ou deux temps forts par jour (une visite, un restaurant réservé, une activité), et du temps libre. Le programme jour par jour garde les horaires et les adresses.</p>'),
   ('Les frais en temps réel', '<p>Courses, essence, péage, restaurant : chacun note ce qu’il paie. Dimanche soir, l’appli dit qui doit combien à qui, avec le moins de virements possible.</p>'),
  ],
  shots=[('assistant','Créer un week-end en quelques secondes'),('comptes','Les comptes du week-end, réglés en deux virements')],
  faq=[('Combien de temps à l’avance réserver un week-end ?','Pour les week-ends prolongés et les vacances scolaires, plusieurs semaines à l’avance ; hors saison, quelques jours suffisent souvent.')],
  rel=['organiser-voyage-entre-amis','partager-depenses-voyage','valise-week-end'])

page(slug='voyage-en-famille-avec-enfants', cat='Types de voyage',
  title='Voyager en famille avec des enfants : organisation et checklist',
  desc='Préparer un voyage en famille avec des enfants : rythme, trajets, logement, valise, papiers des mineurs. Tout le voyage dans un carnet partagé.',
  h1='Voyager en famille avec des enfants',
  lead='Avec des enfants, un voyage réussi tient à un rythme adapté, des trajets courts et une valise bien pensée. Et à quelques papiers à ne pas oublier.',
  sections=[
   ('Un rythme à hauteur d’enfant', '<p>Prévoyez une seule grosse activité par jour et des pauses. Moins de changements d’hébergement, c’est moins de bagages à refaire : trois ou quatre nuits par étape est un bon rythme.</p>'),
   ('Les trajets', '<p>Découpez les longs trajets, prévoyez en-cas et occupations. Dans le programme, chaque trajet affiche ses horaires : pratique pour caler les siestes.</p>'),
   ('Les papiers des enfants', '<p>Chaque enfant a besoin de sa propre pièce d’identité (carte d’identité ou passeport selon la destination). Un mineur qui quitte la France sans un parent titulaire de l’autorité parentale doit aussi voyager avec une autorisation de sortie du territoire. Notez les documents et leurs dates d’expiration pour chaque enfant dans les documents de voyage.</p>'),
   ('Une valise par personne', '<p>La liste de bagages peut créer une liste par voyageur : chaque enfant (ou ado) coche la sienne. Pensez trousse à pharmacie, doudou et chargeurs.</p>'),
   ('Les grands-parents suivent le voyage', '<p>Publiez le voyage pour les abonnés : la famille restée à la maison voit les photos et les étapes depuis un simple lien.</p>'),
  ],
  shots=[('documents','Les documents de chaque voyageur'),('bagages','Une liste de bagages par voyageur'),('journal-abonne','Le voyage suivi par la famille')],
  faq=[('Un enfant peut-il voyager avec la carte d’identité ?','Dans l’Union européenne et l’espace Schengen, oui en général. Ailleurs, un passeport est souvent nécessaire. Vérifiez sur diplomatie.gouv.fr.')],
  rel=['papiers-voyage-enfant-mineur','valise-bebe-enfant','suivre-voyage-famille'])

page(slug='organiser-evjf-evg', cat='Types de voyage',
  title='Organiser un EVJF ou un EVG : budget, programme, surprises',
  desc='Organiser un enterrement de vie de jeune fille ou de garçon : sondage de dates, budget par personne, programme, partage des frais (sans faire payer la future mariée).',
  h1='Organiser un EVJF ou un EVG sans stress',
  lead='Un EVJF ou un EVG, c’est souvent dix personnes, un budget serré et une organisation secrète. Voici comment garder tout sous contrôle.',
  sections=[
   ('Le budget d’abord', '<p>Fixez un budget visé par personne dès le départ, et tenez-vous-y : tout le monde n’a pas les mêmes moyens. L’appli affiche la marge restante.</p>'),
   ('La personne fêtée ne paie pas', '<p>Pour que la future mariée ou le futur marié ne paie rien, partagez chaque dépense entre les autres participants seulement : il suffit de le décocher sur la fiche.</p>'),
   ('Un programme secret', '<p>Préparez le voyage entre organisateurs : la personne fêtée n’est invitée dans le voyage qu’au dernier moment, ou jamais. Les abonnés peuvent suivre les photos, sans voir le programme.</p>'),
   ('Les activités à réserver', '<p>Rangez chaque activité dans une fiche « à réserver » : elle passe au vert une fois payée. Plus de « tu as réservé le karting ? ».</p>'),
  ],
  shots=[('qui-paie','Une dépense partagée entre certains participants seulement'),('budget','Le budget par personne')],
  rel=['voyage-en-groupe','depenses-voyage-budgets-differents','week-end-entre-amis'])

page(slug='voyage-de-noces', cat='Types de voyage',
  title='Préparer son voyage de noces : itinéraire, budget, souvenirs',
  desc='Organiser son voyage de noces : choisir la destination, construire l’itinéraire, étaler le budget, garder les souvenirs et partager le voyage avec la famille.',
  h1='Préparer son voyage de noces',
  lead='Le voyage de noces se prépare souvent en même temps que le mariage. Raison de plus pour tout garder au même endroit.',
  sections=[
   ('La destination', '<p>Choisissez selon la saison du mariage : la météo varie énormément d’un mois à l’autre. Les pages destinations de ce site donnent les températures mois par mois et les meilleures périodes.</p>'),
   ('Étaler le budget', '<p>L’échéancier répartit les paiements jusqu’au départ et calcule combien mettre de côté chaque mois.</p>'),
   ('Un itinéraire à deux vitesses', '<p>Alternez découverte et repos : quelques jours actifs, puis une étape détente. L’assistant crée les étapes, les hôtels et les trajets.</p>'),
   ('Les souvenirs', '<p>Chaque jour, une photo et quelques mots. Au retour : un film, un album à imprimer et la carte de votre voyage.</p>'),
  ],
  shots=[('echeancier','L’échéancier des paiements avant le départ'),('bilan','Le bilan du voyage avec film et album')],
  rel=['voyage-en-couple','souvenirs-voyage-album','idees-de-voyage'])

page(slug='voyage-en-couple', cat='Types de voyage',
  title='Voyage en couple : s’organiser à deux sans se disputer',
  desc='Organiser un voyage en couple : se répartir la préparation, partager les frais équitablement, garder les souvenirs. Un carnet de voyage à deux.',
  h1='Voyager en couple : s’organiser à deux',
  lead='Même à deux, un voyage demande une organisation : qui réserve quoi, qui paie quoi, et où sont les billets.',
  sections=[
   ('Se répartir la préparation', '<p>L’un s’occupe des trajets, l’autre des hébergements : chacun complète le même carnet avec sa couleur, et vous voyez qui a fait quoi.</p>'),
   ('Les frais, à parts égales ou non', '<p>Parts égales, ou chacun paie ses activités : chaque dépense dit qui l’a payée et pour qui. Le solde se calcule tout seul.</p>'),
   ('La checklist commune', '<p>Passeports, adaptateur, réservation du restaurant : la checklist partagée évite les oublis de dernière minute.</p>'),
  ],
  shots=[('accueil','Un voyage préparé à deux'),('checklist','La checklist partagée')],
  rel=['voyage-de-noces','partager-depenses-voyage','checklist-valise-voyage'])

page(slug='voyage-en-groupe', cat='Types de voyage',
  title='Organiser un voyage en groupe (10 personnes et plus)',
  desc='Voyager à 10, 15 ou 20 : coordonner les dates, les chambres, les trajets de chacun et les frais. La méthode et un carnet partagé gratuit.',
  h1='Organiser un voyage en groupe, même à vingt',
  lead='À partir de dix personnes, l’organisation change de dimension : plusieurs points de départ, des chambres à répartir, des dépenses dans tous les sens.',
  sections=[
   ('Un organisateur, plusieurs contributeurs', '<p>Désignez un ou deux organisateurs, mais laissez chacun compléter : ses propres trajets, ses envies, ses dépenses. Tout le monde voit le même carnet.</p>'),
   ('Chacun son trajet', '<p>Dans un grand groupe, personne ne part du même endroit. L’assistant crée l’aller et le retour de chacun, avec son moyen de transport.</p>'),
   ('Qui dort où', '<p>Sur chaque fiche d’hébergement, cochez qui dort là : les comptes en tiennent compte, et chacun sait où il dort.</p>'),
   ('Les comptes simplifiés', '<p>Avec vingt personnes, les dettes croisées deviennent illisibles. L’appli calcule le minimum de remboursements pour tout équilibrer.</p>'),
   ('Voir le programme de quelqu’un', '<p>« Voir pour » filtre le programme d’une seule personne : chacun retrouve ses trajets et ses activités, sans se perdre dans ceux des autres.</p>'),
  ],
  shots=[('fiche-hotel','Qui dort dans quel hébergement'),('comptes','Le minimum de remboursements pour tout le groupe'),('journee','Une journée du programme')],
  rel=['organiser-voyage-entre-amis','organiser-evjf-evg','partager-depenses-voyage'])

page(slug='city-trip', cat='Types de voyage',
  title='Réussir un city trip : 3 jours dans une ville, mode d’emploi',
  desc='Préparer un city trip de 2 à 4 jours : quartiers, visites dans le bon ordre, réservations à créneau, budget. Un programme jour par jour efficace.',
  h1='Réussir un city trip de quelques jours',
  lead='Trois jours dans une grande ville, c’est court : le secret est de grouper les visites par quartier et de réserver les incontournables à l’avance.',
  sections=[
   ('Un quartier par demi-journée', '<p>Regroupez les visites proches les unes des autres. L’organisation d’une journée part de l’hôtel et range les lieux dans le meilleur ordre, avec la distance à pied acceptable.</p>'),
   ('Les visites à créneau', '<p>Musées et monuments célèbres se réservent souvent à heure fixe : notez-les en fiches « à réserver », avec l’horaire, pour qu’elles apparaissent au bon moment.</p>'),
   ('Trouver quoi faire', '<p>L’explorateur propose monuments, quartiers, musées, restaurants et bars pour chaque ville.</p>'),
  ],
  shots=[('organiser-journee','Organiser une journée de visites'),('journee','Le programme d’une journée')],
  rel=['itineraire-voyage-jour-par-jour','valise-week-end','idees-de-voyage'])

page(slug='voyage-en-train-europe', cat='Types de voyage',
  title='Voyager en train en Europe : organiser son itinéraire',
  desc='Préparer un voyage en train à travers l’Europe : étapes, correspondances, billets, horaires. Un carnet partagé qui garde tous les billets hors ligne.',
  h1='Voyager en train à travers l’Europe',
  lead='Le train, c’est le voyage lui-même. Mais plusieurs pays, c’est aussi plusieurs compagnies, plusieurs billets, plusieurs horaires à garder sous la main.',
  sections=[
   ('Des étapes de deux nuits minimum', '<p>Entre deux trains, gardez au moins une journée complète dans chaque ville. L’assistant enchaîne les étapes avec le train comme moyen de transport.</p>'),
   ('Tous les billets au même endroit', '<p>Importez chaque billet (PDF, capture, carte Wallet) : la fiche garde horaires, gares et numéro de voiture, lisibles sans réseau.</p>'),
   ('Le jour du départ', '<p>L’espace « En cours » affiche le prochain train, le temps restant et l’itinéraire jusqu’à la gare.</p>'),
  ],
  shots=[('trajets','Les trajets en train du voyage'),('en-cours','Le prochain train dans l’espace « En cours »')],
  rel=['road-trip-plusieurs-villes','importer-reservations-voyage','voyager-hors-ligne'])

page(slug='voyage-en-van', cat='Types de voyage',
  title='Préparer un voyage en van ou en camping-car',
  desc='Organiser un road trip en van : étapes, budget carburant et péages, checklist matériel, souvenirs géolocalisés. Un carnet de voyage partagé.',
  h1='Préparer un voyage en van ou en camping-car',
  lead='En van, l’itinéraire reste souple, mais le budget (carburant, péages, aires) et le matériel se préparent bien à l’avance.',
  sections=[
   ('Des étapes souples', '<p>Dessinez les grandes étapes, et ajoutez ou déplacez des jours sur la route : les journées suivantes se décalent toutes seules.</p>'),
   ('Le budget de la route', '<p>Carburant, péages, aires et parkings : notez-les au fil de l’eau, partagés entre les passagers. L’analyse des dépenses montre le coût par jour.</p>'),
   ('La checklist matériel', '<p>Câbles, cales, vaisselle, réserve d’eau : une checklist partagée où chacun coche ce qu’il emporte.</p>'),
   ('La route sur la carte', '<p>Si vous l’activez, le suivi trace votre route. Chaque « step » garde un souvenir géolocalisé.</p>'),
  ],
  shots=[('raccourcis','Les raccourcis du jour sur la route'),('checklist','La checklist matériel')],
  rel=['road-trip-plusieurs-villes','combien-prevoir-par-jour-voyage','pendant-le-voyage'])

page(slug='voyage-au-ski', cat='Types de voyage',
  title='Organiser des vacances au ski entre amis',
  desc='Préparer un séjour au ski à plusieurs : logement, forfaits, location de matériel, covoiturage et partage des frais. La valise ski incluse.',
  h1='Organiser des vacances au ski entre amis',
  lead='Logement, forfaits, location de matériel, covoiturage : un séjour au ski accumule les réservations et les dépenses partagées.',
  sections=[
   ('Les réservations', '<p>Logement, forfaits et location de matériel : une fiche pour chacun, avec le prix par personne ou global, et l’état « à réserver ».</p>'),
   ('Le covoiturage', '<p>Chacun indique comment il vient. L’essence et le péage se partagent entre les passagers de la voiture seulement.</p>'),
   ('La valise ski', '<p>La valise intelligente détecte la neige au programme et ajoute gants, masque, sous-vêtements thermiques.</p>'),
  ],
  shots=[('qui-paie','Une dépense partagée entre les passagers'),('valise','La valise intelligente')],
  rel=['valise-ski','voyage-en-groupe','partager-depenses-voyage'])

page(slug='vacances-plage-ile', cat='Types de voyage',
  title='Vacances à la plage ou sur une île : bien préparer son séjour',
  desc='Préparer des vacances au soleil : choisir la bonne période, réserver, faire sa valise plage, gérer le budget sur place. Conseils et carnet partagé.',
  h1='Vacances à la plage ou sur une île',
  lead='Le soleil ne se réserve pas : la période compte autant que la destination. Le reste se prépare tranquillement.',
  sections=[
   ('La bonne période', '<p>Saison des pluies, vents, chaleur écrasante : consultez les températures mois par mois sur nos pages destinations avant de réserver.</p>'),
   ('Ferries, vols, transferts', '<p>Sur une île, les trajets se multiplient. Rangez chaque billet dans sa fiche : ils restent lisibles sans réseau, même à l’embarcadère.</p>'),
   ('La valise plage', '<p>Maillot, crème solaire, serviette microfibre, anti-moustiques : la valise intelligente les propose selon la météo et votre programme.</p>'),
  ],
  shots=[('valise','La valise intelligente selon la météo'),('trajets','Les trajets du voyage')],
  rel=['valise-plage','destinations-plage','idees-de-voyage'])

page(slug='long-voyage-tour-du-monde', cat='Types de voyage',
  title='Préparer un long voyage ou un tour du monde',
  desc='Organiser un voyage de plusieurs mois : étapes, budget par jour, papiers et visas, sauvegarde, partage avec les proches. Un carnet qui tient la distance.',
  h1='Préparer un long voyage ou un tour du monde',
  lead='Plusieurs mois, plusieurs pays : un long voyage se pilote au budget quotidien, aux papiers, et à la sauvegarde de ses souvenirs.',
  sections=[
   ('Un budget par jour', '<p>Sur un long voyage, c’est le coût quotidien qui compte. L’analyse des dépenses donne la moyenne par jour et par personne, et les jours les plus chers.</p>'),
   ('Les papiers et visas', '<p>Passeport valable plusieurs mois après le retour, visas successifs : notez chaque document avec sa date d’expiration.</p>'),
   ('Ne rien perdre', '<p>Le Cloud Vezoria garde votre carnet pour le retrouver sur un nouveau téléphone. Une sauvegarde complète, photos comprises, peut aussi être téléchargée.</p>'),
   ('Les proches suivent', '<p>Publiez le voyage : la famille suit vos étapes depuis un lien, à son rythme.</p>'),
  ],
  shots=[('budget','Le budget du voyage'),('cloud','La sauvegarde du carnet')],
  rel=['combien-prevoir-par-jour-voyage','sauvegarde-voyage-cloud','suivre-voyage-famille'])

page(slug='voyage-solo', cat='Types de voyage',
  title='Voyager seul : s’organiser et rassurer ses proches',
  desc='Préparer un voyage en solo : itinéraire, papiers hors ligne, budget, et partager son voyage avec ses proches pour les rassurer.',
  h1='Voyager seul, bien organisé',
  lead='En solo, tout repose sur vous : avoir ses papiers et billets hors ligne et donner des nouvelles simplement change tout.',
  sections=[
   ('Tout hors ligne', '<p>Billets, réservations, copies des papiers : tout reste sur le téléphone, lisible sans réseau.</p>'),
   ('Rassurer ses proches', '<p>Publiez le voyage pour vos proches : ils voient vos étapes et vos photos. Le suivi de position, si vous l’activez, trace votre route.</p>'),
   ('Un carnet pour soi', '<p>Racontez chaque journée en quelques mots : au retour, vous avez un vrai journal de voyage.</p>'),
  ],
  shots=[('journal-abonne','Le voyage suivi par les proches'),('step','Un souvenir du jour')],
  rel=['suivre-voyage-famille','voyager-hors-ligne','ecrire-carnet-de-voyage'])

page(slug='voyage-surprise-anniversaire', cat='Types de voyage',
  title='Organiser un voyage surprise pour un anniversaire',
  desc='Préparer un voyage surprise entre organisateurs sans rien dévoiler : programme secret, cagnotte, réservations, puis partage du voyage au bon moment.',
  h1='Organiser un voyage surprise',
  lead='Un voyage surprise se prépare à plusieurs… dans le dos de la personne fêtée. Le plus dur : ne rien laisser fuiter.',
  sections=[
   ('Entre organisateurs', '<p>Créez le voyage et invitez seulement les organisateurs. La personne fêtée le rejoindra au moment de la révélation.</p>'),
   ('La cagnotte sans elle', '<p>Toutes les dépenses se partagent entre les participants, sauf la personne fêtée : il suffit de la décocher.</p>'),
   ('La révélation', '<p>Le jour J, invitez-la : elle découvre tout le programme, jour par jour.</p>'),
  ],
  shots=[('qui-paie','Une dépense partagée sans la personne fêtée'),('partager','Inviter un compagnon le moment venu')],
  rel=['organiser-evjf-evg','voyage-en-groupe','inviter-compagnons-voyage'])

# ───────────── Pratique ─────────────
page(slug='combien-prevoir-par-jour-voyage', cat='Budget',
  title='Combien prévoir par jour en voyage ? Calculer son budget quotidien',
  desc='Estimer le budget quotidien d’un voyage : hébergement, repas, transports locaux, activités. Méthode, ordres de grandeur et suivi au jour le jour.',
  h1='Combien prévoir par jour en voyage ?',
  lead='Le budget par jour est le meilleur indicateur d’un voyage : il se compare d’une destination à l’autre et se suit facilement sur place.',
  sections=[
   ('Ce qu’il comprend', '<p>Hébergement (divisé par le nombre de nuits), repas, transports sur place, visites et petites dépenses. Les vols et grands trajets se comptent à part.</p>'),
   ('Des ordres de grandeur', '<p>Le coût sur place varie fortement : une capitale d’Europe du Nord peut coûter deux à trois fois plus qu’une destination d’Asie du Sud-Est. Nos pages destinations donnent un ordre de grandeur « confort » par jour et par personne pour 56 destinations.</p>'),
   ('Suivre au jour le jour', '<p>Pendant le voyage, les dépenses du jour s’affichent face à votre plafond quotidien. L’analyse donne la moyenne par jour et par personne, et les jours les plus chers.</p>'),
  ],
  shots=[('raccourcis','Les dépenses du jour face au plafond'),('budget','Le budget total du voyage')],
  rel=['budget-voyage','destinations','long-voyage-tour-du-monde'])

page(slug='rembourser-un-ami-apres-voyage', cat='Budget',
  title='Rembourser ses amis après un voyage : la méthode la plus simple',
  desc='Après un voyage entre amis, solder les comptes en un minimum de virements : calcul automatique, suivi des remboursements, rappels sans gêne.',
  h1='Rembourser ses amis après un voyage',
  lead='« Je te dois combien déjà ? » Après le voyage, les comptes traînent souvent des semaines. Il suffit de deux minutes pour solder.',
  sections=[
   ('Le minimum de virements', '<p>Au lieu de rembourser chaque petite dépense, l’appli calcule le solde de chacun et propose le chemin le plus court : deux ou trois virements suffisent souvent.</p>'),
   ('Noter le remboursement', '<p>Une fois le virement fait, « Régler » le note : le solde passe à zéro chez tout le monde.</p>'),
   ('Demander sans gêne', '<p>« Demander » prépare un message poli avec le montant. Le bilan du voyage rappelle aussi les remboursements restants.</p>'),
  ],
  shots=[('comptes','Les remboursements à faire'),('bilan','Le bilan rappelle ce qu’il reste à régler')],
  rel=['partager-depenses-voyage','depenses-voyage-budgets-differents','budget-voyage'])

page(slug='depenses-voyage-budgets-differents', cat='Budget',
  title='Partager les frais quand on n’a pas le même budget',
  desc='Voyager entre amis aux budgets différents : dépenses communes, dépenses individuelles, parts inégales. Comment rester équitable sans gêne.',
  h1='Partager les frais quand on n’a pas le même budget',
  lead='Dans un groupe, tout le monde n’a pas les mêmes moyens. L’équité, ce n’est pas forcément tout couper en parts égales.',
  sections=[
   ('Le commun et le personnel', '<p>Le logement et les courses se partagent ; le restaurant gastronomique ou l’excursion en option, seulement entre ceux qui y vont. Chaque fiche peut être limitée à certaines personnes.</p>'),
   ('Des parts différentes', '<p>Une chambre plus grande, un couple contre un solo : répartissez en parts ou en montants plutôt qu’à parts égales.</p>'),
   ('Un objectif visible', '<p>Le budget visé par personne, affiché dès le départ, évite les mauvaises surprises pour ceux qui doivent faire attention.</p>'),
  ],
  shots=[('qui-paie','Une dépense répartie en parts différentes'),('budget','L’objectif de budget par personne')],
  rel=['partager-depenses-voyage','rembourser-un-ami-apres-voyage','organiser-evjf-evg'])

page(slug='depenses-voyage-plusieurs-devises', cat='Budget',
  title='Gérer les dépenses de voyage en plusieurs devises',
  desc='En voyage à l’étranger, noter ses dépenses en monnaie locale et les convertir automatiquement : comptes entre amis et budget toujours justes.',
  h1='Les dépenses de voyage en plusieurs devises',
  lead='Yens, livres, dirhams : à l’étranger, chaque dépense arrive dans une autre monnaie. Inutile de convertir de tête.',
  sections=[
   ('Une devise par voyage', '<p>Chaque voyage a sa devise principale : les totaux et les comptes s’affichent dans celle-ci.</p>'),
   ('Noter en monnaie locale', '<p>Saisissez le montant tel qu’il apparaît sur le ticket, dans la monnaie locale : « Convertir » le passe dans la devise du voyage.</p>'),
   ('Un voyage multi-pays', '<p>Plusieurs pays, plusieurs monnaies : chaque dépense garde sa devise d’origine, et le total reste juste.</p>'),
  ],
  shots=[('depense','Une dépense en monnaie locale, convertie')],
  rel=['partager-depenses-voyage','budget-voyage','combien-prevoir-par-jour-voyage'])

page(slug='payer-voyage-plusieurs-fois', cat='Budget',
  title='Payer un voyage en plusieurs fois : l’échéancier mois par mois',
  desc='Étaler le coût d’un voyage avant le départ : échéancier mois par mois, montant à mettre de côté pour chacun, suivi des paiements.',
  h1='Payer son voyage en plusieurs fois',
  lead='Un gros voyage se réserve parfois un an à l’avance. Étaler les paiements rend la note beaucoup plus légère.',
  sections=[
   ('À mettre de côté chaque mois', '<p>Entre aujourd’hui et le départ, l’échéancier calcule combien chacun doit mettre de côté chaque mois pour tout payer à temps.</p>'),
   ('Des échéances par réservation', '<p>Acompte, solde, paiement en trois fois : chaque réservation peut avoir ses échéances, ou être étalée automatiquement.</p>'),
   ('Cocher au fil de l’eau', '<p>Chaque mois, cochez ce qui est payé : le reste à payer se met à jour.</p>'),
  ],
  shots=[('echeancier','L’échéancier mois par mois')],
  rel=['budget-voyage','echeancier-voyage','voyage-de-noces'])

page(slug='retroplanning-voyage', cat='Préparer',
  title='Rétroplanning d’un voyage : quoi faire à J-90, J-30, J-7',
  desc='Le calendrier de préparation d’un voyage : réservations, papiers, budget, valise. Ce qu’il faut faire trois mois, un mois et une semaine avant le départ.',
  h1='Le rétroplanning d’un voyage, de J-90 à J-1',
  lead='Un voyage se prépare par étapes. Voici quoi faire, et quand, pour ne rien rater.',
  sections=[
   ('Trois mois avant', '<ul><li>Fixer les dates, les étapes et le budget.</li><li>Vérifier les papiers : passeport, visa, délais d’obtention.</li><li>Réserver les grands trajets et les hébergements clés.</li></ul>'),
   ('Un mois avant', '<ul><li>Réserver les visites à créneau.</li><li>Prendre une assurance voyage si besoin.</li><li>Organiser chaque journée dans les grandes lignes.</li></ul>'),
   ('Une semaine avant', '<ul><li>Importer tous les billets dans le carnet.</li><li>Télécharger les cartes hors ligne.</li><li>Faire la valise avec la checklist.</li></ul>'),
   ('Le niveau de préparation', '<p>Dans Vezoria, un pourcentage montre où en est la préparation, et la « prochaine étape » indique ce qu’il reste à faire.</p>'),
  ],
  shots=[('accueil','Le niveau de préparation du voyage'),('checklist','La checklist avant le départ')],
  rel=['organiser-voyage-entre-amis','papiers-voyage-formalites','checklist-valise-voyage'])

page(slug='voyager-hors-ligne', cat='Préparer',
  title='Voyager sans internet : billets, cartes et papiers hors ligne',
  desc='Garder ses billets, réservations, papiers et programme accessibles sans réseau en voyage. Ce qu’il faut préparer avant de partir.',
  h1='Voyager sans internet, sereinement',
  lead='Pas de réseau dans l’avion, à la frontière ou au fond de la vallée : vos billets doivent rester accessibles.',
  sections=[
   ('Ce qui reste disponible', '<p>Le programme, les fiches de réservation, les billets joints, les documents et la checklist sont stockés sur le téléphone : tout se consulte sans réseau.</p>'),
   ('Les cartes hors ligne', '<p>Téléchargez les cartes de vos étapes en Wi-Fi avant le départ : rues, lieux à voir et hôtels restent visibles sans données.</p>'),
   ('Ce que vous ajoutez hors ligne', '<p>Une dépense, un souvenir, une note : tout est enregistré tout de suite et partagé avec les compagnons dès que le réseau revient.</p>'),
  ],
  shots=[('raccourcis','Les papiers et billets accessibles sans réseau'),('importer','Importer ses billets avant de partir')],
  rel=['importer-reservations-voyage','pendant-le-voyage','voyage-solo'])

page(slug='retard-annulation-vol-droits', cat='Préparer',
  title='Vol en retard ou annulé : vos droits et les preuves à garder',
  desc='Vol retardé ou annulé au départ de l’Europe : indemnisation prévue par le règlement européen, preuves à garder, démarches. Points clés à vérifier.',
  h1='Vol en retard ou annulé : ce qu’il faut savoir',
  lead='Un vol retardé ou annulé peut ouvrir droit à une assistance et à une indemnisation. Encore faut-il garder les bonnes preuves.',
  sections=[
   ('Le règlement européen', '<p>Pour les vols au départ de l’Union européenne (ou à destination de l’UE sur une compagnie européenne), le règlement (CE) n° 261/2004 prévoit une assistance et, sauf circonstances extraordinaires, une indemnisation forfaitaire en cas d’annulation tardive ou de retard important à l’arrivée (à partir de 3 heures). Son montant dépend de la distance : 250 €, 400 € ou 600 €.</p><p class="note">Ces règles ont des exceptions et peuvent évoluer : vérifiez sur le site officiel de la Commission européenne (Your Europe) ou auprès de la compagnie.</p>'),
   ('Les preuves à garder', '<ul><li>La carte d’embarquement et la confirmation de réservation.</li><li>L’heure réelle d’arrivée (photo de l’écran, message de la compagnie).</li><li>Les tickets des repas ou de l’hôtel payés en attendant.</li></ul>'),
   ('Tout au même endroit', '<p>Joignez billets et tickets à la fiche du vol dans Vezoria : vous les retrouvez au moment de faire la réclamation.</p>'),
  ],
  shots=[('fiche-hotel','Une fiche avec ses pièces jointes'),('depense','Le ticket d’une dépense imprévue')],
  rel=['importer-reservations-voyage','papiers-voyage-formalites','pendant-le-voyage'])

page(slug='partager-photos-voyage-groupe', cat='Se souvenir',
  title='Partager les photos d’un voyage entre amis, jour par jour',
  desc='Rassembler les photos de tout le groupe après un voyage, rangées par jour et par lieu, sans album partagé à remplir. Puis un film et un album.',
  h1='Rassembler les photos de voyage de tout le groupe',
  lead='Chacun a ses photos dans son téléphone, et l’album partagé reste vide. Il existe plus simple.',
  sections=[
   ('Chacun ajoute les siennes', '<p>Chaque compagnon ajoute ses photos aux souvenirs du voyage : elles se rangent au bon jour grâce à leur date, et sur la carte grâce à leur lieu.</p>'),
   ('Un récit pour chaque jour', '<p>Quelques mots sous les photos suffisent à se souvenir, dix ans plus tard, de ce qu’on avait vécu ce jour-là.</p>'),
   ('Le film et l’album', '<p>Au retour, le voyage se revit en film et en album à imprimer.</p>'),
  ],
  shots=[('souvenir','Ajouter des photos à un souvenir'),('bilan','Film et album du voyage')],
  rel=['souvenirs-voyage-album','film-de-voyage','album-photo-voyage'])

page(slug='ecrire-carnet-de-voyage', cat='Se souvenir',
  title='Écrire son carnet de voyage : idées et méthode simple',
  desc='Tenir un carnet de voyage sans y passer des heures : un souvenir par jour, une photo, quelques phrases. Idées pour écrire et garder ses souvenirs.',
  h1='Écrire son carnet de voyage, simplement',
  lead='Pas besoin d’être écrivain : un carnet de voyage réussi tient en quelques phrases par jour.',
  sections=[
   ('Une scène par jour', '<p>Plutôt que tout raconter, choisissez un moment : un repas, une rencontre, une vue. Un titre, deux ou trois phrases, une photo.</p>'),
   ('Les détails qu’on oublie', '<p>Le nom du petit restaurant, le prix du café, la météo, ce qu’a dit Léo : ce sont les détails qui font revivre le voyage.</p>'),
   ('Le faire sur place', '<p>Un « step » se fait en trente secondes, là où vous êtes : la position est enregistrée, il ne reste qu’à écrire.</p>'),
  ],
  shots=[('step','Un souvenir écrit sur place'),('souvenir','Le récit d’une journée')],
  rel=['souvenirs-voyage-album','voyage-solo','partager-photos-voyage-groupe'])

page(slug='choisir-destination-entre-amis', cat='Préparer',
  title='Choisir une destination entre amis sans débat sans fin',
  desc='Se mettre d’accord sur une destination à plusieurs : idées selon dates et budget, liste d’envies commune, vote. La méthode pour décider vite.',
  h1='Choisir une destination entre amis, sans débat sans fin',
  lead='« On va où ? » Trois semaines plus tard, toujours pas de réponse. Voici comment trancher vite et bien.',
  sections=[
   ('Poser le cadre', '<p>Dates, durée, budget maximum, temps de trajet acceptable : ces quatre critères éliminent déjà la plupart des options.</p>'),
   ('Laisser chacun proposer', '<p>Les envies de chacun (une ville, une plage, un week-end) se rangent dans un espace commun. Plus rien ne se perd dans la conversation.</p>'),
   ('Des idées qui collent au cadre', '<p>Pas d’idée ? La recherche de destinations propose des voyages adaptés à vos dates et à votre budget, avec météo et itinéraire type.</p>'),
   ('Voter', '<p>Un sondage dans le voyage, et la décision est prise.</p>'),
  ],
  shots=[('idees','Des idées de destinations selon les réponses'),('nouveau','Créer le voyage choisi')],
  rel=['idees-de-voyage','destinations','organiser-voyage-entre-amis'])

# ───────────── Checklists ─────────────
def checklist(slug, title, desc, h1, lead, groups, tip, rel, faq=None):
    secs = [(g, '<ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>') for g, items in groups]
    secs.append(('La liste qui s’adapte à ton voyage', '<p>' + tip + '</p>'))
    page(slug=slug, cat='Checklists', title=title, desc=desc, h1=h1, lead=lead, sections=secs,
         shots=[('valise','La valise intelligente de Vezoria'),('checklist','La checklist partagée du voyage'),('bagages','La liste de bagages')], faq=faq or [], rel=rel)

checklist('valise-week-end', 'Valise week-end : la liste pour partir léger (2-3 jours)',
  'La liste de valise pour un week-end de deux ou trois jours : vêtements, trousse de toilette, électronique, papiers. Partir léger sans rien oublier.',
  'La valise d’un week-end : partir léger', 'Pour deux ou trois jours, un bagage cabine suffit, à condition de bien choisir.',
  [('Vêtements', ['2 ou 3 hauts, 1 pantalon de rechange','1 pull ou une veste selon la météo','Sous-vêtements et chaussettes pour chaque jour','1 tenue un peu plus habillée pour le dîner','Chaussures confortables pour marcher']),
   ('Trousse de toilette', ['Brosse à dents, dentifrice, déodorant','Médicaments personnels','Liquides en petits formats si vous prenez l’avion']),
   ('Électronique et papiers', ['Téléphone, chargeur, batterie externe','Carte d’identité, carte bancaire','Billets et réservation du logement'])],
  'La valise intelligente regarde la météo de l’étape et le programme pour ajouter ce qui manque, puis la checklist est partagée avec tes compagnons.',
  ['week-end-entre-amis','valise-cabine-liquides','checklist-valise-voyage'])

checklist('valise-ski', 'Valise ski : la liste complète pour la montagne',
  'Que mettre dans sa valise pour le ski : vêtements techniques, accessoires, après-ski, papiers et santé. La liste complète à cocher.',
  'La valise ski : ne rien oublier pour la montagne', 'Le froid ne pardonne pas les oublis : voici la liste complète, des sous-couches à l’après-ski.',
  [('Sur les pistes', ['Veste et pantalon de ski','Sous-vêtements thermiques','Polaire ou couche intermédiaire','Gants, bonnet, tour de cou','Masque et lunettes de soleil','Chaussettes de ski']),
   ('Après-ski', ['Après-ski ou chaussures chaudes','Vêtements confortables pour le chalet','Maillot de bain si spa ou piscine']),
   ('Santé', ['Crème solaire haute protection','Baume à lèvres','Petite trousse à pharmacie'])],
  'Quand la neige ou le ski sont au programme, la valise intelligente ajoute d’elle-même gants, masque et sous-vêtements thermiques.',
  ['voyage-au-ski','trousse-pharmacie-voyage','checklist-valise-voyage'])

checklist('valise-plage', 'Valise plage et vacances au soleil : la liste',
  'La liste de valise pour des vacances à la plage : maillots, protection solaire, tenues légères, accessoires, santé. À cocher avant de partir.',
  'La valise plage : la liste des vacances au soleil', 'Soleil, mer et chaleur : une valise légère, mais avec quelques indispensables.',
  [('Plage', ['Maillots de bain (deux, pour qu’ils sèchent)','Serviette microfibre','Chapeau ou casquette, lunettes de soleil','Sandales ou chaussures d’eau','Sac de plage']),
   ('Protection', ['Crème solaire et après-soleil','Anti-moustiques','Gourde']),
   ('Vêtements', ['Tenues légères, en lin ou en coton','Une tenue qui couvre épaules et genoux pour les lieux de culte','Un pull léger pour les soirées'])],
  'Au-dessus de 24 °C sur une étape, la valise intelligente propose crème solaire, shorts et lunettes ; avec la plage au programme, maillot et serviette.',
  ['vacances-plage-ile','destinations-plage','trousse-pharmacie-voyage'])

checklist('valise-bebe-enfant', 'Voyager avec un bébé ou un enfant : la checklist',
  'La liste de valise pour voyager avec un bébé ou un jeune enfant : papiers, repas, sommeil, change, santé et occupations pendant le trajet.',
  'Voyager avec un bébé ou un enfant : la checklist', 'Avec un enfant, la valise double de volume. Voici l’essentiel, sans le superflu.',
  [('Papiers', ['Pièce d’identité de l’enfant (carte ou passeport selon la destination)','Carnet de santé','Autorisation de sortie du territoire si l’enfant voyage sans un parent titulaire de l’autorité parentale']),
   ('Repas et sommeil', ['Biberons, lait, petits pots ou en-cas','Doudou et tétine','Turbulette ou gigoteuse','Lit parapluie si le logement n’en fournit pas']),
   ('Change et santé', ['Couches et lingettes pour le trajet et les premiers jours','Thermomètre, antipyrétique adapté, sérum physiologique','Crème solaire enfant']),
   ('Pendant le trajet', ['Jouets, livres, écouteurs','Vêtements de rechange à portée de main'])],
  'La liste de bagages peut créer une liste par voyageur, et l’option « avec enfants » ajoute ce qu’il faut pour eux.',
  ['voyage-en-famille-avec-enfants','papiers-voyage-enfant-mineur','trousse-pharmacie-voyage'])

checklist('trousse-pharmacie-voyage', 'Trousse à pharmacie de voyage : quoi emporter',
  'Composer sa trousse à pharmacie de voyage : soins de base, médicaments courants, protection solaire et anti-moustiques. Liste indicative à adapter avec un professionnel.',
  'La trousse à pharmacie de voyage', 'Une petite trousse évite de chercher une pharmacie le premier soir. À adapter avec ton médecin ou ton pharmacien.',
  [('Soins de base', ['Pansements, compresses, désinfectant','Pince à épiler, ciseaux','Sérum physiologique']),
   ('Médicaments courants', ['Tes traitements habituels, avec l’ordonnance','Antidouleur et anti-fièvre habituels','Ce que ton médecin te conseille pour la destination']),
   ('Selon la destination', ['Crème solaire, après-soleil','Anti-moustiques','Pastilles pour l’eau si besoin'])],
  'La valise intelligente ajoute la trousse à pharmacie, la crème solaire et l’anti-moustiques selon la chaleur de tes étapes.',
  ['checklist-valise-voyage','papiers-voyage-formalites','valise-plage'],
  faq=[('Peut-on prendre ses médicaments en cabine ?','En général oui, dans leur emballage d’origine et avec l’ordonnance. Vérifiez les règles de la compagnie et du pays de destination.')])

checklist('valise-cabine-liquides', 'Bagage cabine : liquides, règles et liste',
  'Préparer son bagage cabine : la règle des liquides (100 ml dans un sachet transparent), les objets interdits, ce qu’il faut garder sur soi.',
  'Le bagage cabine : liquides et liste', 'En cabine, la règle la plus connue reste celle des liquides. Le reste, c’est du bon sens.',
  [('La règle des liquides', ['Contenants de 100 ml maximum','Tous dans un sachet transparent refermable d’environ 1 litre','Exceptions habituelles : médicaments et aliments pour bébé, à présenter au contrôle']),
   ('À garder sur soi', ['Papiers d’identité et billets','Médicaments','Chargeur et batterie externe (les batteries vont en cabine, pas en soute)','Un pull pour l’avion']),
   ('Confort', ['Coussin de voyage, bouchons d’oreilles','Écouteurs','Gourde vide à remplir après le contrôle'])],
  'Quand un vol est au programme, la valise intelligente ajoute le sachet de liquides de moins de 100 ml et le confort de voyage.',
  ['valise-week-end','checklist-valise-voyage','voyager-hors-ligne'],
  faq=[('La règle des 100 ml s’applique-t-elle partout ?','Certains aéroports assouplissent la règle grâce à de nouveaux scanners, mais pas tous : préparez votre sachet par défaut et vérifiez auprès de l’aéroport.')])

page(slug='papiers-voyage-enfant-mineur', cat='Checklists',
  title='Papiers d’un enfant mineur pour voyager : la liste',
  desc='Quels papiers pour faire voyager un enfant mineur : pièce d’identité, autorisation de sortie du territoire, carnet de santé. Points à vérifier avant le départ.',
  h1='Les papiers d’un enfant mineur pour voyager',
  lead='Un enfant a besoin de ses propres papiers, et parfois d’une autorisation. Mieux vaut le savoir avant l’aéroport.',
  sections=[
   ('Sa propre pièce d’identité', '<p>Chaque enfant, même bébé, doit avoir sa carte d’identité ou son passeport selon la destination.</p>'),
   ('L’autorisation de sortie du territoire', '<p>Un mineur résidant en France qui quitte le territoire sans être accompagné d’un parent titulaire de l’autorité parentale (avec ses grands-parents, en colonie, avec un seul ami de la famille…) doit présenter une autorisation de sortie du territoire (formulaire officiel), accompagnée de la copie de la pièce d’identité du parent signataire.</p>'),
   ('Les autres documents', '<ul><li>Le carnet de santé.</li><li>Un livret de famille ou un acte de naissance peut être utile si les noms diffèrent.</li><li>Les éventuels visas, comme pour un adulte.</li></ul><p class="note">Vérifiez toujours les règles en vigueur sur service-public.fr et diplomatie.gouv.fr avant de partir.</p>'),
   ('Les dates d’expiration de chacun', '<p>Dans Vezoria, les documents de voyage se notent par voyageur, avec leur date d’expiration : l’appli prévient si l’un expire trop tôt.</p>'),
  ],
  shots=[('documents','Les documents de chaque voyageur')],
  rel=['voyage-en-famille-avec-enfants','valise-bebe-enfant','papiers-voyage-formalites'])

# ───────────── L'appli ─────────────
def feat(slug, title, desc, h1, lead, secs, shots, rel, faq=None):
    page(slug=slug, cat='L’appli', title=title, desc=desc, h1=h1, lead=lead, sections=secs, shots=shots, faq=faq or [], rel=rel)

feat('valise-intelligente', 'La valise intelligente : une liste selon la météo et les pays',
  'La valise intelligente de Vezoria propose ta liste de bagages selon la météo de tes étapes, ton programme et les pays visités. Partagée avec tes compagnons.',
  'La valise intelligente', 'Elle regarde la météo de chaque étape, ton programme et les pays visités, puis propose ce qu’il faut emporter.',
  [('Selon la météo', '<p>Manteau sous 5 °C, pull le matin frais, shorts et crème solaire au-dessus de 24 °C, K-way si la pluie est annoncée sur une étape.</p>'),
   ('Selon le programme', '<p>Randonnée, plage, bains, ski, lieux de culte, vol, train : chaque activité ajoute ce qui lui correspond.</p>'),
   ('Selon les pays', '<p>Passeport ou carte d’identité, formalités d’entrée, carte européenne d’assurance maladie, type de prise électrique : selon les pays visités et la nationalité du passeport. Ajoute autant de pays que tu veux.</p>'),
   ('Dans la checklist', '<p>Décoche ce qui ne te sert pas : le reste rejoint la checklist partagée.</p>')],
  [('valise','La valise intelligente avec les pays visités'),('checklist','La checklist partagée')],
  ['checklist-valise-voyage','adaptateur-prise-electrique-pays','papiers-voyage-formalites'])

feat('carte-du-monde-pays-visites', 'Carte du monde de ses voyages et pays visités',
  'Tous tes voyages sur une carte du monde en 3D : pays visités, étapes, kilomètres. Et le pourcentage du monde déjà parcouru.',
  'La carte du monde de tes voyages', 'Tous tes voyages sur un globe à faire tourner du bout des doigts.',
  [('Les pays visités', '<p>Chaque pays visité s’allume, d’après les villes de tes hébergements et tes souvenirs. Le compteur affiche le nombre de pays et la part du monde parcourue.</p>'),
   ('Les étapes et la route', '<p>Les étapes de chaque voyage et, si tu l’as activé, la route suivie.</p>'),
   ('Les badges', '<p>Globe-trotter, explorateur, photographe… des badges se débloquent au fil de tes voyages.</p>')],
  [('bilan','Le voyage survolé sur le globe')],
  ['souvenirs-voyage-album','film-de-voyage','long-voyage-tour-du-monde'])

feat('film-de-voyage', 'Faire un film de son voyage avec ses photos',
  'Revivre son voyage en film : tes photos et tes étapes s’enchaînent automatiquement, jour après jour. À regarder ou à partager.',
  'Le film de ton voyage', 'Au retour, tes photos et tes étapes s’enchaînent en un petit film du voyage.',
  [('Automatique', '<p>Le film suit l’ordre du voyage, jour après jour, avec les lieux et les photos de tous les compagnons.</p>'),
   ('Depuis le bilan', '<p>Touche « Revivre en film » dans le bilan du voyage.</p>')],
  [('bilan','Revivre le voyage en film depuis le bilan')],
  ['album-photo-voyage','souvenirs-voyage-album','partager-photos-voyage-groupe'])

feat('album-photo-voyage', 'Créer un album photo de son voyage',
  'Un album photo du voyage, rangé jour par jour avec les récits : à télécharger ou à imprimer. Choisis la photo de couverture.',
  'L’album photo de ton voyage', 'Tes souvenirs, jour par jour, réunis en un album à télécharger ou à imprimer.',
  [('Rangé jour par jour', '<p>Chaque journée avec ses photos et son récit, dans l’ordre du voyage.</p>'),
   ('La couverture', '<p>Choisis la photo de couverture, ou une photo de la destination.</p>'),
   ('À imprimer', '<p>L’album se télécharge pour être gardé, envoyé ou imprimé.</p>')],
  [('bilan','L’album depuis le bilan du voyage'),('souvenir','Un souvenir avec ses photos')],
  ['film-de-voyage','souvenirs-voyage-album','ecrire-carnet-de-voyage'])

feat('mode-lecture-seule', 'Le mode lecture seule : prêter son téléphone sans risque',
  'Un geste et plus rien ne peut être modifié ni supprimé : idéal pour montrer son voyage ou pour un proche peu à l’aise avec les téléphones.',
  'Le mode lecture seule', 'Un geste sur le crayon, et le carnet devient impossible à modifier par erreur.',
  [('À quoi ça sert', '<p>Montrer ton voyage à quelqu’un, prêter ton téléphone, ou aider un proche qui craint de tout effacer.</p>'),
   ('Ce qui est bloqué', '<p>Toutes les modifications et suppressions, y compris celles du partage et des abonnés.</p>'),
   ('Revenir', '<p>Touche à nouveau le cadenas pour repasser en mode modification.</p>')],
  [('lecture-seule','Le cadenas du mode lecture seule')],
  ['application-voyage-gratuite-sans-pub','voyage-en-famille-avec-enfants','sauvegarde-voyage-cloud'])

feat('sauvegarde-voyage-cloud', 'Sauvegarder ses voyages et changer de téléphone',
  'Retrouver tous ses voyages sur un nouveau téléphone : le Cloud Vezoria (facultatif), le code personnel, la sauvegarde complète avec photos.',
  'Sauvegarder ses voyages', 'Changer de téléphone ne doit jamais faire perdre un voyage.',
  [('Trois choix', '<ul><li><b>Tout le carnet dans le cloud</b> : tous tes voyages arrivent sur ton autre téléphone avec ton code.</li><li><b>Voyage par voyage</b> : tu choisis ce qui est sauvegardé.</li><li><b>Sans cloud</b> : tout reste sur ce téléphone.</li></ul>'),
   ('Le code personnel', '<p>Garde précieusement ton code : sur le nouveau téléphone, il suffit de le coller pour tout retrouver.</p>'),
   ('La sauvegarde complète', '<p>Une sauvegarde de tout le carnet, photos comprises, peut être téléchargée depuis les voyages passés.</p>')],
  [('cloud','Les trois choix de sauvegarde')],
  ['application-voyage-gratuite-sans-pub','long-voyage-tour-du-monde','mode-lecture-seule'])

feat('explorer-une-ville', 'Que faire dans une ville ? L’explorateur de Vezoria',
  'Monuments, quartiers, musées, restaurants, bars : l’explorateur propose quoi voir et faire dans chaque étape du voyage, à ajouter en un geste.',
  'Explorer une ville', 'Pour chaque étape, l’explorateur propose quoi voir, quoi faire et où manger.',
  [('À voir, à faire, manger, boire, shopping', '<p>Les lieux sont rangés par rubrique, avec photo, description, horaires et prix quand ils sont connus.</p>'),
   ('Un geste pour l’ajouter', '<p>Touche un lieu puis « Ajouter à ma journée » : il rejoint l’itinéraire du jour, prêt à être organisé.</p>'),
   ('Y aller', '<p>Chaque lieu propose l’itinéraire pour s’y rendre.</p>')],
  [('organiser-journee','Explorer une ville depuis l’organisation d’une journée')],
  ['optimiser-itineraire-journee','city-trip','itineraire-voyage-jour-par-jour'])

feat('optimiser-itineraire-journee', 'Optimiser l’itinéraire d’une journée de visites',
  'Ranger les visites d’une journée dans le meilleur ordre : départ et arrivée au choix, distance à pied acceptable, carte de l’itinéraire.',
  'Optimiser l’itinéraire d’une journée', 'Tu choisis les lieux, l’appli trouve le meilleur ordre de visite.',
  [('Départ et arrivée', '<p>Le point de départ (souvent l’hôtel) et l’arrivée : retour à l’hôtel, une gare, un aéroport ou le dernier lieu visité.</p>'),
   ('La marche', '<p>Indique la distance que tu veux bien faire à pied entre deux visites : au-delà, métro, bus ou taxi.</p>'),
   ('Toute l’étape', '<p>« Organiser toute l’étape » répartit les lieux sur tous les jours passés dans la ville.</p>')],
  [('organiser-journee','L’organisation d’une journée')],
  ['explorer-une-ville','itineraire-voyage-jour-par-jour','city-trip'])

feat('echeancier-voyage', 'L’échéancier : étaler les paiements d’un voyage',
  'L’échéancier de Vezoria répartit les paiements d’un voyage mois par mois et calcule ce que chacun doit mettre de côté avant le départ.',
  'L’échéancier du voyage', 'Mois par mois, ce que chacun doit payer, et pour quoi.',
  [('À mettre de côté', '<p>Le montant mensuel pour tout régler avant le départ, pour chaque voyageur.</p>'),
   ('Étaler automatiquement', '<p>Ce qui n’est pas encore planifié s’étale tout seul sur les mois restants.</p>'),
   ('Cocher', '<p>Chaque échéance payée se coche : le reste se met à jour.</p>')],
  [('echeancier','L’échéancier mois par mois')],
  ['payer-voyage-plusieurs-fois','budget-voyage','voyage-de-noces'])

feat('inviter-compagnons-voyage', 'Inviter ses compagnons dans un voyage',
  'Inviter un ami à préparer le voyage avec toi : invitation par message ou QR code, réponse dans l’appli, chacun son profil et sa couleur.',
  'Inviter ses compagnons de voyage', 'Un voyage se prépare mieux à plusieurs : invite tes compagnons en un geste.',
  [('Envoyer l’invitation', '<p>Par message ou en montrant le QR code. Si ton compagnon a déjà l’appli, l’invitation arrive directement chez lui.</p>'),
   ('En attente, puis accepté', '<p>Tant qu’il n’a pas répondu, il est noté « en attente » et tu peux le relancer. Une fois accepté, il voit et complète tout le voyage.</p>'),
   ('Chacun son profil', '<p>Chacun choisit son prénom et sa couleur, et lui seul peut les modifier.</p>'),
   ('Un voyage à la fois', '<p>Partager un voyage ne montre rien de tes autres voyages.</p>')],
  [('partager','La fenêtre de partage'),('mes-voyages','Les raccourcis sous chaque voyage')],
  ['organiser-voyage-entre-amis','suivre-voyage-famille','voyage-en-groupe'])

feat('application-voyage-multilingue', 'Une appli de voyage en 14 langues pour les groupes internationaux',
  'Vezoria parle 14 langues : chaque compagnon utilise l’appli dans la sienne, et les fiches gardent la langue dans laquelle elles ont été écrites.',
  'Une appli en 14 langues', 'Un groupe d’amis venus de plusieurs pays ? Chacun utilise Vezoria dans sa langue.',
  [('14 langues', '<p>Français, anglais, espagnol, allemand, italien, portugais, néerlandais, arabe, hindi, japonais, coréen, russe, turc et chinois : l’interface s’adapte, et la langue se change dans les réglages.</p>'),
   ('Les fiches restent telles quelles', '<p>Ce que chacun écrit reste dans sa langue : seule l’interface change.</p>'),
   ('Les devises aussi', '<p>Chaque voyage a sa devise, et les dépenses en monnaie locale sont converties.</p>')],
  [('accueil','L’écran d’un voyage')],
  ['voyage-en-groupe','depenses-voyage-plusieurs-devises','application-voyage-gratuite-sans-pub'])

feat('installer-vezoria-iphone', 'Installer Vezoria sur iPhone (en 30 secondes)',
  'Comment installer Vezoria sur iPhone : ouvrir le lien dans Safari, Partager, « Sur l’écran d’accueil ». L’appli s’utilise ensuite comme les autres.',
  'Installer Vezoria sur iPhone', 'Sur iPhone, Vezoria s’installe depuis Safari, en trois gestes.',
  [('Les trois gestes', '<ol><li>Ouvre le lien de Vezoria dans <b>Safari</b>.</li><li>Touche le bouton <b>Partager</b> (le carré avec une flèche).</li><li>Choisis <b>« Sur l’écran d’accueil »</b>, puis <b>« Ajouter »</b>.</li></ol>'),
   ('Toujours depuis l’icône', '<p>Ouvre ensuite Vezoria depuis son icône : c’est là que ton carnet est rangé, et les notifications fonctionnent.</p>')],
  [('accueil','Vezoria une fois installée')],
  ['installer-vezoria-android','application-voyage-gratuite-sans-pub','carnet-de-voyage-partage'])

feat('installer-vezoria-android', 'Installer Vezoria sur Android (Play Store)',
  'Comment installer Vezoria sur Android : depuis le Play Store, gratuitement. Puis choisir sa langue, son prénom et sa couleur.',
  'Installer Vezoria sur Android', 'Sur Android, Vezoria s’installe depuis le Play Store, comme n’importe quelle appli.',
  [('Depuis le Play Store', '<ol><li>Ouvre le <b>Play Store</b>.</li><li>Cherche <b>Vezoria</b>.</li><li>Touche <b>Installer</b>.</li></ol>'),
   ('Au premier lancement', '<p>Choisis ta langue et ta devise, puis ton prénom et ta couleur. Tu peux aussi commencer avec le voyage de démo.</p>')],
  [('mes-voyages','Tes voyages dans Vezoria')],
  ['installer-vezoria-iphone','application-voyage-gratuite-sans-pub','guide-utilisateur'])
