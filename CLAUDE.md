# Architecture technique — Pascal Gagnon

**Dernière mise à jour :** 2026-05-08 (architecture 12 systèmes, nav Explorer/Infolettre, sidebar homepage)

---

## Vue d'ensemble

```
pascalgagnon.ca          → Site statique Python/Jinja2 → GitHub → Dokploy → VPS Hostinger
histoire.pascalgagnon.ca → WordPress/Kadence → Likuid.ca (migration Hostinger prévue)
n8n.pascalgagnon.ca      → N8N + PostgreSQL → Docker → Dokploy → VPS Hostinger
[autres sous-domaines]   → Docker → Dokploy → VPS Hostinger → Traefik (SSL)
```

---

## pascalgagnon.ca — Site statique

| Élément | Détail |
|---|---|
| **Générateur** | Python/Jinja2 — générateur maison (`build.py`) |
| **Repo GitHub** | `pascalgagnon-blog/pascalgagnon-site` |
| **Hébergement** | VPS Hostinger via Dokploy (projet `sites`, service `pascalgagnon-site`) |
| **Build dans Dokploy** | Dockerfile multistage : `python:3.11-slim` → `pip install` → `python3 build.py` → `nginx:alpine` |
| **Domaine primaire** | `pascalgagnon.ca` |
| **DNS** | A record `187.124.233.114` + A record `www` → `187.124.233.114` (chez Likuid.ca/cPanel) |
| **SSL** | Let's Encrypt via Traefik (automatique) |
| **Déploiement** | Modifier `src/` → `git push` → Dokploy webhook → redéploie automatiquement |
| **Webhook Dokploy** | `http://187.124.233.114:3000/api/deploy/CgUrlmKfMWMnO8-c0JGin` |

**Page d'accueil — logique `build.py` :**
- `src/index.md` → rendu via `src/_layouts/home.html.j2` (Jinja2 + données `articles.yaml`)
- L'accueil se met à jour automatiquement en modifiant `src/_data/articles.yaml`
- Depuis 2026-03-23 : bascule de `src/index.html` statique → `src/index.md` + `home.html.j2`

**Articles — workflow complet :**
1. Rédiger le `.md` dans `src/articles/[slug].md` avec frontmatter YAML (`layout: article.html.j2`)
2. Ajouter le champ `system: cX` (c1 à c12) dans le frontmatter — **obligatoire**
3. Mettre à jour `src/_data/articles.yaml` (champs `featured` et `recent`)
4. `git push` → Dokploy redéploie automatiquement
- Template article : `src/_layouts/article.html.j2` (hero sombre + corps crème, palette inline)
- Le H1 du corps `.md` est masqué par CSS — le titre est affiché dans le hero via `page.title`
- Une pill "Système de pensée" est affichée en fin d'article, avec lien vers `/systemes/cX/`

**Champ `system` — frontmatter obligatoire :**
- `system: c3` → IA & Contenu (vos_formations_ignorent_la_science_du_jeu_video)
- `system: c4` → IA & Économie Politique (1929-ia, gouvernance_ia)
- `system: c6` → Métabolisme & Santé (12_livres + tous les articles sante-metabolique/)
- `system: c11` → Organisation & Culture (culture-entrepreneuriale/le-quebec-ne-vend-pas-mal)
- `system: c12` → EROEI & Transition (electrification_machinerie_forestiere)
- `build.py` scanne automatiquement tous les `.md` avec `system:` pour peupler les pages hub

**Layouts disponibles (`src/_layouts/`) :**
- `base.html.j2` — structure de base (head, nav, footer)
- `home.html.j2` — page d'accueil (sidebar 12 systèmes desktop + featured + recent depuis `articles.yaml`)
- `article.html.j2` — article standard (hero sombre + corps crème)
- `systeme.html.j2` — page hub par système (hero coloré + liste articles + CTA explorer)
- `sante-metabolique.html.j2` — layout spécifique vertical santé métabolique

**Navigation (tous les templates) :**
- Desktop : logo · Explorer (`/systemes/explorer.html`) · Infolettre CTA (`/#newsletter`)
- Mobile : hamburger → Explorer · Infolettre
- ⚠️ Les anciens liens Économie/PME/Santé/À propos ont été retirés de la nav principale

**Page d'accueil — structure :**
- Hero : pleine largeur (inchangé)
- Corps : grille `[210px sidebar | 1fr contenu]` sur desktop
  - Gauche (sticky) : liste des 12 systèmes avec points colorés, lien vers `/systemes/cX/`
  - Droite : article vedette + articles récents
- Mobile : sidebar masquée → liste compacte 2 colonnes affichée sous les articles récents
- Newsletter : pleine largeur sous la grille

**Palette (inline dans les templates, pas dans main.css) :**
- `--creme: #f5f0e8` · `--noir: #0a0a0a` · `--bleu: #0063b2` · `--bleu-clair: #4d92c9` · `--bleu-pale: #e6eff7`

**Vault local :** `C:\Users\Acer\Documents\Claude_rajotte\pascalgagnon-site` → synchro manuelle vers repo GitHub

---

## Architecture 12 systèmes — pascalgagnon.ca

Depuis mai 2026 : tous les contenus sont organisés en 12 systèmes de pensée plutôt qu'en verticaux thématiques.

| Élément | Détail |
|---|---|
| **Données systèmes** | `src/_data/systemes.yaml` — 12 systèmes (id, name, short, color, description, tags, concepts) |
| **Explorer interactif** | `src/systemes/explorer.html` — page standalone D3.js (bubble chart), copiée telle quelle dans dist/ |
| **Pages hub auto** | `dist/systemes/cX/index.html` — générées par `build_systems()` dans `build.py` |
| **Template hub** | `src/_layouts/systeme.html.j2` — hero coloré par système, grille articles, CTA explorer |
| **Redirections** | `src/economie-energie/`, `src/pme-ia/`, `src/culture-entrepreneuriale/`, `src/sante-metabolique/`, `src/blog/` → meta-refresh vers `/systemes/cX/` ou `/articles/` |

**build.py — fonctions clés ajoutées :**
```python
collect_all_articles(src)   # scanne tous les .md avec system: field → retourne liste avec src_dir + slug
build_systems(env, site, all_articles, dist)  # groupe par système → dist/systemes/cX/index.html
```
- `systemes` est dans `SKIP_VERTICALS` (pas traité comme vertical générique)
- `src/systemes/*.html` sont copiés statiquement dans `dist/systemes/`
- Lien article dans hub : `/{{ article.src_dir }}/{{ article.slug }}/`

**Répertoires scannés par `collect_all_articles` :**
- `src/articles/` · `src/sante-metabolique/` · tout autre répertoire non exclu

**explorer.html — données JS :**
- Hardcodé dans le fichier (pas depuis systemes.yaml — page standalone)
- Pour modifier les articles listés : éditer directement la const `SYSTEMES` dans le `<script>` de explorer.html

---

## histoire.pascalgagnon.ca — WordPress (Likuid)

| Élément | Détail |
|---|---|
| **CMS** | WordPress + thème Kadence |
| **Hébergement** | Likuid.ca (cPanel) |
| **Statut** | Actif — migration vers Hostinger prévue |
| **Child theme** | `kadence-histoire` |

**À faire lors de la migration :** répliquer la config Traefik + Docker sur le VPS Hostinger, pointer le DNS vers 187.124.233.114.

---

## VPS Hostinger — Infrastructure principale

| Élément | Détail |
|---|---|
| **Fournisseur** | Hostinger |
| **IP** | `187.124.233.114` |
| **OS** | Ubuntu 22.04 |
| **Panneau** | Dokploy → `http://187.124.233.114:3000` |
| **Reverse proxy** | Traefik (SSL automatique via ACME Let's Encrypt) |
| **Email ACME** | gagnon.wolfric@gmail.com |
| **Réseau Docker principal** | `dokploy-network` |

### Traefik — Fichiers de configuration

```
/etc/dokploy/traefik/traefik.yml              ← config principale
/etc/dokploy/traefik/dynamic/                 ← providers file (un .yml par service)
/etc/dokploy/traefik/dynamic/acme.json        ← certificats Let's Encrypt
```

**Règle importante :** Traefik peut recevoir ses routes de deux sources — labels Docker dans le `docker-compose.yml` OU fichiers dans `dynamic/`. Les deux peuvent coexister mais il faut éviter les doublons.

---

## N8N — Automatisation

| Élément | Détail |
|---|---|
| **URL** | `https://n8n.pascalgagnon.ca` ✅ |
| **Projet Dokploy** | `automation-n8nwithpostgres-pfpoqz` |
| **Compose** | `/etc/dokploy/compose/automation-n8nwithpostgres-pfpoqz/code/docker-compose.yml` |
| **Env** | `/etc/dokploy/compose/automation-n8nwithpostgres-pfpoqz/code/.env` |
| **Conteneur N8N** | `automation-n8nwithpostgres-pfpoqz-n8n-1` — port interne **5678** |
| **Conteneur PostgreSQL** | `automation-n8nwithpostgres-pfpoqz-postgres-1` |
| **Réseau Docker** | `automation-n8nwithpostgres-pfpoqz` (Traefik y est aussi rattaché) |
| **Volumes** | `automation-n8nwithpostgres-pfpoqz_n8n_data` / `_postgres_data` |
| **Timezone** | `America/Toronto` |

**Commande de redéploiement obligatoire** (depuis le répertoire `code/`) :
```bash
docker compose -p automation-n8nwithpostgres-pfpoqz up -d
```
⚠️ Ne pas utiliser `docker compose up -d` seul — cela crée des conteneurs `code-n8n-1` avec de nouveaux volumes (données perdues).

**Variables .env critiques :**
```
N8N_PORT=5678          ← OBLIGATOIRE — sans ça N8N bind sur port 0 (random) → Bad Gateway
GENERIC_TIMEZONE=America/Toronto
```

**Bug connu résolu (2026-03-23) :** `N8N_PORT` absent du `.env` → N8N se liait à un port aléatoire → Traefik pointait sur 5678 → Bad Gateway. Fix : ajouter `N8N_PORT=5678`.

---

## Méthode Reset — Lead Magnet & Automatisation (Brevo + N8N)

Projet de capture et nurturing d'abonnés autour du produit **Méthode Reset** (Gumroad).

| Élément | Détail |
|---|---|
| **Email marketing** | Brevo ✅ configuré |
| **Mail forwarding** | Configuré ✅ |
| **Produit** | `wolfric6.gumroad.com/l/methode-reset` |
| **Lead magnet** | Tableau Reset (PDF) — offert en échange du courriel |
| **Dossier de travail** | `C:\Users\Acer\Documents\Claude_rajotte\N8N Brevo pour Method Reset` |

**Séquence d'emails Brevo (3 emails) :**
- **Email 1 — Livraison immédiate** : Livraison du Tableau Reset PDF
- **Email 2 — J+2** : La vraie raison de l'épuisement → teaser Méthode Reset
- **Email 3 — J+4** : Résultat concret + offre finale → lien Gumroad

**Placeholders à remplacer dans les templates Brevo :**
- `LIEN_TABLEAU_PDF` → lien direct de téléchargement du tableau
- `LIEN_GUMROAD` → `wolfric6.gumroad.com/l/methode-reset`

**À compléter :**
- [ ] Page / formulaire de capture de courriel (landing page)
- [ ] Relier formulaire → Brevo via N8N ou webhook natif Brevo
- [ ] Tester la séquence complète end-to-end

---

## Workflow déploiement d'un nouveau service sur Hostinger

1. Créer un nouveau projet dans Dokploy (UI web port 3000)
2. Créer le `docker-compose.yml` avec labels Traefik ou fichier dans `dynamic/`
3. S'assurer que le service est sur `dokploy-network` (pour que Traefik le voie)
4. Pointer le DNS du sous-domaine vers `187.124.233.114`
5. Traefik émet le certificat Let's Encrypt automatiquement

---

## Notes de migration (histoire.pascalgagnon.ca → Hostinger)

- Exporter WordPress (contenu + médias)
- Installer WordPress dans un conteneur Docker sur le VPS
- Configurer Traefik pour `histoire.pascalgagnon.ca`
- Tester en staging avant de changer le DNS chez le registraire
- Résilier l'hébergement Likuid après validation

---

*Fichier maintenu manuellement. Mettre à jour à chaque changement d'infrastructure.*
