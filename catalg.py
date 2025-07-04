import streamlit as st
import os

st.set_page_config(page_title="🧩 Sélecteur de Poste", layout="wide")
st.title("🧩 Configurateur de Poste de Travail")

# Étape 1 : Choix de la famille
famille = st.selectbox("Choisissez une famille de produit :", [
    "Postes de travail", "Chariot", "Étagère"])

# Définir les chemins des images
image_path_postes = {
    "Poste de travail simple": "images/simple.png",
    "Poste de travail avec stockeur intégré (Assis)": "images/stockeur.png",
    "Poste de travail avec tiroir": "images/tiroir.png",
    "Poste de travail (Assis debout)": "images/assis_debout.png"
}

image_path_accessoires = {
    "Tiroir (T)": "images/accessoires/tiroir.png",
    "Prise (P)": "images/accessoires/prise.png",
    "Lampe Loupe (LL)": "images/accessoires/lampe_loupe.png",
    "Support bouteille (SB)": "images/accessoires/bouteille.png",
    "Support écran (SE)": "images/accessoires/ecran.png",
    "Repose pied (RP)": "images/accessoires/repose_pied.png",
    "Éclairage LED (E)": "images/accessoires/led.png",
    "Support air chaud (AC)": "images/accessoires/air_chaud.png"
}

if famille == "Postes de travail":
    st.subheader("Sélectionnez le type de poste de travail")

    type_poste_selectionne = None
    cols = st.columns(4)
    for i, (label, img) in enumerate(image_path_postes.items()):
        with cols[i % 4]:
            st.image(img, caption=label, use_container_width=True)
            if st.button(f"Choisir : {label}", key=f"poste_{i}"):
                st.session_state["type_poste"] = label

    if "type_poste" in st.session_state:
        type_poste = st.session_state["type_poste"]
        st.success(f"✅ Type de poste sélectionné : {type_poste}")

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

        # Étape Accessoires
        st.subheader("Ajoutez vos accessoires")
        accessoires_choisis = []

        acc_cols = st.columns(4)
        for i, (acc_label, acc_img) in enumerate(image_path_accessoires.items()):
            with acc_cols[i % 4]:
                st.image(acc_img, caption=acc_label, use_container_width=True)
                if st.checkbox(acc_label, key=f"acc_{i}"):
                    accessoires_choisis.append(acc_label)

        accessoires_ref = {
            "Tiroir (T)": "T",
            "Prise (P)": "P",
            "Lampe Loupe (LL)": "LL",
            "Support bouteille (SB)": "SB",
            "Support écran (SE)": "SE",
            "Repose pied (RP)": "RP",
            "Éclairage LED (E)": "E",
            "Support air chaud (AC)": "AC"
        }

        if st.button("🔍 Générer la référence"):
            accessoires_code = "-" + "-".join([accessoires_ref[a] for a in accessoires_choisis]) if accessoires_choisis else ""
            reference_finale = ref_principale + accessoires_code
            st.success(f"📦 Référence générée : {reference_finale}")
    else:
        st.warning("Veuillez sélectionner un type de poste pour continuer.")
