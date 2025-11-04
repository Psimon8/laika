# Déploiement

## Options de déploiement

### 1. Streamlit Community Cloud (Gratuit)

Le moyen le plus simple pour déployer l'application.

**Étapes :**

1. Poussez votre code sur GitHub
2. Rendez-vous sur [share.streamlit.io](https://share.streamlit.io)
3. Connectez votre compte GitHub
4. Sélectionnez votre dépôt `laika`
5. Définissez le fichier principal : `app.py`
6. Cliquez sur "Deploy"

**Configuration des secrets (API keys) :**
- Dans l'interface Streamlit Cloud, allez dans Settings > Secrets
- Ajoutez vos clés au format TOML :
```toml
OPENAI_API_KEY = "sk-..."
DATAFORSEO_LOGIN = "votre_login"
DATAFORSEO_PASSWORD = "votre_password"
```

### 2. Heroku

**Fichiers requis :**

Créez un `Procfile` :
```
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

Créez un `setup.sh` :
```bash
mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
```

**Déploiement :**
```bash
heroku create votre-app-name
git push heroku main
```

### 3. Docker

**Dockerfile :**
```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

**docker-compose.yml :**
```yaml
version: '3.8'
services:
  streamlit:
    build: .
    ports:
      - "8501:8501"
    volumes:
      - .:/app
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - DATAFORSEO_LOGIN=${DATAFORSEO_LOGIN}
      - DATAFORSEO_PASSWORD=${DATAFORSEO_PASSWORD}
```

**Commandes :**
```bash
# Build
docker-compose build

# Run
docker-compose up

# Run en arrière-plan
docker-compose up -d
```

### 4. VPS (Ubuntu/Debian)

**Installation :**
```bash
# Mise à jour du système
sudo apt update && sudo apt upgrade -y

# Installation de Python et pip
sudo apt install python3 python3-pip -y

# Clone du projet
git clone https://github.com/Psimon8/laika.git
cd laika

# Installation des dépendances
pip3 install -r requirements.txt

# Installation de nginx (pour reverse proxy)
sudo apt install nginx -y
```

**Configuration Nginx :**

Créez `/etc/nginx/sites-available/laika` :
```nginx
server {
    listen 80;
    server_name votre-domaine.com;

    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

Activez le site :
```bash
sudo ln -s /etc/nginx/sites-available/laika /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

**Service systemd :**

Créez `/etc/systemd/system/laika.service` :
```ini
[Unit]
Description=Laika SEO Hub
After=network.target

[Service]
Type=simple
User=votre-user
WorkingDirectory=/path/to/laika
ExecStart=/usr/bin/streamlit run app.py --server.port=8501
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

Démarrez le service :
```bash
sudo systemctl daemon-reload
sudo systemctl enable laika
sudo systemctl start laika
sudo systemctl status laika
```

### 5. AWS EC2

Suivez les mêmes étapes que pour VPS, mais :

1. Lancez une instance EC2 (Ubuntu recommandé)
2. Configurez le Security Group pour autoriser le port 80 (HTTP) et 443 (HTTPS)
3. Associez une Elastic IP
4. Installez un certificat SSL avec Let's Encrypt :

```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d votre-domaine.com
```

## Optimisations pour la production

### Performance

**Dans `app.py`, ajoutez :**
```python
# Cache des fonctions coûteuses
@st.cache_data
def load_heavy_data():
    # ...
    pass
```

### Sécurité

1. **Ne jamais commiter les clés API**
   - Utilisez `.env` ou secrets Streamlit
   
2. **Rate limiting**
   - Implémentez des limites sur les appels API
   
3. **HTTPS obligatoire**
   - Utilisez toujours SSL/TLS en production

### Monitoring

**Avec Streamlit Cloud :**
- Logs disponibles dans l'interface
- Métriques d'utilisation

**Avec VPS/Docker :**
```bash
# Logs en temps réel
journalctl -u laika -f

# Ou avec Docker
docker-compose logs -f
```

## Coûts estimés

### Gratuit
- Streamlit Community Cloud (avec limitations)
- GitHub (dépôt public)

### Payant
- **Heroku** : ~$7/mois (Hobby tier)
- **VPS** : ~$5-10/mois (DigitalOcean, Linode, etc.)
- **AWS EC2** : ~$3.50/mois (t2.micro)
- **APIs** :
  - OpenAI : Variable selon usage (~$0.01-1/jour)
  - DataForSEO : Variable selon requêtes (~$0.002/keyword)

## Recommandations

**Pour tester / usage personnel :**
→ Streamlit Community Cloud (gratuit)

**Pour petite équipe :**
→ VPS Digital Ocean ($5/mois) + Docker

**Pour production entreprise :**
→ AWS EC2 + Load Balancer + Auto-scaling

**Pour scaling important :**
→ Kubernetes (GKE, EKS, AKS)
