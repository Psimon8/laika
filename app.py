import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="AstroSuite SEO",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé pour dark mode
st.markdown("""
<style>
    /* Sidebar simple */
    [data-testid="stSidebar"] {
        border-right: 1px solid rgba(250, 250, 250, 0.1);
    }
    
    /* Conteneur de la sidebar */
    [data-testid="stSidebar"] > div:first-child {
        padding-top: 2rem;
    }
    
    /* Titre de la sidebar */
    .sidebar-title {
        font-size: 18px;
        font-weight: 600;
        padding: 0 0 20px 20px;
        text-align: left;
    }
    
    /* Réduire l'espacement entre les boutons au minimum */
    .stButton {
        margin: 0 !important;
        padding: 0 !important;
    }
    
    div[data-testid="stVerticalBlock"] > div {
        gap: 0 !important;
        padding: 0 !important;
    }
    
    .element-container {
        margin: 0 !important;
        padding: 0 !important;
    }
    
    /* Style des boutons - alignés à gauche */
    .stButton>button {
        border: none !important;
        background: transparent !important;
        padding: 6px 20px !important;
        width: 100%;
        text-align: left !important;
        font-size: 15px !important;
        font-weight: 400 !important;
        color: rgba(250, 250, 250, 0.75) !important;
        box-shadow: none !important;
        border-radius: 6px !important;
        margin: 0 !important;
        height: auto !important;
        min-height: 0 !important;
        line-height: 1.4 !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif !important;
        transition: all 0.15s ease !important;
        display: block !important;
    }
    
    .stButton>button:hover {
        background-color: rgba(250, 250, 250, 0.08) !important;
        color: rgba(250, 250, 250, 0.95) !important;
    }
    
    .stButton>button:focus:not(:active) {
        background-color: rgba(250, 250, 250, 0.12) !important;
        color: rgba(250, 250, 250, 1) !important;
    }
    
    /* Footer de la sidebar */
    .sidebar-footer {
        text-align: left;
        padding: 16px 0 16px 20px;
        font-size: 11px;
        opacity: 0.4;
        margin-top: 40px;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    }
</style>
""", unsafe_allow_html=True)

# Menu latéral simplifié
with st.sidebar:
    st.markdown('<div class="sidebar-title">🚀 AstroSuite</div>', unsafe_allow_html=True)
    
    # Initialisation de la sélection
    if 'selected_page' not in st.session_state:
        st.session_state.selected_page = "Accueil"
    
    # Menu avec liens simples - espacement minimal
    if st.button("Home", key="home", use_container_width=True):
        st.session_state.selected_page = "Accueil"
        st.rerun()
    
    if st.button("Structured Data Analyser", key="structured_data", use_container_width=True):
        st.session_state.selected_page = "Structured Data Analyser"
        st.rerun()
    
    if st.button("Maillage Interne", key="maillage", use_container_width=True):
        st.session_state.selected_page = "Maillage Interne"
        st.rerun()
    
    if st.button("Questions Conversationnelles", key="questions", use_container_width=True):
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
    import os
    
    try:
        # Utiliser le chemin relatif au fichier app.py
        current_dir = os.path.dirname(os.path.abspath(__file__))
        json_app_path = os.path.join(current_dir, 'Jsonoptimiser', 'json.py')
        
        if not os.path.exists(json_app_path):
            st.error(f"❌ Fichier introuvable: {json_app_path}")
            st.info("Vérifiez que le dossier Jsonoptimiser existe.")
        else:
            sys.path.insert(0, os.path.join(current_dir, 'Jsonoptimiser'))
            
            # Charger le module sans l'exécuter
            spec = importlib.util.spec_from_file_location("json_app", json_app_path)
            json_app = importlib.util.module_from_spec(spec)
            
            # L'exécution du module charge l'interface Streamlit
            spec.loader.exec_module(json_app)
    except Exception as e:
        st.error(f"❌ Erreur lors du chargement de Structured Data Analyser: {e}")
        st.info("Assurez-vous que toutes les dépendances sont installées.")
        import traceback
        with st.expander("Détails de l'erreur"):
            st.code(traceback.format_exc())

elif selected == "Maillage Interne":
    # Importer et exécuter l'app Maillage Interne
    import sys
    import importlib.util
    import os
    
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        maillage_app_path = os.path.join(current_dir, 'blablamaillage-interneblabla', 'app.py')
        
        if not os.path.exists(maillage_app_path):
            st.error(f"❌ Fichier introuvable: {maillage_app_path}")
        else:
            sys.path.insert(0, os.path.join(current_dir, 'blablamaillage-interneblabla'))
            
            # Charger le module
            spec = importlib.util.spec_from_file_location("maillage_app", maillage_app_path)
            maillage_app = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(maillage_app)
            
            # Exécuter la fonction main si elle existe
            if hasattr(maillage_app, 'main'):
                maillage_app.main()
    except Exception as e:
        st.error(f"❌ Erreur lors du chargement de Maillage Interne: {e}")
        st.info("Assurez-vous que toutes les dépendances sont installées.")
        import traceback
        with st.expander("Détails de l'erreur"):
            st.code(traceback.format_exc())

elif selected == "Conversational Queries":
    # Importer et exécuter l'app Conversational Queries
    import sys
    import importlib.util
    import os
    
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        conv_app_path = os.path.join(current_dir, 'conversational-queries', 'app.py')
        
        if not os.path.exists(conv_app_path):
            st.error(f"❌ Fichier introuvable: {conv_app_path}")
        else:
            sys.path.insert(0, os.path.join(current_dir, 'conversational-queries'))
            
            # Charger le module
            spec = importlib.util.spec_from_file_location("conv_app", conv_app_path)
            conv_app = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(conv_app)
            
            # Exécuter la fonction main
            if hasattr(conv_app, 'main'):
                conv_app.main()
    except Exception as e:
        st.error(f"❌ Erreur lors du chargement de Conversational Queries: {e}")
        st.info("Assurez-vous que toutes les dépendances sont installées.")
        import traceback
        with st.expander("Détails de l'erreur"):
            st.code(traceback.format_exc())
