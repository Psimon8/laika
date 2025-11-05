import streamlit as st
from bs4 import BeautifulSoup
import extruct
from w3lib.html import get_base_url
import pandas as pd
import json
import datetime
import requests

st.set_page_config(page_title="🚀 Structured Data Analyser", layout="wide")

# CSS pour fixer le header et les tabs
st.markdown("""
<style>
    /* Fixer le header */
    .main > div:first-child {
        position: sticky;
        top: 0;
        background-color: white;
        z-index: 999;
        padding-bottom: 1rem;
    }
    
    /* Améliorer l'espacement */
    .stTabs {
        position: sticky;
        top: 80px;
        background-color: white;
        z-index: 998;
        padding: 1rem 0;
    }
    
    /* Style pour les colonnes */
    [data-testid="column"] {
        padding: 1rem;
    }
</style>
""", unsafe_allow_html=True)

st.title("🚀 Structured Data Analyser")

def extract_jsonld_schema(html_content, url="http://example.com"):
    base_url = get_base_url(html_content, url)
    data = extruct.extract(
        html_content,
        base_url=base_url,
        syntaxes=['json-ld'],
        uniform=True
    )
    return data.get('json-ld', [])

def flatten_schema(jsonld_data):
    results = set()
    def recurse(obj, current_type=None):
        if isinstance(obj, dict):
            obj_type = obj.get('@type', current_type)
            # Gestion du cas où @type peut être une liste ou une chaîne
            if obj_type:
                if isinstance(obj_type, list):
                    # Si @type est une liste, on prend le premier élément
                    obj_type = obj_type[0] if obj_type else current_type
                if obj_type:
                    results.add((obj_type, '@type'))
            for key, value in obj.items():
                if key != '@type' and obj_type:  # On ajoute uniquement si obj_type n'est pas None
                    results.add((obj_type, key))
                    recurse(value, obj_type)
        elif isinstance(obj, list):
            for item in obj:
                recurse(item, current_type)
    recurse(jsonld_data)
    return results

def fetch_html_from_url(url):
    """Récupère le contenu HTML d'une URL"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        st.error(f"❌ Erreur lors de la récupération de {url}: {str(e)}")
        return None

def display_comparison_results(client_schema, competitor_schemas, competitor_names):
    """Affiche les résultats de la comparaison"""
    # Construction du tableau
    all_keys = set(client_schema)
    for comp_schema in competitor_schemas:
        all_keys |= comp_schema

    rows = []
    missing_opportunities = []
    # Tri sécurisé en gérant les None potentiels
    for item_type, prop in sorted(all_keys, key=lambda x: (x[0] or '', x[1] or '')):
        row = {
            "Type": item_type or "Non défini",
            "Propriété": prop,
            "Votre site": "✅" if (item_type, prop) in client_schema else "❌"
        }

        at_least_one_has_it = False
        for i, schema in enumerate(competitor_schemas):
            has_it = "✅" if (item_type, prop) in schema else "❌"
            if has_it == "✅":
                at_least_one_has_it = True
            row[competitor_names[i]] = has_it

        if row["Votre site"] == "❌" and at_least_one_has_it:
            missing_opportunities.append((item_type, prop))

        rows.append(row)

    df = pd.DataFrame(rows)

    # ------------------------
    # � TABLEAU COMPARATIF PAR TYPE
    # ------------------------

    st.subheader("🧩 Données Comparées par Type")
    grouped = df.groupby("Type")
    for group_type, group_df in grouped:
        with st.expander(f"📂 {group_type}"):
            def colorize(val):
                return "color: green" if val == "✅" else "color: red"
            styled_group = group_df.style.applymap(colorize, subset=group_df.columns[2:])
            st.dataframe(styled_group, use_container_width=True)

    # ------------------------
    # 📌 RAPPORT OPPORTUNITÉS
    # ------------------------

    with st.expander("� Rapport d'Opportunités Manquantes", expanded=True):
        st.markdown(f"**Nombre total d'opportunités manquantes sur votre site :** `{len(missing_opportunities)}`")
        if missing_opportunities:
            oppo_df = pd.DataFrame(missing_opportunities, columns=["Type", "Propriété"])
            st.dataframe(oppo_df)
        else:
            st.success("🎉 Votre site contient toutes les données structurées détectées chez les concurrents.")

    # ------------------------
    # 🛠️ GÉNÉRER JSON-LD À AJOUTER
    # ------------------------

    with st.expander("🛠️ Générer les données manquantes en JSON-LD", expanded=False):
        if missing_opportunities:
            schema_to_generate = {}
            for item_type, prop in missing_opportunities:
                if item_type not in schema_to_generate:
                    schema_to_generate[item_type] = {}
                if prop != '@type':
                    schema_to_generate[item_type][prop] = f"Exemple_{prop}"

            generated_jsonld = []
            for schema_type, props in schema_to_generate.items():
                block = {
                    "@context": "https://schema.org",
                    "@type": schema_type
                }
                block.update(props)
                generated_jsonld.append(block)

            editable_json = json.dumps(generated_jsonld, indent=2, ensure_ascii=False)
            user_json = st.text_area("✍️ JSON-LD généré automatiquement (modifiable)", value=editable_json, height=300)

            st.download_button(
                label="📥 Télécharger le JSON-LD",
                data=user_json,
                file_name=f"donnees-structurees-{datetime.date.today()}.json",
                mime="application/json"
            )

            st.markdown("👉 Copiez ce code dans une balise `<script type=\"application/ld+json\">` pour l'intégrer dans votre site.")
        else:
            st.info("Aucune donnée à générer. Votre site est complet sur les données analysées.")

# ------------------------
# 📑 CRÉATION DES ONGLETS
# ------------------------

tab1, tab2 = st.tabs(["🔗 Vérification par URLs", "📝 Code HTML Manuel"])

# ========================
# TAB 1: VÉRIFICATION PAR URLs
# ========================

with tab1:
    st.header("🔗 Vérification par URLs")
    st.markdown("Renseignez les URLs pour analyser automatiquement les données structurées.")
    
    # Créer 2 colonnes pour Votre site et Concurrents
    col1, col2 = st.columns(2)
    
    # Colonne 1: URL du client
    with col1:
        st.subheader("🟢 Votre site")
        client_url = st.text_input("URL de votre site", placeholder="https://www.exemple.com", key="client_url_input")

    # Colonne 2: URLs des concurrents
    with col2:
        st.subheader("🔴 Concurrents")
        competitor_count_url = st.number_input("Nombre de concurrents", min_value=1, max_value=5, value=2, step=1, key="url_comp_count")

        competitor_urls = []
        for i in range(competitor_count_url):
            url = st.text_input(f"URL du concurrent {i+1}", key=f"url_competitor_{i}", placeholder=f"https://www.concurrent{i+1}.com")
            competitor_urls.append(url)

    # Bouton de comparaison
    if st.button("🔍 Analyser les URLs", key="analyze_urls"):
        if not client_url.strip():
            st.error("❌ Merci de fournir l'URL de votre site.")
        else:
            with st.spinner("🔄 Récupération et analyse des données structurées..."):
                # Récupération HTML du client
                client_html_content = fetch_html_from_url(client_url)
                
                if client_html_content:
                    client_data = extract_jsonld_schema(client_html_content, client_url)
                    client_schema = set()
                    for block in client_data:
                        client_schema |= flatten_schema(block)

                    # Récupération HTML des concurrents
                    competitor_schemas = []
                    competitor_names = []
                    
                    for i, comp_url in enumerate(competitor_urls):
                        if comp_url.strip():
                            comp_html = fetch_html_from_url(comp_url)
                            if comp_html:
                                comp_data = extract_jsonld_schema(comp_html, comp_url)
                                comp_schema = set()
                                for block in comp_data:
                                    comp_schema |= flatten_schema(block)
                                competitor_schemas.append(comp_schema)
                                competitor_names.append(f"Concurrent {i+1}")

                    if competitor_schemas:
                        st.success("✅ Analyse terminée !")
                        st.header("📈 Résultat Comparatif")
                        display_comparison_results(client_schema, competitor_schemas, competitor_names)
                    else:
                        st.warning("⚠️ Aucun concurrent n'a pu être analysé.")

# ========================
# TAB 2: CODE HTML MANUEL
# ========================

with tab2:
    st.header("📝 Saisie HTML Manuelle")
    st.markdown("Collez directement le code HTML pour une analyse personnalisée.")
    
    # Créer 2 colonnes pour Votre site et Concurrents
    col1, col2 = st.columns(2)
    
    # ------------------------
    # 🟢 ZONE DE SAISIE CLIENT
    # ------------------------
    with col1:
        st.subheader("🟢 Votre site")
        client_html = st.text_area("Code HTML complet de votre site", height=400, key="manual_client_html")

    # ------------------------
    # 🔴 ZONE DE SAISIE CONCURRENTS
    # ------------------------
    with col2:
        st.subheader("🔴 Concurrents")
        competitor_count = st.number_input("Nombre de concurrents", min_value=1, max_value=5, value=2, step=1, key="manual_comp_count")

        competitor_htmls = []
        competitor_names = []
        for i in range(competitor_count):
            name = st.text_input(f"Nom du site Concurrent {i+1}", key=f"manual_name_{i}", value=f"Concurrent {i+1}")
            html = st.text_area(f"Code HTML - {name}", key=f"manual_competitor_{i}", height=200)
            competitor_names.append(name)
            competitor_htmls.append(html)

    # ------------------------
    # 🔍 COMPARAISON
    # ------------------------

    if st.button("🔍 Comparer les schémas", key="compare_manual"):
        if not client_html.strip():
            st.error("❌ Merci de fournir le code HTML de votre site.")
        else:
            st.header("📈 Résultat Comparatif")

            # Extraction client
            client_data = extract_jsonld_schema(client_html)
            client_schema = set()
            for block in client_data:
                client_schema |= flatten_schema(block)

            # Extraction concurrents
            competitor_schemas = []
            for html in competitor_htmls:
                if html.strip():
                    comp_data = extract_jsonld_schema(html)
                    comp_schema = set()
                    for block in comp_data:
                        comp_schema |= flatten_schema(block)
                    competitor_schemas.append(comp_schema)

            if competitor_schemas:
                display_comparison_results(client_schema, competitor_schemas, competitor_names)
            else:
                st.warning("⚠️ Aucun concurrent n'a fourni de code HTML.")

