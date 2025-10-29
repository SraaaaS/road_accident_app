import streamlit as st

# 1. Configuration pour le titre (nécessaire même si l'app redirige)
st.set_page_config(
    page_title="Application de Prévention contre les Accidents Routiers", 
    layout="wide"
)

# 2. Injection des MÉTADONNÉES CRITIQUES (og:image) dans le <body>
# Ceci est le seul moyen de forcer Streamlit à inclure ces balises.

image_url = "https://raw.githubusercontent.com/SraaaaS/road_accident_app/master/APAR_thumbnail_v2.png" 
app_url = "https://road-accident-application2.streamlit.app/frontend/application.py" # L'URL complète de votre VRAIE app

og_tags = f"""
    <meta property="og:title" content="Application de Prévention contre les Accidents Routiers">
    <meta property="og:image" content="{image_url}">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
"""

# Le contenu n'est pas affiché, mais les balises sont injectées.
st.components.v1.html(og_tags, height=0, width=0)

# 3. Redirection immédiate
st.experimental_rerun() 

# Si vous voulez une redirection immédiate, utilisez st.markdown avec du code HTML
# C'est plus fiable pour une redirection instantanée.

redirection_script = f"""
<meta http-equiv="refresh" content="1; url=/">
"""
st.markdown(redirection_script, unsafe_allow_html=True)
# Si vous voulez être sûr que les balises sont lues avant la redirection,
# il faut mettre un délai (content="1; url=...") mais c'est moins 'furtif'.
