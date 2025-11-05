# 🚀 Structured Data Analyser

## 📋 Description

Outil d'analyse et de comparaison des données structurées JSON-LD entre votre site et vos concurrents.

## ✨ Fonctionnalités

### 🔗 Onglet 1 : Vérification par URLs

**Mode automatique - Le plus rapide !**

#### Utilisation

1. **Entrez l'URL de votre site**
   ```
   https://www.monsite.com
   ```

2. **Ajoutez les URLs concurrentes** (jusqu'à 5)
   ```
   https://www.concurrent1.com
   https://www.concurrent2.com
   ```

3. **Cliquez sur "🔍 Analyser les URLs"**

#### Avantages
- ✅ Récupération automatique du HTML
- ✅ Aucun copier-coller nécessaire
- ✅ Analyse en temps réel
- ✅ Données toujours à jour
- ✅ Gain de temps considérable

#### Prérequis
- URLs accessibles publiquement
- Connexion internet active

---

### 📝 Onglet 2 : Code HTML Manuel

**Mode manuel - Contrôle total**

#### Utilisation

1. **Récupérez le code HTML complet**
   - Ouvrez la page dans votre navigateur
   - Clic droit > "Afficher le code source" (Ctrl+U)
   - Copiez tout le contenu

2. **Collez dans l'interface**
   - Zone "Votre site" : votre code HTML
   - Zones "Concurrent X" : codes HTML des concurrents

3. **Cliquez sur "🔍 Comparer les schémas"**

#### Avantages
- ✅ Fonctionne avec du HTML local
- ✅ Test avant mise en production
- ✅ Analyse de code modifié
- ✅ Aucune limitation d'accès

#### Cas d'usage
- Sites non publics (staging, développement)
- Test de modifications avant déploiement
- Analyse de HTML généré dynamiquement
- Sites protégés par authentification

---

## 📊 Résultats de l'analyse

### Tableau comparatif

Visualisation par type de schema :

| Type | Propriété | Votre site | Concurrent 1 | Concurrent 2 |
|------|-----------|------------|--------------|--------------|
| Organization | name | ✅ | ✅ | ✅ |
| Organization | logo | ❌ | ✅ | ✅ |
| Product | price | ✅ | ✅ | ❌ |

**Légende :**
- ✅ Propriété présente
- ❌ Propriété absente

### Rapport d'opportunités

Liste des propriétés manquantes sur votre site mais présentes chez au moins un concurrent.

**Exemple :**
```
Nombre total d'opportunités manquantes : 3

Type            | Propriété
----------------|------------
Organization    | logo
Organization    | sameAs
Product         | aggregateRating
```

### Génération JSON-LD

L'outil génère automatiquement le code JSON-LD pour les données manquantes :

```json
[
  {
    "@context": "https://schema.org",
    "@type": "Organization",
    "logo": "Exemple_logo",
    "sameAs": "Exemple_sameAs"
  }
]
```

**Intégration :**
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "logo": "https://www.example.com/logo.png",
  "sameAs": [
    "https://www.facebook.com/example",
    "https://twitter.com/example"
  ]
}
</script>
```

---

## 🛠️ Technologies utilisées

- **Python 3.12+**
- **Streamlit** : Interface utilisateur
- **extruct** : Extraction des données structurées
- **BeautifulSoup4** : Parsing HTML
- **requests** : Récupération HTTP (onglet URLs)
- **pandas** : Manipulation de données

---

## 💡 Bonnes pratiques

### Analyse par URLs
1. Utilisez des URLs représentatives (pages principales)
2. Comparez des pages de même type (article vs article, produit vs produit)
3. Vérifiez que les URLs sont accessibles publiquement

### Analyse manuelle
1. Utilisez le code source complet (pas uniquement les balises `<script>`)
2. Vérifiez que le JSON-LD est bien formé
3. Testez avec plusieurs concurrents pour une meilleure vision

### Implémentation
1. Validez le JSON-LD généré avec [Google Rich Results Test](https://search.google.com/test/rich-results)
2. Personnalisez les valeurs d'exemple
3. Respectez les guidelines Schema.org
4. Testez en environnement de staging avant production

---

## 🐛 Dépannage

### Erreur de récupération d'URL

**Problème :** `❌ Erreur lors de la récupération de https://...`

**Causes possibles :**
- URL inaccessible ou inexistante
- Site bloque les robots/scrapers
- Timeout réseau
- Certificat SSL invalide

**Solutions :**
- Vérifiez que l'URL est accessible dans un navigateur
- Utilisez l'onglet "Code HTML Manuel" pour ce site
- Vérifiez votre connexion internet

### Aucune donnée structurée détectée

**Problème :** Tableau vide ou "Aucune donnée détectée"

**Causes possibles :**
- Site ne contient pas de JSON-LD
- JSON-LD mal formé
- HTML incomplet

**Solutions :**
- Vérifiez la présence de balises `<script type="application/ld+json">`
- Validez le JSON avec un outil en ligne
- Utilisez le code source complet de la page

### Différences entre modes

**Problème :** Résultats différents entre URL et manuel

**Explication :**
- Le mode URL récupère le HTML en temps réel
- Le HTML peut varier (géolocalisation, cookies, A/B testing)
- Certains sites génèrent le JSON-LD dynamiquement (JavaScript)

**Solution :**
- Utilisez le mode qui correspond à vos besoins
- Pour du HTML généré par JS, préférez le mode manuel avec le code source rendu

---

## 📚 Ressources

- [Schema.org Documentation](https://schema.org/)
- [Google Search Central - Structured Data](https://developers.google.com/search/docs/appearance/structured-data)
- [JSON-LD Playground](https://json-ld.org/playground/)
- [Google Rich Results Test](https://search.google.com/test/rich-results)

---

## 🤝 Support

Pour toute question ou suggestion :
- Ouvrez une issue sur GitHub
- Consultez le [TROUBLESHOOTING.md](../TROUBLESHOOTING.md)
- Consultez le [GUIDE.md](../GUIDE.md) principal
