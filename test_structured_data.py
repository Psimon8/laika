#!/usr/bin/env python3
"""
Test de l'application Structured Data Analyser avec les nouveaux onglets
"""

import os
import sys

def test_structured_data_app():
    """Teste les modifications de l'application Structured Data"""
    print("🧪 Test de Structured Data Analyser")
    print("=" * 60)
    
    # Vérifier le fichier
    json_path = os.path.join(os.getcwd(), 'Jsonoptimiser', 'json.py')
    
    if not os.path.exists(json_path):
        print(f"❌ Fichier non trouvé: {json_path}")
        return False
    
    print(f"✅ Fichier trouvé: {json_path}")
    
    # Lire le contenu
    with open(json_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Vérifications
    checks = {
        "Module requests importé": "import requests" in content,
        "Onglets créés (st.tabs)": "st.tabs" in content,
        "Fonction fetch_html_from_url": "def fetch_html_from_url" in content,
        "Fonction display_comparison_results": "def display_comparison_results" in content,
        "Tab 1: Vérification par URLs": "🔗 Vérification par URLs" in content,
        "Tab 2: Code HTML Manuel": "📝 Code HTML Manuel" in content,
        "Input URL client": 'client_url = st.text_input("URL de votre site"' in content,
        "Bouton Analyser URLs": '"🔍 Analyser les URLs"' in content,
        "Bouton Comparer schémas": '"🔍 Comparer les schémas"' in content,
    }
    
    print("\n📋 Vérifications:")
    print("-" * 60)
    
    all_passed = True
    for check_name, result in checks.items():
        status = "✅" if result else "❌"
        print(f"{status} {check_name}")
        if not result:
            all_passed = False
    
    print("\n" + "=" * 60)
    
    if all_passed:
        print("🎉 Tous les tests sont passés !")
        print("\n📚 Fonctionnalités disponibles:")
        print("  • Tab 1: Analyse automatique par URLs")
        print("  • Tab 2: Analyse manuelle par code HTML")
        print("  • Comparaison des données structurées")
        print("  • Génération JSON-LD pour données manquantes")
        return True
    else:
        print("❌ Certains tests ont échoué")
        return False

if __name__ == "__main__":
    success = test_structured_data_app()
    sys.exit(0 if success else 1)
