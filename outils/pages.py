# -*- coding: utf-8 -*-
# Contenu du site Vezoria (une entrée = une page).
# Pour ajouter une page : copier un bloc, changer le slug et le texte, puis lancer  python3 outils/generer.py
# Les captures viennent de assets/img/ (nom sans .webp).

PAGES = []
def page(**k): PAGES.append(k)

page(slug='organiser-voyage-entre-amis',
  cat='Préparer', title='Organiser un voyage entre amis : la méthode simple (2026)',
  desc='Organiser un voyage entre amis sans tableur ni groupe WhatsApp perdu : dates, étapes, réservations et dépenses dans un seul carnet partagé. Gratuit.',
  h1='Organiser un voyage entre amis, sans prise de tête',
  lead='Un voyage à plusieurs, c’est vite dix conversations, trois tableaux et des captures d’écran perdues. Voici une méthode en cinq étapes, et l’outil gratuit qui la rend facile.',
  sections=[
   ('1. Mettez-vous d’accord sur l’essentiel', '<p>Avant de réserver quoi que ce soit, fixez ensemble trois choses : <b>les dates</b> (ou une fourchette), <b>le budget par personne</b> et <b>le style du voyage</b> (city trip, plage, road trip, rando…). Tant que ces trois points ne sont pas clairs, chaque discussion repart de zéro.</p><p>Dans Vezoria, ces informations deviennent la base du voyage : le nom, les dates, les voyageurs et le budget visé par personne. L’appli vous prévient ensuite si les dépenses dépassent l’objectif.</p>'),
   ('2. Dessinez l’itinéraire, étape par étape', '<p>Listez les villes où vous dormez et le nombre de nuits dans chacune. C’est la colonne vertébrale du voyage : tout le reste (hôtels, trajets, visites) vient s’y accrocher.</p><p>L’assistant de Vezoria le fait en cinq petites étapes : il crée le programme jour par jour, un hébergement par étape et les trajets entre les villes. Chacun peut même avoir son propre moyen de transport pour l’aller et le retour : l’un en train, l’autre en avion.</p>'),
   ('3. Un seul endroit pour toutes les réservations', '<p>Le piège classique : la confirmation de l’hôtel est dans la boîte mail de l’un, les billets de train dans le téléphone d’un autre. Le jour J, personne ne retrouve rien.</p><p>Rangez chaque réservation dans une fiche partagée : prix, dates, numéro de réservation, et le billet lui-même en pièce jointe. Avec l’import, une capture d’écran ou le PDF du mail suffit à remplir la fiche. Et tout reste lisible <b>sans réseau</b>, même dans l’avion.</p>'),
   ('4. Les comptes au fil de l’eau', '<p>Notez chaque dépense dès qu’elle est payée : qui a payé, et entre qui elle se partage. À la fin, plus besoin de refaire les calculs : l’appli indique le plus simple pour équilibrer, du genre « Léo doit 137 € à Camille ».</p>'),
   ('5. Une checklist commune', '<p>Passeports, adaptateurs, assurance, réservation du restaurant d’anniversaire… Une liste partagée où chacun coche de son côté évite le fameux « je croyais que c’était toi ».</p>'),
  ],
  shots=[('assistant','L’assistant de création de voyage, étape 1 : le nom et les voyageurs'),('etapes','Les étapes du voyage, ville par ville, avec le nombre de nuits'),('trajets','La liste des trajets du voyage, avec leur prix et leur état')],
  faq=[('Combien coûte Vezoria ?','Rien. Vezoria est gratuite, sans publicité et sans abonnement.'),
       ('Faut-il que tout le monde installe l’appli ?','Les compagnons qui préparent le voyage avec vous l’installent pour pouvoir compléter. La famille qui veut seulement suivre le voyage peut le faire depuis un simple lien, sans rien installer.'),
       ('Peut-on compter quelqu’un qui n’a pas encore l’appli dans les dépenses ?','Oui : il suffit de lui créer un profil. Il pourra rejoindre le voyage plus tard.')],
  rel=['partager-depenses-voyage','itineraire-voyage-jour-par-jour','carnet-de-voyage-partage'])

page(slug='partager-depenses-voyage',
  cat='Budget', title='Partager les dépenses d’un voyage : qui doit combien ?',
  desc='Calculer qui doit combien à qui après un voyage entre amis : parts égales ou différentes, plusieurs devises, remboursements. Méthode et appli gratuite.',
  h1='Partager les dépenses d’un voyage entre amis',
  lead='« Qui a payé le taxi ? » « Je t’ai avancé l’hôtel ! » Les comptes de voyage gâchent souvent le retour. Voici comment les tenir sans effort, et sans dispute.',
  sections=[
   ('Le principe : qui a payé, et pour qui', '<p>Chaque dépense se résume à deux questions : <b>qui a avancé l’argent</b>, et <b>entre qui la dépense se partage</b>. Un dîner payé par Inès pour quatre personnes, c’est 1 payeur et 4 bénéficiaires. Avec ces deux informations pour chaque dépense, le reste est du calcul… que l’appli fait pour vous.</p>'),
   ('Parts égales, montants ou parts différentes', '<p>Tout ne se partage pas à parts égales. La chambre double se divise en deux, le billet d’avion est par personne, et le guide privé se répartit entre ceux qui l’ont suivi. Dans Vezoria, chaque fiche peut être :</p><ul><li><b>par personne</b> (un billet chacun) ou <b>globale</b> (une chambre à partager) ;</li><li>partagée <b>à parts égales</b>, en <b>montants</b> précis ou en <b>parts</b> (2 parts pour un couple, 1 pour un solo) ;</li><li>limitée à <b>certaines personnes</b> seulement.</li></ul>'),
   ('Le calcul final : le moins de virements possible', '<p>Au lieu d’une liste interminable de petites dettes croisées, l’écran « Qui doit quoi » propose le chemin le plus court pour équilibrer : deux ou trois remboursements au lieu de dix. Un bouton « Régler » note le remboursement, un autre permet de le demander poliment.</p>'),
   ('Plusieurs devises ?', '<p>En voyage à l’étranger, notez la dépense dans la monnaie locale : le montant est converti pour les comptes. Chaque voyage a sa devise principale.</p>'),
   ('Payer en plusieurs fois', '<p>Pour un gros voyage réservé longtemps à l’avance, l’échéancier étale les paiements mois par mois et indique combien chacun doit mettre de côté chaque mois avant le départ.</p>'),
  ],
  shots=[('comptes','L’écran « Qui doit quoi » avec les remboursements à faire'),('qui-paie','La répartition d’une dépense entre les voyageurs'),('echeancier','L’échéancier mois par mois avant le départ')],
  faq=[('Les comptes sont-ils visibles par tous les compagnons ?','Oui, tous les voyageurs voient les mêmes comptes. Les abonnés (la famille qui suit le voyage) ne voient jamais les dépenses.'),
       ('Peut-on ajouter une dépense sans réseau ?','Oui. Elle est enregistrée sur le téléphone et partagée dès que le réseau revient.'),
       ('Et si quelqu’un n’a pas participé à une dépense ?','Il suffit de le décocher sur la fiche : la dépense est partagée seulement entre ceux qui sont concernés.')],
  rel=['budget-voyage','organiser-voyage-entre-amis','pendant-le-voyage'])

page(slug='carnet-de-voyage-partage',
  cat='Découvrir', title='Carnet de voyage partagé : l’appli gratuite à plusieurs',
  desc='Un carnet de voyage numérique que l’on remplit à plusieurs : programme, réservations, budget, photos et souvenirs. Gratuit, sans pub, sans compte.',
  h1='Un carnet de voyage qu’on remplit à plusieurs',
  lead='Le carnet de voyage, c’est l’endroit où tout le voyage tient : avant, pendant et après. Version numérique et partagée, il devient le meilleur compagnon de route du groupe.',
  sections=[
   ('Avant : on prépare ensemble', '<p>Le programme jour par jour, les hôtels, les trajets, les visites à réserver, le budget et la valise. Chacun complète de son côté, avec sa couleur : on voit tout de suite qui a ajouté quoi.</p>'),
   ('Pendant : l’essentiel du jour', '<p>Le jour du départ, l’espace « En cours » s’allume : la prochaine étape et le temps qu’il reste, les billets en un geste, la météo, les dépenses du jour. Un « step » garde l’endroit où vous êtes avec une photo et quelques mots.</p>'),
   ('Après : on revit le voyage', '<p>Chaque souvenir se range sous sa journée. Au retour, le carnet devient un bilan, un film, un album et une carte du monde de tous vos voyages.</p>'),
   ('Pensé pour les vraies conditions du voyage', '<ul><li><b>Hors ligne</b> : programme, billets et papiers restent consultables sans réseau.</li><li><b>Sans compte</b> : pas d’adresse e-mail, pas de mot de passe, juste un prénom.</li><li><b>Sans publicité</b> et gratuit.</li><li><b>Protégé</b> : un voyage partagé n’est visible que par ceux qui ont reçu son invitation.</li><li><b>En 14 langues</b>, pour les groupes internationaux.</li></ul>'),
  ],
  shots=[('accueil','L’écran principal d’un voyage dans Vezoria'),('mes-voyages','La liste des voyages, chacun sous forme de carte postale'),('bilan','Le bilan d’un voyage terminé : jours, kilomètres, pays, photos')],
  faq=[('Vezoria fonctionne sur iPhone ?','Oui. Sur iPhone, Vezoria s’ajoute à l’écran d’accueil depuis Safari et s’utilise comme une appli. Sur Android, elle s’installe depuis le Play Store.'),
       ('Mes données sont-elles revendues ?','Non. Il n’y a ni publicité ni pistage. Les voyages partagés sont chiffrés : seuls ceux qui ont l’invitation peuvent les lire.'),
       ('Peut-on l’utiliser seul ?','Bien sûr. Le carnet fonctionne aussi pour un voyage en solo, et vous pouvez inviter quelqu’un plus tard.')],
  rel=['organiser-voyage-entre-amis','souvenirs-voyage-album','application-voyage-gratuite-sans-pub'])

page(slug='itineraire-voyage-jour-par-jour',
  cat='Préparer', title='Faire son itinéraire de voyage jour par jour (méthode + outil)',
  desc='Construire un itinéraire de voyage jour par jour : étapes, nuits, visites dans le bon ordre, temps à pied. Méthode simple et appli gratuite pour l’organiser.',
  h1='Construire son itinéraire de voyage jour par jour',
  lead='Un bon itinéraire, c’est un équilibre entre envies et réalisme : pas trop de villes, pas trop de visites par jour, et des trajets qui ne mangent pas toutes les vacances.',
  sections=[
   ('Commencer par les nuits', '<p>Le squelette d’un itinéraire, c’est la liste des villes où vous dormez et le nombre de nuits dans chacune. Comptez au minimum deux nuits par étape : une seule nuit, c’est surtout une journée de bagages.</p>'),
   ('Puis les journées', '<p>Pour chaque journée, notez un titre (« Arrivée à Rome », « Journée plage ») et deux ou trois incontournables. Le reste se décide sur place. Dans Vezoria, les trajets et l’hôtel du soir s’affichent automatiquement au bon jour.</p>'),
   ('Des visites dans le bon ordre', '<p>Pour une journée de visites, l’écran « Itinéraire » part de l’hôtel, liste les lieux à voir et les range dans le meilleur ordre, avec la carte. Vous choisissez où finir la journée (retour à l’hôtel, une gare, un aéroport) et la distance que vous acceptez de faire à pied entre deux visites.</p>'),
   ('Trouver quoi faire', '<p>Pas d’idée pour une ville ? L’explorateur propose monuments, quartiers, musées et adresses où manger : un geste pour l’ajouter à votre journée.</p>'),
   ('Rester souple', '<p>Un jour de plus à Lisbonne ? Insérez un jour : les journées suivantes se décalent avec leurs réservations. Un imprévu ? Le programme se modifie par n’importe quel voyageur, et tout le monde voit la nouvelle version.</p>'),
  ],
  shots=[('journee','Une journée du programme avec ses trajets et son hôtel'),('organiser-journee','L’organisation d’une journée : départ, arrivée, lieux à voir'),('etapes','Les étapes d’un voyage dans l’assistant')],
  faq=[('Combien de visites prévoir par jour ?','En ville, trois ou quatre lieux par jour est déjà bien rempli, surtout avec les temps de trajet et les repas.'),
       ('Peut-on préparer un road trip avec plusieurs villes ?','Oui, l’assistant gère autant d’étapes que nécessaire, avec un moyen de transport par étape.')],
  rel=['road-trip-plusieurs-villes','organiser-voyage-entre-amis','checklist-valise-voyage'])

page(slug='checklist-valise-voyage',
  cat='Préparer', title='Checklist valise de voyage : la liste à ne rien oublier',
  desc='La checklist complète pour faire sa valise : papiers, santé, électronique, vêtements selon la météo. Une liste partagée qui s’adapte à ton voyage.',
  h1='La checklist valise pour ne rien oublier',
  lead='Le chargeur resté sur la table de nuit, le passeport expiré, l’adaptateur introuvable… Une bonne checklist évite 90 % des galères de départ.',
  sections=[
   ('Les papiers d’abord', '<ul><li>Carte d’identité ou passeport en cours de validité (pour beaucoup de pays hors Union européenne, il doit être valable plusieurs mois après le retour).</li><li>Visa ou autorisation de voyage si le pays l’exige.</li><li>Carte européenne d’assurance maladie pour l’Europe, assurance voyage ailleurs.</li><li>Billets, réservations, permis de conduire si location de voiture.</li><li>Copies numériques de tout ça.</li></ul><p class="note">Les formalités changent : vérifiez toujours avant de partir sur le site officiel du pays ou sur diplomatie.gouv.fr.</p>'),
   ('Santé', '<ul><li>Médicaments personnels et ordonnances.</li><li>Petite trousse à pharmacie.</li><li>Crème solaire, anti-moustiques selon la destination.</li></ul>'),
   ('Électronique', '<ul><li>Chargeur et batterie externe.</li><li>Adaptateur de prise : le type change selon le pays.</li><li>Cartes hors ligne téléchargées avant de partir.</li></ul>'),
   ('Vêtements selon la météo', '<p>La météo de chaque étape décide du reste : pull ou t-shirts, K-way, maillot de bain. Une tenue qui couvre épaules et genoux est utile pour visiter des lieux de culte.</p>'),
   ('La valise intelligente', '<p>Dans Vezoria, la valise intelligente regarde la météo de vos étapes, votre programme (plage, randonnée, ski…) et les pays visités pour proposer la liste : papiers et formalités, adaptateurs de prise, vêtements. Vous décochez ce qui ne sert pas, le reste rejoint la checklist partagée, où chacun coche de son côté.</p>'),
  ],
  shots=[('valise','La valise intelligente avec les pays visités et les idées proposées'),('checklist','La checklist partagée du voyage'),('bagages','La liste de bagages selon le climat et les activités')],
  faq=[('La checklist est-elle partagée avec les compagnons ?','Oui. Quand quelqu’un coche une ligne, tout le monde le voit, avec sa pastille de couleur.'),
       ('Peut-on faire une liste par personne ?','Oui, la liste de bagages peut être commune ou une liste par voyageur.')],
  rel=['papiers-voyage-formalites','itineraire-voyage-jour-par-jour','organiser-voyage-entre-amis'])

page(slug='budget-voyage',
  cat='Budget', title='Calculer le budget d’un voyage (et s’y tenir)',
  desc='Estimer le budget d’un voyage par personne, suivre le réel au fil des réservations et étaler les paiements avant le départ. Méthode simple et appli gratuite.',
  h1='Calculer le budget d’un voyage, et s’y tenir',
  lead='Le budget d’un voyage se joue en trois temps : l’estimation, les réservations, puis les dépenses sur place. Les suivre au même endroit évite les mauvaises surprises.',
  sections=[
   ('Les grands postes', '<p>Un budget de voyage se découpe en quatre ou cinq postes : <b>trajets</b>, <b>hébergements</b>, <b>visites et activités</b>, <b>repas</b> et <b>dépenses sur place</b>. Les deux premiers représentent souvent plus de la moitié du total.</p>'),
   ('Estimé, réservé, payé', '<p>Pour chaque fiche, notez d’abord une estimation, puis le prix réel une fois réservé. L’écran du budget montre trois chiffres : ce qui était prévu, ce qui est réservé et ce qui est déjà payé. Vous voyez tout de suite si le voyage dérape.</p>'),
   ('Un objectif par personne', '<p>Fixez un budget visé par personne à la création du voyage : l’appli affiche la marge qu’il vous reste, ou le dépassement.</p>'),
   ('Mettre de côté chaque mois', '<p>L’échéancier calcule combien chacun doit mettre de côté chaque mois jusqu’au départ, et étale automatiquement ce qui n’est pas encore planifié.</p>'),
   ('Sur place : un plafond par jour', '<p>Pendant le voyage, les dépenses du jour s’affichent face à votre plafond quotidien. Un café, un taxi, un musée : deux secondes pour les noter, avec la photo du ticket si besoin.</p>'),
  ],
  shots=[('budget','Le budget total du voyage par personne'),('echeancier','L’échéancier : ce qu’il faut mettre de côté chaque mois'),('depense','L’ajout d’une dépense pendant le voyage')],
  faq=[('Peut-on avoir un budget dans une autre devise ?','Oui, chaque voyage a sa devise, et les dépenses en monnaie locale sont converties.'),
       ('Les estimations comptent-elles dans le total ?','Oui, tant que le prix réel n’est pas saisi : vous avez ainsi une vision complète du voyage dès le début.')],
  rel=['partager-depenses-voyage','organiser-voyage-entre-amis','pendant-le-voyage'])

page(slug='suivre-voyage-famille',
  cat='Partager', title='Partager son voyage avec sa famille, sans réseaux sociaux',
  desc='Ta famille suit ton voyage étape par étape, avec photos et récits, depuis un simple lien sans installer d’appli. Tu choisis ce qui est publié.',
  h1='Partager son voyage avec sa famille, simplement',
  lead='Les grands-parents veulent des nouvelles, mais pas forcément un compte sur un réseau social. Avec un carnet publié, ils suivent le voyage comme un journal, depuis un simple lien.',
  sections=[
   ('Un journal de voyage, étape par étape', '<p>Chaque souvenir que vous ajoutez (une photo, un lieu, quelques mots) devient une étape du journal. Vos proches voient les plus récentes en premier, peuvent aimer et laisser un commentaire.</p>'),
   ('Sans installer d’appli', '<p>Vous envoyez un lien par message : il s’ouvre dans le navigateur, sans compte ni installation. S’ils installent l’appli plus tard, ils retrouvent leurs voyages suivis.</p>'),
   ('Vous choisissez ce qui est vu', '<ul><li>Les abonnés voient seulement les étapes publiées et leurs photos.</li><li>Jamais vos réservations, billets, dépenses ni notes.</li><li>Un souvenir marqué « privé » reste pour vous.</li><li>Vous pouvez retirer l’accès à quelqu’un ou arrêter de publier à tout moment.</li></ul>'),
   ('Une grille de tous les voyages suivis', '<p>Côté famille, tous les voyages suivis s’affichent avec leur photo, rangés par personne. On touche une photo pour ouvrir le voyage, et un gros bouton ramène à la liste : pensé pour être simple, même pour ceux qui sont peu à l’aise avec les téléphones.</p>'),
  ],
  shots=[('journal-abonne','Le journal d’un voyage suivi par un proche'),('suivis','La grille des voyages suivis, une photo par voyage'),('partager','La fenêtre de partage : compagnons, abonnés, voyages suivis')],
  faq=[('Combien de personnes peuvent suivre un voyage ?','Autant que vous voulez.'),
       ('Deux abonnés ont le même prénom ?','Un numéro est ajouté automatiquement (« Claire 2 ») pour qu’on ne les confonde pas.'),
       ('Les abonnés peuvent-ils modifier le voyage ?','Non, ils le suivent en lecture seule.')],
  rel=['carnet-de-voyage-partage','souvenirs-voyage-album','application-voyage-gratuite-sans-pub'])

page(slug='importer-reservations-voyage',
  cat='Préparer', title='Ranger ses billets et réservations de voyage (même hors ligne)',
  desc='Billets d’avion, de train, hôtels : importe le PDF, le mail ou une capture d’écran, la fiche se remplit toute seule et reste lisible sans réseau.',
  h1='Tous ses billets et réservations au même endroit',
  lead='Mail de confirmation, PDF, appli de la compagnie, billet papier : chaque réservation arrive par un chemin différent. Les ranger au même endroit change le voyage.',
  sections=[
   ('Importer au lieu de recopier', '<p>Le bouton « Importer une résa » accepte le PDF reçu par mail, une capture d’écran, la photo d’un billet papier, une carte Wallet ou le texte du mail. L’appli reconnaît le type de réservation et remplit la fiche : dates, horaires, ville, numéro de réservation. Plusieurs vols sur la même capture ? Ils sont tous proposés.</p>'),
   ('Le billet reste joint à la fiche', '<p>Le PDF ou la photo du billet est rangé avec la fiche et reste sur le téléphone : vous le retrouvez sans réseau, au guichet comme à l’embarquement.</p>'),
   ('Un état pour chaque réservation', '<p>À réserver, réservé, payé : la couleur de chaque fiche dit où vous en êtes. Tant qu’une fiche est « à réserver », des liens vers des sites de réservation connus aident à comparer, déjà remplis avec la ville et les dates quand c’est possible.</p>'),
   ('Le bon jour, au bon moment', '<p>Chaque réservation apparaît automatiquement au bon jour du programme. Le jour J, l’espace « En cours » affiche la prochaine et le temps qu’il reste avant de partir.</p>'),
  ],
  shots=[('importer','L’import d’une réservation : PDF, capture, photo, mail'),('fiche-hotel','Une fiche d’hôtel avec ses dates et ses voyageurs'),('reserver','Les liens pour comparer et réserver')],
  faq=[('Mes billets sont-ils envoyés quelque part ?','Ils restent sur votre téléphone et sont partagés uniquement avec les compagnons du voyage.'),
       ('Faut-il vérifier la fiche après un import ?','Oui, jetez toujours un œil avant d’enregistrer : l’appli lit le document mais vous restez maître de la fiche.')],
  rel=['organiser-voyage-entre-amis','pendant-le-voyage','budget-voyage'])

page(slug='papiers-voyage-formalites',
  cat='Préparer', title='Papiers de voyage : passeport, visa, assurance, ne rien oublier',
  desc='Les papiers à prévoir pour voyager : passeport ou carte d’identité, visa, assurance, carte européenne d’assurance maladie. Liste et rappels par voyageur.',
  h1='Papiers de voyage : la liste à vérifier avant de partir',
  lead='Un passeport qui expire trop tôt ou un visa oublié peut annuler un voyage à l’aéroport. Quelques minutes de vérification avant de réserver suffisent.',
  sections=[
   ('Carte d’identité ou passeport ?', '<p>Dans l’espace Schengen et une partie de l’Europe, la carte d’identité en cours de validité suffit souvent aux citoyens européens. Ailleurs, le passeport est généralement demandé, souvent valable plusieurs mois après la date de retour.</p>'),
   ('Visa et autorisations de voyage', '<p>Certains pays demandent un visa ou une autorisation électronique à faire en ligne avant le départ. Les délais varient : renseignez-vous dès la réservation.</p>'),
   ('Assurance et santé', '<p>En Europe, la carte européenne d’assurance maladie facilite les soins. Hors d’Europe, une assurance voyage couvrant les frais médicaux et le rapatriement est vivement conseillée.</p>'),
   ('Les dates d’expiration de chacun', '<p>Dans Vezoria, chaque voyageur peut noter ses documents (passeport, carte d’identité, visa, permis, assurance) avec leur date d’expiration. L’appli prévient si un document expire trop tôt par rapport au voyage. La valise intelligente ajoute aussi les formalités courantes selon les pays visités et la nationalité.</p>'),
  ],
  shots=[('documents','Les documents de voyage de chaque voyageur'),('valise','Les formalités proposées selon les pays visités')],
  faq=[('Les règles affichées sont-elles officielles ?','Ce sont des règles générales pour un court séjour touristique. Vérifiez toujours sur le site officiel du pays ou sur diplomatie.gouv.fr avant de partir.')],
  rel=['checklist-valise-voyage','organiser-voyage-entre-amis','itineraire-voyage-jour-par-jour'])

page(slug='road-trip-plusieurs-villes',
  cat='Préparer', title='Préparer un road trip ou un voyage en plusieurs villes',
  desc='Organiser un road trip ou un city trip en plusieurs étapes : nuits par ville, trajets, hôtels, visites. L’assistant crée tout le programme en 5 étapes.',
  h1='Préparer un road trip ou un voyage en plusieurs villes',
  lead='Rome, Naples, Malte, Athènes… Les voyages en plusieurs étapes sont les plus beaux, et les plus compliqués à organiser. Voici comment garder la vue d’ensemble.',
  sections=[
   ('Une ligne par ville', '<p>Listez les villes dans l’ordre, avec les nuits passées dans chacune et le moyen de transport pour y arriver. L’assistant de Vezoria en déduit le programme jour par jour, un hébergement par étape et tous les trajets intermédiaires.</p>'),
   ('Chacun son départ', '<p>Dans un groupe, tout le monde ne part pas du même endroit : l’un vient de Paris en train, l’autre de Lyon en avion. L’appli crée l’aller et le retour de chacun, avec son propre moyen de transport.</p>'),
   ('La carte de l’itinéraire', '<p>L’itinéraire s’affiche sur une carte, ville par ville, et chaque étape propose ses incontournables à explorer.</p>'),
   ('Sur la route', '<p>Pendant le voyage, le suivi (à activer si vous le souhaitez) trace votre route sur la carte, et chaque « step » garde un souvenir géolocalisé. Au retour, le voyage se revit sur un globe en 3D.</p>'),
  ],
  shots=[('etapes','Les étapes d’un voyage en plusieurs villes'),('accueil','L’itinéraire sur l’écran principal du voyage'),('en-cours','L’espace « En cours » pendant le voyage')],
  faq=[('Combien d’étapes peut-on ajouter ?','Autant que nécessaire.'),
       ('Peut-on changer l’ordre des étapes ensuite ?','Oui, tout se modifie après la création : jours, hôtels, trajets.')],
  rel=['itineraire-voyage-jour-par-jour','organiser-voyage-entre-amis','pendant-le-voyage'])

page(slug='pendant-le-voyage',
  cat='Voyager', title='Pendant le voyage : billets, dépenses, souvenirs en un geste',
  desc='Pendant le voyage, tout l’essentiel du jour : prochaine étape, billets hors ligne, météo, dépenses, souvenirs géolocalisés. Une appli de voyage gratuite.',
  h1='Pendant le voyage : l’essentiel du jour, en un geste',
  lead='Sur place, on n’a pas envie de chercher : on veut le billet du train de 10 h 12, l’adresse de l’hôtel et noter le dîner. L’espace « En cours » est fait pour ça.',
  sections=[
   ('La prochaine étape', '<p>Le haut de l’écran affiche la prochaine étape et le temps restant avant le départ, avec « Y aller » pour l’itinéraire et « Fiche » pour les billets.</p>'),
   ('Les raccourcis du jour', '<p>Step ici, dépense, fiche du jour, liste de courses partagée, météo, carte, import, papiers : tout ce qui sert sur place est à un geste.</p>'),
   ('Raconter sa journée', '<p>Un « step », c’est un moment du voyage : l’endroit où vous êtes, une photo et quelques mots. Il rejoint la journée et la carte, et vos abonnés le reçoivent si le voyage est publié.</p>'),
   ('Même sans réseau', '<p>Billets, papiers et programme sont sur le téléphone. Ce que vous ajoutez hors ligne part vers vos compagnons dès que le réseau revient.</p>'),
  ],
  shots=[('en-cours','L’espace « En cours » avec la prochaine étape'),('raccourcis','Les raccourcis du jour pendant le voyage'),('step','L’ajout d’un souvenir « Je suis ici »')],
  faq=[('Le suivi de position est-il obligatoire ?','Non. Il ne fonctionne que si vous l’activez, et vous pouvez l’arrêter à tout moment.')],
  rel=['souvenirs-voyage-album','partager-depenses-voyage','suivre-voyage-famille'])

page(slug='souvenirs-voyage-album',
  cat='Se souvenir', title='Garder les souvenirs d’un voyage : journal, album et film',
  desc='Range tes photos et récits jour par jour, puis revis le voyage : bilan, film, album à imprimer, carte du monde de tous tes voyages. Gratuit.',
  h1='Garder les souvenirs de voyage, jour après jour',
  lead='Des centaines de photos éparpillées dans plusieurs téléphones, et rien pour raconter le voyage. Un carnet de souvenirs rangé jour par jour change tout.',
  sections=[
   ('Une journée, un souvenir', '<p>Chaque souvenir se range sous sa journée : un titre, un lieu, un récit et des photos. En ajoutant des photos, leur date et leur lieu sont repris automatiquement.</p>'),
   ('Les photos de tout le groupe', '<p>Chaque compagnon ajoute ses propres photos au même voyage : fini les albums partagés qu’on oublie de remplir.</p>'),
   ('Le bilan du voyage', '<p>Au retour : les jours, les kilomètres, les pays et les photos du voyage, et ce qu’il reste à boucler (remboursements, souvenirs manquants).</p>'),
   ('Revivre le voyage', '<ul><li>Un <b>film</b> du voyage avec vos photos.</li><li>Un <b>album</b> à télécharger ou à imprimer.</li><li>Le voyage survolé sur un <b>globe en 3D</b>.</li><li>La <b>carte du monde</b> de tous vos voyages et des pays visités.</li></ul>'),
  ],
  shots=[('bilan','Le bilan d’un voyage avec film, album et globe'),('souvenir','L’ajout d’un souvenir avec photos et récit')],
  faq=[('Peut-on garder un souvenir privé ?','Oui : un souvenir marqué « privé » n’est jamais publié pour les abonnés.'),
       ('Comment sauvegarder ses souvenirs ?','Le Cloud Vezoria garde votre carnet pour le retrouver sur un autre téléphone, et une sauvegarde complète peut être téléchargée.')],
  rel=['carnet-de-voyage-partage','suivre-voyage-famille','pendant-le-voyage'])

page(slug='application-voyage-gratuite-sans-pub',
  cat='Découvrir', title='Une appli de voyage gratuite, sans pub et sans compte',
  desc='Vezoria est une appli de voyage gratuite, sans publicité, sans compte ni pistage. Voyages partagés protégés, fonctionne hors ligne, en 14 langues.',
  h1='Une appli de voyage gratuite, sans pub, sans compte',
  lead='Beaucoup d’applis de voyage vivent de la publicité et de vos données. Vezoria a fait un autre choix.',
  sections=[
   ('Gratuite, vraiment', '<p>Pas d’abonnement, pas de version payante qui bloque les fonctions utiles, pas de publicité.</p>'),
   ('Sans compte', '<p>Pas d’adresse e-mail, pas de mot de passe. Vous donnez un prénom et choisissez une couleur : c’est tout.</p>'),
   ('Vos voyages restent les vôtres', '<ul><li>Pas de pistage de votre utilisation.</li><li>Un voyage partagé n’est lisible que par ceux qui ont reçu son invitation.</li><li>Le Cloud Vezoria est facultatif : sans lui, tout reste sur votre téléphone.</li><li>Le mode « lecture seule » évite les suppressions par erreur.</li></ul>'),
   ('Hors ligne et en 14 langues', '<p>Le programme, les billets et les papiers restent consultables sans réseau. L’appli parle 14 langues, pratique pour les groupes d’amis venus de plusieurs pays.</p>'),
  ],
  shots=[('cloud','Le choix de sauvegarde : tout le carnet, voyage par voyage ou sans cloud'),('lecture-seule','Le mode lecture seule')],
  faq=[('Comment l’installer sur iPhone ?','Ouvrez le lien de Vezoria dans Safari, touchez Partager puis « Sur l’écran d’accueil ».'),
       ('Et sur Android ?','Installez Vezoria depuis le Play Store.')],
  rel=['carnet-de-voyage-partage','suivre-voyage-famille','organiser-voyage-entre-amis'])

page(slug='idees-de-voyage',
  cat='Préparer', title='Où partir ? Trouver une idée de voyage selon ses envies',
  desc='Pas d’idée de destination ? Réponds à quelques questions (dates, budget, durée, envies) et découvre des destinations adaptées avec météo et itinéraire type.',
  h1='Où partir ? Trouver la destination qui vous ressemble',
  lead='Envie de partir mais aucune idée d’où ? Quelques questions suffisent pour faire émerger des destinations adaptées à vos dates, votre budget et vos envies.',
  sections=[
   ('Les bonnes questions', '<p>D’où partez-vous, quand, combien de jours, à combien, avec qui, et pour quoi faire (plage, ville, nature, gastronomie, fête…) ? Ces réponses éliminent déjà la plupart des destinations.</p>'),
   ('Des idées argumentées', '<p>Pour chaque idée : la météo à cette période, le temps de trajet, un budget estimé par personne, les papiers nécessaires et un itinéraire type ville par ville.</p>'),
   ('De l’idée au voyage', '<p>Une idée vous plaît ? Composez-la à votre façon, ou créez le voyage tel quel : le programme est prêt, il ne reste qu’à réserver.</p>'),
  ],
  shots=[('idees','Les idées de destinations proposées'),('nouveau','Les façons de créer un nouveau voyage')],
  faq=[('Les budgets sont-ils exacts ?','Ce sont des ordres de grandeur pour comparer les destinations. Les prix réels dépendent des dates et des réservations.')],
  rel=['organiser-voyage-entre-amis','itineraire-voyage-jour-par-jour','budget-voyage'])

FAQ_HOME = [
 ('Qu’est-ce que Vezoria ?','Un carnet de voyage que l’on remplit à plusieurs : programme jour par jour, réservations, budget partagé, checklist, souvenirs. Gratuit, sans publicité et sans compte.'),
 ('Vezoria est-elle gratuite ?','Oui, entièrement, sans publicité ni abonnement.'),
 ('Sur quels téléphones ?','Sur Android depuis le Play Store, et sur iPhone en l’ajoutant à l’écran d’accueil depuis Safari.'),
 ('Ma famille peut-elle suivre mon voyage ?','Oui, depuis un simple lien, sans installer d’appli. Elle voit seulement les étapes et les photos que vous publiez.'),
 ('Ça marche sans réseau ?','Oui : programme, billets et papiers restent consultables hors ligne.'),
]
