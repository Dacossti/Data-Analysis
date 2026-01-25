![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat&logo=plotly&logoColor=white)
![Status](https://img.shields.io/badge/status-completed-success?style=flat)

---

# 🇺🇸 Analyse de la criminalité aux États-Unis (1977–1999)
**Dashboard interactif avec Streamlit et Plotly**

[➡️ Accéder à l'application en ligne](https://us-criminality-1977-1999.streamlit.app/)

---

## 📌 Objectif du projet

Ce projet explore les relations entre :

- **Criminalité** (taux de crimes violents, meurtres, vols, nombre de prisonniers)  
- **Démographie** (population, densité, composition raciale, revenu moyen)  
- **Présence de lois sur les armes**  

Les données couvrent **1977 à 1999** pour les **51 États américains** et proviennent du jeu `Guns` de la bibliothèque **AER** en R.  

Le dashboard permet de :

- Comparer les États pour différents indicateurs par année  
- Analyser l’évolution temporelle des indicateurs par État  
- Explorer la distribution des crimes en fonction des lois sur les armes  
- Visualiser les relations entre indicateurs démographiques et criminels

---

## 🗂️ Contenu du repository

- `app.py` : script principal de l’application Streamlit  
- `requirements.txt` : dépendances nécessaires  
- `data/` (optionnel) : fichiers de données supplémentaires  
- `README.md` : documentation du projet  

---

## 🧪 Méthodologie

1. **Chargement des données** depuis le lien en ligne du dataset `Guns`  
2. **Visualisations interactives** : barres, boxplots, scatterplots, animations, graphiques circulaires  
3. **Infobulles personnalisées** : État, année, indicateur de crime, indicateur démographique, population  
4. **Navigation rapide** : menu dans la sidebar pour accéder aux sections du dashboard  

---

## 📊 Technologies utilisées

- **Python 3.x**  
- **Streamlit** – dashboard interactif  
- **Pandas** – manipulation des données  
- **Plotly** – visualisation et animations  
- **NumPy / SciPy** – statistiques et calculs  

---

## 📈 Résultats et fonctionnalités

- Comparaison des États pour un indicateur et une année  
- Animation de l’évolution temporelle des indicateurs  
- Analyse des relations entre indicateurs démographiques et criminels  
- Distribution des taux de crimes violents selon la présence de lois sur les armes  
- Dashboard interactif et responsive  

---

## 👨‍💻 Auteur

<div style="display:flex; justify-content:space-around; align-items:center; width:600px;">
  <div style="text-align:center;">
    <img src="https://avatars.githubusercontent.com/u/104396909?v=4&size=64" width="60"/><br>
    **Stave Icnel Dany OSIAS**<br>
    [GitHub](https://github.com/Dacossti)<br>
    [LinkedIn](https://www.linkedin.com/in/stave-icnel-dany-osias)
  </div>
</div>

---

## 🚀 Déploiement

### Localement
```bash
pip install -r requirements.txt
streamlit run app.py
```

### En ligne

- Déployé sur Streamlit Cloud : https://us-criminality-1977-1999.streamlit.app/
