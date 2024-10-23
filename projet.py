import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns



#file_path = "C:/Users/zadel/Desktop/Cours/ING2/DV/projet/data_proj.csv"

#data = pd.read_csv(file_path, sep=';')

data = pd.read_csv("data_proj.csv", sep=';')

# Titre principal de la page
st.set_page_config(page_title="Project Presentation Dashboard", layout="wide")

# Titre dans la sidebar
st.sidebar.title("Navigation")

# Ajout d'une barre de défilement dans la sidebar
section = st.sidebar.radio(
    " ",
    ("Introduction", "Analyse des Données", "Corrélation")
)


#Ajout des contacts
st.sidebar.header("Mes contacts")

st.sidebar.markdown("""
**Nom :** ZAIRI

**Prénom :** Adel

**Email :** [adel.zairi@efrei.fr](mailto:adel.zairi@efrei.net)

**Téléphone :** +33 6 63 19 13 70

[![LinkedIn](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=linkedin&logoColor=white&link=https://www.linkedin.com/in/adel-zairi-705a07292/)](https://www.linkedin.com/in/adel-zairi-705a07292/)

""")



# Titre principal de la page
st.title("Les titres les plus prêtés dans les bibliothèques")
st.write("""
    Ce dataset présente les titres les plus prêtés dans les bibliothèques à Paris en 2022.
""")


# Contenu basé sur la sélection dans la sidebar
if section == "Introduction":
    st.header("Introduction")
    st.write("""
        Mon projet consiste en l'étude d'un dataset sur les titres les plus prêtés
        dans les bibliothèques de prêt.
    """)
    st.subheader("Voici la manière dont les données sont structurées :")
    st.dataframe(data.head())

    # Afficher les colonnes du dataset
    st.subheader("Liste des colonnes du dataset")
    colonnes = data.columns.tolist()
    st.write(colonnes)
    
    # Afficher les types de documents
    st.subheader("Types de documents :")
    compte_types = data['Type de document'].value_counts()

    # Graphique en barres
    fig = px.bar(
        x=compte_types.index,
        y=compte_types.values,
        labels={'x':' ', 'y':'Nombre'},
        title=""
    )
    st.plotly_chart(fig)
   
    # Créer un graphique en camembert
    fig = px.pie(
         values=compte_types.values,
         names=compte_types.index,
         title='',
         )

    # Afficher le graphique
    st.plotly_chart(fig)



    st.subheader("Top 5 des titres les plus prêtés en 2022")
        
    # Sélectionner les 5 titres les plus prêtés en 2022
    top_5_titres = data.nlargest(5, 'Prêts 2022')

    # Créer un graphique en barres pour les 5 titres les plus prêtés    
    fig = px.bar(
        top_5_titres,
        x='Titre',
        y='Prêts 2022',
        labels={'Titre': ' ', 'Prêts 2022': 'Nombre de prêts'},
        )
    
    # Afficher le graphique
    st.plotly_chart(fig)


    st.subheader("Top 5 des titres avec le plus grand nombre de prêts totaux")

    # Sélectionner les 5 titres avec le plus grand nombre de prêts totaux
    top_5_pret_totaux = data.nlargest(5, 'Nombre de prêt total')
    
    # Créer un graphique en barres
    fig_totaux = px.bar(
        top_5_pret_totaux,
        x='Titre',
        y='Nombre de prêt total',
        labels={'Titre': ' ', 'Nombre de prêt total': 'Nombre de prêts totaux'},
        )

    # Afficher le graphique
    st.plotly_chart(fig_totaux)
    

    st.subheader("Top 5 des auteurs avec le plus grand nombre de prêts en 2022")


    # Sommer le nombre de prêts totaux pour chaque auteur
    auteurs_populaires = data.groupby('Auteur')['Nombre de prêt total'].sum().reset_index()
    
    # Sommer le nombre de prêts en 2022 pour chaque auteur
    auteurs_populaires_2022 = data.groupby('Auteur')['Prêts 2022'].sum().reset_index()
    
    # Sélectionner les 5 auteurs avec le plus grand nombre de prêts en 2022
    top_5_auteurs_2022 = auteurs_populaires_2022.nlargest(5, 'Prêts 2022')
    
    # Créer un graphique en barres
    fig_auteurs_2022 = px.bar(
        top_5_auteurs_2022,
        x='Auteur',
        y='Prêts 2022',
        labels={'Auteur': '', 'Prêts 2022': 'Nombre de prêts en 2022'},
        )

    # Afficher le graphique
    st.plotly_chart(fig_auteurs_2022)

    
    
    st.subheader("Top 5 des auteurs avec le plus grand nombre de prêts totaux")

    # Sélectionner les 5 auteurs avec le plus grand nombre de prêts totaux
    top_5_auteurs = auteurs_populaires.nlargest(5, 'Nombre de prêt total')

    # Créer un graphique en barres
    fig_auteurs = px.bar(
        top_5_auteurs,
        x='Auteur',
        y='Nombre de prêt total',
        labels={'Auteur': ' ', 'Nombre de prêt total': 'Nombre de prêts totaux'},
        )

    # Afficher le graphique
    st.plotly_chart(fig_auteurs)





elif section == "Analyse des Données":
    st.header("")
    


    st.subheader("Analyse par titre")

    # Sélectionner les titres à afficher
    titres_disponibles = data['Titre'].unique()
    titres_selectionnes = st.multiselect(
        "Sélectionnez les titres à afficher", 
        options=titres_disponibles,
        )
    
    # Filtrer les données en fonction des titres sélectionnés
    if titres_selectionnes:
        data_filtre_titres = data[data['Titre'].isin(titres_selectionnes)]
        
        # Créer un graphique en barres
        fig6 = px.histogram(
            data_filtre_titres,
            x='Titre',
            y='Prêts 2022',
            color='Type de document',
            barmode='stack',
            labels={'Titre': 'Titre', 'Prêts 2022': 'Nombre de prêts'},
            title="Répartition des prêts par titre"
            )
        
        st.plotly_chart(fig6)


    st.subheader("Analyse par artiste")

    # Sélectionner les auteurs à afficher
    auteurs_disponibles = data['Auteur'].unique()
    auteurs_selectionnes = st.multiselect(
        "Sélectionnez les auteurs à afficher", 
        options=auteurs_disponibles,
        )
    
    # Filtrer les données en fonction des auteurs sélectionnés
    if auteurs_selectionnes:
        data_filtre_auteurs = data[data['Auteur'].isin(auteurs_selectionnes)]
        
        # Créer un graphique en barres
        fig6 = px.histogram(
            data_filtre_auteurs,
            x='Auteur',
            y='Prêts 2022',
            color='Type de document',
            barmode='stack',
            labels={'Auteur': 'Auteur', 'Prêts 2022': 'Nombre de prêts'},
            title="Répartition des prêts par auteur"
            )
        
        # Afficher le graphique
        st.plotly_chart(fig6)


    st.subheader("Analyse par catégorie")
    
    # Sélection du type de document
    types_disponibles = data['Type de document'].unique()
    

    # Créer une sélection multiple avec la liste des types disponibles
    types_selectionnes = st.multiselect(
        "Sélectionnez les types de documents à afficher", 
        options=types_disponibles,
        )
    
    # Filtrer les données en fonction des types sélectionnés
    if types_selectionnes:
        data_filtre = data[data['Type de document'].isin(types_selectionnes)]
        
        # Sélectionner les 5 titres les plus prêtés parmi les types sélectionnés
        top_5_titres = data_filtre.nlargest(5, 'Prêts 2022')
        
        # Grouper les prêts par auteur et sélectionner les 5 auteurs avec le plus de prêts
        auteurs_populaires = data_filtre.groupby('Auteur')['Prêts 2022'].sum().reset_index()
        top_5_auteurs = auteurs_populaires.nlargest(5, 'Prêts 2022')
        
        # Créer deux graphiques en barres
        
        # Graphique pour les titres
        fig3 = px.bar(
            top_5_titres,
            x='Titre',
            y='Prêts 2022',
            labels={'Titre': ' ', 'Prêts 2022': 'Nombre de prêts'},
            title="Titres les plus prêtés par type de document"
            )
        
        # Graphique pour les auteurs
        fig4 = px.bar(
            top_5_auteurs,
            x='Auteur',
            y='Prêts 2022',
            labels={'Auteur': ' ', 'Prêts 2022': 'Nombre de prêts'},
            title="Auteurs les plus populaires par type de document"
            )
        
        # Afficher les graphiques
        st.plotly_chart(fig3)
        st.plotly_chart(fig4)
        
        st.write("On remarque que l'auteur du livre le plus prêté n'est pas forcément l'auteur qui a le plus de prêts au total")

        
    else:
        st.write("Veuillez sélectionner au moins un type de document.")

    


elif section == "Corrélation":
    st.header("Corrélation")
    
    # Sélectionner uniquement les colonnes numériques pertinentes pour la corrélation
    colonnes_numeriques = ['Prêts 2022', 'Nombre de localisations', 'Nombre de prêt total', 'Nombre d\'exemplaires']
    
    # Créer une matrice de corrélation
    correlation_matrix = data[colonnes_numeriques].corr()
    
    # Afficher la matrice de corrélation sous forme de heatmap
    st.subheader("Matrice de corrélation des variables liées aux prêts")
    
    # Créer la heatmap
    plt.figure(figsize=(8, 4))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
    
    # Afficher la heatmap
    st.pyplot(plt)
    

    # Scatter plot entre "Prêts 2022" et "Nombre d'exemplaires"
    st.subheader("Relation entre Prêts 2022 et Nombre d'exemplaires")
    
    fig1 = px.scatter(
        data,
        x='Nombre d\'exemplaires',
        y='Prêts 2022',
        labels={'Nombre d\'exemplaires': 'Nombre d\'exemplaires', 'Prêts 2022': 'Prêts 2022'}
        )

    st.plotly_chart(fig1)
    
    # Scatter plot entre "Nombre de localisations" et "Nombre d'exemplaires"
    st.subheader("Relation entre Nombre de localisations et Nombre d'exemplaires")
    
    fig3 = px.scatter(
        data,
        x='Nombre de localisations',
        y='Nombre d\'exemplaires',
        labels={'Nombre de localisations': 'Nombre de localisations', 'Nombre d\'exemplaires': 'Nombre d\'exemplaires'}
        )
    
    # Afficher le graphique
    st.plotly_chart(fig3)



# Footer
st.markdown("""
    <hr>
    <footer style='text-align: center;'>
        
    </footer>
    """, unsafe_allow_html=True)
