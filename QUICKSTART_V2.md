# 🚀 Quick Start - Structured Data Analyser v2.0

## 🎯 En 30 secondes

```
┌────────────────────────────────────────────────┐
│  1. Ouvrir l'application Streamlit             │
│  2. Cliquer sur "Structured Data Analyser"     │
│  3. Choisir l'onglet "🔗 Vérification par URLs"│
│  4. Coller vos URLs                            │
│  5. Cliquer sur "🔍 Analyser les URLs"         │
│  6. ✅ Résultats instantanés !                 │
└────────────────────────────────────────────────┘
```

---

## 📋 Mode d'emploi illustré

### Étape 1 : Accès à l'application

```bash
streamlit run app.py
```

Ouvrir : http://localhost:8501

### Étape 2 : Navigation

```
Menu latéral > Structured Data Analyser
```

### Étape 3 : Choix de l'onglet

```
┌──────────────────────────┬─────────────────────────┐
│ 🔗 Vérification par URLs │ 📝 Code HTML Manuel     │ ← Cliquer ici
├──────────────────────────┴─────────────────────────┤
│                                                     │
│  Nouveau ! Plus rapide ! Recommandé !              │
│                                                     │
```

### Étape 4 : Remplissage

#### 🟢 Votre site
```
┌────────────────────────────────────────┐
│ URL de votre site                      │
├────────────────────────────────────────┤
│ https://www.monsite.com                │ ← Coller ici
└────────────────────────────────────────┘
```

#### 🔴 Concurrents
```
Nombre de concurrents : [1] ▼  ← Choisir 1-5

┌────────────────────────────────────────┐
│ URL du concurrent 1                    │
├────────────────────────────────────────┤
│ https://www.concurrent1.com            │ ← Coller ici
└────────────────────────────────────────┘
```

### Étape 5 : Analyse

```
┌──────────────────────┐
│ 🔍 Analyser les URLs │ ← Cliquer !
└──────────────────────┘
```

### Étape 6 : Résultats

```
📈 RÉSULTAT COMPARATIF

┌─────────────────────────────────────────────────┐
│ 📂 Organization                                 │
├──────────┬──────────┬──────────┬───────────────┤
│ Type     │ Propriété│ Votre    │ Concurrent 1  │
├──────────┼──────────┼──────────┼───────────────┤
│ Org      │ name     │    ✅    │      ✅       │
│ Org      │ logo     │    ❌    │      ✅       │ ⚠️ Opportunité !
│ Org      │ url      │    ✅    │      ✅       │
└──────────┴──────────┴──────────┴───────────────┘

📌 Opportunités manquantes : 1
• Organization.logo
```

### Étape 7 : Export

```
🛠️ Générer les données manquantes en JSON-LD

┌─────────────────────────────────────────┐
│ {                                       │
│   "@context": "https://schema.org",    │
│   "@type": "Organization",             │
│   "logo": "Exemple_logo"               │
│ }                                       │
└─────────────────────────────────────────┘

┌──────────────────────┐
│ 📥 Télécharger JSON  │ ← Cliquer pour télécharger
└──────────────────────┘
```

---

## ⚡ Exemples d'URLs à tester

### E-commerce
```
Votre site     : https://www.monshop.com/produit-123
Concurrent 1   : https://www.amazon.fr/dp/B08XYZ
Concurrent 2   : https://www.cdiscount.com/produit-456
```

### Blog / Article
```
Votre site     : https://www.monblog.com/article-seo
Concurrent 1   : https://moz.com/blog/seo-guide
Concurrent 2   : https://ahrefs.com/blog/seo-tips
```

### Site vitrine
```
Votre site     : https://www.monentreprise.com
Concurrent 1   : https://www.concurrent-a.com
Concurrent 2   : https://www.concurrent-b.com
```

---

## 🎓 Conseils rapides

### ✅ À faire
1. **Comparer des pages similaires**
   - Article ↔ Article
   - Produit ↔ Produit
   - Page d'accueil ↔ Page d'accueil

2. **Analyser plusieurs concurrents**
   - Minimum : 2 concurrents
   - Optimal : 3-5 concurrents

3. **Personnaliser le JSON généré**
   - Remplacer "Exemple_logo" par votre vraie URL
   - Ajouter vos vraies valeurs

### ❌ À éviter
1. **Comparer des pages différentes**
   - ❌ Article ↔ Produit
   - ❌ Accueil ↔ Contact

2. **Utiliser des URLs inaccessibles**
   - ❌ Sites protégés par mot de passe
   - ❌ Pages en local (localhost)

3. **Copier-coller tel quel le JSON**
   - ❌ Laisser "Exemple_logo"
   - ✅ Remplacer par vraies valeurs

---

## 🚨 Dépannage rapide

### Problème : "❌ Erreur lors de la récupération"

**Solution :**
1. Vérifier que l'URL est accessible dans un navigateur
2. Vérifier votre connexion internet
3. Essayer le mode "📝 Code HTML Manuel"

### Problème : "Aucune donnée structurée détectée"

**Solution :**
1. Vérifier que la page contient du JSON-LD
2. Afficher le code source (Ctrl+U) et chercher `"@type"`
3. Utiliser [Google Rich Results Test](https://search.google.com/test/rich-results)

### Problème : Timeout

**Solution :**
1. Le site est peut-être lent → Réessayer
2. Vérifier votre connexion internet
3. Utiliser le mode manuel si le problème persiste

---

## 📊 Comprendre les résultats

### Signification des symboles

| Symbole | Signification |
|---------|---------------|
| ✅ | Propriété présente |
| ❌ | Propriété absente |
| ⚠️ | Opportunité (absent chez vous, présent chez concurrent) |

### Types de schemas courants

| Type | Description | Exemple |
|------|-------------|---------|
| `Organization` | Informations entreprise | nom, logo, réseaux sociaux |
| `Product` | Informations produit | prix, disponibilité, avis |
| `Article` | Informations article | titre, auteur, date |
| `WebPage` | Informations page web | URL, description |
| `BreadcrumbList` | Fil d'Ariane | Navigation |
| `FAQPage` | Page FAQ | Questions/Réponses |

---

## 🎯 Workflow recommandé

### 1. Analyse
```
Analyser > Identifier opportunités > Prioriser
```

### 2. Implémentation
```
Télécharger JSON > Personnaliser > Intégrer au site
```

### 3. Validation
```
Google Rich Results Test > Corriger erreurs > Republier
```

### 4. Suivi
```
Attendre indexation > Vérifier Google Search Console
```

---

## 🔗 Ressources utiles

### Validation
- [Google Rich Results Test](https://search.google.com/test/rich-results)
- [Schema.org Validator](https://validator.schema.org/)
- [JSON-LD Playground](https://json-ld.org/playground/)

### Documentation
- [Schema.org](https://schema.org/)
- [Google Search Central](https://developers.google.com/search/docs/appearance/structured-data)

### Outils
- [Structured Data Linter](http://linter.structured-data.org/)
- [Merkle Schema Markup Generator](https://technicalseo.com/tools/schema-markup-generator/)

---

## 💡 Cas d'usage

### E-commerce
**Priorité :** `Product`, `Offer`, `AggregateRating`
```json
{
  "@type": "Product",
  "name": "Nom du produit",
  "offers": {
    "@type": "Offer",
    "price": "99.99",
    "priceCurrency": "EUR"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.5",
    "reviewCount": "89"
  }
}
```

### Blog
**Priorité :** `Article`, `Person` (auteur), `Organization`
```json
{
  "@type": "Article",
  "headline": "Titre de l'article",
  "author": {
    "@type": "Person",
    "name": "Nom de l'auteur"
  },
  "datePublished": "2025-11-05"
}
```

### Entreprise locale
**Priorité :** `LocalBusiness`, `PostalAddress`, `GeoCoordinates`
```json
{
  "@type": "LocalBusiness",
  "name": "Mon Entreprise",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "123 Rue Example",
    "addressLocality": "Paris",
    "postalCode": "75001"
  }
}
```

---

## ✨ Prêt ?

### Lancement rapide
```bash
streamlit run app.py
```

### Navigation
```
Menu > Structured Data Analyser > 🔗 Vérification par URLs
```

### Test rapide
```
Votre URL : https://www.example.com
Analyse !
```

---

**Bonne analyse ! 🚀**
