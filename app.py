import streamlit as st
import random

# 1. Configuration de la page
st.set_page_config(page_title="Objectif Chef d'Agrès", page_icon="🚑", layout="centered")

# 2. Style CSS personnalisé
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #e63946; color: white; font-weight: bold; }
    .stProgress > div > div > div > div { background-color: #e63946; }
    .stRadio > label { font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚑 Expert Chef d'Agrès SUAP")
st.write("---")

# 3. Base de données des 20 questions EXPERT
if 'quiz_data' not in st.session_state:
    st.session_state.quiz_data = [
        {"q": "Lors d'un relevage complexe, l'équipier propose une technique risquée. Quelle est votre posture ?", "r": "Stopper l'action, réévaluer et imposer la technique sécurisée", "options": ["Laisser faire pour ne pas briser la confiance", "Stopper l'action, réévaluer et imposer la technique sécurisée", "Déléguer la responsabilité de l'accident à l'équipier"], "expli": "Le CA est responsable pénalement de la sécurité de son personnel."},
        {"q": "Tentative de suicide par défenestration. La victime est au sol. Quelle est votre première action ?", "r": "Identifier les risques persistants (objets chutant, tiers présent)", "options": ["Réaliser le maintien de tête immédiatement", "Identifier les risques persistants (objets chutant, tiers présent)", "Demander l'accord du CODIS pour toucher la victime"], "expli": "L'analyse des risques précède tout contact physique."},
        {"q": "Que signifie 'nuancer le dysfonctionnement' pour une bouteille d'O2 à 50 bars ?", "r": "Le matériel est indisponible pour une intervention longue", "options": ["Le matériel est parfaitement opérationnel", "Le matériel est indisponible pour une intervention longue", "Il faut jeter la bouteille"], "expli": "Le CA doit mesurer l'impact de l'autonomie réduite sur la mission."},
        {"q": "Bilan ABCDE : détresse circulatoire (C) et suspicion de fracture fémur. Priorité ?", "r": "Traiter la détresse circulatoire avant l'immobilisation", "options": ["Poser l'attelle immédiatement", "Traiter la détresse circulatoire avant l'immobilisation", "Passer le bilan radio avant tout soin"], "expli": "La hiérarchie impose de traiter les menaces vitales en priorité."},
        {"q": "L'équipier met 5 min à prendre une tension. Quelle compétence appliquez-vous ?", "r": "Réajuster l'action de l'équipier pour respecter les délais", "options": ["Le laisser finir pour qu'il apprenne", "Prendre la tension à sa place sans rien dire", "Réajuster l'action de l'équipier pour respecter les délais"], "expli": "Le CA doit 'Faire réaliser' dans un temps compatible avec l'urgence."},
        {"q": "Saturation O2 impossible à prendre. Que transmettez-vous au CRRA ?", "r": "Annoncer l'impossibilité technique et décrire les signes cliniques", "options": ["Inventer un chiffre plausible (95%)", "Annoncer l'impossibilité technique et décrire les signes cliniques", "Raccrocher et retenter la mesure"], "expli": "La fiabilité clinique prime sur une valeur chiffrée incertaine."},
        {"q": "Sur AVP, la Police demande de déplacer le VSAV alors que le bilan est en cours. Décision ?", "r": "Refuser si cela compromet la sécurité, proposer une alternative", "options": ["Obéir immédiatement", "Refuser si cela compromet la sécurité, proposer une alternative", "Ignorer la demande"], "expli": "Le CA coordonne sans compromettre la sécurité de la victime."},
        {"q": "Un témoin agressif entrave votre action. Priorité ?", "r": "Demander renfort FDO et mettre l'équipe en sécurité", "options": ["Tenter de maîtriser le témoin", "Demander renfort FDO et mettre l'équipe en sécurité", "Continuer les soins normalement"], "expli": "La sauvegarde de l'équipage est une compétence majeure."},
        {"q": "En Multi-victimes, quel est l'élément clé du message d'ambiance ?", "r": "L'estimation du nombre de victimes et le besoin en renfort", "options": ["Le nom de la première victime", "L'estimation du nombre de victimes et le besoin en renfort", "La liste du matériel utilisé"], "expli": "Permet au CODIS d'ajuster immédiatement les moyens."},
        {"q": "Le niveau 'NA' (Non Acquis) est prononcé en MSP si :", "r": "Une erreur majeure met en cause la sécurité ou la survie", "options": ["Oubli de politesse", "Une erreur majeure met en cause la sécurité ou la survie", "Retard de 2 minutes"], "expli": "La sécurité est le critère d'exclusion principal."},
        {"q": "Différence entre 'Habileté' et 'Attitude' (RNAC) ?", "r": "Habileté = savoir-faire technique, Attitude = savoir-être", "options": ["C'est la même chose", "Habileté = savoir-faire technique, Attitude = savoir-être", "Théorie vs Pratique"], "expli": "Le CA est jugé sur sa posture de chef autant que sur sa technique."},
        {"q": "Pourquoi superviser l'installation du DSA ?", "r": "Garantir la sécurité électrique et la continuité du MCE", "options": ["L'équipier n'a pas le droit de l'allumer", "Garantir la sécurité électrique et la continuité du MCE", "Noter l'heure exacte"], "expli": "La coordination du duo MCE/DSA est un point critique de survie."},
        {"q": "Patient refusant son transport après bilan alarmant. Démarche ?", "r": "Informer, contacter le régulateur et demander signature", "options": ["Forcer le patient", "Partir immédiatement", "Informer, contacter le régulateur et demander signature"], "expli": "Le CA gère le cadre juridique en lien avec le médecin."},
        {"q": "Accouchement imminent : mission prioritaire du CA ?", "r": "Préparer l'accueil du nouveau-né et guider l'équipier", "options": ["Pratiquer l'accouchement seul", "Préparer l'accueil du nouveau-né et guider l'équipier", "Attendre le SMUR sans rien toucher"], "expli": "Le CA anticipe et dirige les gestes de l'équipier."},
        {"q": "Mention obligatoire sur fiche bilan pour traumatisé ?", "r": "Les circonstances précises du mécanisme lésionnel", "options": ["La plaque d'immatriculation", "Les circonstances précises du mécanisme lésionnel", "La météo"], "expli": "Le mécanisme aide à suspecter des lésions internes invisibles."},
        {"q": "Attelle à dépression qui fuit. Action ?", "r": "Signaler et identifier une solution alternative", "options": ["Mettre l'attelle quand même", "Signaler et identifier une solution alternative", "Mettre du scotch"], "expli": "Gestion des dégradations de matériel en opération."},
        {"q": "Gestion du secret médical en intervention ?", "r": "Isoler la victime des regards et oreilles indiscrètes", "options": ["Crier le bilan à la radio", "Isoler la victime des regards et oreilles indiscrètes", "En parler aux voisins"], "expli": "Le respect de la dignité est une compétence évaluée."},
        {"q": "Manque d'un dispositif médical au reconditionnement. Action ?", "r": "Informer le chef de garde et noter l'indisponibilité", "options": ["Ne rien dire", "Informer le chef de garde et noter l'indisponibilité", "Accuser l'équipier"], "expli": "La transparence sur l'état de l'agrès est vitale."},
        {"q": "'Maintenir sa capacité opérationnelle' inclut :", "r": "La formation continue et le maintien des acquis de l'équipe", "options": ["Le sport uniquement", "La formation continue et le maintien des acquis de l'équipe", "La lecture"], "expli": "Le CA est moteur de la formation de ses équipiers."},
        {"q": "Dernier rôle du CA vis-à-vis de l'équipe en fin d'intervention ?", "r": "Effectuer un débriefing rapide (RETEX)", "options": ["Rentrer se coucher", "Effectuer un débriefing rapide (RETEX)", "Critiquer devant tout le monde"], "expli": "Le RETEX fait partie des savoir-être de commandement."}
    ]

# 4. Initialisation des variables de session
if 'score' not in st.session_state: st.session_state.score = 0
if 'current_q' not in st.session_state: st.session_state.current_q = 0

# 5. Logique du Quiz
if st.session_state.current_q < len(st.session_state.quiz_data):
    item = st.session_state.quiz_data[st.session_state.current_q]
    
    st.progress(st.session_state.current_q / len(st.session_state.quiz_data))
    st.subheader(f"Question {st.session_state.current_q + 1} / {len(st.session_state.quiz_data)}")
    st.info(item["q"])
    
    # Mélange des options
    if f"opt_{st.session_state.current_q}" not in st.session_state:
        opts = list(item["options"])
        random.shuffle(opts)
        st.session_state[f"opt_{st.session_state.current_q}"] = opts
    
    with st.form(key=f"q_{st.session_state.current_q}"):
        choix = st.radio("Sélectionnez votre réponse :", st.session_state[f"opt_{st.session_state.current_q}"])
        submit = st.form_submit_button("Valider")
        
        if submit:
            if choix == item["r"]:
                st.success(f"🎯 CORRECT ! {item['expli']}")
                st.session_state.score += 1
            else:
                st.error(f"❌ ERREUR. La réponse était : {item['r']}")
                st.warning(f"💡 {item['expli']}")
            st.write("Cliquez sur le bouton 'Suivant' ci-dessous.")

    if st.button("Question Suivante ➡️"):
        st.session_state.current_q += 1
        st.rerun()

else:
    st.balloons()
    st.success(f"🏆 TEST TERMINÉ ! Score : {st.session_state.score} / {len(st.session_state.quiz_data)}")
    if st.button("Recommencer à zéro"):
        for key in list(st.session_state.keys()): del st.session_state[key]
        st.rerun()
