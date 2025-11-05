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
    
    /* Titre de la sidebar */
    .sidebar-title {
        font-size: 24px;
        font-weight: 700;
        text-align: center;
        padding: 20px 0 10px 0;
    }
    
    /* Retirer les bordures des boutons */
    .stButton>button {
        border: none !important;
        border-radius: 6px;
        padding: 10px 16px;
        width: 100%;
        text-align: left;
        font-size: 14px;
        font-weight: 500;
        transition: all 0.2s ease;
        margin-bottom: 4px;
    }
    
    /* Footer de la sidebar */
    .sidebar-footer {
        text-align: center;
        padding: 20px;
        font-size: 11px;
        opacity: 0.6;
        border-top: 1px solid rgba(250, 250, 250, 0.1);
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
    
    # Bouton Accueil uniquement
    if st.button("🏠 Accueil", key="home", use_container_width=True):
        st.session_state.selected_page = "Accueil"
        st.rerun()
    
    st.markdown("---")
    
    # Menu déroulant pour les outils
    tool_options = [
        "Sélectionner un outil...",
        "🔍 Structured Data Analyser",
        "🔗 Maillage Interne",
        "💬 Questions Conversationnelles"
    ]
    
    selected_tool = st.selectbox(
        "Outils SEO",
        tool_options,
        index=0,
        key="tool_selector"
    )
    
    # Gérer la sélection du menu déroulant
    if selected_tool == "🔍 Structured Data Analyser":
        st.session_state.selected_page = "Structured Data Analyser"
        st.rerun()
    elif selected_tool == "🔗 Maillage Interne":
        st.session_state.selected_page = "Maillage Interne"
        st.rerun()
    elif selected_tool == "💬 Questions Conversationnelles":
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
