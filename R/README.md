
![R](https://img.shields.io/badge/R-276DC3?style=flat&logo=r&logoColor=white)
![RStudio](https://img.shields.io/badge/RStudio-75AADB?style=flat&logo=rstudio&logoColor=white)
![Status](https://img.shields.io/badge/status-completed-success?style=flat)

![PCA](https://img.shields.io/badge/Method-PCA-orange?style=flat)
![CAH](https://img.shields.io/badge/Method-Hierarchical%20Clustering-orange?style=flat)
![KMeans](https://img.shields.io/badge/Method-K--Means-orange?style=flat)
![Silhouette](https://img.shields.io/badge/Validation-Silhouette-informational?style=flat)
![CH](https://img.shields.io/badge/Validation-Calinski--Harabasz-informational?style=flat)

![FactoMineR](https://img.shields.io/badge/FactoMineR-Statistics-blueviolet?style=flat)
![factoextra](https://img.shields.io/badge/factoextra-Visualization-blueviolet?style=flat)
![ggplot2](https://img.shields.io/badge/ggplot2-Visualization-blueviolet?style=flat)
![cluster](https://img.shields.io/badge/cluster-Clustering-blueviolet?style=flat)
![dplyr](https://img.shields.io/badge/dplyr-Data%20Wrangling-blueviolet?style=flat)
![ggrepel](https://img.shields.io/badge/ggrepel-Labels-blueviolet?style=flat)

---


# 📊 Socio-Economic Analysis of French Departments
**PCA & Clustering (Hierarchical + K-means)**

## Main project Overview

[See report (pp. 121–137)](report/report.pdf)

This project explores the **socio-economic structure of French departments** using **multivariate data analysis techniques**.

The workflow combines:
- Exploratory Data Analysis (EDA)
- Correlation analysis
- **Principal Component Analysis (PCA)**
- **Hierarchical Clustering (CAH)**
- **K-means clustering**
- Model validation using **Silhouette index** and **Calinski–Harabasz criterion**

The objective is to **identify homogeneous groups of departments** and provide an interpretable socio-economic typology.

---

## 📌 Main Questions

- Which socio-economic variables are strongly correlated?
- How many principal components should be retained?
- How many clusters best describe the data?
- How can French departments be meaningfully grouped?

---

## 🗂️ Data Description

- **Observations**: French departments  
- **Variables** (examples):
  - Urbanization rate (URBR)
  - Employment rate (EMPL)
  - Unemployment rate (CHOM)
  - Share of executives (CADR)
  - Share of agricultural workers (AGRI)
  - Fiscal pressure (FISC)
  - Crime rate (CRIM)
  - Demographic indicators (AGE, JEUN, TXCR)

> All quantitative variables were standardized prior to PCA.

---

## 🧪 Methodology

### 1️⃣ Data Preparation
- Cleaning and standardization
- Handling missing values
- Variable selection

### 2️⃣ Correlation Analysis
- Identification of strongly correlated variables
- Pairwise scatter plots

### 3️⃣ Principal Component Analysis (PCA)
- Eigenvalue analysis (Kaiser criterion)
- Scree plot (elbow method)
- Interpretation of axes, variables, and individuals

### 4️⃣ Clustering
- **Hierarchical clustering** on PCA coordinates
- **K-means consolidation**
- Comparison of:
  - Silhouette score
  - Calinski–Harabasz index

### 5️⃣ Interpretation
- Socio-economic profiling of clusters
- Geographic and structural interpretation

---

## 📈 Key Results

- **4 clusters** provide the best compromise between:
  - Statistical quality
  - Interpretability
- Clear differentiation between:
  - Highly urbanized & wealthy departments
  - Southern/touristic departments
  - Rural & aging territories
  - Industrial/young-population areas

---

## 📊 Visual Outputs

- PCA individual and variable maps
- Biplots
- Convex hull cluster visualizations
- Silhouette and CH index plots

All figures are available in `reports/figures/`.


---

## 🧠 Additional Practice & Post-Course Work

Beyond the main project, this repository also contains **personal work completed after the course**, aimed at reinforcing and extending the concepts seen in class.

These exercises were carried out independently and focus on:
- Exploring datasets beyond guided examples
- Applying statistical methods from scratch
- Interpreting results in a rigorous and structured way
- Improving data visualization and reporting (R Markdown)

The topics addressed include:
- Exploratory data analysis
- Linear regression and diagnostic tools
- ANOVA
- PCA, CA, MCA, FAMD
- Hierarchical clustering and K-means
- Interpretation of variables, individuals, and clusters

This work reflects a **self-driven effort to consolidate theoretical knowledge through practical implementation**.

---


