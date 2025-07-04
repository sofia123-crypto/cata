import streamlit as st

st.set_page_config(page_title="🧩 Sélecteur de Poste", layout="centered")
st.title("🧩 Configurateur de Poste de Travail")

# Étape 1 : Choix de la famille
famille = st.selectbox("Choisissez une famille de produit :", [
    "Postes de travail", "Chariot", "Étagère"])

# Étape 2 : Si "Postes de travail" est choisi
if famille == "Postes de travail":
    type_poste = st.selectbox("Choisissez un type de poste de travail :", [
        "Poste de travail simple",
        "Poste de travail avec stockeur intégré (Assis)",
        "Poste de travail avec tiroir",
        "Poste de travail (Assis debout)"
    ])

    longueurs = {
        "1200": "A-1",
        "1500": "A-2",
        "1800": "A-3",
        "2500": "A-4",
        "3000": "A-5"
    }

    if type_poste == "Poste de travail avec stockeur intégré (Assis)":
        suffixe = "-1"
    elif type_poste == "Poste de travail avec tiroir":
        suffixe = "-2"
    elif type_poste == "Poste de travail (Assis debout)":
        suffixe = "-3"
        longueurs = {
            "1200": "A-1-3",
            "1500": "A-2-3"
        }
    else:
        suffixe = ""

    longueur = st.selectbox("Choisissez une longueur :", list(longueurs.keys()))
    ref_principale = longueurs[longueur]

    # Étape 3 : Choix des accessoires
    st.subheader("Accessoires")
    accessoires = {
        "Tiroir (T)": "T",
        "Prise (P)": "P",
        "Lampe Loupe (LL)": "LL",
        "Support bouteille (SB)": "SB",
        "Support écran (SE)": "SE",
        "Repose pied (RP)": "RP",
        "Éclairage LED (E)": "E",
        "Support air chaud (AC)": "AC"
    }

    accessoires_choisis = st.multiselect("Choisissez les accessoires :", list(accessoires.keys()))

    # Affichage de la référence finale
    if st.button("🔍 Générer la référence"):
        accessoires_ref = "-" + "-".join([accessoires[a] for a in accessoires_choisis]) if accessoires_choisis else ""
        reference_finale = ref_principale + accessoires_ref
        st.success(f"📦 Référence générée : {reference_finale}")
