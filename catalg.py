import streamlit as st
import base64
import os

st.set_page_config(page_title="🔩 Sélecteur de Poste", layout="wide")

# Style des boutons
st.markdown("""
    <style>
    .stButton > button {
        border-radius: 8px;
        padding: 10px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Utilitaire image en base64 (pour encadrement)
def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# === Logo & Titre ===
col1, col2 = st.columns([5, 1])
with col1:
    st.title("🔩 Configurateur de Poste de Travail")
with col2:
    st.image("images/safran_logo.png", width=120)

# === Dictionnaires d'images ===
image_path_familles = {
    "Postes de travail": "images/familles/poste.png",
    "Chariot": "images/familles/chariot.png",
    "Étagère": "images/familles/etagere.png"
}

image_path_postes = {
    "Poste de travail simple": "images/simple.jpg",
    "Poste de travail avec stockeur intégré (Assis)": "images/stockeur.jpg",
    "Poste de travail avec tiroir": "images/tiroir.jpg",
    "Poste de travail (Assis debout)": "images/assis_debout.jpg"
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
    "Tiroir (T)": "images/accessoires/tiroir.jpg",
    "Prise (P)": "images/accessoires/prise.jpg",
    "Lampe Loupe (LL)": "images/accessoires/lampe_loupe.jpg",
    "Support bouteille (SB)": "images/accessoires/bouteille.jpg",
    "Support écran (SE)": "images/accessoires/ecran.jpg",
    "Repose pied (RP)": "images/accessoires/repose_pied.jpg",
    "Éclairage LED (E)": "images/accessoires/led.jpg",
    "Support air chaud (AC)": "images/accessoires/air_chaud.jpg"
}

# === Sélection famille ===
st.subheader("Sélectionnez une famille de produits")
familles = [
    ("Postes de travail", image_path_familles["Postes de travail"], "Choisir Postes de travail"),
    ("Chariot", image_path_familles["Chariot"], "Choisir Chariots"),
    ("Étagère", image_path_familles["Étagère"], "Choisir Étagères"),
]

cols = st.columns(3)
for i, (label, img_path, bouton_label) in enumerate(familles):
    with cols[i]:
        is_selected = st.session_state.get("famille") == label
        if is_selected:
            st.markdown(
                f"<div style='border: 3px solid #2980b9; border-radius: 10px; padding: 5px;'>"
                f"<img src='data:image/png;base64,{get_image_base64(img_path)}' style='width:100%; border-radius:5px;'/>"
                f"</div>",
                unsafe_allow_html=True
            )
        else:
            st.image(img_path, use_container_width=True)

        if st.button(bouton_label, key=f"famille_{i}"):
            st.session_state["famille"] = label

if "famille" not in st.session_state:
    st.stop()

famille = st.session_state["famille"]
st.markdown(f"### ✅ Famille sélectionnée : **{famille}**")

# === Sélection générique ===
def select_type(image_dict, state_key, cols_per_row=3):
    items = list(image_dict.items())
    rows = (len(items) + cols_per_row - 1) // cols_per_row
    for r in range(rows):
        cols = st.columns(cols_per_row)
        for i in range(cols_per_row):
            idx = r * cols_per_row + i
            if idx >= len(items):
                continue
            label, img = items[idx]
            with cols[i]:
                is_selected = st.session_state.get(state_key) == label
                if is_selected:
                    st.markdown(
                        f"<div style='border: 3px solid #2980b9; border-radius: 10px; padding: 5px;'>"
                        f"<img src='data:image/jpeg;base64,{get_image_base64(img)}' style='width:100%; border-radius:5px;'/>"
                        f"</div>",
                        unsafe_allow_html=True
                    )
                else:
                    st.image(img, use_container_width=True)

                if st.button(label, key=f"{state_key}_{idx}"):
                    st.session_state[state_key] = label

def select_largeur(largeurs, state_key):
    st.subheader("Choisissez une largeur")
    cols = st.columns(len(largeurs))
    for i, val in enumerate(largeurs):
        with cols[i]:
            if st.button(f"📏 {val} mm", key=f"btn_{state_key}_{i}"):
                st.session_state[state_key] = val
    return st.session_state.get(state_key)

def generate_ref_button(reference):
    if st.button("🔍 Générer la référence"):
        st.success(f"📦 Référence générée : {reference}")

# === POSTES ===
if famille == "Postes de travail":
    st.subheader("Sélectionnez le type de poste de travail")
    select_type(image_path_postes, "type_poste", 4)

    if "type_poste" in st.session_state:
        type_poste = st.session_state["type_poste"]
        st.success(f"✅ Type de poste sélectionné : {type_poste}")

        largeurs = {
            "1200": "P-1200",
            "1500": "P-1500",
            "1800": "P-1800",
            "2500": "P-2500",
            "3000": "P-3000"
        }
        suffixe = {
            "Poste de travail avec stockeur intégré (Assis)": "-st",
            "Poste de travail simple": "-sp",
            "Poste de travail avec tiroir": "-tr",
            "Poste de travail (Assis debout)": "-ad"
        }.get(type_poste, "")

        if type_poste == "Poste de travail (Assis debout)":
            largeurs = {"1200": "P-1200", "1500": "P-1500"}

        selected = select_largeur(list(largeurs.keys()), "largeur")
        if selected:
            ref_base = largeurs[selected] + suffixe
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
                            st.image(acc_img, width=80)
                            if st.checkbox(acc_label, key=f"acc_{idx}"):
                                accessoires_choisis.append(acc_label)

            accessoires_ref = {
                "Tiroir (T)": "T", "Prise (P)": "P", "Lampe Loupe (LL)": "LL",
                "Support bouteille (SB)": "SB", "Support écran (SE)": "SE",
                "Repose pied (RP)": "RP", "Éclairage LED (E)": "E",
                "Support air chaud (AC)": "AC"
            }
            acc_code = "-" + "-".join([accessoires_ref[a] for a in accessoires_choisis]) if accessoires_choisis else ""
            reference_finale = ref_base + acc_code
            generate_ref_button(reference_finale)

# === CHARIOTS ===
elif famille == "Chariot":
    st.subheader("Sélectionnez le type de chariot")
    select_type(image_path_chariots, "chariot", 4)

    if "chariot" in st.session_state:
        choix = st.session_state["chariot"]
        st.success(f"✅ Chariot sélectionné : {choix}")
        types = {
            "Chariot de bacs (1200)": "C-b-1200",
            "Chariot de transport des produits": {"1100": "C-tr-1100", "500": "C-tr-500"},
            "Chariot pour produits de grande taille (1300)": "C-pdg-1300",
            "Support visseuse (1800)": "SP-1800",
            "Chariot transport 4 étages": {"600": "C-tr4-600", "1000": "C-tr4-1000"},
            "Chariot 4 étages avec base MDF": {"600": "C-trMDF-600", "1000": "C-trMDF-1000"},
            "Chariot pour cartons (1050)": "C-crt-1050"
        }
        if isinstance(types[choix], dict):
            selected = select_largeur(list(types[choix].keys()), "largeur_chariot")
            if selected:
                generate_ref_button(types[choix][selected])
        else:
            generate_ref_button(types[choix])

# === ÉTAGÈRES ===
elif famille == "Étagère":
    st.subheader("Sélectionnez le type d'étagère")
    select_type(image_path_etageres, "etagere", 3)

    if "etagere" in st.session_state:
        choix = st.session_state["etagere"]
        st.success(f"✅ Étagère sélectionnée : {choix}")
        types = {
            "Étagère pour petits bacs": {"700": "E-pb-700", "1500": "E-pb-1500"},
            "Étagère entrée-sortie (1100)": "E-es-1100",
            "Stockeur des bacs (700)": "SB-700",
            "Étagère 4 étages MDF": {"600": "E-MDF-600", "1000": "E-MDF-1000"},
            "Étagère pour grands bacs (2000)": "E-gb-2000",
            "Étagère de stockage à 3 étages (1600)": "E-s3-1600"
        }
        if isinstance(types[choix], dict):
            selected = select_largeur(list(types[choix].keys()), "largeur_etagere")
            if selected:
                generate_ref_button(types[choix][selected])
        else:
            generate_ref_button(types[choix])
