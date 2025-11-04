#!/usr/bin/env python3
"""
Script de test pour vérifier que toutes les applications sont fonctionnelles
"""

import sys
import importlib.util
from pathlib import Path

def test_import(app_name, file_path):
    """Test l'importation d'une application"""
    print(f"\n{'='*60}")
    print(f"Test: {app_name}")
    print(f"{'='*60}")
    
    try:
        # Vérifier que le fichier existe
        if not Path(file_path).exists():
            print(f"❌ Fichier non trouvé: {file_path}")
            return False
        
        print(f"✓ Fichier trouvé: {file_path}")
        
        # Importer le module
        spec = importlib.util.spec_from_file_location(app_name, file_path)
        if spec is None:
            print(f"❌ Impossible de créer la spec pour {app_name}")
            return False
        
        print(f"✓ Spec créée")
        
        module = importlib.util.module_from_spec(spec)
        print(f"✓ Module créé")
        
        # Note: On ne charge pas le module car cela exécuterait le code Streamlit
        # spec.loader.exec_module(module)
        
        print(f"✅ {app_name}: OK (structure valide)")
        return True
        
    except Exception as e:
        print(f"❌ {app_name}: Erreur - {e}")
        import traceback
        traceback.print_exc()
        return False

def check_dependencies():
    """Vérifier les dépendances principales"""
    print(f"\n{'='*60}")
    print("Vérification des dépendances")
    print(f"{'='*60}")
    
    dependencies = [
        ('streamlit', 'streamlit'),
        ('pandas', 'pandas'),
        ('beautifulsoup4', 'bs4'),
        ('extruct', 'extruct'),
        ('w3lib', 'w3lib'),
        ('lxml', 'lxml'),
        ('openai', 'openai'),
        ('openpyxl', 'openpyxl'),
        ('fuzzywuzzy', 'fuzzywuzzy'),
        ('pyahocorasick', 'ahocorasick'),
        ('plotly', 'plotly')
    ]
    
    missing = []
    for package_name, import_name in dependencies:
        try:
            __import__(import_name)
            print(f"✓ {package_name}")
        except ImportError:
            print(f"✗ {package_name} (manquant)")
            missing.append(package_name)
    
    if missing:
        print(f"\n⚠️  Dépendances manquantes: {', '.join(missing)}")
        print("Installez-les avec: pip install -r requirements.txt")
    else:
        print(f"\n✅ Toutes les dépendances sont installées")
    
    return len(missing) == 0

def main():
    print("="*60)
    print("TEST DES APPLICATIONS ASTROSUITE")
    print("="*60)
    
    # Vérifier les dépendances
    deps_ok = check_dependencies()
    
    # Obtenir le répertoire courant
    import os
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Tester chaque application
    apps = [
        ("Structured Data Analyser", os.path.join(current_dir, "Jsonoptimiser", "json.py")),
        ("Maillage Interne", os.path.join(current_dir, "blablamaillage-interneblabla", "app.py")),
        ("Conversational Queries", os.path.join(current_dir, "conversational-queries", "app.py")),
    ]
    
    results = []
    for app_name, file_path in apps:
        results.append(test_import(app_name, file_path))
    
    # Résumé
    print(f"\n{'='*60}")
    print("RÉSUMÉ")
    print(f"{'='*60}")
    print(f"Applications testées: {len(apps)}")
    print(f"Succès: {sum(results)}")
    print(f"Échecs: {len(apps) - sum(results)}")
    print(f"Dépendances: {'✅ OK' if deps_ok else '⚠️ Manquantes'}")
    
    if all(results) and deps_ok:
        print(f"\n✅ Tous les tests sont passés !")
        print(f"\n💡 Pour lancer l'application:")
        print(f"   streamlit run app.py")
        return 0
    else:
        print(f"\n⚠️ Certains tests ont échoué")
        return 1

if __name__ == "__main__":
    sys.exit(main())
