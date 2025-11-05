# 📖 Guide d'utilisation - Hub SEO & Analytics

## 🚀 Démarrage

### Installation

1. Clonez le dépôt :
```bash
git clone https://github.com/Psimon8/laika.git
cd laika
```

2. Installez les dépendances :
```bash
pip install -r requirements.txt
```

3. Lancez l'application :
```bash
streamlit run app.py
# ou
./run.sh
```

4. Ouvrez votre navigateur à l'adresse : http://localhost:8501

## 📚 Guide des applications

### 1. 🔍 Structured Data Analyser

#### Objectif
Comparer et optimiser vos données structurées JSON-LD par rapport à la concurrence.

#### Deux modes d'analyse disponibles

L'application propose **2 onglets** pour s'adapter à vos besoins :

##### 📑 **Onglet 1 : 🔗 Vérification par URLs** *(Nouveau)*

Le mode le plus simple et rapide !

1. **Renseignez les URLs**
   - Entrez l'URL de votre site (ex: `https://www.monsite.com`)
   - Définissez le nombre de concurrents (1 à 5)
   - Entrez les URLs des sites concurrents

2. **Lancez l'analyse automatique**
   - Cliquez sur "🔍 Analyser les URLs"
   - L'application récupère automatiquement le HTML de chaque URL
   - Extraction et analyse des données structurées en temps réel

3. **Avantages**
   - ✅ Aucun copier-coller nécessaire
   - ✅ Analyse directe depuis les URLs
   - ✅ Gain de temps considérable
   - ✅ Données toujours à jour

##### 📑 **Onglet 2 : 📝 Code HTML Manuel**

Le mode traditionnel pour une analyse personnalisée.

1. **Préparez vos données HTML**
   - Copiez le code HTML complet de votre page (incluant les balises `<script type="application/ld+json">`)
   - Faites de même pour vos concurrents (jusqu'à 5)

2. **Entrez les données dans l'interface**
   - Collez votre code HTML dans la zone "Votre site"
   - Définissez le nombre de concurrents à analyser
   - Donnez un nom à chaque concurrent
   - Collez le code HTML de chaque concurrent

3. **Lancez la comparaison**
   - Cliquez sur "🔍 Comparer les schémas"
   - Attendez l'analyse

4. **Avantages**
   - ✅ Contrôle total sur le HTML analysé
   - ✅ Utile pour tester avant mise en production
   - ✅ Analyse de code HTML local ou modifié

#### Résultats de l'analyse (communs aux 2 onglets)

4. **Analysez les résultats**
   - **Tableau comparatif par type** : Visualisez les différences par type de schema (Organization, Product, Article, etc.)
   - **Rapport d'opportunités** : Identifiez les propriétés manquantes sur votre site
   - **Génération JSON-LD** : Obtenez le code à ajouter pour combler les lacunes

5. **Implémentez les améliorations**
   - Téléchargez le JSON-LD généré
   - Modifiez les valeurs d'exemple selon vos besoins
   - Intégrez le code dans votre site

#### Bonnes pratiques
- Analysez les pages similaires (ex: tous les articles de blog, toutes les pages produits)
- Concentrez-vous sur les schémas pertinents pour votre secteur
- Validez vos données avec l'outil de test de Google avant publication

---

### 2. 🔗 Maillage Interne SEO

#### Objectif
Détecter automatiquement les opportunités de liens internes en croisant vos données Google Search Console avec le contenu de vos pages.

#### Prérequis

**Fichier Google Search Console (GSC)**
- Exportez vos données depuis la GSC (Performance > Pages)
- Format : Excel (.xlsx, .xls) ou CSV
- Colonnes requises : `Page`, `Query` (Requête), `Clicks` (Clics)
- Optionnel : `Position` (Position Moyenne)

**Archive HTML de votre site**

**Méthode recommandée : Screaming Frog SEO Spider**

1. **Configuration du crawl**
   - Ouvrez Screaming Frog
   - Configuration > Spider > Rendu
   - **Important** : Sélectionnez "Stocker le HTML" (pas le rendu JS)

2. **Lancez le crawl**
   - Entrez votre URL de départ
   - Cliquez sur "Démarrer"
   - Attendez la fin du crawl

3. **Export du HTML**
   - Export > HTML/Bulk Export > HTML
   - Screaming Frog crée un dossier avec tous les fichiers

4. **Créez le ZIP**
   - Compressez tout le dossier HTML dans un fichier .zip
   - Assurez-vous que les pages contiennent les balises `<link rel="canonical">`

#### Comment l'utiliser

1. **Configurez les paramètres (Sidebar)**
   - **Filtres de données** : Clics minimum, position max, longueur mots-clés
   - **Exclusions** : Stop-words, pages classiques (CGU, contact, etc.)
   - **Analyse floue** : Détection de variations de mots-clés (pluriels, etc.)
   - **Ciblage du contenu** : Sélecteurs HTML à analyser (p, li, span, etc.)

2. **Uploadez vos fichiers**
   - **Colonne gauche** : Fichier GSC (Excel/CSV)
   - **Colonne droite** : Archive ZIP du HTML

3. **Détection automatique des classes CSS (optionnel)**
   - Si activée, l'outil scanne votre HTML
   - Propose les classes CSS contenant le plus de texte
   - Permet de cibler précisément les zones de contenu

4. **Lancez l'analyse**
   - Cliquez sur "Lancer l'Analyse Complète"
   - Suivez la progression dans la barre

5. **Exploitez les résultats**
   - **Tableau des opportunités** : Liste toutes les opportunités détectées
   - **[OK] Nouvelle opportunité** : Aucun lien n'existe, à implémenter
   - **[X] Lien présent** : Un lien existe déjà, pas d'action requise
   - **Priorité** : Score basé sur clics × (1/position)
   - **Export** : CSV ou Excel pour partager avec votre équipe

6. **Tableau de bord**
   - Métriques globales (opportunités totales, nouvelles, existantes)
   - Graphiques de distribution
   - Top 10 des pages sources et cibles

#### Bonnes pratiques

- **Filtrez intelligemment** : Ne gardez que les opportunités pertinentes
- **Vérifiez la cohérence** : Le lien doit avoir du sens dans le contexte
- **Privilégiez le contenu principal** : Liens dans `<p>` > liens dans sidebar
- **Utilisez l'ancre suggérée** : Ou adaptez-la pour plus de naturel
- **Suivez la priorité** : Commencez par les opportunités à fort impact

#### Conseils d'optimisation

- **Réduisez le scope** : Limitez le nombre de pages analysées pour accélérer
- **Installez pyahocorasick** : Améliore drastiquement les performances
- **Désactivez l'analyse floue** : Si vous n'en avez pas besoin (gain de temps)
- **Matching précis** : Assurez-vous que vos canonicals sont bien configurées

---

### 3. 💬 Conversational Queries

#### Objectif
Générer des questions conversationnelles optimisées pour le SEO et la recherche vocale en utilisant l'IA.

#### Prérequis

**Obligatoire**
- Clé API OpenAI (GPT-3.5 ou GPT-4)
  - Créez un compte sur https://platform.openai.com
  - Générez une clé API dans Settings > API Keys
  - **Coût estimé** : ~$0.01-0.10 par analyse selon le nombre de mots-clés

**Optionnel (recommandé)**
- Compte DataForSEO
  - Inscription sur https://dataforseo.com
  - Login + Password pour l'API
  - **Coût** : ~$0.002 par mot-clé pour les volumes de recherche
  - Permet d'obtenir : volumes, CPC, concurrence, suggestions Ads

#### Comment l'utiliser

**Workflow par étapes**

L'application fonctionne en 4 étapes séquentielles :

##### Étape 1 : Collecte des suggestions Google

1. **Entrez vos mots-clés**
   - Un par ligne dans la zone de texte
   - Exemple :
     ```
     restaurant paris
     hôtel luxe
     voyage écologique
     ```

2. **Configurez les niveaux de suggestions**
   - **Niveau 1** : Suggestions directes de Google (ex: "restaurant paris 16")
   - **Niveau 2** : Suggestions des suggestions niveau 1 (si activé)
   - **Niveau 3** : Suggestions des suggestions niveau 2 (si activé)
   - Nombre de suggestions par niveau (1-10)

3. **Cliquez sur "1️⃣ Suggestions"**
   - L'outil interroge l'API Google Suggestions
   - Récupère toutes les suggestions multi-niveaux
   - Affiche le nombre de suggestions collectées

##### Étape 2 : Enrichissement avec volumes (optionnel)

Si DataForSEO est configuré :

1. **Cliquez sur "2️⃣ Volumes"**
   - Récupère les volumes de recherche mensuels
   - Obtient le CPC et le niveau de concurrence
   - Enrichit chaque mot-clé et suggestion

2. **Consultez l'estimation des coûts** (avant de lancer)
   - Nombre de mots-clés estimés
   - Coût pour les volumes
   - Coût total estimé

##### Étape 3 : Recherche de mots-clés Ads (optionnel)

Si l'étape 2 a récupéré des volumes :

1. **Cliquez sur "3️⃣ Recherche mots-clés"**
   - Interroge l'API Google Ads Keywords
   - Récupère des suggestions publicitaires
   - Ajoute encore plus de variantes

##### Étape 4 : Génération de questions conversationnelles

1. **Activez la génération** (Sidebar > Options d'analyse)
   - Cochez "Générer des questions conversationnelles"
   - Définissez le nombre final de questions (défaut: 20)

2. **Cliquez sur "4️⃣ Génération questions"**
   - L'IA analyse les thèmes dans vos suggestions
   - Détecte les intentions de recherche
   - Groupe par thématiques

3. **Sélectionnez les thèmes**
   - Pour chaque mot-clé, des thèmes sont proposés
   - Cochez ceux qui vous intéressent
   - Indice d'importance affiché (1-5/5)

4. **Générez les questions**
   - Cliquez sur "✨ Générer les questions"
   - L'IA crée des questions naturelles
   - Score d'importance attribué à chaque question

#### Résultats et exports

**Section Questions Conversationnelles**
- Liste des questions générées
- Score d'importance
- Mot-clé source
- Thème associé

**Section Mots-clés avec volumes** (si DataForSEO)
- Tableau complet avec volumes, CPC, concurrence
- Filtres et tri disponibles
- Export Excel/CSV

**Section Analyse détaillée**
- Statistiques globales
- Graphiques de distribution
- Analyse thématique

#### Bonnes pratiques

**Choix des mots-clés**
- Privilégiez des mots-clés spécifiques plutôt que génériques
- Variez les intentions (informationnelle, transactionnelle, navigationnelle)
- Commencez avec 5-10 mots-clés pour tester

**Configuration des niveaux**
- **Niveau 1 uniquement** : Pour rester proche de vos mots-clés
- **Niveau 2** : Bonne profondeur sans explosion du volume
- **Niveau 3** : Pour une exploration exhaustive (coût élevé)

**Utilisation de DataForSEO**
- **Essentiel** si vous voulez prioriser par volume
- **Optionnel** si vous explorez juste des idées
- Surveillez les coûts sur de gros volumes

**Sélection des thèmes**
- Ne gardez que les thèmes pertinents pour votre business
- L'importance 4-5/5 = haute priorité
- Désélectionnez les thèmes hors-sujet

**Génération de questions**
- Visez 15-30 questions pour un bon équilibre
- Adaptez le ton selon votre audience
- Utilisez les questions dans vos FAQ, articles, meta descriptions

#### Cas d'usage

**Blog SEO**
- Générez des questions pour vos articles de blog
- Créez des sections FAQ optimisées
- Identifiez de nouveaux sujets à couvrir

**E-commerce**
- Questions produits pour les fiches
- FAQ clients anticipées
- Optimisation pour la recherche vocale

**Service local**
- Questions géolocalisées ("restaurant végétarien près de moi")
- FAQ pour Google Business Profile
- Contenu local optimisé

---

## 🔧 Configuration avancée

### Variables d'environnement (optionnel)

Créez un fichier `.env` à la racine pour stocker vos clés :

```env
OPENAI_API_KEY=sk-...
DATAFORSEO_LOGIN=votre_login
DATAFORSEO_PASSWORD=votre_password
```

Puis modifiez le code pour les charger automatiquement (non implémenté par défaut).

### Performance

**Maillage Interne**
- Installez `pyahocorasick` pour de meilleures performances
- Limitez le nombre de pages analysées
- Utilisez des filtres stricts (clics min, position max)

**Conversational Queries**
- Commencez avec peu de mots-clés
- Activez niveau 2 uniquement si nécessaire
- Désactivez DataForSEO pour des tests rapides

## 🐛 Dépannage

### Erreur "Module not found"
```bash
pip install -r requirements.txt
```

### Application ne démarre pas
```bash
# Vérifiez les logs
streamlit run app.py --logger.level=debug
```

### Problèmes d'import des sous-applications
- Vérifiez que tous les dépôts sont bien clonés
- Les chemins dans `app.py` sont corrects

### DataForSEO ne fonctionne pas
- Vérifiez vos identifiants
- Consultez votre solde sur dataforseo.com
- Vérifiez votre connexion internet

### Questions non générées (Conversational Queries)
- Vérifiez votre clé API OpenAI
- Vérifiez votre quota/solde OpenAI
- Assurez-vous d'avoir sélectionné au moins un thème

## 📞 Support

Pour toute question ou problème :
1. Consultez d'abord ce guide
2. Vérifiez les issues GitHub du projet concerné
3. Ouvrez une nouvelle issue avec les détails de votre problème

## 🎯 Feuille de route

- [ ] Mode sombre
- [ ] Sauvegarde des configurations
- [ ] Historique des analyses
- [ ] Export PDF des rapports
- [ ] API REST pour les outils
- [ ] Authentification utilisateur
- [ ] Dashboard multi-projets

---

Bon SEO ! 🚀
