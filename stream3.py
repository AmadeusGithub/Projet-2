import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from streamlit_option_menu import option_menu

# Fonction pour la page d'accueil
def accueil():
    st.title("Bienvenue sur le Service WildFlix")

    # Sidebar avec radio et menu
    with st.sidebar:
        # Choix de l'envoi (don)
        add_radio = st.radio(
            "Faites-nous un don",
            ("Standard 3500 €", "Premium 40 000 €")
        )

        # Menu de sélection avec les rubriques
        selection = option_menu(
            menu_title=None,
            options=["Rechercher un film", "Note Book", "Nous contacter", "Indicateurs", "Le Projet 2"]
        )

    # Afficher le logo WILD-FLIX uniquement pour "Rechercher un film" ou par défaut
    if selection == "Rechercher un film" or selection is None:
        st.image("https://raw.githubusercontent.com/AmadeusGithub/Projet-2/refs/heads/main/DALL%C2%B7E%202025-04-10%2011.54.01%20-%20A%20logo%20inspired%20by%20the%20Netflix%20style%2C%20with%20the%20text%20'WILD-FLIX'%20in%20bold%2C%20cinematic%20font.%20The%20text%20is%20deep%20red%20with%20a%20glowing%20effect%2C%20placed%20on%20a%20pure%20.webp", 
                 use_container_width=True)

    # Afficher l'image d'accueil uniquement si aucune rubrique n'est sélectionnée
    if selection is None:
        st.image("https://th.bing.com/th/id/OIP.Sc73CNz3g0TnfaxljGQkBwHaEK?rs=1&pid=ImgDetMain", 
                 use_container_width=True)

    # Contenu pour chaque rubrique
    if selection == "Rechercher un film":
        st.header("Rechercher un film")
        st.write("Entrez le titre du film que vous souhaitez trouver :")
        
        # Première barre de recherche : Modèle 1
        film_search_model1 = st.text_input("Rechercher avec le modèle 1")
        if film_search_model1:
            st.write(f"Recherche en cours avec le modèle 1 pour : {film_search_model1}...")
            # À implémenter : logique de recherche spécifique au modèle 1

        # Deuxième barre de recherche : Modèle 2
        film_search_model2 = st.text_input("Rechercher avec le modèle 2")
        if film_search_model2:
            st.write(f"Recherche en cours avec le modèle 2 pour : {film_search_model2}...")
            # À implémenter : logique de recherche spécifique au modèle 2

    elif selection == "Nous contacter":
        st.header("Nous contacter")
        st.write("Remplissez le formulaire ci-dessous pour nous contacter :")
        name = st.text_input("Votre nom")
        email = st.text_input("Votre email")
        message = st.text_area("Votre message")
        if st.button("Envoyer"):
            st.success("Message envoyé avec succès !")

    elif selection == "Indicateurs":
        st.header("Indicateurs")
        st.image("https://raw.githubusercontent.com/AmadeusGithub/Projet-2/main/projet.png", 
                 use_container_width=True)
        st.write("Accès au tableau de pilotage dynamique :")
        st.write("https://app.powerbi.com/groups/me/reports/10c6bc70-f01e-431d-b4bd-af24e7fed0e0/8d92dbb7a4b312b2d6b9?experience=power-bi")
    
    elif selection == "Note Book":
        st.header("Les Note Book de nos 2 modèles ")
        st.write("Le modèle 1 : https://github.com/AmadeusGithub/Projet-2/blob/7213d8ead6d552951804076c42257cb8ef91b689/model1_notebook.ipynb")  # Remplace par une URL valide si disponible
        st.write("Le modèle 2 : https://github.com/AmadeusGithub/Projet-2/blob/7213d8ead6d552951804076c42257cb8ef91b689/model1_notebook.ipynb")

    elif selection == "Le Projet 2":
        st.header("A propos du Projet 2")
        st.write("WildFlix est un projet de plateforme de streaming dédié à l'élaboration d'un outil de conseil de film.")
        st.write("Cet outil a été conçu pour répondre au besoin de notre client CINEMA-CREUSE.")
        st.write("Sous la supervision de notre professeur Frédéric, l'objectif de ce projet est de formaliser les connaissances théoriques et techniques en Machine Learning. Ce travail vise à approfondir notre compréhension des algorithmes d'apprentissage automatique tout en les appliquant à des problèmes concrets. Nous explorons également les différentes méthodes d'optimisation pour améliorer les performances des modèles. Enfin, ce projet nous permet de développer des compétences pratiques en programmation et en analyse de données.")
        
        # Première image centrée avec légende
        col1, col2, col3 = st.columns([2, 3, 2])  # Ajustement pour centrage
        with col2:  # Colonne centrale
            st.image("https://raw.githubusercontent.com/AmadeusGithub/Projet-2/e53920c662db8f8bf7ffe91ff563214efdeb10df/frederic_potter.jpg", 
                     width=600,  # Taille fixe pour une grande image
                     use_container_width=False)  # Désactiver l'ajustement automatique
            st.markdown("<div style='text-align: center; font-size: 12px;'>Frédéric en plein cours</div>", 
                        unsafe_allow_html=True)

        # Paragraphe entre les deux photos
        st.write("Le groupe 3 était composé de Malik, Lionel et Bryan. Dans le cadre de leur second projet scolaire, ils doivent relever le défi de développer un outil de suggestion de films innovant. Leur objectif ? Créer une plateforme Stream-Lit capable de recommander des films adaptés aux goûts de chaque utilisateur, en s’appuyant sur leurs compétences fraîchement acquises en programmation et en machine learning. Entre lignes de code, café froid et Quêtes Odyssée, ils travaillent en équipe pour transformer leur connaissances en réalité, tout en découvrant les défis du développement collaboratif.")

        # Deuxième image centrée avec la même légende
        col1, col2, col3 = st.columns([2, 2, 2])  # Ajustement pour centrage
        with col2:  # Colonne centrale
            st.image("https://raw.githubusercontent.com/AmadeusGithub/Projet-2/c87917c696b9cd9c9002df72bfa3f694245a4803/jackson.png", 
                     width=600,  # Taille fixe pour une grande image
                     use_container_width=False)  # Désactiver l'ajustement automatique
            st.markdown("<div style='text-align: center; font-size: 12px;'>Le groupe 3 en réunion Scrum matinale</div>", 
                        unsafe_allow_html=True)

        st.write("Le projet ce clôturera Vendredi 11 avril 2025. Après une présentation formelle de l'outil devant un jury composé entre autre du professeur de la promotion et du directeur pédagogique, la performance de l'outil sera analysée. Une appréciation finale ainsi que des axes d'amélioration seront traités à la suite de la présentation ") 

# Appel de la fonction
if __name__ == "__main__":
    accueil()
