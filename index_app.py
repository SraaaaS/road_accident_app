import streamlit as st

# La seule ligne nécessaire pour définir le titre de la page pour le navigateur
st.set_page_config(page_title="Application de Prévention contre les Accidents Routiers", layout="wide")

# --- MÉTADONNÉES OG:IMAGE ---
# (Assurez-vous que l'URL d'image est la plus récente, par ex. avec ?v=8)
image_url = "https://raw.githubusercontent.com/SraaaaS/road_accident_app/master/APAR_thumbnail_v2.png?v=9" 
TARGET_PATH = "/frontend/application.py"
WAIT_TIME = 1 # Délai d'une seconde pour que le scraper lise les balises

og_tags = f"""
    <meta property="og:title" content="Application de Prévention contre les Accidents Routiers">
    <meta property="og:image" content="{image_url}">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
"""

# 1. Injection des balises og:image/og:title (Invisible)
st.components.v1.html(og_tags, height=0, width=0)

# 2. Redirection HTML (après 1 seconde)
# Cela est beaucoup plus fiable que st.rerun() ou la redirection instantanée.
redirection_script = f"""
<meta http-equiv="refresh" content="{WAIT_TIME}; url={TARGET_PATH}">
<script>
    // Ajout d'un petit script pour garantir la redirection sur certains navigateurs
    setTimeout(function() {{
        window.location.href = '{TARGET_PATH}';
    }}, {WAIT_TIME * 1000});
</script>
"""
st.markdown(redirection_script, unsafe_allow_html=True)

# Affichage d'un message minimal pendant la redirection (pour éviter l'écran blanc)
st.write(f"Chargement de l'application... Vous serez redirigé dans {WAIT_TIME} seconde(s).")

# Le script s'arrête ici. Il ne doit contenir aucune autre logique.
