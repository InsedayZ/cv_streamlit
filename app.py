import streamlit as st
from PIL import Image

# --- Configuration de la page ---
st.set_page_config(
    page_title="CV - Nathan ZOUHOU",
    page_icon="📄",
    layout="wide"
)

# --- Chargement de l'image ---
image_path = "portrait.png"
try:
    image = Image.open(image_path)
except FileNotFoundError:
    st.warning("Image de portrait non trouvée. Vérifie que 'portrait.png' est dans le dossier du script.")
    image = None

# --- Header avec disposition stylisée ---
col1, col2 = st.columns([1, 2], gap="large")

with col1:
    if image:
        st.image(image, caption="Nathan ZOUHOU", width=220)
with col2:
    st.title("👨‍💻 Nathan ZOUHOU")
    st.subheader("Spécialiste en Humanités Numériques • Python • Streamlit • IA")
    st.markdown("### 🎯 À propos de moi")
    st.write(
        "Je suis passionné par les Humanités Numériques, le développement de solutions Python, "
        "la visualisation de données avec Streamlit et les projets à impact humain. "
        "J'allie la créativité aux outils numériques pour rendre les données accessibles et impactantes, "
        "et je m'initie à l’IA générative."
    )
    st.markdown("> 🧠 _“Mon parcours est la preuve que l'apprentissage ne s'arrête pas à l'obtention d'un diplôme, mais continue à chaque défi relevé.”_")

st.markdown("---")

# --- Compétences techniques & Soft Skills ---
st.markdown("### 🧰 Compétences techniques")
cols = st.columns(2)
with cols[0]:
    st.markdown("- Python (avancé)")
    st.markdown("- Power BI")
    st.markdown("- HTML / CSS")
    st.markdown("- Streamlit")
with cols[1]:
    st.markdown("- GitHub / Git")
    st.markdown("- Analyse de données")
    st.markdown("- Gestion de projet digital")
    st.markdown("- IA / LLM (bases)")

st.markdown("### 🧩 Soft Skills")
st.write("💡 Créatif, 🔥 Déterminé, 🧠 Curieux, 🔧 Rigoureux")

# --- Parcours académique ---
st.markdown("### 🎓 Parcours académique")
st.markdown("""
- **2025** : Cursus Humanités Numériques (à venir)  
- **2024** : Autoformation Python, IA, GitHub  
- **2023** : Spécialisation en Management Commercial  
- **2022** : Études de Développement SHS  
- **2020** : Licence Études de Développement SHS
""")

# --- Portfolio / Projets ---
st.markdown("### 📁 Projets")
st.markdown("""
- 🧮 [Visualiseur de données Power BI](https://github.com/InsedayZ/portfolio)  
- 🌐 [Portfolio web Humanités Numériques](https://tonsite.github.io)  
- 🧠 Mini application IA avec Streamlit *(bientôt disponible)*
""")

# --- Contact ---
st.markdown("### 📫 Me contacter")
st.write("[GitHub](https://github.com/InsedayZ) 💻")
st.write("[zouhounath5@gmail.com](mailto:zouhounath5@gmail.com) 📧")

st.markdown("---")
st.caption("© 2025 Nathan ZOUHOU - CV généré avec Streamlit ✨")
