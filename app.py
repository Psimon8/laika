import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="AstroSuite SEO",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé simplifié
st.markdown("""
<style>
    /* Fond blanc général */
    .stApp {
        background-color: #ffffff;
        color: #000000;
    }
    
    /* Sidebar simple */
    [data-testid="stSidebar"] {
        background-color: #f8f9fa;
        border-right: 1px solid #e0e0e0;
    }
    
    /* Titre de la sidebar */
    .sidebar-title {
        font-size: 24px;
        font-weight: 700;
        color: #000000;
        text-align: center;
        padding: 20px 0 10px 0;
    }
    
    /* Boutons du menu */
    .stButton>button {
        background-color: #ffffff;
        color: #000000;
        border: 1px solid #e0e0e0;
        border-radius: 6px;
        padding: 10px 16px;
        width: 100%;
        text-align: left;
        font-size: 14px;
        font-weight: 500;
        transition: all 0.2s ease;
        margin-bottom: 4px;
    }
    
    .stButton>button:hover {
        background-color: #f0f0f0;
        border-color: #000000;
    }
    
    /* Footer de la sidebar */
    .sidebar-footer {
        text-align: center;
        padding: 20px;
        font-size: 11px;
        color: #666666;
        border-top: 1px solid #e0e0e0;
        margin-top: 30px;
    }
</style>
""", unsafe_allow_html=True)

# Menu latéral simplifié
with st.sidebar:
    st.markdown('<div class="sidebar-title">🚀 AstroSuite</div>', unsafe_allow_html=True)
    st.markdown("---")
    
    # Initialisation de la sélection
    if 'selected_page' not in st.session_state:
        st.session_state.selected_page = "Accueil"
    
    # Menu simple sans catégories
    if st.button("🏠 Accueil", key="home", use_container_width=True):
        st.session_state.selected_page = "Accueil"
        st.rerun()
    
    if st.button("🔍 Structured Data Analyser", key="structured_data", use_container_width=True):
        st.session_state.selected_page = "Structured Data Analyser"
        st.rerun()
    
    if st.button("🔗 Maillage Interne", key="maillage", use_container_width=True):
        st.session_state.selected_page = "Maillage Interne"
        st.rerun()
    
    if st.button("💬 Questions Conversationnelles", key="questions", use_container_width=True):
        st.session_state.selected_page = "Conversational Queries"
        st.rerun()
    
    st.markdown('<div class="sidebar-footer">AstroSuite © 2025</div>', unsafe_allow_html=True)

# Récupération de la page sélectionnée
selected = st.session_state.selected_page

# Chargement de l'application sélectionnée
if selected == "Accueil":
    st.title("🏠 Bienvenue dans l'AstroSuite")
    
    st.markdown("""
    ## 🎯 Vos outils SEO professionnels
    
    L'AstroSuite regroupe une collection d'outils SEO puissants pour optimiser votre stratégie digitale.
    Naviguez dans les différentes sections via le menu latéral.
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🔍 Structured Data Analyser")
        st.markdown("""
        Analysez et optimisez vos données structurées
        
        - Extraction de schémas JSON-LD
        - Comparaison concurrentielle
        - Génération automatique
        - Optimisation SEO
        """)
        if st.button("Accéder →", key="goto_structured"):
            st.session_state.selected_page = "Structured Data Analyser"
            st.rerun()
    
    with col2:
        st.markdown("### 🔗 Maillage Interne")
        st.markdown("""
        Optimisez votre stratégie de liens internes
        
        - Analyse opportunités de liens
        - Détection automatique des ancres
        - Croisement GSC + HTML
        - Export des recommandations
        """)
        if st.button("Accéder →", key="goto_maillage"):
            st.session_state.selected_page = "Maillage Interne"
            st.rerun()
    
    with col3:
        st.markdown("### 💬 Questions Conversationnelles")
        st.markdown("""
        Générez des questions optimisées pour le SEO
        
        - Suggestions Google multi-niveaux
        - Enrichissement DataForSEO
        - Génération de questions via IA
        - Analyse thématique
        """)
        if st.button("Accéder →", key="goto_questions"):
            st.session_state.selected_page = "Conversational Queries"
            st.rerun()
    
    st.markdown("---")
    
    st.markdown("""
    ## 🚀 Démarrage rapide
    
    1. **Sélectionnez un outil** dans le menu latéral à gauche
    2. **Configurez vos paramètres** selon vos besoins
    3. **Uploadez vos données** ou entrez vos mots-clés
    4. **Lancez l'analyse** et exploitez les résultats
    """)

elif selected == "Structured Data Analyser":
    # Importer et exécuter l'app JSON Optimiser
    import sys
    import importlib.util
    
    try:
        sys.path.insert(0, '/workspaces/laika/Jsonoptimiser')
        
        # Charger le module sans l'exécuter
        spec = importlib.util.spec_from_file_location("json_app", "/workspaces/laika/Jsonoptimiser/json.py")
        json_app = importlib.util.module_from_spec(spec)
        
        # L'exécution du module charge l'interface Streamlit
        spec.loader.exec_module(json_app)
    except Exception as e:
        st.error(f"❌ Erreur lors du chargement de Structured Data Analyser: {e}")
        st.info("Assurez-vous que toutes les dépendances sont installées.")

elif selected == "Maillage Interne":
    # Importer et exécuter l'app Maillage Interne
    import sys
    import importlib.util
    
    try:
        sys.path.insert(0, '/workspaces/laika/blablamaillage-interneblabla')
        
        # Charger le module
        spec = importlib.util.spec_from_file_location("maillage_app", "/workspaces/laika/blablamaillage-interneblabla/app.py")
        maillage_app = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(maillage_app)
        
        # Exécuter la fonction main si elle existe
        if hasattr(maillage_app, 'main'):
            maillage_app.main()
    except Exception as e:
        st.error(f"❌ Erreur lors du chargement de Maillage Interne: {e}")
        st.info("Assurez-vous que toutes les dépendances sont installées.")

elif selected == "Conversational Queries":
    # Importer et exécuter l'app Conversational Queries
    import sys
    import importlib.util
    
    try:
        sys.path.insert(0, '/workspaces/laika/conversational-queries')
        
        # Charger le module
        spec = importlib.util.spec_from_file_location("conv_app", "/workspaces/laika/conversational-queries/app.py")
        conv_app = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(conv_app)
        
        # Exécuter la fonction main
        if hasattr(conv_app, 'main'):
            conv_app.main()
    except Exception as e:
        st.error(f"❌ Erreur lors du chargement de Conversational Queries: {e}")
        st.info("Assurez-vous que toutes les dépendances sont installées.")
