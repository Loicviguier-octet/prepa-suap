import streamlit as st
import random

# Configuration de l'interface
st.set_page_config(page_title="Objectif Chef d'Agrès", page_icon="🚑", layout="centered")

# Style personnalisé (Rouge Secours)
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #e63946; color: white; }
    .stProgress > div > div > div > div { background-color: #e63946; }
    </style>
    """, unsafe_allow_index=True)

st.title("🚑 Prépa Chef d'Agrès SUAP")
st.write("---")

# Base de données de questions (On pourra en ajouter des centaines)
if 'quiz_data' not in st.session_state:
    st.session_state.quiz_data = [
        {"q": "Quelle est la fréquence de compression (MCE) ?", "r": "100-120/min", "options": ["80-100/min", "100-120/min", "120-140/min"], "expli": "Référence GNR ACR 2024."},
        {"q": "Que signifie le 'P' dans l'acronyme PESTE ?", "r": "Pouls", "options": ["Pression", "Pouls", "Pupilles"], "expli": "Examen circulatoire rapide."},
        {"q": "Quel est le débit d'O2 pour un ACR avec insufflateur ?", "r": "15 L/min", "options": ["9 L/min", "12 L/min", "15 L/min"], "expli": "Débit maximum pour remplir le réservoir."},
    ]

# Initialisation du score et de l'index
if 'score' not in st.session_state: st.session_state.score = 0
if 'current_q' not in st.session_state: st.session_state.current_q = 0

# Barre de progression (corrigée)
progression = (st.session_state.current_q) / len(st.session_state.quiz_data)
st.progress(progression)

# Affichage de la question (corrigée)
if st.session_state.current_q < len(st.session_state.quiz_data):
    item = st.session_state.quiz_data[st.session_state.current_q] # <--- Le crochet est ici !
    
    st.subheader(f"Question {st.session_state.current_q + 1}")
    st.info(item["q"])
    
    reponse = st.radio("Ta réponse :", item["options"], key=f"radio_{st.session_state.current_q}")
    
    if st.button("Valider la réponse"):
        if reponse == item["r"]:
            st.success(f"Bravo ! 🎯 {item['expli']}")
            st.session_state.score += 1
        else:
            st.error(f"Raté... La réponse était : {item['r']}. {item['expli']}")
        
        # Petit bouton pour passer à la suite
        if st.button("Question suivante ➡️"):
            st.session_state.current_q += 1
            st.rerun()
else:
    st.balloons()
    st.success(f"🏆 Quiz terminé ! Ton score final : {st.session_state.score} / {len(st.session_state.quiz_data)}")
    if st.button("Recommencer"):
        st.session_state.current_q = 0
        st.session_state.score = 0
        st.rerun()
