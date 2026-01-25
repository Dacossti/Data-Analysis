import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# =========================
# CONFIGURATION DE LA PAGE
# =========================
st.set_page_config(
    page_title="Criminalité, population et lois sur les armes aux États-Unis (1977–1999)",
    page_icon="🇺🇸",
    layout="wide"
)

# =========================
# SECTION D'INFORMATION SUR LE PROJET
# =========================
st.markdown(
    '<h1 style="font-size:36px;">🇺🇸 Criminalité, population et lois sur les armes aux États-Unis (1977–1999)</h1>',
    unsafe_allow_html=True
)

st.markdown('<h2 style="font-size:24px;">Visualisation et Analyse de Données</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("**Auteur**")
    st.write("Stave Icnel Dany OSIAS")
with col2:
    st.markdown("**Source des données**")
    st.write("[Jeu de données `Guns` du package `AER`](https://vincentarelbundock.github.io/Rdatasets/datasets.html)")
with col3:
    st.markdown("**Dernière mise à jour**")
    st.write("24 janvier 2026")

st.divider()

# =========================
# Menu de navigation rapide dans la barre latérale
# =========================

# CSS pour la largeur et les boutons de la barre de navigation
st.markdown("""
<style>
/* Augmenter la largeur de la sidebar */
[data-testid="stSidebar"] {
    width: 400px;
}

/* Décaler le contenu principal pour ne pas chevaucher la sidebar */
[data-testid="stSidebar"][aria-expanded="true"] ~ div[data-testid="stVerticalBlock"] {
    margin-left: 400px;
}

/* Styles des boutons de navigation existants */
.nav-btn {
    display: block;
    padding: 6px 10px;
    margin-bottom: 4px;
    border-radius: 5px;
    text-decoration: none !important;
    color: black;
    font-weight: bold;
    transition: 0.2s;
}
.nav-btn:hover {
    background-color: #d0e2ff;
    color: #1f77b4;
}
</style>
""", unsafe_allow_html=True)


# Ajout des boutons de navigation dans la barre latérale
st.sidebar.markdown('<h1 style="font-size:26px;"> 📌 Navigation rapide</h1>', unsafe_allow_html=True)
st.sidebar.markdown("""
<a class="nav-btn" href="#accueil">🏠 Accueil</a>
<a class="nav-btn" href="#chargement-et-apercu-des-donnees">⏳ Chargement des données</a>
<a class="nav-btn" href="#comparaison-des-etats-par-annee">📊 Comparaison par année</a>
<a class="nav-btn" href="#evolution-des-indicateurs-par-etat">📈 Évolution par état</a>
<a class="nav-btn" href="#loi-sur-les-armes-et-distribution-des-indicateurs-de-crimes">⚖️ Loi et Crimes (distribution et relation)</a>
<a class="nav-btn" href="#distribution-de-la-variable-qualitative-law-par-annee">📊 Distribution de la variable qualitative `law`</a>
<a class="nav-btn" href="#demographie-et-indicateurs-de-crimes">👥 Démographie et Crimes (relation)</a>
""", unsafe_allow_html=True)


# =========================
# SECTION 1 : ACCUEIL
# =========================
st.markdown('<h2>Accueil</h2>', unsafe_allow_html=True)

st.markdown("""
    Dans ce travail, nous nous proposons d'analyser **les différents crimes**, 
    **la composition démographique** et la **présence de lois sur les armes**, ainsi que 
    les **relations** existant entre ces 3 catégories de caractéristiques des États américains.

    Les données couvrent la période de **1977 à 1999** et proviennent du jeu de données 
    `Guns` de la bibliothèque **AER** en R.

    Dans les sections qui suivent, nous effectuerons :
    - des **comparaisons entre les États** selon un indicateur donné ;
    - des **analyses de l’évolution temporelle** d’un indicateur au sein d’un État;
    - des **analyses de la distribution globale** d’un indicateur, ainsi qu’en fonction 
    de la présence ou non de lois sur les armes.
    - des **études des relations** entre indicateurs démographiques (variables quantitatives) 
    et indicateurs de crimes (variables quantitatives), et entre indicateurs de crimes 
    (variables quantitatives) et la présence de lois sur les armes (variables qualitatives binaires).
""")


# =========================
# SECTION 2 : CHARGEMENT DES DONNÉES ET APERÇU
# =========================

st.markdown('<h2>Chargement et Aperçu des données</h2>', unsafe_allow_html=True)

# Commentaire sur les données
st.markdown("""
    - Les données ont été chargées directement depuis le lien source.
    - Elles contiennent des informations sur divers indicateurs de criminalité,
    des caractéristiques démographiques et la présence de lois sur les armes pour chaque État américain de 1977 à 1999.
    - Ici, nous vous en donnons un aperçu avec 6 lignes aléatoires.
""")

@st.cache_data
def load_data():
    url = "https://vincentarelbundock.github.io/Rdatasets/csv/AER/Guns.csv"
    df = pd.read_csv(url, index_col=0)  # première colonne: rownames
    return df

try:
    df_guns = load_data()
    st.dataframe(df_guns.sample(6), width='stretch')
except Exception as e:
    st.error("❌ Échec du chargement des données")
    st.exception(e)
    st.stop()




# =========================
# SECTION 3 : COMPARAISON DES ÉTATS PAR ANNÉE
# =========================
st.markdown('<h2>Comparaison des états par année</h2>', unsafe_allow_html=True)

# Contenu de la section
st.markdown("""
    - Cette section permet de comparer les différents États américains
    selon un indicateur choisi pour une année donnée.
    - L'objectif est d'analyser les variations des indicateurs entre les États et
    d'identifier d'éventuelles tendances liées à la présence ou non de lois sur les armes.
""")

# Dictionnaire des indicateurs disponibles
indicateurs = {
    "Indicateur de Crimes violents": "violent",
    "Indicateur de Meurtres": "murder",
    "Indicateur de Vols": "robbery",
    "Population totale": "population",
    "Densité de population": "density",
    "Pourcentage d'hommes": "male",
    "Pourcentage d'afro-américains": "afam",
    "Pourcentage de blancs": "cauc",
    "Nombre de prisonniers": "prisoners",
    "Revenu moyen": "income"
}

# Sélection de l'année et de l'indicateur pour la comparaison
with st.container(border=True):

    col1, col2 = st.columns(2)

    with col1:
        annees = sorted(df_guns["year"].unique())
        annee = st.selectbox(
            "Sélectionnez une année",
            annees,
            index=annees.index(1999),
            key="annee_comparaison"
        )

    with col2:
        indicateur_label = st.selectbox(
            "Sélectionnez un indicateur pour la comparaison",
            list(indicateurs.keys()),
            key="indicateur_comparaison"
        )

# Récupérer le nom de la colonne correspondant à l'indicateur sélectionné
indicateur = indicateurs[indicateur_label]

# Filtrer les données pour l'année choisie et selon l'indicateur
df_annee = df_guns[df_guns["year"] == annee].sort_values(indicateur, ascending=False)


# Graphique à barres horizontales car on a beaucoup d'états (51) - trop long en position verticale 
fig1 = px.bar(
    df_annee,
    x="state",
    y=indicateur,
    color="law",
    color_discrete_map={
        "yes": "blue",
        "no": "orange"
    },
    title=f"{indicateur_label} par État ({annee})",
    labels={indicateur: f"{indicateur_label}", "state": "État", "law": "Présence de loi sur les armes"},
    template="plotly_white"
)

# Ligne verticale de la moyenne de l'indicateur choisi
moyenne_indicateur = df_annee[indicateur].mean()

fig1.add_hline(
    y=moyenne_indicateur,
    line_dash="dash",
    line_color="red",
    annotation_text="Moyenne globale",
    annotation_position="right"
)

# Personnalisation des infobulles avec alignement des textes
labels = ["État", "Année", "Population", "Présence d'une loi"] + list(indicateurs.keys())

# Calculer la longueur max pour aligner le texte
max_len = max(len(label) for label in labels)

# Fonction pour l'alignement
def pad(label):
    return label.ljust(max_len)

# Mise à jour des infobulles
fig1.update_traces(
    hovertemplate=
    "<span style='font-family:monospace;'>"
    f"{pad('État')} : <b>%{{x}}</b><br>"
    f"{pad(indicateur_label)} : <b>%{{y:.1f}}</b>"
    "</span><extra></extra>"
)

# Rotation des labels de l'axe x pour une meilleure lisibilité
fig1.update_layout(
    xaxis_tickangle=-70
)

# Affichage dans Streamlit
st.plotly_chart(fig1, width=1000, height=600)

# Commentaire sur le graphique
st.markdown(f"""
    - Les barres oranges indiquent les états sans loi `({df_annee[df_annee['law'] == 'no'].shape[0]})` et les barres bleues indiquent les états avec loi sur les armes (`{df_annee[df_annee['law'] == 'yes'].shape[0]}`).
    - La ligne rouge en pointillés représente la moyenne globale de l'indicateur sélectionné pour l'année sélectionnée.
    - A titre d'exemple, pour l'`{indicateur_label}` en `{annee}`, on pourrait penser que les états avec des lois sur les armes (en bleu) observent généralement des valeurs plus basses
    par rapport à ceux sans lois (en orange). **Mais ce n'est pas le cas.** 
    - Ce jugement serait surtout influencé par le fait que le District de Columbia (état sans loi) observe un indicateur qui dépasse de loin tous les autres,
    faussant ainsi la perception visuelle.
    - En réalité, si on regarde de plus près, on observe qu'il y a autant d'états avec des lois sur les armes (en bleu) dépassant la moyenne que d'états sans lois (en orange). 
    - Cela suggère que la présence de lois sur les armes n'a pas d'impact clair et direct sur l'`{indicateur_label}` pour l'année `{annee}`.
""")


# =========================
# SECTION 2 : ÉVOLUTION DE L'INDICE DE CRIMES VIOLENTS PAR ÉTAT
# =========================

st.markdown('<h2>Évolution des indicateurs par état</h2>', unsafe_allow_html=True)

# Contenu de la section
st.markdown("""
    - Cette section permet d'analyser l'évolution temporelle d'un indicateur
    au sein d'un État américain choisi.
    - L'objectif est d'observer les tendances et les variations de l'indicateur
    au fil des années, et de comparer ces tendances avec la moyenne de l'indicateur 
    pour l'état sélectionné sur toute la période de 1977 à 1999.
""")

with st.container(border=True):

    col1, col2 = st.columns(2)

    with col1:
        # Séléction de l'état
        etat = st.selectbox(
            "Choisissez un état",
            sorted(df_guns["state"].unique()),
            index=sorted(df_guns["state"].unique()).index("District of Columbia"),
            key="etat_evolution"
        )

    with col2:
        indicateur_label = st.selectbox(
            "Sélectionnez un indicateur",
            list(indicateurs.keys()),
            key="indicateur_evolution"
        )

# Récupérer le nom de la colonne correspondant à l'indicateur sélectionné
indicateur = indicateurs[indicateur_label]

# Filtrer les données pour l'état choisi
df_etat = df_guns[df_guns["state"] == etat].sort_values("year")


# Style commun pour les info-bulles
infobulle_style = (
    "<span style='font-family:monospace;'>"
    f"{pad('Année')} : <b>%{{x}}</b><br>"
    f"{pad(indicateur_label)} : <b>%{{y:.1f}}</b><br>"
    f"{pad('Population')} : <b>%{{customdata[0]:,.2f}} millions</b>"
    "</span><extra></extra>"
)

# Style commun pour les lignes et les marqueurs
scatter_style = dict(
    mode="lines+markers",
    line=dict(color="blue", width=3),
    marker=dict(size=7),
    hovertemplate=infobulle_style
)

# Création des frames pour l'animation
frames = []
for i in range(1, len(df_etat) + 1):
    subset = df_etat.iloc[:i]  # Sous-ensemble des données jusqu'à l'année i

    frames.append(
        go.Frame(
            data=[go.Scatter(
                x=subset["year"],
                y=subset[indicateur],
                customdata=subset[["population"]],
                **scatter_style
            )],
            name=str(subset["year"].iloc[-1])
        )
    )

# Initialisation de la figure
fig2 = go.Figure(
    data=[go.Scatter(
        x=[df_etat["year"].iloc[0]],            # Premier point
        y=[df_etat[indicateur].iloc[0]],
        customdata=df_etat[["population"]].iloc[:1],
        **scatter_style
    )],
    layout=go.Layout(
        title=f"{indicateur_label} à {etat} de {df_etat['year'].min()} à {df_etat['year'].max()}",
        template="plotly_white",
        xaxis=dict(
            title="Année",
            range=[df_etat["year"].min(), df_etat["year"].max()]
        ),
        yaxis=dict(
            title=indicateur_label,
            range=[
                df_etat[indicateur].min() - 100,
                df_etat[indicateur].max() + 100
            ]
        ),
        # Bouton Play pour l'animation
        updatemenus=[dict(
            type="buttons",
            showactive=False,
            buttons=[dict(
                label="Play",
                method="animate",
                args=[None, {
                    "frame": {"duration": 60},
                    "fromcurrent": True,
                    "transition": {"duration": 0}
                }]
            )],
            x=0,
            y=0
        )]
    ),
    frames=frames
)

# Calcul de la moyenne de l'indicateur pour l'état sélectionné sur toute la période
moyenne_indic_etat = df_etat[indicateur].mean()

# Ajout d'une ligne horizontale pour la moyenne de l'indicateur
fig2.add_hline(
    y=moyenne_indic_etat,
    line_dash="dash",
    line_color="red",
    annotation_text="Moyenne pour l'etat",
    annotation_position="top right"
)

# Affichage dans Streamlit
st.plotly_chart(fig2, width=800)


# Commentaire sur le graphique
st.markdown(f"""
    - Le graphique animé montre l'évolution de l'`{indicateur_label}` à `{etat}` de 1977 à 1999.
    - La ligne rouge en pointillés représente la moyenne de l'indicateur sélectionné pour l'état sélectionné sur toute la période.
    - Par exemple, pour l'`Indicateur de Crimes violents` à `District of Columbia`, on remarque qu'il atteint son maximum en 1993, puis on observe une tendance générale à la **baisse** de 1993 à 1999.
    - Par contre, pour le `nombre de prisonniers`, on observe une tendance générale à la **hausse** de 1977 à 1999.
""")

# =========================
# SECTION 3 : DISTRIBUTION DES INDICATEURS DE CRIMES ET RELATION AVEC LA PRÉSENCE DE LOIS SUR LES ARMES
# =========================
st.markdown('<h2>Loi sur les armes et Distribution des indicateurs de crimes</h2>', unsafe_allow_html=True)

# Contenu de la section
st.markdown("""
    - Cette section permet d'analyser la **distribution** d'un indicateur de crimes (`variables quantitatives`)
    au sein de l'ensemble des États américains, globalement ou en fonction de la présence ou non de lois sur les armes.
    - L'objectif est d'observer comment les indicateurs de crimes varient et globalement et en fonction de la présence de lois sur les armes.
    - Par ailleurs, cette section permet aussi d'analyser la **relation** entre la présence de lois sur les armes (`variable qualitative`) et
    la distribution des indicateurs de crimes (`variables quantitatives`).
""")

with st.container(border=True):

    col1, col2 = st.columns(2)

    with col1:
        # Sélection de l'indicateur
        indicateur_label = st.selectbox(
            "Sélectionnez un indicateur",
            list(indicateurs.keys()),
            key="indicateur_distribution"
        )

    with col2:
        # Choix de la distribution selon la présence de loi
        selon_loi = st.radio(
            "Distribution selon la présence de loi sur les armes?",
            ("Oui", "Non"),
            key="Distribution_selon_loi"
        )


# Récupérer le nom de la colonne correspondant à l'indicateur sélectionné
indicateur = indicateurs[indicateur_label]

# Créer la boxplot selon le choix
if selon_loi == "Non":
    # Boxplot globale sans considération de loi
    fig3 = px.box(
        df_guns,
        y=indicateur,
        labels={indicateur: indicateur_label},
        title=f"{indicateur_label} - Distribution globale",
        template="plotly_white",
        color_discrete_sequence=["blue"],  # couleur unique
        custom_data=["state", "year"]  # pour les infobulles
    )
else:
    # Boxplot comparant la distribution de l'indicateur dans les pays avec et sans loi
    fig3 = px.box(
        df_guns,
        x="law",
        y=indicateur,
        color="law",
        custom_data=["state", "year"],  # pour les infobulles
        color_discrete_map={"yes": "blue", "no": "orange"},
        labels={"law": "Présence d'une loi sur les armes", indicateur: indicateur_label},
        title=f"{indicateur_label} - Distribution selon la présence de loi sur les armes",
        template="plotly_white"
    )

# Ajouter une ligne horizontale pour la moyenne globale
fig3.add_hline(
    y=df_guns[indicateur].mean(),
    line_dash="dash",
    annotation_text="Moyenne globale"
)

# Reglage des infobulles
fig3.update_traces(
    hoverlabel=dict(
        font_size=13,
        font_family="monospace"  # pour aligner les chiffres
    ),
    hovertemplate=(
        "<span style='font-family:monospace;'>"
        f"{pad('État')}: " + "<b>%{customdata[0]}</b><br>"
        f"{pad('Année')}: " + "<b>%{customdata[1]}</b><br>"
        f"{pad(indicateur_label)}: " + "<b>%{y}</b><br>"
        "</span><extra></extra>"
    )
)

# Affichage dans Streamlit
st.plotly_chart(fig3, width=800, height=600)

# Commentaire sur le graphique
st.markdown(f"""
- Si on choisit `non`, le boxplot illustre la distribution globale de l'indicateur à travers l'ensemble des États américains.
- Si on choisit `oui`, le boxplot compare la distribution de l'indicateur entre les États avec loi (`yes`) et ceux sans loi (`no`).
- La ligne en pointillés représente la moyenne globale de l'indicateur sélectionné sur toute la période de 1977 à 1999.
- À titre d'exemple, on observe que la variabilité de l'**Indicateur de crimes violents** au sein des États sans loi est tirée vers le haut,
  notamment en raison de la présence de valeurs extrêmes associées au District of Columbia.
- On remarque également que la médiane de l'**Indicateur de crimes violents** pour les États sans loi est plus élevée que celle des États avec loi.
- Cela suggère que la présence de lois sur les armes pourrait être associée à des niveaux plus faibles de crimes violents,
  sans pour autant établir un lien de causalité directe.
""")

# =========================
# SECTION 4 : DISTRIBUTION DE LA VARIABLE QUALITATIVE 'law'
# =========================
st.header("Distribution de la variable qualitative `law` par année")

# Contenu de la section
st.markdown("""
    - Cette section permet d'analyser la **distribution** de la variable qualitative `law`
    (présence ou non de lois sur les armes) pour une année donnée.
    - L'objectif est d'observer comment la présence de lois sur les armes varie au fil des années.
""")

# Sélection de l'année
annees = sorted(df_guns["year"].unique())
annee = st.selectbox(
    "Sélectionnez une année",
    annees,
    index=annees.index(1999),
    key="annee_distribution_loi"
)   

fig4 = px.pie(
    df_guns[df_guns["year"] == annee],
    names="law",
    title=f"Répartition des États selon la présence de loi en {annee}"
)

# Personnalisation des infobulles
fig4.update_traces(
    hovertemplate=(
        "<span style='font-family:monospace;'>"
        f"{pad('Année')}: " + f"<b>{annee}</b><br>"
        f"{pad('Présence de loi')}: " + "<b>%{label}</b><br>"
        f"{pad('Nombre d\'États')}: " + "<b>%{value}</b>"
        "</span><extra></extra>"
    ),
    textinfo="percent+label"
)

# Marges pour éviter le chevauchement du titre
fig4.update_layout(
    margin=dict(t=80, b=40, l=40, r=40)
)

# Affichage dans Streamlit
st.plotly_chart(fig4, width=800)

# Commentaire sur le graphique
st.markdown(f"""
    - Le graphique circulaire illustre la répartition des États américains
    en fonction de la présence (`yes`) ou de l'absence (`no`) de lois sur les armes pour l'année `{annee}`.
    - On observe qu'en `{annee}`, un nombre de `{df_guns[df_guns['year'] == annee]['law'].value_counts()['yes']}` états sur `51`
    ont mis en place des lois sur les armes, tandis que `{df_guns[df_guns['year'] == annee]['law'].value_counts()['no']}` sur `51` n'en ont pas.
    - En gros, on observe une tendance à l'augmentation du nombre d'États adoptant des lois sur les armes au fil des années.
""")


# =========================
# SECTION 5 : DÉMOGRAPHIE ET INDICATEURS DE CRIMES
# =========================
st.markdown('<h2>Démographie et Indicateurs de crimes</h2>', unsafe_allow_html=True)

st.markdown("### Relation entre un indicateur démographique et un indicateur de crimes pour un état donné")
# Contenu de la section
st.markdown("""
    - Cette section permet d'analyser la relation entre un indicateur démographique
    (variable quantitative) et un indicateur de crimes (variable quantitative)
    pour un État américain choisi.
    - L'objectif est d'observer comment les caractéristiques démographiques
    peuvent être liées aux niveaux de criminalité dans un État donné.
""")

# Dictionnaire des indicateurs disponibles
indicateurs_crime = {
    "Indicateur de Crimes violents": "violent",
    "Indicateur de Meurtres": "murder",
    "Indicateur de Vols": "robbery",
    "Nombre de prisonniers": "prisoners"
}

# Dictionnaire des indicateurs disponibles
indicateurs_demo = {
    "Population totale": "population",
    "Densité de population": "density",
    "Pourcentage d'hommes": "male",
    "Pourcentage d'afro-américains": "afam",
    "Pourcentage de blancs": "cauc",
    "Revenu moyen": "income"
}


with st.container(border=True):

    col1, col2, col3 = st.columns((1, 1.5, 1))

    with col1:
        # Sélection de l'état
        etat = st.selectbox(
            "Sélectionnez un état",
            df_guns["state"].unique(),
            index=list(df_guns["state"].unique()).index("District of Columbia"),
            key="etat_demographie_crime"
        )

    with col2:
       # Sélection de l'indicateur demographique
        indicateur_demo_label = st.selectbox(
            "Sélectionnez un indicateur démographique",
            list(indicateurs_demo.keys()),
            index=list(indicateurs_demo.keys()).index("Pourcentage d'afro-américains"),  # valeur par défaut
            key="indicateur_demographie"
        )   

    with col3:
        # Sélection de l'indicateur de crime
        indicateur_crime_label = st.selectbox(
            "Sélectionnez un indicateur de crime",
            list(indicateurs_crime.keys()),
            key="indicateur_crime"
        )


# Récupérer les noms de colonnes correspondant aux indicateurs sélectionnés
indicateur_demo = indicateurs_demo[indicateur_demo_label] 
indicateur_crime = indicateurs_crime[indicateur_crime_label]


# Scatterplot pour illustrer la relation entre indicateur démographique et indicateur de crime
fig5 = px.scatter(
    df_guns[df_guns["state"] == etat],
    x=indicateur_demo,
    y=indicateur_crime,
    size="population",
    labels={indicateur_demo: indicateur_demo_label, 
            indicateur_crime: indicateur_crime_label,
            "year": "Année",
            "population": "Population"},
    title=f"{indicateur_demo_label} vs {indicateur_crime_label} à {etat} (1977-1999)",
    template="plotly_white"
)

# Personnalisation de l'infobulle
fig5.update_traces(
    customdata=df_guns[df_guns["state"] == etat][["state", "year", indicateur_crime,indicateur_demo, "population"]],
    hovertemplate=(
        "<span style='font-family:monospace;'>"
        f"{pad('État')} : " + "<b>%{customdata[0]}</b><br>"
        f"{pad('Année')} : " + "<b>%{customdata[1]}</b><br>"
        f"{pad(indicateur_crime_label)} : " + "<b>%{customdata[2]:.2f}</b><br>"
        f"{pad(indicateur_demo_label)} : " + "<b>%{customdata[3]:.2f}</b><br>"
        f"{pad('Population')} : " + "<b>%{customdata[4]:,.2f} millions</b><br>"
        "</span><extra></extra>"
    )
)

# Affichage dans Streamlit
st.plotly_chart(fig5, width=800)

# Commentaire sur le graphique
st.markdown(f"""
    - Dans notre premier exemple par défaut, le nuage de points illustre la relation entre le `Pourcentage d'afro-américains` et l'Indicateur de Crimes violents pour l'état de `{etat}`.
    - Pour l'état de `District of Columbia`, la forme du nuage de points ne suggère aucunement une tendance positive entre le `Pourcentage d'afro-américains` et l'`Indicateur de Crimes violents`.
    - On observe des hausses et des baisses régulieres selon une période ou une autre, 
    peut-être influencées par d'autres facteurs sociaux et historiques non pris en compte dans cette analyse.
    - Par contre, si on choisit pour ce même état l'indicateur démographique `Pourcentage d'afro-américains` et l'indicateur de crime `Nombre de prisonniers`,
    on observe une relation négative claire entre les deux indicateurs.
    - Cela suggère que dans le `District of Columbia`, une augmentation du `Pourcentage d'afro-américains` est associée à une diminution du `Nombre de prisonniers`.
    - Cela pourrait refléter des dynamiques sociales spécifiques à cet État, mais il est important de noter que cette relation ne peut pas être généralisée sans une analyse plus approfondie.
""")

st.markdown("### Animation globale pour tous les états")

st.markdown("""
    - Ici, nous allons juste observer l'évolution au fil des années de la relation entre l'indicateur démographique sélectionné
    et l'indicateur de crimes sélectionné sur l'ensemble des États américains.
""")

# Créer l'animation pour toutes les années et tous les états
fig6 = px.scatter(
    df_guns,
    x=indicateur_demo,
    y=indicateur_crime,
    size="population",
    color="state",
    animation_frame="year",
    animation_group="state",
    labels={indicateur_demo: indicateur_demo_label, 
            indicateur_crime: indicateur_crime_label, 
            "state": "État"
    },
    title=f"{indicateur_demo_label} vs {indicateur_crime_label} dans le temps",
    template="plotly_white"
)

# Définir l'infobulle pour chaque frame séparément
for frame in fig6.frames:
    year = int(frame.name)
    df_frame = df_guns[df_guns["year"] == year]
    for i, trace in enumerate(frame.data):
        # Associer le bon état à la bonne ligne
        state_name = trace.name
        df_state = df_frame[df_frame["state"] == state_name]
        trace.customdata = df_state[["state", "year", indicateur_demo, indicateur_crime, "population", "law"]].values
        trace.hovertemplate = (
            "<span style='font-family:monospace;'>"
            f"{pad('État')} : <b>%{{customdata[0]}}</b><br>"
            f"{pad('Année')} : <b>%{{customdata[1]}}</b><br>"
            f"{pad(indicateur_demo_label)} : <b>%{{customdata[2]:.2f}}</b><br>"
            f"{pad(indicateur_crime_label)} : <b>%{{customdata[3]:.2f}}</b><br>"
            f"{pad('Population')} : <b>%{{customdata[4]:,.2f}} millions</b><br>"
            f"{pad('Loi')} : <b>%{{customdata[5]}}</b><br>"
            "</span><extra></extra>"
        )

# Appliquer aussi aux traces initiales
df_init = df_guns[df_guns["year"] == df_guns["year"].min()]
for trace in fig6.data:
    state_name = trace.name
    df_state = df_init[df_init["state"] == state_name]
    trace.customdata = df_state[["state", "year", indicateur_demo, indicateur_crime, "population", "law"]].values
    trace.hovertemplate = (
        "<span style='font-family:monospace;'>"
        f"{pad('État')} : <b>%{{customdata[0]}}</b><br>"
        f"{pad('Année')} : <b>%{{customdata[1]}}</b><br>"
        f"{pad(indicateur_demo_label)} : <b>%{{customdata[2]:.2f}}</b><br>"
        f"{pad(indicateur_crime_label)} : <b>%{{customdata[3]:.2f}}</b><br>"
        f"{pad('Population')} : <b>%{{customdata[4]:,.2f}} millions</b><br>"
        f"{pad('Loi')} : <b>%{{customdata[5]}}</b><br>"
        "</span><extra></extra>"
    )


# Affichage dans Streamlit
st.plotly_chart(fig6, width=800, height=600)

# Commentaire sur le graphique
st.markdown(f"""
    - L'animation illustre l'évolution de la relation entre `{indicateur_demo_label}` et `{indicateur_crime_label}` pour tous les États américains de 1977 à 1999.
    - La taille des points représente la population de chaque État.
    - On observe que la relation entre les deux indicateurs varie au fil des années, avec des tendances différentes selon les États et surtout non lineaires.
    - Par ailleurs, c'est intéressant de noter que, dans le cas de `Pourcentage d'afro-américains` vs `Indicateur de Crimes Violents`, si on ne faisait aucune distinction selon les états, on aurait pu conclure 
    qu'il y a une tendance générale à la hausse du `Pourcentage d'afro-américains` avec l'augmentation de l'`Indicateur de Crimes Violents`.
    - Mais ce serait faussé parce qu'en réalité, cette perception globale masquerait des variations significatives entre les différents États.
    - Cela souligne l'importance de considérer les contextes locaux et les spécificités de chaque État lors de l'analyse de telles relations. 
    Cela suggère aussi que les dynamiques criminelles sont complexes et influencées par de multiples facteurs. 
""")


#=========================
# Pied de page
# =========================
st.markdown("---")

st.markdown("""
<div style="display: flex; justify-content: space-around; align-items: center; margin-top: 10px;">
    <div style="text-align: center;">
        <strong>Auteur</strong><br>
        Stave Icnel Dany OSIAS
    </div>
    <div style="text-align: center;">
        <strong>GitHub</strong><br>
        <a href="https://github.com/Dacossti" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/32/25/25231.png" style="display:block; margin:0 auto;">
        </a><br>
    </div>
    <div style="text-align: center;">
        <strong>LinkedIn</strong><br>
        <a href="https://www.linkedin.com/in/stave-icnel-dany-osias/" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/32/174/174857.png" style="display:block; margin:0 auto;">
        </a><br>
    </div>
</div>
""", unsafe_allow_html=True)
