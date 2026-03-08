# 📊 Business Intelligence Portfolio

![Power BI](https://img.shields.io/badge/PowerBI-Dashboard-F2C811?logo=powerbi&logoColor=black)
![Data Analysis](https://img.shields.io/badge/Data-Analysis-blue)
![Open Data](https://img.shields.io/badge/Open%20Data-data.gouv.fr-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)
![Status](https://img.shields.io/badge/Project-Active-success)

Portfolio de projets **Business Intelligence** réalisés avec **Power BI** et des **données ouvertes**.  
Ces projets explorent des problématiques réelles à travers **data visualisation, data modelling et analyse décisionnelle**.

---

# 📂 Projets

| Projet | Description | Technologies |
|------|------|------|
| 🌍 Impact environnemental de l’IA générative | Analyse des infrastructures, de la consommation énergétique et des modèles d’IA | Power BI, Open Data |
| 🎓 Performance académique des étudiants | Analyse des notes universitaires, réussite et évolution académique | Power BI, DAX |


🔗 **Dashboards Power BI** 

- [AI Environmental Impact Dashboard](https://app.powerbi.com/groups/me/reports/53b5e1df-12d7-49df-8ac9-04a4d9b96c4f/9b5599aa242022140006?experience=power-bi)
- [Student Performance Dashboard](https://app.powerbi.com/groups/me/reports/d99ec42d-93de-44a8-96fa-d2359a8395d9/46ccbc08aad361085ee3?experience=power-bi)

---

# 🌍 Projet 1 — Impact environnemental de l’IA générative

![Power BI](https://img.shields.io/badge/PowerBI-Visualization-yellow)
![Open Data University](https://img.shields.io/badge/Open%20Data-data.gouv.fr-blue)
![ADEME](https://img.shields.io/badge/ADEME-Project-green)

## 📖 Contexte

Projet réalisé dans le cadre du défi :

➡️ **L’impact environnemental de l’IA générative**  
proposé par l’ADEME sur la plateforme :

https://defis.data.gouv.fr

L'objectif est d’analyser la **matérialité de l’IA** et ses impacts environnementaux :

- infrastructures physiques
- consommation énergétique
- croissance des centres de données
- impacts territoriaux

L’IA générative repose sur :

- des **terminaux**
- des **réseaux**
- des **data centers**

Ces infrastructures ont un impact environnemental :

- consommation énergétique
- consommation d’eau
- extraction de minerais
- occupation du sol

---

# 🎯 Objectif du projet

Répondre à la question :

> Comment mobiliser les données ouvertes pour éclairer le débat public sur l’impact environnemental de l’IA générative ?

Le projet vise à :

- visualiser la **répartition des datacenters**
- analyser la **consommation énergétique**
- comparer la **consommation des modèles d’IA**
- sensibiliser aux impacts environnementaux du numérique

---

# 📊 Dashboard

![Dashboard Impact IA](images/impactIA.gif)

Le dashboard met en évidence :

- la concentration des datacenters
- la distribution territoriale
- les déséquilibres régionaux

---

# 📈 Indicateurs analysés

## Infrastructure numérique

- nombre total de datacenters
- datacenters par région

Ces indicateurs montrent la **matérialité et la concentration des infrastructures numériques**.

---

## Consommation énergétique territoriale

Données analysées :

- consommation totale d’énergie
- évolution entre **2012 et 2023**
- consommation moyenne

Objectif :

Identifier les tendances énergétiques dans le contexte du développement du numérique.

---

## Consommation énergétique de l’IA

Source : **AI Energy Score**

Indicateurs :

- consommation par fournisseur
- consommation par modèle
- énergie nécessaire pour **1000 requêtes**
- énergie estimée pour **1 milliard de requêtes**

---

# 📊 Visualisations utilisées

| Visualisation | Power BI | Objectif |
|---|---|---|
| Carte des datacenters | Azure Map | Localisation des infrastructures |
| Bar chart | Bar chart | Comparaison par région |
| Série temporelle | Line chart | Évolution énergétique |
| KPI | Card | Indicateurs clés |
| Pie chart | Camembert | Répartition régionale |
| Button slicer | Filtrage interactif | Type de requête |

---

# 📌 Limites des données

Certaines contraintes existent :

- données de datacenters **non temporelles**
- données énergétiques **globales**
- absence de volume réel de requêtes IA

Cela empêche :

- d’établir une corrélation directe
- de mesurer précisément l’impact réel de l’IA

Le projet repose donc sur **des ordres de grandeur et des estimations comparatives**.

---

# 🔎 Insights principaux

- forte concentration des datacenters en **Île-de-France**
- croissance rapide de la consommation énergétique
- forte variabilité de consommation entre modèles d’IA
- manque de transparence des entreprises technologiques

---

# 🎓 Projet 2 — Analyse des notes des étudiants

![Power BI](https://img.shields.io/badge/PowerBI-Dashboard-yellow)
![DAX](https://img.shields.io/badge/DAX-Analytics-blue)

## 📖 Objectif

Créer un **dashboard décisionnel universitaire** pour analyser :

- la performance académique
- les taux de réussite
- les absences
- l’évolution des notes

---

# 📊 Dashboard

![Student Dashboard](images/students.gif)

---

# 📈 Indicateurs clés

- 👨‍🎓 Nombre d’étudiants
- 📝 Nombre d’évaluations
- 📊 Note moyenne
- ✅ Taux de réussite
- ❌ Taux d’absence

---

# 📊 Analyses réalisées

## Distribution des notes

Histogramme des notes permettant de visualiser :

- la répartition des performances
- la concentration des notes

---

## Performance par cours

Tableau comparatif :

- moyenne par cours
- taux de réussite
- taux d’absence

---

## Analyse temporelle

Deux analyses temporelles :

### évolution par mois
permet d’identifier :

- variations saisonnières
- périodes d’examens

### évolution par année
compare la performance académique entre promotions.

---

# 📊 Visualisations utilisées

| Visualisation | Objectif |
|---|---|
| Histogramme | distribution des notes |
| Line chart | évolution des notes |
| Bar chart | comparaison annuelle |
| Matrix | analyse par cours |
| KPI cards | indicateurs clés |
| Gauge | taux de réussite |

---

# 🧠 Modélisation des données

Structure **Star Schema**
