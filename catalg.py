import streamlit as st
import os

st.set_page_config(page_title="🧩 Sélecteur de Poste", layout="wide")

# === En-tête avec logo ===
col1, col2 = st.columns([5, 1])
with col1:
    st.title("🧩 Configurateur de Poste de Travail")
with col2:
    st.image("images/safran_logo.png", width=120)

# === Définition des images ===
image_path_familles = {
    "Postes de travail": "images/familles/poste.png",
    "Chariot": "images/familles/chariot.png",
    "Étagère": "images/familles/etagere.png"
}

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

# === Étape 1 : Sélection de la famille ===
st.subheader("Sélectionnez une famille de produits")
cols = st.columns(3)
for i, (label, img_path) in enumerate(image_path_familles.items()):
    with cols[i]:
        st.image(img_path, caption=label, use_container_width=True)
        if st.button(f" {label}", key=f"famille_{i}"):
            st.session_state["famille"] = label

if "famille" not in st.session_state:
    st.stop()

famille = st.session_state["famille"]
st.markdown(f"### ✅ Famille sélectionnée : **{famille}**")

# === POSTES DE TRAVAIL ===
if famille == "Postes de travail":
    st.subheader("Sélectionnez le type de poste de travail")

    cols = st.columns(4)
    for i, (label, img) in enumerate(image_path_postes.items()):
        with cols[i % 4]:
            st.image(img, caption=label, use_container_width=True)
            if st.button(f"{label}", key=f"poste_{i}"):
                st.session_state["type_poste"] = label

    if "type_poste" in st.session_state:
        type_poste = st.session_state["type_poste"]
        st.success(f"✅ Type de poste sélectionné : {type_poste}")

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
        elif type_poste == "Poste de travail simple":
            suffixe = "-sp"
        elif type_poste == "Poste de travail avec tiroir":
            suffixe = "-tr"
        elif type_poste == "Poste de travail (Assis debout)":
            suffixe = "-ad"
            longueurs = {
                "1200": "P-1200",
                "1500": "P-1500"
            }

        st.subheader("Choisissez une longueur")
        selected_longueur = None
        length_cols = st.columns(len(longueurs))
        for i, longueur_val in enumerate(longueurs.keys()):
            with length_cols[i]:
                if st.button(f"{longueur_val}", key=f"btn_long_{i}"):
                    st.session_state["longueur"] = longueur_val
                st.markdown(f"**{longueur_val}**")

        if "longueur" in st.session_state:
            longueur = st.session_state["longueur"]
            ref_base = longueurs[longueur] + suffixe
        else:
            st.warning("Sélectionnez une longueur pour continuer.")
            st.stop()

        st.subheader("Ajoutez vos accessoires")
        accessoires_choisis = []
        acc_items = list(image_path_accessoires.items())
        acc_rows = (len(acc_items) + 3) // 4
        for row in range(acc_rows):
            cols = st.columns(4)
            for col in range(4):
                idx = row * 4 + col
                if idx < len(acc_items):
                    acc_label, acc_img = acc_items[idx]
                    with cols[col]:
                        st.image(acc_img, caption=acc_label, width=100)
                        if st.checkbox(acc_label, key=f"acc_{idx}"):
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

# === CHARIOTS ===
elif famille == "Chariot":
    st.subheader("Sélectionnez le type de chariot")

    cols = st.columns(3)
    for i, (label, img) in enumerate(image_path_chariots.items()):
        with cols[i % 3]:
            st.image(img, caption=label, width=200)
            if st.button(f"{label}", key=f"chariot_{i}"):
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
            "Chariot pour produits de grande taille (1300)": "C-pdg-1300",
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

# === ÉTAGÈRES ===
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

    cols = st.columns(2)
    for i, (label, img) in enumerate(image_path_etageres.items()):
        with cols[i % 2]:
            if os.path.exists(img):
                st.image(img, caption=label, width=200)
            else:
                st.warning(f"⚠️ Image manquante : {img}")
            if st.button(f"{label}", key=f"etagere_{i}"):
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
