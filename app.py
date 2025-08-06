import streamlit as st
from PIL import Image

# --- Configuration de la page ---
st.set_page_config(
    page_title="CV - Nathan ZOUHOU",
    page_icon="📄",
    layout="wide"
)

# --- CSS personnalisé ---
st.markdown("""
<style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 0rem;
        padding-left: 5%;
        padding-right: 5%;
    }
    h1, h2, h3, h4, h5, h6 {
        margin-top: 0.5rem;
        margin-bottom: 0.5rem;
    }
    p {
        margin-top: 0.2rem;
        margin-bottom: 0.2rem;
    }
    .stMarkdown {
        margin-top: 0.2rem;
        margin-bottom: 0.2rem;
    }
    .stImage {
        margin-top: 0rem;
        margin-bottom: 0rem;
    }
</style>
""", unsafe_allow_html=True)

# --- Chargement de l'image ---
image_path = "portrait.png"
try:
    image = Image.open(image_path)
except FileNotFoundError:
    st.warning("Image de portrait non trouvée. Vérifie que 'portrait.png' est dans le dossier du script.")
    image = None

# --- Header ---
col1, col2 = st.columns([1, 2])  # Retire gap si version < 1.29.0

with col1:
    if image:
        st.image(image, caption="Nathan ZOUHOU", width=180)
with col2:
    st.title("👨‍💻 Nathan ZOUHOU")
    st.subheader("Spécialiste en Humanités Numériques • Python • Streamlit • IA")
    st.markdown("### 🎯 À propos de moi")
    st.write(
        "Passionné par les Humanités Numériques, je développe des solutions Python, "
        "visualise des données avec Streamlit et m'initie à l’IA générative. "
        "J'allie créativité et outils numériques pour rendre les données accessibles et impactantes."
    )
    st.markdown("> 🧠 _“Mon parcours est la preuve que l'apprentissage ne s'arrête pas à l'obtention d'un diplôme, mais continue à chaque défi relevé.”_", unsafe_allow_html=True)

st.markdown("---")

# --- Compétences ---
st.markdown("### 🧰 Compétences")
cols_skills = st.columns(2)
with cols_skills[0]:
    st.markdown("**Techniques :**")
    st.markdown("- Python (avancé)")
    st.markdown("- Power BI")
    st.markdown("- HTML / CSS")
    st.markdown("- Streamlit")
with cols_skills[1]:
    st.markdown("**Outils & Méthodes :**")
    st.markdown("- GitHub / Git")
    st.markdown("- Analyse de données")
    st.markdown("- Gestion de projet digital")
    st.markdown("- IA / LLM (bases)")

st.markdown("**Soft Skills :** 💡 Créatif, 🔥 Déterminé, 🧠 Curieux, 🔧 Rigoureux")

st.markdown("---")

# --- Formation ---
st.markdown("### 🎓 Formation")
col_year, col_degree = st.columns([0.2, 0.8])
with col_year:
    st.write("**2025**")
    st.write("**2024**")
    st.write("**2023**")
    st.write("**2022**")
    st.write("**2020**")
with col_degree:
    st.write("Cursus Humanités Numériques (à venir)")
    st.write("Autoformation Python, IA, GitHub")
    st.write("Spécialisation en Management Commercial")
    st.write("Études de Développement SHS")
    st.write("Licence Études de Développement SHS")

st.markdown("---")

# --- Projets ---
st.markdown("### 📁 Projets")
st.markdown("""
- 🧮 [Analyse de données de livres](https://github.com/InsedayZ/dataviz-collection-livres)
- 🌐 [Portfolio web Humanités Numériques](https://insedayz.github.io/Portfolio_responsive/)
- 🧠 [CV Streamlit](https://github.com/InsedayZ/cv_streamlit)
""")

st.markdown("---")

# --- Contact ---
st.markdown("### 📫 Contact")
contact_col1, contact_col2 = st.columns(2)
with contact_col1:
    st.write("[GitHub](https://github.com/InsedayZ) 💻")
with contact_col2:
    st.write("[zouhounath5@gmail.com](mailto:zouhounath5@gmail.com) 📧")

st.markdown("---")
st.caption("© 2025 Nathan ZOUHOU - CV généré avec Streamlit ✨")
