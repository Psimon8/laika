# 🚀 Hub SEO & Analytics

Une application Streamlit centralisée regroupant trois outils puissants pour optimiser votre stratégie SEO.

## 📚 Applications disponibles

### 1. 🔍 Structured Data Analyser
Analysez et optimisez vos données structurées JSON-LD.

**Fonctionnalités :**
- Extraction automatique des schémas JSON-LD
- Comparaison avec la concurrence
- Identification des opportunités manquantes
- Génération automatique de données structurées
- Export et téléchargement des résultats

**Source :** [Jsonoptimiser](https://github.com/RoiduSeo/Jsonoptimiser)

### 2. 🔗 Maillage Interne SEO
Optimisez votre stratégie de liens internes en croisant données GSC et contenu HTML.

**Fonctionnalités :**
- Analyse des opportunités de maillage
- Détection automatique des ancres pertinentes
- Croisement Google Search Console + HTML
- Filtrage intelligent (stop-words, pages classiques)
- Export CSV/Excel des recommandations

**Source :** [blablamaillage-interneblabla](https://github.com/Juankuatro-lab/blablamaillage-interneblabla)

### 3. 💬 Conversational Queries
Générez des questions conversationnelles optimisées pour le SEO et la recherche vocale.

**Fonctionnalités :**
- Suggestions Google multi-niveaux
- Enrichissement DataForSEO (volumes, CPC, concurrence)
- Génération de questions via OpenAI
- Analyse thématique intelligente
- Workflow par étapes avec suivi

**Source :** [conversational-queries](https://github.com/Psimon8/conversational-queries)

## 🚀 Installation

### Prérequis
- Python 3.8+
- pip

### Installation des dépendances

```bash
pip install -r requirements.txt
```

## 🎯 Lancement de l'application

```bash
streamlit run app.py
```

L'application sera accessible à l'adresse : `http://localhost:8501`

## 📖 Utilisation

1. **Lancez l'application** avec la commande ci-dessus
2. **Naviguez** entre les différents outils via le menu latéral
3. **Configurez** vos paramètres selon l'outil sélectionné
4. **Uploadez** vos données ou entrez vos mots-clés
5. **Analysez** et exploitez les résultats

## 🔧 Configuration

### Structured Data Analyser
- Aucune configuration requise
- Préparez le code HTML de votre site et de vos concurrents

### Maillage Interne
- Données Google Search Console (format CSV ou Excel)
- Archive ZIP du HTML de votre site (crawl Screaming Frog recommandé)

### Conversational Queries
- **Requis :** Clé API OpenAI
- **Optionnel :** Identifiants DataForSEO (login + password)

## 📁 Structure du projet

```
laika/
├── app.py                              # Application principale avec navigation
├── requirements.txt                    # Dépendances consolidées
├── README.md                          # Ce fichier
├── Jsonoptimiser/                     # Application Structured Data
│   ├── json.py
│   └── requirements.txt
├── blablamaillage-interneblabla/      # Application Maillage Interne
│   ├── app.py
│   └── requirements.txt
└── conversational-queries/            # Application Conversational Queries
    ├── app.py
    ├── requirements.txt
    ├── services/
    ├── utils/
    └── ...
```

## 🛠️ Technologies utilisées

- **Streamlit** : Framework d'interface utilisateur
- **streamlit-option-menu** : Menu de navigation
- **BeautifulSoup4** : Parsing HTML
- **Pandas** : Manipulation de données
- **OpenAI API** : Génération de contenu IA
- **DataForSEO API** : Données de recherche
- **Plotly** : Visualisations interactives

## 📝 Licence

Ce projet regroupe trois applications distinctes, chacune avec sa propre licence :
- Jsonoptimiser : Voir le dépôt source
- blablamaillage-interneblabla : Voir le dépôt source
- conversational-queries : Voir le dépôt source

## 🤝 Contributions

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou une pull request.

## 📧 Support

Pour toute question ou problème, veuillez consulter la documentation de chaque outil ou ouvrir une issue sur le dépôt GitHub correspondant.

---

Développé avec ❤️ pour optimiser votre SEO