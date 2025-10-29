import streamlit as st

# 1. PARAMÈTRES (A MODIFIER)
# Utilisez un nouveau paramètre d'image pour garantir le cache busting
IMAGE_URL = "https://raw.githubusercontent.com/SraaaaS/road_accident_app/master/APAR_thumbnail_v3.png?v=9" 
TARGET_PATH = "/frontend/application.py"
WAIT_TIME = 1 # Délai de 1 seconde

# 2. CONFIGURATION ET INJECTION OG
st.set_page_config(page_title="Application de Prévention contre les Accidents Routiers", layout="wide")

og_tags = f"""
    <meta property="og:title" content="Application de Prévention contre les Accidents Routiers">
    <meta property="og:image" content="{IMAGE_URL}">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
"""

# Injection des balises OG (Invisible)
st.components.v1.html(og_tags, height=0, width=0)

# 3. AFFICHAGE ET REDIRECTION
# Affiche un message pendant le délai
st.title("Chargement de l'Application...")
st.info(f"Veuillez patienter, redirection en cours (délai de {WAIT_TIME}s pour garantir l'aperçu du lien).")

# Redirection HTML (La plus stable avec délai)
redirection_script = f"""
<meta http-equiv="refresh" content="{WAIT_TIME}; url={TARGET_PATH}">
"""
st.markdown(redirection_script, unsafe_allow_html=True)

# Fin du script. Ne rien ajouter d'autre.
