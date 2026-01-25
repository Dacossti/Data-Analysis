![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat&logo=plotly&logoColor=white)
![Status](https://img.shields.io/badge/status-completed-success?style=flat)

---

# 🇺🇸 Analyse de la criminalité aux États-Unis (1977–1999)
**Dashboard interactif avec Streamlit et Plotly**

---

## 📌 Objectif du projet

Ce projet vise à explorer les relations entre :

- **Criminalité** (taux de crimes violents, meurtres, vols, nombre de prisonniers)
- **Démographie** (population, densité, composition raciale, revenu moyen)
- **Présence de lois sur les armes**  

Les données couvrent **1977 à 1999** pour les **51 États américains** et proviennent du jeu `Guns` de la bibliothèque **AER** en R.  

Le dashboard permet :

- La **comparaison annuelle** des États pour différents indicateurs
- L’**analyse de l’évolution temporelle** des indicateurs par État
- L’exploration de la **distribution des crimes** en fonction des lois sur les armes
- La **visualisation des relations** entre indicateurs démographiques et indicateurs de criminalité

---

## 🗂️ Contenu du repository

- `app.py` : script principal de l’application Streamlit  
- `requirements.txt` : dépendances nécessaires pour exécuter l’application  
- `data/` (optionnel) : fichiers de données supplémentaires, si utilisés  
- `README.md` : documentation du projet  

---

## 🧪 Méthodologie

1. **Chargement des données**  
   - Directement depuis le lien en ligne du dataset `Guns`.
   - Visualisation de l’aperçu des données.

2. **Visualisations interactives**  
   - Graphiques à barres et boxplots par État et par indicateur  
   - Scatterplots et animations pour les relations entre indicateurs démographiques et criminels  
   - Graphiques circulaires pour la distribution des lois sur les armes

3. **Personnalisation des infobulles**  
   - Affichage clair des informations : État, année, indicateur de crime, indicateur démographique, population, etc.

4. **Navigation rapide**  
   - Menu dans la sidebar avec boutons cliquables vers chaque section du dashboard

---

## 📊 Technologies et bibliothèques utilisées

- **Python 3.x** – langage principal  
- **Streamlit** – création du dashboard interactif  
- **Pandas** – manipulation des données  
- **Plotly** – visualisation interactive et animations  
- **NumPy / SciPy** – calculs et statistiques  

---

## 📈 Résultats et fonctionnalités

- Comparaison des États pour un indicateur et une année sélectionnés
- Animation de l’évolution des indicateurs dans le temps
- Analyse des relations entre indicateurs démographiques et indicateurs de criminalité
- Distribution des taux de crimes violents selon la présence de lois sur les armes
- Dashboard entièrement interactif et responsive

---

## 👨‍💻 Auteur

<div style="display:flex; justify-content:space-between; align-items:center; width:600px;">
  <div style="text-align:center;">
    <img src="https://avatars.githubusercontent.com/u/Dacossti" width="60"/><br>
    **Stave Icnel Dany OSIAS**<br>
    [GitHub](https://github.com/Dacossti)<br>
    [LinkedIn](https://www.linkedin.com/in/stave-icnel-dany-osias)
  </div>
</div>

---

## 🚀 Déploiement

L’application peut être exécutée localement avec :

```bash
pip install -r requirements.txt
streamlit run app.py
```

Ou déployée sur **Streamlit Cloud** directement depuis ce repository.
