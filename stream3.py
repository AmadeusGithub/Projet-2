import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from streamlit_option_menu import option_menu

# Fonction pour la page d'accueil
def accueil():
    st.title("Bienvenu sur mon service de produits de soins naturels")
    st.image("https://th.bing.com/th/id/OIP.Sc73CNz3g0TnfaxljGQkBwHaEK?rs=1&pid=ImgDetMain")

    with st.sidebar:
        # Choix de l'envoi
        add_radio = st.radio(
            "Choose a shipping method",
            ("Standard (5-15 days)", "Express (2-5 days)")
        )

        # Menu de sélection
        selection = option_menu(
            menu_title=None,
            options=["Soins chat", "Soins chien", "Soins catcheur"]
        )

    if selection == "Soins chat":
        st.header("Soins chat")
        st.image("https://static.streamlit.io/examples/cat.jpg")
    elif selection == "Soins chien":
        st.header("Soins chien")
        st.image("https://static.streamlit.io/examples/dog.jpg")
    elif selection == "Soins catcheur":
        st.header("Soins catcheur")
        st.image("https://www.wwe.com/f/all/2019/04/132_SD_04232019ca_3144--ca4e6a0f0a79d2cf3c3bf6231e7470e7.jpg")

# Appel direct de la fonction sans authentification
accueil()
