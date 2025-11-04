#!/bin/bash

# Script de lancement de l'application Hub SEO & Analytics

echo "🚀 Lancement du Hub SEO & Analytics..."
echo ""
echo "📝 L'application sera accessible à l'adresse : http://localhost:8501"
echo ""
echo "Pour arrêter l'application, appuyez sur Ctrl+C"
echo ""

cd /workspaces/laika
streamlit run app.py
