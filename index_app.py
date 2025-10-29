import streamlit as st
import time

# 1. Configuration et Injection des MÉTADONNÉES (Gardez ceci !)
st.set_page_config(
    page_title="Application de Prévention contre les Accidents Routiers", 
    layout="wide"
)

# ... (Votre injection og_tags via st.components.v1.html ici) ...

# 2. Redirection via Python (la partie critique)
# Définissez l'URL de redirection (le chemin de votre VRAI fichier Streamlit)
# Note : Nous utilisons le chemin relatif comme Streamlit Cloud s'attend.
TARGET_URL = "/frontend/application.py"

# Placez la redirection dans un bloc conditionnel pour qu'elle ne se lance pas sans fin
if st.session_state.get('redirect_done', False) == False:
    st.session_state['redirect_done'] = True
    st.info("Chargement de l'application complète...") # Message de transition si besoin
    time.sleep(0.5) # Petite pause pour laisser le temps au scraper de lire les balises
    st.rerun() # Ceci relance l'application
    
# 3. Code de secours (pour éviter l'écran blanc)
st.markdown(f'<meta http-equiv="refresh" content="0; url={TARGET_URL}">', unsafe_allow_html=True)
# Nous conservons la balise HTML de secours pour les navigateurs ou les environnements qui ne supportent pas st.rerun ou qui ont un cache agressif.

# Le code ci-dessous ne devrait jamais être atteint si la redirection fonctionne.
st.stop()
