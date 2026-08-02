Test connexion VS Code GitHub
# 💎 DiamondScope

### 🔍 Application d'analyse et de prédiction de diamants basée sur le Machine Learning

DiamondScope est une application interactive développée avec **Streamlit** permettant d'estimer la valeur d'un diamant et d'analyser ses caractéristiques grâce à des modèles de Machine Learning.

<p align="center">
  <a href="https://diamondscope-n5ifux47qsjbudaj7fzufx.streamlit.app/">
    <img src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg" alt="Open in Streamlit">
  </a>
</p>

<p align="center">
  🚀 <b>Tester l'application en ligne</b> : 
  <a href="https://diamondscope-n5ifux47qsjbudaj7fzufx.streamlit.app/">
    DiamondScope Live Demo
  </a>
</p>

## 📌 Présentation du projet

DiamondScope est un prototype d'application d'analyse joaillière développé avec **Streamlit**.

L'objectif est d'aider à l'évaluation d'un diamant grâce à des modèles de Machine Learning capables de :

- 💰 estimer son prix ;
- 💎 prédire si un diamant appartient à une coupe premium ;
- 📊 analyser les performances des modèles utilisés.

---

## 👉 Accéder à DiamondScope : [Ouvrir l'application Streamlit](http://localhost:8501/)
---
## 📸 Aperçu de l'application

![Capture DiamondScope](screenshot_prediction.png)
---

## 🚀 Fonctionnalités

### 💰 Prédiction du prix

L'utilisateur renseigne les caractéristiques du diamant :

- poids (carat) ;
- profondeur ;
- table ;
- couleur ;
- clarté.

Le modèle de régression estime ensuite un prix en dollars.

---

### 💎 Classification Premium

L'application utilise un modèle de classification afin de prédire si un diamant correspond à une coupe premium.

Les variables utilisées :

- carat ;
- profondeur ;
- table ;
- dimensions (x, y, z) ;
- couleur ;
- clarté.

---

### 📊 Analyse des résultats

Une page dédiée présente :

- les variables influençant le prix ;
- les performances du modèle de classification ;
- la matrice de confusion.

---

## 🤖 Modèles Machine Learning

Deux modèles ont été utilisés :

### Régression linéaire

Objectif :
- prédire le prix du diamant.

### KNN (K-Nearest Neighbors)

Objectif :
- classifier les diamants selon leur potentiel premium.

Performance obtenue :

- Accuracy : **78 %**
- Rappel Premium : **90 %**

---

## 🛠️ Technologies utilisées

- Python
- Pandas
- Scikit-learn
- Streamlit
- Pickle
- UV pour la gestion des dépendances

---
## 📂 Données

Le modèle a été entraîné sur un jeu de données de diamants contenant des caractéristiques physiques :

- carat ;
- coupe ;
- couleur ;
- clarté ;
- profondeur ;
- dimensions du diamant ;
- prix.

Ces variables ont été utilisées pour entraîner les modèles de Machine Learning.
---

## ▶️ Installation et lancement

Installer les dépendances :

```bash
uv sync



