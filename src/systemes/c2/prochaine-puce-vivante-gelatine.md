---
title: "La prochaine puce sera vivante. Et elle va pousser dans de la gélatine."
description: "Le cerveau humain tourne à 20 watts et résout des problèmes qu'un datacenter à plusieurs mégawatts ne peut pas encore formaliser. Ce ratio n'est pas une curiosité biologique. C'est la prochaine rupture technologique."
date: "10 mai 2026"
reading_time: "11 min"
system: c2
systeme: "Biophysique & Intelligence Distribuée"
serie: "L'intelligence avant le cerveau"
serie_index: 4
tag: "ARTICLE DE FOND"
slug: "prochaine-puce-vivante-gelatine"
layout: article.html.j2
---

# La prochaine puce sera vivante. Et elle va pousser dans de la gélatine.

Le débat sur l'avenir de l'informatique est mal posé depuis le début. On demande si les cellules biologiques vont « remplacer » les puces en silicium. Mauvaise question. La vraie question est celle-ci : **quel type de problème chaque substrat résout-il mieux, et à quel coût énergétique ?**

Quand on la reformule ainsi, la réponse cesse d'être spéculative. Elle devient analytique. Et l'analyse pointe vers une architecture que personne n'avait vraiment anticipée : des systèmes hybrides où le silicium, les organoïdes neuronaux et éventuellement le quantique coexistent — chacun sur sa niche de problèmes, chacun optimisé pour son propre profil énergie-rendement.

C'est la thèse que je veux défendre ici. Elle s'appuie sur trois découvertes récentes qui ont changé ma façon de lire ce domaine.

![Organoïde neuronal dans un substrat d'hydrogel — la prochaine frontière du calcul](/assets/img/articles/prochaine-puce-vivante-gelatine/hero_prochaine-puce-vivante-gelatine.webp)

---

## Le cerveau humain est la machine la plus efficace jamais construite

Commençons par le ratio le plus stupéfiant de toute l'ingénierie moderne.

L'entraînement de GPT-4 a consommé selon les estimations disponibles plusieurs gigawattheures d'électricité — soit des dizaines de millions de dollars en énergie pour un seul cycle d'apprentissage¹. L'infrastructure physique qui soutient les grands modèles de langage aujourd'hui mobilise des datacenters qui consomment chacun l'équivalent en électricité de petites villes.

Le cerveau humain consomme **20 watts en continu**. Il fait fonctionner 86 milliards de neurones, gère la perception, le langage, la mémoire épisodique, la planification à long terme et la régulation corporelle — simultanément, en temps réel, pendant 80 ans.

Dans mon cadre d'analyse biophysique — Y = f(K, EN × η) — le paramètre η, l'efficacité de conversion énergétique, est la variable centrale. Et quand on calcule η pour le cerveau humain face à n'importe quel système artificiel équivalent, le résultat est brutal : aucun substrat technologique actuel ne s'en approche même pour les tâches de type apprentissage adaptatif.

Ce n'est pas une curiosité biologique. C'est un signal d'ingénierie.

L'ordinateur quantique — l'autre grand espoir technologique — opère à −273,14 °C. Il nécessite une isolation vibratoire extrême, une infrastructure cryogénique massive, et reste limité à des classes très spécifiques de problèmes d'optimisation combinatoire. Son η réel, en tenant compte de toute l'infrastructure de refroidissement, est catastrophique pour les usages généraux.

Le bioprocesseur, lui, opère à **37 °C dans de la gélatine salée**. Il se reconfigure lui-même. Et il ne consomme que quelques microwatts pour des tâches d'apprentissage adaptatif basique.

---

## 800 000 neurones ont appris à jouer à Pong en 5 minutes

En 2022, Cortical Labs à Melbourne a publié les résultats de DishBrain — et l'expérience méritait plus d'attention qu'elle n'en a reçu².

Le principe : **800 000 neurones humains et de souris cultivés sur une puce**, exposés à des signaux électriques représentant les données du jeu vidéo Pong. Quand la balle dépasse la palette du joueur, les neurones reçoivent un signal de désordre (bruit aléatoire). Quand ils la repoussent, ils reçoivent un signal structuré. En cinq minutes, les neurones ont appris à contrôler la palette de manière cohérente.

Cinq minutes. Sans rétropropagation du gradient. Sans architecture d'entraînement préconçue. Sans GPU.

Ce que DishBrain démontre n'est pas un gadget de laboratoire : c'est une preuve de concept sur le type de problème que le substrat biologique gère naturellement — l'**apprentissage par renforcement dans des environnements variables**. C'est précisément la classe de problèmes que le silicium gère mal : elle exige une adaptation continue à des données non stationnaires, une capacité à inférer des règles à partir de très peu d'exemples, et une tolérance native à l'incertitude.

Un GPU entraîné sur Pong a besoin de millions d'épisodes simulés. Les neurones de DishBrain y arrivent en quelques minutes, avec une fraction de l'énergie.

La question qui m'a immédiatement frappé en lisant ces résultats n'était pas « est-ce éthique de faire jouer des neurones humains à Pong ? » — même si c'est une vraie question. C'était : **quel est le rapport énergie/performance comparé à un GPU pour la même tâche, et est-ce que ça peut s'industrialiser ?**

![GPU vs DishBrain vs Quantique — profil énergie-rendement comparé par substrat de calcul](/assets/img/articles/prochaine-puce-vivante-gelatine/info_prochaine-puce-vivante-gelatine.webp)

---

## Les Anthrobots ne sont pas des robots. Ce sont des organes de calcul personnalisés.

Michael Levin et son équipe à l'Université Tufts ont franchi un autre seuil en 2023.

Après les Xenobots — des entités construites à partir de cellules de grenouille reconfigurées par signaux bioélectriques, capables de locomotion collective et d'auto-organisation — l'équipe a développé les **Anthrobots** : des structures construites à partir de **cellules trachéales humaines**³.

La différence n'est pas seulement taxonomique. Les Anthrobots peuvent être construits à partir des cellules d'un patient spécifique, ce qui ouvre une voie vers des systèmes de réparation biologique personnalisés — notamment pour les dommages neurologiques. L'application visée est précise : des agents biologiques capables de naviguer dans un environnement complexe et d'effectuer des réparations locales là où aucun instrument chirurgical ne peut atteindre.

Mais le résultat publié en juin 2025 dans *Advanced Science* a ajouté une dimension inattendue⁴ : **les cellules assemblées en Anthrobots deviennent biologiquement plus jeunes que les cellules originales**. Pas légèrement. De manière mesurable, avec des marqueurs épigénétiques caractéristiques de cellules en début de différenciation. C'est un résultat que personne n'avait prévu, et ses implications pour la médecine régénérative — et pour notre compréhension du vieillissement cellulaire — dépassent largement le domaine du biocomputing.

Ce que ça révèle sur le plan des systèmes : la biologie n'est pas seulement un substrat de calcul alternatif. C'est un substrat qui peut se régénérer, se personnaliser selon le patient, et se comporter différemment selon le problème qu'on lui soumet. **Le profil de performance énergétique du système change radicalement selon la tâche.**

Ce n'est pas une puce. C'est un organe de calcul biodégradable.

---

## La forme n'est pas dans l'ADN. Elle est dans le courant électrique.

Pour comprendre pourquoi ces systèmes fonctionnent, il faut passer par Levin.

Sa contribution centrale n'est pas les Xenobots ou les Anthrobots — c'est le cadre théorique qui les rend possibles. Le concept d'**anatomical setpoints** : l'information sur la forme d'un organisme n'est pas seulement encodée dans la séquence génétique. Elle est distribuée dans les **états électriques dynamiques des cellules** — les gradients de tension transmembranaire qui forment un système de signalisation parallèle à la génétique⁵.

Ce cadre a une implication radicale : on peut reconfigurer le comportement collectif de cellules non pas en modifiant leur ADN, mais en modifiant leur champ bioélectrique. C'est ce que les Xenobots démontrent. Et c'est ce qui permet aux Anthrobots de s'assembler spontanément en structures fonctionnelles à partir de cellules trachéales dispersées.

La métaphore que Levin utilise pour le cancer est révélatrice : les cellules cancéreuses ne sont pas des cellules « brisées ». Ce sont des cellules qui ont **perdu leur intégration au collectif morphogénétique** — elles continuent à exécuter leur programme local, mais sans référence à l'identité de l'organe auquel elles appartiennent. Il parle de « trouble dissociatif de l'identité morphogénétique ».

Ce glissement conceptuel — de la génétique vers la bioélectricité comme substrat de l'information structurale — est précisément ce qui ouvre la voie au biocomputing. Si la forme est dans le champ électrique, alors le champ électrique peut être reprogrammé. Et si le champ électrique peut être reprogrammé, alors les cellules peuvent être dirigées vers des configurations de calcul délibérément conçues.

Un article publié en mars 2026 sur mycosmicventures.com revient sur les implications des xenobots et des anatomical setpoints dans le contexte plus large des systèmes cognitifs distribués⁶. La trajectoire de Levin est claire : il ne travaille plus seulement sur la biologie du développement. Il travaille sur une théorie générale de l'intelligence distribuée dont le biocomputing n'est qu'une application.

---

## L'avenir appartient aux architectures hybrides, pas aux substrats uniques

Voici ma position, et elle est délibérément tranchée.

Le débat silicium vs biologique est une fausse dichotomie. Ce n'est pas un combat de substrats. C'est une question de niches de performance.

**Le silicium est imbattable** pour la précision arithmétique, le déterminisme absolu, et la répétabilité à grande échelle. Aucune cellule vivante ne va calculer la trajectoire d'un satellite ou exécuter une transaction financière avec la fiabilité d'un microprocesseur classique. Ce n'est pas son rôle.

**Les organoïdes sont imbattables** pour l'exploration heuristique, l'adaptation continue à des environnements non stationnaires, et l'efficience énergétique sur des problèmes mal définis. La classe de problèmes où le silicium brûle des gigawattheures pour faire ce qu'une poignée de neurones font en quelques minutes.

**Le quantique est pertinent** pour une troisième niche très spécifique : l'optimisation combinatoire de problèmes à très haute dimensionnalité — chimie moléculaire, cryptographie, simulation de systèmes quantiques. Pour tout le reste, son infrastructure est un gouffre énergétique injustifiable.

L'architecture qui va émerger n'est pas une victoire d'un substrat sur les autres. C'est une **allocation de problèmes par type de substrat** — chaque couche faisant ce pour quoi elle est naturellement adaptée, interfacées par des protocoles de conversion qu'on n'a pas encore entièrement inventés.

Le précédent existe dans la biologie elle-même. Le cerveau humain n'est pas un substrat uniforme : il combine des systèmes rapides et automatiques (ganglions basaux, cervelet) avec des systèmes lents et délibératifs (cortex préfrontal), chacun spécialisé sur sa classe de décisions. L'efficacité globale émerge de la composition, pas de la compétition.

---

## Quand chaque problème choisit son propre substrat

Ce qui va changer dans les prochaines décennies, ce n'est pas l'arrivée d'un ordinateur miracle. C'est la **désagrégation du calcul** selon les profils énergie-rendement.

Un problème de diagnostic médical pourrait mobiliser un organoïde construit à partir des cellules du patient — personnalisé, biodégradable, localement adaptatif — pour explorer l'espace des hypothèses diagnostiques, pendant que le silicium gère les bases de données et le quantique optimise la sélection thérapeutique dans un espace de combinaisons trop large pour les deux autres substrats.

Les barrières à franchir sont réelles. On n'a pas encore les interfaces de lecture-écriture fiables entre organoïdes et circuits électroniques à grande échelle. Les questions éthiques sur les organoïdes dérivés de tissu humain sont ouvertes et méritent un cadre réglementaire sérieux — pas du moratoire par défaut, mais une réflexion structurée. Et l'industrialisation de la culture cellulaire en dehors du laboratoire reste un défi majeur de bioingénierie.

Mais les résultats de DishBrain, d'Anthrobots et du programme de Levin indiquent que le substrat biologique n'est plus une curiosité de laboratoire. C'est un candidat sérieux à une niche de performance spécifique, avec un profil énergétique qu'aucun autre substrat n'égale sur sa classe de problèmes.

Le ratio η du cerveau humain — 20 watts pour un système cognitif général — reste le benchmark que toute ingénierie devrait viser. On ne le dépassera probablement pas avec du silicium. On pourrait l'approcher en apprenant de lui.

---

*Sources*

¹ Estimations agrégées de la consommation énergétique de l'entraînement GPT-4, incluant les travaux de Luccioni et al. (2023), *Estimating the Carbon Footprint of BLOOM*, et diverses analyses sectorielles sur les coûts d'infrastructure des grands modèles de langage.

² Kagan, B.J. et al. (2022). « In vitro neurons learn and exhibit sentience when embodied in a simulated game-world. » *Neuron*, 105(6).

³ Gumuskaya, G. et al. (2023). « Motile Living Biobots Self-Construct from Adult Human Somatic Progenitor Seed Cells. » *Advanced Science*.

⁴ Suivi du programme Anthrobots, Levin Lab, Université Tufts, publications actives 2025 — cycle de vie complet et rajeunissement cellulaire observé.

⁵ Levin, M. (2021). « Bioelectric signaling regulates size in zebrafish fins. » *PLOS Genetics* ; et Levin, M. (2023). « Darwin's agentive animals: on the role of goal-directedness in evolution. » *Biological Journal of the Linnean Society*.

⁶ Référence : mycosmicventures.com, article sur les xenobots et anatomical setpoints, mars 2026.

---

**Note personnelle**

Quand j'ai découvert le travail de Levin via ses conférences en ligne, ma première réaction n'était pas « c'est fascinant biologiquement ». C'était : quel est le ratio énergie/performance comparé au silicium, et est-ce que ça peut s'industrialiser ? C'est le réflexe d'un analyste de systèmes complexes qui pense avec EN × η depuis que j'ai écrit mon rapport de cours à l'UQAC en 2006 sur le déclin de l'économie pétrolière.

La deuxième réaction a été plus personnelle. Si on peut construire des Anthrobots à partir des cellules d'un patient — un organe de calcul biodégradable et personnalisé — alors le mot « puce » n'a plus tout à fait le même sens. Ce n'est pas de l'électronique. C'est de la biologie dirigée. Et la frontière entre instrument et organisme commence à devenir poreuse d'une façon que ni la réglementation ni la philosophie ne sont encore équipées pour traiter.

Je n'ai pas de laboratoire. Mais si un jour pascalgagnon.ca génère des revenus significatifs, c'est exactement le type de programme de recherche que je regarderais à financer — pas nécessairement institutionnel, mais ciblé sur une question expérimentale précise. Levin lui-même fonctionne par collaborations distribuées. La recherche de rupture n'a pas besoin de s'embourber dans les structures universitaires pour avancer.

Ce qui me fascine dans ce domaine, c'est qu'il réunit mes quatre obsessions récurrentes : l'énergie comme fondation, la transmission et la transformation des formes, les systèmes qui se reconfigurent de l'intérieur, et la question du territoire — ici, le territoire cellulaire, morphogénétique, électrique. La biologie distribuée et l'économie distribuée parlent le même langage. Je commence à peine à l'entendre clairement.

*— Pascal Gagnon, Roberval, mai 2026*
