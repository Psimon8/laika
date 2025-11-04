import streamlit as st
from streamlit_option_menu import option_menu

# Configuration de la page
st.set_page_config(
    page_title="Hub SEO & Analytics",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Menu latéral
with st.sidebar:
    st.title("🚀 Hub SEO & Analytics")
    st.markdown("---")
    
    selected = option_menu(
        menu_title=None,
        options=["Accueil", "Structured Data Analyser", "Maillage Interne", "Conversational Queries"],
        icons=["house", "code-square", "diagram-3", "chat-dots"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "#0066cc", "font-size": "20px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#0066cc"},
        }
    )
    
    st.markdown("---")
    st.markdown("### 📚 À propos")
    st.info(
        "Cette application regroupe plusieurs outils SEO et d'analyse de données. "
        "Sélectionnez un outil dans le menu ci-dessus pour commencer."
    )

# Chargement de l'application sélectionnée
if selected == "Accueil":
    st.title("🏠 Bienvenue sur le Hub SEO & Analytics")
    
    st.markdown("""
    ## 🎯 Outils disponibles
    
    Cette plateforme regroupe trois applications puissantes pour optimiser votre stratégie SEO :
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🔍 Structured Data Analyser")
        st.markdown("""
        **Analysez et optimisez vos données structurées**
        
        - Extraction de schémas JSON-LD
        - Comparaison avec la concurrence
        - Génération automatique de données manquantes
        - Identification des opportunités SEO
        
        📊 Parfait pour améliorer votre présence dans les résultats enrichis Google.
        """)
    
    with col2:
        st.markdown("### 🔗 Maillage Interne")
        st.markdown("""
        **Optimisez votre stratégie de liens internes**
        
        - Analyse des opportunités de maillage
        - Détection automatique des ancres
        - Croisement GSC + contenu HTML
        - Export des recommandations
        
        🎯 Améliorez votre crawl budget et la distribution du PageRank.
        """)
    
    with col3:
        st.markdown("### 💬 Conversational Queries")
        st.markdown("""
        **Générez des questions conversationnelles optimisées**
        
        - Suggestions Google multi-niveaux
        - Enrichissement DataForSEO
        - Génération de questions via IA
        - Analyse thématique
        
        🤖 Créez du contenu adapté à la recherche vocale et FAQ.
        """)
    
    st.markdown("---")
    
    st.markdown("""
    ## 🚀 Démarrage rapide
    
    1. **Sélectionnez un outil** dans le menu latéral à gauche
    2. **Configurez vos paramètres** selon vos besoins
    3. **Uploadez vos données** ou entrez vos mots-clés
    4. **Lancez l'analyse** et exploitez les résultats
    
    ### 💡 Conseils d'utilisation
    
    - **Structured Data Analyser** : Préparez le code HTML de votre site et de vos concurrents
    - **Maillage Interne** : Exportez vos données GSC et crawlez votre site avec Screaming Frog
    - **Conversational Queries** : Munissez-vous d'une clé API OpenAI et optionnellement DataForSEO
    
    ### 🔧 Support et Documentation
    
    Chaque outil dispose de sa propre documentation intégrée. Consultez les sections d'aide
    pour des instructions détaillées.
    """)
    
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: #666;'>"
        "Développé avec ❤️ pour optimiser votre SEO"
        "</div>",
        unsafe_allow_html=True
    )

elif selected == "Structured Data Analyser":
    # Importer et exécuter l'app JSON Optimiser
    import sys
    sys.path.insert(0, '/workspaces/laika/Jsonoptimiser')
    
    # Charger le module
    import importlib.util
    spec = importlib.util.spec_from_file_location("json_app", "/workspaces/laika/Jsonoptimiser/json.py")
    json_app = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(json_app)

elif selected == "Maillage Interne":
    # Importer et exécuter l'app Maillage Interne
    import sys
    sys.path.insert(0, '/workspaces/laika/blablamaillage-interneblabla')
    
    # Charger le module
    import importlib.util
    spec = importlib.util.spec_from_file_location("maillage_app", "/workspaces/laika/blablamaillage-interneblabla/app.py")
    maillage_app = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(maillage_app)
    
    # Exécuter la fonction main si elle existe
    if hasattr(maillage_app, 'main'):
        maillage_app.main()

elif selected == "Conversational Queries":
    # Importer et exécuter l'app Conversational Queries
    import sys
    sys.path.insert(0, '/workspaces/laika/conversational-queries')
    
    # Charger le module
    import importlib.util
    spec = importlib.util.spec_from_file_location("conv_app", "/workspaces/laika/conversational-queries/app.py")
    conv_app = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(conv_app)
    
    # Exécuter la fonction main
    if hasattr(conv_app, 'main'):
        conv_app.main()
