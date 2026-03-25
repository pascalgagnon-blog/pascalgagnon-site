# ================================================
# Étape 1 : Build avec Python/Jinja2
# ================================================
FROM python:3.11-slim AS builder

WORKDIR /app

# Installer les dépendances Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code source et générer le site statique
COPY . .
RUN python3 build.py

# ================================================
# Étape 2 : Servir avec Nginx
# ================================================
FROM nginx:alpine

# Copier les fichiers générés dans le dossier dist/
COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]