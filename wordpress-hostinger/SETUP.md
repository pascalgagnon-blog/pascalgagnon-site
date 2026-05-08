# Setup WordPress sur Hostinger — pascalgagnon.ca

Staging sur `wp.pascalgagnon.ca` → basculer sur `pascalgagnon.ca` quand prêt.

---

## Étape 1 — DNS (chez Likuid.ca / cPanel)

Ajouter un A record :
- **Nom** : `wp`
- **Valeur** : `187.124.233.114`
- TTL : 300

---

## Étape 2 — Créer le projet dans Dokploy

1. Ouvrir `http://187.124.233.114:3000`
2. **New Project** → nommer `wordpress-pascalgagnon`
3. Dans le projet → **New Service** → **Docker Compose**
4. Coller le contenu de `docker-compose.yml`
5. Aller dans **Environment** → coller les variables du `.env.example` avec tes vrais mots de passe
6. Cliquer **Deploy**

Traefik va automatiquement émettre le certificat SSL pour `wp.pascalgagnon.ca`.

---

## Étape 3 — Installer WordPress

1. Ouvrir `https://wp.pascalgagnon.ca`
2. Langue : **Français**
3. Remplir :
   - Titre du site : `Pascal Gagnon`
   - Nom d'utilisateur : (à toi)
   - Mot de passe fort
   - Email : `gagnon.wolfric@gmail.com`
4. Cliquer **Installer WordPress**

---

## Étape 4 — Thème Apostrophe 2

1. Tableau de bord WP → **Apparence** → **Thèmes** → **Ajouter**
2. Rechercher : `Apostrophe 2`
3. **Installer** → **Activer**
4. **Apparence** → **Personnaliser** → ajuster couleurs (bleu Roberval `#0063b2`), logo, etc.

---

## Étape 5 — Plugins minimum (et seulement ceux-là)

| Plugin | Raison |
|---|---|
| **Yoast SEO** | SEO de base, balises meta |
| **AI Experiments** (Automattic) | Active les WordPress Abilities → nécessaire pour le MCP |
| **WP Mail SMTP** | Pour que les emails WP partent correctement |

**Ne pas installer** : Elementor, WPBakery, ni aucun page builder. Apostrophe 2 est fait pour rester simple.

---

## Étape 6 — Connecteur MCP WordPress (Cowork)

Une fois WordPress live avec le plugin AI Experiments :

1. Dans WP → **Utilisateurs** → **Profil** → descendre à **Mots de passe d'application**
2. Créer un mot de passe d'application : nommer `Claude Cowork`
3. Copier le mot de passe généré
4. Dans Cowork / Claude Desktop → ajouter le connecteur MCP WordPress :
   - URL : `https://wp.pascalgagnon.ca`
   - Utilisateur : ton nom d'utilisateur WP
   - Mot de passe : le mot de passe d'application

Après ça : Claude peut créer/éditer/publier des articles directement depuis Cowork.

---

## Étape 7 — Basculer pascalgagnon.ca (quand tu es prêt)

1. Changer le label Traefik dans `docker-compose.yml` :
   - `wp.pascalgagnon.ca` → `pascalgagnon.ca`
2. Redéployer dans Dokploy
3. Mettre à jour l'URL dans **Réglages** → **Général** dans WP Admin
4. DNS : le A record `pascalgagnon.ca` pointe déjà sur `187.124.233.114` → rien à changer

---

## Notes importantes

- Les volumes `wp_data` et `wp_db_data` persistent même si le conteneur redémarre
- Commande de redéploiement forcé si besoin depuis le VPS :
  ```bash
  docker compose -p wordpress-pascalgagnon up -d
  ```
- Sauvegarder la DB régulièrement (plugin UpdraftPlus ou backup manuel via `mysqldump`)
