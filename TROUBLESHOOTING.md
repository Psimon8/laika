# 🔧 Guide de Débogage - AstroSuite

## Problèmes courants et solutions

### ❌ Erreur: "No such file or directory"

**Symptôme:**
```
❌ Erreur lors du chargement de [App]: [Errno 2] No such file or directory
```

**Cause:** Chemins absolus hardcodés qui ne fonctionnent pas dans tous les environnements.

**Solution:** ✅ Résolu dans la version actuelle
- L'application utilise maintenant des chemins relatifs
- Compatible avec tous les environnements (local, Docker, cloud)

**Vérification:**
```bash
python3 test_apps.py
```

---

### ❌ Erreur: "Module not found"

**Symptôme:**
```
ModuleNotFoundError: No module named 'xxx'
```

**Solutions:**

1. **Vérifier les dépendances installées:**
```bash
python3 test_apps.py
```

2. **Réinstaller les dépendances:**
```bash
pip install -r requirements.txt
```

3. **Vérifier la version de Python:**
```bash
python3 --version  # Doit être ≥ 3.8
```

---

### ❌ Application ne démarre pas

**Symptôme:**
```
Cannot GET /
```

**Solutions:**

1. **Vérifier qu'aucun processus n'écoute sur le port:**
```bash
lsof -i :8501
```

2. **Arrêter les anciens processus:**
```bash
pkill -f "streamlit run"
```

3. **Lancer l'application:**
```bash
streamlit run app.py
# ou
./run.sh
```

4. **Vérifier que l'app est accessible:**
- Ouvrir http://localhost:8501

---

### ❌ Page blanche ou erreur au chargement d'une app

**Symptôme:**
L'application principale s'affiche mais une sous-app ne charge pas.

**Solutions:**

1. **Vérifier les détails de l'erreur:**
   - Cliquer sur "Détails de l'erreur" dans l'interface
   - Consulter les logs dans le terminal

2. **Vérifier que les fichiers existent:**
```bash
ls -la Jsonoptimiser/json.py
ls -la blablamaillage-interneblabla/app.py
ls -la conversational-queries/app.py
```

3. **Tester l'import individuellement:**
```bash
cd Jsonoptimiser && python3 -c "import json; print('OK')"
```

---

### 🔑 Erreur: "API key required"

**Symptôme (Conversational Queries):**
```
⚠️ API OpenAI requise pour la génération de questions
```

**Solution:**
1. Obtenir une clé API sur https://platform.openai.com
2. L'entrer dans la sidebar de l'application Conversational Queries
3. (Optionnel) Créer un fichier `.env`:
```env
OPENAI_API_KEY=sk-...
```

---

### 📊 Problème avec DataForSEO

**Symptôme:**
```
⚠️ DataForSEO non configuré
```

**Solution:**
C'est normal ! DataForSEO est **optionnel**.
- Sans DataForSEO : L'app fonctionne avec les suggestions Google uniquement
- Avec DataForSEO : Enrichissement avec volumes de recherche, CPC, etc.

Pour activer :
1. S'inscrire sur https://dataforseo.com
2. Entrer login + password dans la sidebar

---

### 🐛 Problème de parsing HTML (Structured Data)

**Symptôme:**
```
lxml.etree.ParserError: Document is empty
```

**Cause:** Le champ HTML est vide ou invalide.

**Solution:**
1. Copier le code HTML **complet** de la page (Ctrl+U dans le navigateur)
2. Inclure les balises `<html>`, `<head>`, `<body>`
3. S'assurer que le HTML contient des balises `<script type="application/ld+json">`

---

### 💾 Problème d'upload de fichiers (Maillage Interne)

**Symptôme:**
Fichier non reconnu ou erreur de lecture.

**Solutions:**

**Pour le fichier GSC:**
- Format accepté: `.xlsx`, `.xls`, `.csv`
- Colonnes requises: `Page`, `Query`, `Clicks`
- Optionnel: `Position`

**Pour le ZIP HTML:**
- Le ZIP doit contenir des fichiers `.html`
- Les pages doivent avoir des balises `<link rel="canonical">`
- Exporter depuis Screaming Frog: Export > HTML/Bulk Export > HTML

---

## 🔍 Commandes de diagnostic

### Vérifier l'état complet
```bash
python3 test_apps.py
```

### Vérifier les dépendances
```bash
pip list | grep -E "streamlit|pandas|beautifulsoup4|openai"
```

### Vérifier la structure des fichiers
```bash
tree -L 2 -I '__pycache__|.git'
```

### Voir les logs Streamlit
```bash
# L'application affiche les logs dans le terminal
# Chercher les lignes contenant "Error" ou "Exception"
```

### Redémarrer proprement
```bash
# 1. Arrêter tous les processus
pkill -f "streamlit run"

# 2. Nettoyer le cache
rm -rf .streamlit/cache

# 3. Relancer
streamlit run app.py
```

---

## 📝 Logs utiles

### Activer le mode debug
```bash
streamlit run app.py --logger.level=debug
```

### Voir les ports utilisés
```bash
lsof -i :8501
```

### Vérifier la version de Streamlit
```bash
streamlit version
```

---

## 🆘 Support

Si le problème persiste :

1. **Consulter les fichiers de documentation:**
   - `README.md` - Vue d'ensemble
   - `GUIDE.md` - Guide d'utilisation détaillé
   - `VERIFICATION.md` - Rapport de tests
   - `DEPLOYMENT.md` - Déploiement

2. **Exécuter le diagnostic complet:**
```bash
python3 test_apps.py
```

3. **Vérifier les issues GitHub:**
   - Rechercher dans les issues existantes
   - Ouvrir une nouvelle issue avec :
     - Le message d'erreur complet
     - La sortie de `python3 test_apps.py`
     - Votre environnement (OS, Python version)

4. **Réinitialiser complètement:**
```bash
# Sauvegarder vos modifications
git stash

# Repartir de zéro
git pull origin main
pip install -r requirements.txt
streamlit run app.py
```

---

## ✅ Checklist de dépannage rapide

- [ ] `python3 test_apps.py` passe tous les tests
- [ ] `pip list` montre toutes les dépendances
- [ ] Aucun processus sur le port 8501 (`lsof -i :8501`)
- [ ] Les fichiers des 3 apps existent
- [ ] Les clés API sont configurées (si nécessaire)
- [ ] Le navigateur est à jour
- [ ] JavaScript est activé dans le navigateur
- [ ] Pas de bloqueur de pop-up actif

---

**Dernière mise à jour:** 2025-11-04  
**Version de l'app:** 1.0
