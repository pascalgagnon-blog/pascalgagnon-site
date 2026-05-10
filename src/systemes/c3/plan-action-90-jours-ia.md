---
title: "Votre plan d'action en 90 jours pour une IA conforme et souveraine"
description: "Secteurs à risque élevé, coûts réels, outils nommés, étapes concrètes. Tout ce qu'il faut pour passer de la lecture à l'action — cette semaine."
date: "9 mai 2026"
reading_time: "9 min"
system: c3
systeme: "IA & Contenu"
tag: "GUIDE PRATIQUE"
slug: "plan-action-90-jours-ia"
serie: "IA souveraine pour les PME québécoises"
serie_index: 4
layout: article.html.j2
---

# Votre plan d'action en 90 jours pour une IA conforme et souveraine

## Les secteurs à risque élevé — votre exposition réelle


Tous les secteurs qui traitent des données clients sont visés par la loi 25. Mais certains sont structurellement plus exposés que d'autres — soit parce qu'ils manipulent des données particulièrement sensibles, soit parce que leur usage de l'IA est particulièrement intensif, soit les deux.


Services financiers, comptabilité et assurances


C'est le secteur le plus exposé, sans conteste. Les données traitées — revenus, dettes, actifs, historiques de crédit, numéros d'assurance sociale — figurent parmi les plus sensibles de la loi 25. Un cabinet comptable qui utilise ChatGPT pour analyser un bilan client, une firme d'assurance dont les conseillers génèrent des résumés de dossiers avec Copilot, une PME qui traite ses paies avec un outil IA — tous sont en infraction potentielle. La tolérance zéro de la CAI pour ce secteur est documentée : c'est là que les premières sanctions spectaculaires tomberont.


Santé, services sociaux et RH


Les renseignements de santé sont explicitement désignés comme données sensibles dans la loi 25, avec des obligations de protection renforcées et un consentement explicite obligatoire. Cela inclut les cliniques médicales, les services de psychologie, les ressources humaines qui traitent des dossiers d'invalidité ou de gestion de performance, et toute organisation qui utilise l'IA pour analyser des informations sur l'état de santé ou le rendement au travail d'employés.


Secteur municipal et organismes publics


Les municipalités québécoises sont assujetties à la Loi sur l'accès aux documents des organismes publics — l'équivalent de la loi 25 pour le secteur public. Un employé municipal qui utilise ChatGPT pour rédiger un avis d'urbanisme ou traiter une demande de renseignements engage la responsabilité de la Ville. Avec des dossiers fiscaux, des informations sur les propriétés et des données personnelles de citoyens, le risque est réel et sous-estimé.


Services juridiques, notariat et immobilier


Le secret professionnel n'est pas compatible avec l'envoi de données clients dans un outil IA cloud tiers, point. Pour un notaire qui utilise Claude pour résumer un acte de vente ou un avocat qui demande à ChatGPT d'analyser un contrat contenant des informations confidentielles sur son client, le problème dépasse la loi 25 : il touche aux obligations déontologiques. Le Private AI est ici la seule solution qui respecte simultanément la loi et les codes professionnels.


Commerce de détail, CRM et marketing


Toute organisation qui traite des données clients pour du marketing personnalisé, du profilage comportemental ou de la segmentation est directement concernée. La loi 25 encadre explicitement le profilage automatisé — obligation de transparence, droit d'opposition, interdiction de faire tourner ces technologies par défaut. Un outil de marketing IA qui analyse des comportements d'achat clients sans EFVP documentée est une source de risque réel.


## Les coûts réels — sans langue de bois


Voici les chiffres honnêtes pour déployer un Private AI dans une PME québécoise. Ces estimations sont basées sur le hardware disponible en 2025-2026 et les logiciels open-source documentés dans l'article 2.


Organisation de 5 à 15 utilisateurs simultanés


Serveur avec GPU NVIDIA RTX 4080 (16 Go VRAM) : entre 2 500 $ et 3 500 $ CAD pour un système complet. Ce GPU fait tourner confortablement des modèles de 8 à 14 milliards de paramètres — suffisants pour la rédaction, l'analyse de documents, les résumés et les questions-réponses sur base documentaire. Vitesse typique : 30 à 50 tokens par seconde, soit une réponse complète en 5 à 15 secondes.


Organisation de 15 à 50 utilisateurs simultanés


Serveur avec GPU NVIDIA RTX 4090 (24 Go VRAM) : entre 4 000 $ et 6 000 $ CAD pour un système complet. Fait tourner des modèles de 14 à 32 milliards de paramètres avec une qualité de raisonnement nettement supérieure. Recommandé pour les organisations où l'IA sera utilisée intensivement pour l'analyse de documents complexes, la rédaction juridique ou comptable.


Organisation de 50 à 200 utilisateurs simultanés


Serveur avec 2x GPU NVIDIA RTX 4090 ou GPU professionnel A100 : entre 12 000 $ et 20 000 $ CAD selon la configuration. À ce niveau, la gestion requiert une ressource technique interne ou un partenaire TI régional. Le retour sur investissement par rapport aux abonnements SaaS se matérialise en moins de 18 mois pour 50 utilisateurs actifs.


## Les outils nommés — la boîte à outils complète


Voici les logiciels concrets qui composent un Private AI d'entreprise en 2025-2026. Tous sont open-source, gratuits, et activement maintenus par des communautés de développeurs mondiales.


Ollama — le moteur d'inférence


C'est le cœur technique du système. Ollama télécharge et fait tourner les modèles localement avec une seule commande. Il gère la mémoire GPU automatiquement, supporte tous les grands modèles open-weight (Llama 4, Gemma 4, Mistral, Qwen, DeepSeek), et expose une API locale que les autres outils utilisent. Installation : 5 minutes sur Windows, Mac ou Linux. Site : ollama.com


Open WebUI — l'interface utilisateur


C'est ce que vos employés voient. Une interface web identique à ChatGPT — fenêtre de conversation, historique, gestion de fichiers joints. Accessible depuis n'importe quel navigateur sur le réseau interne. Gestion des utilisateurs par rôle (admin, utilisateur standard, département). Supporte le téléchargement de documents pour analyse directe (PDF, Word, Excel). Site : openwebui.com


Les modèles recommandés par usage


Llama 4 Scout (Meta) — usage général, raisonnement, rédaction. Modèle de référence pour la plupart des PME. Gratuit, téléchargeable via Ollama.


Gemma 4 (Google) — rapidité maximale, excellent pour les usages à volume élevé. 85 tokens/seconde sur hardware standard.


Mistral Small 3 — fort en multilinguisme (français/anglais), idéal pour les communications clients bilingues.


Qwen 2.5 Coder — spécialisé code et analyse structurée, recommandé pour les organisations avec des besoins en automatisation.


DeepSeek R1 (distilled) — raisonnement en chaîne de pensée visible, idéal pour les analyses complexes ou la vérification de conformité.


Pour connecter l'IA à vos documents internes (RAG)


Le RAG (Retrieval-Augmented Generation) permet au modèle de répondre en s'appuyant sur vos propres documents — politiques, contrats, procédures, dossiers. Open WebUI intègre cette fonctionnalité nativement depuis la version 0.4. Pour des besoins plus avancés, LangChain et LlamaIndex sont les deux bibliothèques open-source de référence. Aucune de ces options n'envoie vos données à l'extérieur.


## Le plan en 90 jours — semaine par semaine


Phase 1 — Jours 1 à 30 : Conformité de base


L'objectif de cette phase n'est pas la perfection — c'est la bonne foi documentée. Trois actions suffisent pour placer votre organisation dans une posture défendable devant la CAI.


Désigner officiellement votre RPRP. Si vous êtes dirigeant, c'est vous par défaut. Publier son nom et son courriel sur votre site web. Durée : 2 heures.


Faire l'inventaire des outils IA utilisés. Sondage interne de 10 minutes : quels outils, quels employés, quelles données. Documenter dans un fichier conservé 5 ans minimum. Durée : une demi-journée.


Rédiger et publier une politique minimale d'utilisation de l'IA. Une page suffit : quels outils sont autorisés, quelles données ne doivent jamais y transiter, qui est responsable. Durée : une demi-journée avec un gabarit.


Phase 2 — Jours 31 à 60 : Déploiement du Private AI


L'objectif est d'avoir un modèle qui tourne en interne et que deux ou trois employés pilotes utilisent activement.


Acquisition et configuration du serveur. Si vous n'avez pas de ressource TI interne, un partenaire régional peut faire la configuration initiale en une journée. Alternativement : commencer avec un PC haute performance existant pour tester avant d'investir.


Installation Ollama + Open WebUI. Téléchargement du modèle Llama 4 ou Gemma 4. Première conversation de test. Durée : 2 à 4 heures pour un technicien compétent.


Pilote avec 3 à 5 utilisateurs volontaires. Identifier les cas d'usage prioritaires (rédaction de courriels, résumés de réunion, recherche dans les politiques internes). Mesurer le temps gagné. Collecter les retours.


Mettre à jour la politique IA. Ajouter le Private AI comme outil approuvé. Retirer l'accès aux outils cloud pour les données sensibles. Communiquer à tous les employés.


Phase 3 — Jours 61 à 90 : Optimisation et financement


Déploiement complet à tous les employés. Formation de 30 minutes par département. Documenter les cas d'usage validés. Mesurer l'adoption.


Activer le RAG sur vos documents internes. Charger les politiques RH, les procédures opérationnelles, les FAQ clients dans Open WebUI. Tester les réponses. Valider la qualité.


Déposer une demande de subvention. Contacter le Réseau accès PME ou Investissement Québec avec votre dossier documenté (problématique, solution, coûts, gains mesurés). L'Offensive de transformation numérique couvre jusqu'à 50 % des coûts admissibles.


Mesurer le ROI à 90 jours. Temps économisé par employé, réduction des abonnements SaaS, incidents de conformité évités. Ce document devient votre argument pour les prochains investissements.


## Ce que vous pouvez faire aujourd'hui — en moins d'une heure


Si vous avez lu les quatre articles de cette série, vous avez maintenant une compréhension que la grande majorité des dirigeants de PME québécoises n'ont pas encore. Ne laissez pas cette information dormir.


Voici trois actions concrètes que vous pouvez compléter avant la fin de la journée, sans budget, sans technicien, sans consultant :


Ouvrir le site ollama.com et télécharger Ollama sur votre ordinateur personnel. Lancer le modèle Llama 4 ou Gemma 4. Faites une conversation test avec un document que vous avez déjà. Vous verrez concrètement ce que ça fait — sans aucune donnée qui sort de votre machine.


Écrire un courriel à votre équipe de direction pour mettre le sujet à l'ordre du jour de la prochaine réunion. Joindre le lien vers cette série d'articles. Une phrase suffit : « On doit parler de notre exposition loi 25 et de l'alternative Private AI. »


Appeler votre conseiller Réseau accès PME ou contacter Investissement Québec pour demander une rencontre exploratoire sur la transformation numérique. C'est gratuit. C'est leur mandat. Et ils ont accès aux programmes de financement.
