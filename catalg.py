import streamlit as st
import os

st.set_page_config(page_title="🧩 Sélecteur de Poste", layout="wide")
# Affichage du titre avec le logo aligné à droite (logo redimensionné)
col1, col2 = st.columns([5, 1])  # Plus d’espace pour le titre que pour le logo
with col1:
    st.title("🧩 Configurateur de Poste de Travail")
with col2:
    st.image("images/safran_logo.png", width=150)  # ← ajuste ici la taille du logo


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

image_path_chariots = {
    "Chariot de bacs (1200)": "images/chariots/bacs.png",
    "Chariot de transport des produits": "images/chariots/transport.png",
    "Chariot pour produits de grande taille (1300)": "images/chariots/grand.png",
    "Support visseuse (1800)": "images/chariots/visseuse.png",
    "Chariot transport 4 étages": "images/chariots/etages.png",
    "Chariot 4 étages avec base MDF": "images/chariots/etages_mdf.png",
    "Chariot pour cartons (1050)": "images/chariots/carton.png"
}

image_path_etageres = {
    "Étagère pour petits bacs": "images/etagere/petits-bacs.png",
    "Étagère entrée-sortie (1100)": "images/etagere/entree_sortie.png",
    "Stockeur des bacs (700)": "images/etagere/stockeur_bacs.png",
    "Étagère 4 étages MDF": "images/etagere/etages_mdf.png",
    "Étagère pour grands bacs (2000)": "images/etagere/grand_bacs.png",
    "Étagère de stockage à 3 étages (1600)": "images/etagere/stockage_3.png"
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

# ... le reste du code ne change pas ...



# ==== POSTES DE TRAVAIL ====
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

        # Par défaut
        longueurs = {
            "1200": "P-1200",
            "1500": "P-1500",
            "1800": "P-1800",
            "2500": "P-2500",
            "3000": "P-3000"
        }
        suffixe = ""

        if type_poste == "Poste de travail avec stockeur intégré (Assis)":
            suffixe = "-st"
        elif type_poste=="Poste de travail simple":
            suffixe= "-sp"
        elif type_poste == "Poste de travail avec tiroir":
            suffixe = "-tr"
        elif type_poste == "Poste de travail (Assis debout)":
            suffixe = "-ad"
            longueurs = {
                "1200": "P-1200",
                "1500": "P-1500"
            }

        longueur = st.selectbox("Choisissez une longueur :", list(longueurs.keys()))
        ref_base = longueurs[longueur] + suffixe

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
            reference_finale = ref_base + accessoires_code
            st.success(f"📦 Référence générée : {reference_finale}")
    else:
        st.warning("Veuillez sélectionner un type de poste pour continuer.")

# ==== CHARIOTS ====
elif famille == "Chariot":
    st.subheader("Sélectionnez le type de chariot")

    chariot_selectionne = None
    chariot_options = list(image_path_chariots.keys())
    cols = st.columns(3)
    for i, label in enumerate(chariot_options):
        with cols[i % 3]:
            st.image(image_path_chariots[label], caption=label, width=200)  # ← taille réduite ici
            if st.button(f"Choisir : {label}", key=f"chariot_{i}"):
                st.session_state["chariot"] = label

    if "chariot" in st.session_state:
        choix_chariot = st.session_state["chariot"]
        st.success(f"✅ Chariot sélectionné : {choix_chariot}")

        types_chariots = {
            "Chariot de bacs (1200)": "C-b-1200",
            "Chariot de transport des produits": {
                "1100": "C-tr-1100",
                "500": "C-tr-500"
            },
            "Chariot pour produits de grande taille (1300)": "C-pd-1300",
            "Support visseuse (1800)": "SP-1800",
            "Chariot transport 4 étages": {
                "600": "C-tr4-600",
                "1000": "C-tr4-1000"
            },
            "Chariot 4 étages avec base MDF": {
                "600": "C-trMDF-600",
                "1000": "C-trMDF-1000"
            },
            "Chariot pour cartons (1050)": "C-crt-1050"
        }

        if isinstance(types_chariots[choix_chariot], dict):
            largeur = st.selectbox("Choisissez la largeur :", list(types_chariots[choix_chariot].keys()))
            ref_chariot = types_chariots[choix_chariot][largeur]
        else:
            ref_chariot = types_chariots[choix_chariot]

        if st.button("🔍 Générer la référence"):
            st.success(f"📦 Référence générée : {ref_chariot}")


# ==== ÉTAGÈRES ====
elif famille == "Étagère":
    st.subheader("Sélectionnez le type d'étagère")

    types_etageres = {
        "Étagère pour petits bacs": {
            "700": "E-pb-700",
            "1500": "E-pb-1500"
        },
        "Étagère entrée-sortie (1100)": "E-es-1100",
        "Stockeur des bacs (700)": "SB-700",
        "Étagère 4 étages MDF": {
            "600": "E-MDF-600",
            "1000": "E-MDF-1000"
        },
        "Étagère pour grands bacs (2000)": "E-gb-2000",
        "Étagère de stockage à 3 étages (1600)": "E-s3-1600"
    }

    etagere_selectionne = None
    etagere_options = list(image_path_etageres.keys())
    cols = st.columns(2)
    for i, label in enumerate(etagere_options):
        with cols[i % 2]:
            image_path = image_path_etageres[label]
            if os.path.exists(image_path):
                st.image(image_path, caption=label, width=200)
            else:
                st.warning(f"⚠️ Image manquante : {image_path}")
            if st.button(f"Choisir : {label}", key=f"etagere_{i}"):
                st.session_state["etagere"] = label

    if "etagere" in st.session_state:
        choix_etagere = st.session_state["etagere"]
        st.success(f"✅ Étagère sélectionnée : {choix_etagere}")

        if isinstance(types_etageres[choix_etagere], dict):
            largeur = st.selectbox("Choisissez la largeur :", list(types_etageres[choix_etagere].keys()))
            ref_etagere = types_etageres[choix_etagere][largeur]
        else:
            ref_etagere = types_etageres[choix_etagere]

        if st.button("🔍 Générer la référence"):
            st.success(f"📦 Référence générée : {ref_etagere}")

