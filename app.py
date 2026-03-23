import streamlit as st
import random

# 1. Configuration
st.set_page_config(page_title="Formation CA 1 Équipe", page_icon="🚑", layout="wide")

# 2. Style CSS pour un aspect "Fiche Mémo"
st.markdown("""
    <style>
    .memo-card { background-color: #f8f9fa; padding: 20px; border-left: 5px solid #e63946; border-radius: 10px; margin-bottom: 20px; }
    .priority-box { background-color: #ffe3e3; padding: 15px; border-radius: 10px; border: 1px dashed #e63946; }
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #e63946; color: white; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 3. Initialisation des variables de session
if 'step' not in st.session_state: st.session_state.step = 'cours'
if 'page_cours' not in st.session_state: st.session_state.page_cours = 1
if 'score' not in st.session_state: st.session_state.score = 0
if 'current_q' not in st.session_state: st.session_state.current_q = 0

# --- PARTIE 1 : LE COURS THÉORIQUE ---
if st.session_state.step == 'cours':
    st.title("📖 Module de Formation : Chef d'Agrès 1 Équipe")
    st.write(f"Étape {st.session_state.page_cours} / 4")
    st.progress(st.session_state.page_cours / 4)

    if st.session_state.page_cours == 1:
        st.header("🛡️ Module 1 : La Sécurité & L'Arrivée")
        st.markdown("""
        <div class="memo-card">
        <h3>La règle d'or : "S'arrêter, Observer, Agir"</h3>
        <ul>
            <li><b>Sécurité immédiate :</b> Avant même de descendre, analysez les risques (Trafic, Gaz, Électricité, Tiers).</li>
            <li><b>Balisage :</b> C'est votre priorité n°1. Un VSAV mal placé est un danger.</li>
            <li><b>Contrôle croisé :</b> Vérifiez que votre équipier porte ses gants et son gilet haute visibilité.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1582213726893-ec70498877f2?auto=format&fit=crop&q=80&w=400", caption="Analyse de zone")

    elif st.session_state.page_cours == 2:
        st.header("🧠 Module 2 : La Posture de Chef (RNAC)")
        st.markdown("""
        <div class="memo-card">
        <h3>Commander, ce n'est pas forcément faire.</h3>
        <p>Le CA 1 équipe doit :</p>
        <ul>
            <li><b>Diriger :</b> Donner des ordres clairs (ex: "Installe le collier cervical").</li>
            <li><b>Superviser :</b> Vérifier que le geste est bien fait sans le faire soi-même.</li>
            <li><b>Anticiper :</b> Demander le SMUR 5 minutes <i>avant</i> d'en avoir désespérément besoin.</li>
        </ul>
        </div>
        <div class="priority-box">
        ⚠️ <b>Point RIOFE :</b> Votre capacité à "Rendre compte" au CODIS/CRRA définit votre niveau de compétence.
        </div>
        """, unsafe_allow_html=True)

    elif st.session_state.page_cours == 3:
        st.header("🩺 Module 3 : Le Bilan ABCDE / PESTE")
        st.markdown("""
        <div class="memo-card">
        <h3>La rigueur du bilan</h3>
        <p>Le CA organise le recueil d'informations :</p>
        <ul>
            <li><b>A (Airways) :</b> Liberté des voies aériennes.</li>
            <li><b>B (Breathing) :</b> Fréquence, amplitude, saturation.</li>
            <li><b>C (Circulation) :</b> Pouls, TA, saignements (Priorité absolue si hémorragie).</li>
            <li><b>D (Disability) :</b> Conscience (GCS), pupilles, motricité.</li>
            <li><b>E (Exposure) :</b> Traumatisme, température, protéger la pudeur.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    elif st.session_state.page_cours == 4:
        st.header("📞 Module 4 : Transmissions & Régulation")
        st.markdown("""
        <div class="memo-card">
        <h3>Le passage du bilan (La Radio)</h3>
        <p>Soyez structuré pour être crédible auprès du médecin :</p>
        <ol>
            <li><b>Présentation :</b> Qui vous êtes, où vous êtes.</li>
            <li><b>Circonstances :</b> Pourquoi vous êtes là (mécanisme lésionnel).</li>
            <li><b>Bilan Vital :</b> L'essentiel du ABCDE.</li>
            <li><b>Actions :</b> Ce que vous avez déjà fait (O2, immobilisation).</li>
        </ol>
        </div>
        """, unsafe_allow_html=True)
        st.success("Félicitations ! Vous avez terminé la théorie. Prêt pour l'examen ?")

    # Navigation Cours
    col1, col2 = st.columns(2)
    with col1:
        if st.session_state.page_cours > 1:
            if st.button("⬅️ Précédent"):
                st.session_state.page_cours -= 1
                st.rerun()
    with col2:
        if st.session_state.page_cours < 4:
            if st.button("Suivant ➡️"):
                st.session_state.page_cours += 1
                st.rerun()
        else:
            if st.button("🚀 ACCÉDER AU QUIZ EXAMEN"):
                st.session_state.step = 'quiz'
                st.rerun()

# --- PARTIE 2 : LE QUIZ (Logique identique à la précédente) ---
elif st.session_state.step == 'quiz':
    if 'quiz_data' not in st.session_state:
        # On insère ici les 20 questions expertes générées précédemment
        st.session_state.quiz_data = [
            {"q": "Lors d'un relevage complexe, l'équipier propose une technique risquée. Quelle est votre posture ?", "r": "Stopper l'action, réévaluer et imposer la technique sécurisée", "options": ["Laisser faire pour ne pas briser la confiance", "Stopper l'action, réévaluer et imposer la technique sécurisée", "Déléguer la responsabilité de l'accident à l'équipier"], "expli": "Le CA est responsable pénalement de la sécurité de son personnel."},
            # ... (Ajoute ici les autres questions expertes du message précédent)
        ]

    st.title("🚑 Examen Chef d'Agrès")
    
    if st.session_state.current_q < len(st.session_state.quiz_data):
        item = st.session_state.quiz_data[st.session_state.current_q]
        st.progress(st.session_state.current_q / len(st.session_state.quiz_data))
        
        st.subheader(f"Question {st.session_state.current_q + 1}")
        st.info(item["q"])
        
        # Mélange des options
        if f"opt_{st.session_state.current_q}" not in st.session_state:
            opts = list(item["options"])
            random.shuffle(opts)
            st.session_state[f"opt_{st.session_state.current_q}"] = opts

        with st.form(key=f"q_{st.session_state.current_q}"):
            choix = st.radio("Votre réponse :", st.session_state[f"opt_{st.session_state.current_q}"])
            submit = st.form_submit_button("Valider")
            
            if submit:
                if choix == item["r"]:
                    st.success(f"🎯 CORRECT ! {item['expli']}")
                    st.session_state.score += 1
                else:
                    st.error(f"❌ ERREUR. La réponse était : {item['r']}")
                    st.warning(f"💡 {item['expli']}")

        if st.button("Question Suivante ➡️"):
            st.session_state.current_q += 1
            st.rerun()
    else:
        st.balloons()
        st.success(f"🏆 Score Final : {st.session_state.score} / {len(st.session_state.quiz_data)}")
        if st.button("Recommencer la formation"):
            for key in list(st.session_state.keys()): del st.session_state[key]
            st.rerun()
            
