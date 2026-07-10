import streamlit as st
import pickle
import pandas as pd


# =====================================================
# Chargement des modèles
# =====================================================

with open("linear_regression_model.pkl", "rb") as f:
    regression_model = pickle.load(f)

with open("knn_classification_model.pkl", "rb") as f:
    classification_model = pickle.load(f)

with open("scaler_classification.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("regression_features.pkl", "rb") as f:
    regression_features = pickle.load(f)



# =====================================================
# Présentation
# =====================================================

st.title("💎 DiamondScope")

st.write(
    """
    DiamondScope est un prototype d'analyse joaillière.

    Cet outil permet :
    
    - d'estimer le prix d'un diamant ;
    - de prédire si un diamant appartient à une coupe premium ;
    - d'analyser les performances des modèles.
    """
)



# =====================================================
# Navigation
# =====================================================

page = st.sidebar.selectbox(
    "Navigation",
    [
        "💰 Prédiction du prix",
        "💎 Coupe premium",
        "📊 Analyse"
    ]
)



# =====================================================
# PAGE 1 : REGRESSION - PRIX
# =====================================================

if page == "💰 Prédiction du prix":

    st.header("💰 Prédiction du prix d'un diamant")


    carat = st.number_input(
        "Poids du diamant (carat)",
        min_value=0.1,
        max_value=5.0,
        value=1.0
    )


    depth = st.number_input(
        "Profondeur (%)",
        value=61.0
    )


    table = st.number_input(
        "Table (%)",
        value=57.0
    )


    color = st.selectbox(
        "Couleur",
        ["D", "E", "F", "G", "H", "I", "J"]
    )


    clarity = st.selectbox(
        "Clarté",
        [
            "I1",
            "SI1",
            "SI2",
            "VS1",
            "VS2",
            "VVS1",
            "VVS2"
        ]
    )


    if st.button("Prédire le prix"):


        diamant = pd.DataFrame(
            {
                "carat": [carat],
                "depth": [depth],
                "table": [table],
                "color": [color],
                "clarity": [clarity]
            }
        )


        diamant = pd.get_dummies(
            diamant,
            columns=["color", "clarity"],
            dtype=int
        )


        diamant = diamant.reindex(
            columns=regression_features,
            fill_value=0
        )


        prix = regression_model.predict(diamant)[0]


        st.success(
            f"💰 Prix estimé : {prix:,.2f} $"
        )



# =====================================================
# PAGE 2 : CLASSIFICATION COUPE PREMIUM
# =====================================================

elif page == "💎 Coupe premium":

    st.header("💎 Prédiction d'une coupe premium")


    carat = st.number_input(
        "Poids du diamant (carat)",
        min_value=0.1,
        value=1.0
    )


    depth = st.number_input(
        "Profondeur (%)",
        value=61.0
    )


    table = st.number_input(
        "Table (%)",
        value=57.0
    )


    x = st.number_input(
        "Longueur x",
        value=5.0
    )


    y = st.number_input(
        "Largeur y",
        value=5.0
    )


    z = st.number_input(
        "Hauteur z",
        value=3.0
    )


    color = st.selectbox(
        "Couleur",
        ["D", "E", "F", "G", "H", "I", "J"]
    )


    clarity = st.selectbox(
        "Clarté",
        [
            "I1",
            "SI1",
            "SI2",
            "VS1",
            "VS2",
            "VVS1",
            "VVS2"
        ]
    )


    if st.button("Prédire la coupe premium"):


        diamant = pd.DataFrame(
            {
                "carat": [carat],
                "depth": [depth],
                "table": [table],
                "x": [x],
                "y": [y],
                "z": [z],
                "color": [color],
                "clarity": [clarity]
            }
        )


        diamant = pd.get_dummies(
            diamant,
            columns=["color", "clarity"],
            dtype=int
        )


        # remettre exactement les colonnes du modèle

        diamant = diamant.reindex(
            columns=scaler.feature_names_in_,
            fill_value=0
        )


        diamant_scaled = scaler.transform(
            diamant
        )


        prediction = classification_model.predict(
            diamant_scaled
        )[0]


        if prediction == 1:

            st.success(
                "💎 Ce diamant appartient à une coupe PREMIUM"
            )

        else:

            st.warning(
                "Ce diamant n'appartient pas à une coupe premium"
            )



# =====================================================
# PAGE 3 : ANALYSE (à faire ensuite)
# =====================================================

else:

    st.header("📊 Analyse du prototype")


    st.subheader(
        "Analyse destinée à Camille Arnaud"
    )


    st.write(
        """
        Le modèle de régression permet d'estimer le prix d'un diamant
        à partir de ses caractéristiques.

        Les variables ayant le plus d'influence sur le prix sont :
        - carat : influence positive importante sur la valeur du diamant ;
        - clarity_I1 : une faible qualité de clarté réduit fortement le prix ;
        - clarity_SI2 : une clarté inférieure diminue également la valeur estimée.

        Le modèle de classification KNN obtient une accuracy de 78%.
        Il est particulièrement efficace pour détecter les diamants Premium
        avec un rappel de 90%.

        Cependant, le modèle identifie moins bien les diamants Non Premium
        avec un rappel de 55%. La matrice de confusion montre un nombre
        important de faux positifs.

        Une limite du prototype est que seuls des modèles simples ont été
        testés. Avec plus de temps, il serait intéressant d'utiliser des
        modèles plus avancés, d'optimiser les hyperparamètres et d'ajouter
        davantage de données métier.
        """
    )


    # -----------------------------
    # Importance des variables prix
    # -----------------------------

    st.subheader(
        "Variables influençant le prix"
    )


    importance = pd.DataFrame(
        {
            "Feature": [
                "carat",
                "clarity_I1",
                "clarity_SI2"
            ],
            "Importance": [
                8902.23,
                5598.68,
                2829.54
            ]
        }
    )


    st.bar_chart(
        importance.set_index("Feature")
    )



    # -----------------------------
    # Matrice de confusion
    # -----------------------------

    st.subheader(
        "Matrice de confusion - KNN"
    )


    confusion = pd.DataFrame(
        [
            [2055, 1665],
            [711, 6357]
        ],
        columns=[
            "Prédit Non Premium",
            "Prédit Premium"
        ],
        index=[
            "Réel Non Premium",
            "Réel Premium"
        ]
    )


    st.dataframe(confusion)
    



    