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
    """, unsafe_allow_html=True)

st.title("🚑 Prépa Chef d'Agrès SUAP")
st.write("---")

# Base de données de questions (On pourra en ajouter des centaines)
if 'quiz_data' not in st.session_state:
    if 'quiz_data' not in st.session_state:
    st.session_state.quiz_data = [
        # --- TACTIQUE ET COMMANDEMENT ---
        {"q": "Lors d'un relevage complexe, l'équipier propose une technique qui vous semble risquée. Quelle est votre posture ?", "r": "Stopper l'action, réévaluer et imposer la technique sécurisée", "options": ["Laisser faire pour ne pas briser la confiance", "Stopper l'action, réévaluer et imposer la technique sécurisée", "Déléguer la responsabilité de l'accident à l'équipier"], "expli": "Le CA est responsable pénalement et administrativement de la sécurité de son personnel."},
        {"q": "Vous intervenez sur une tentative de suicide par défenestration. La victime est au sol. Quelle est votre première action de 'Chef' ?", "r": "Identifier les risques persistants (objets chutant, tiers présent)", "options": ["Réaliser le maintien de tête immédiatement", "Identifier les risques persistants (objets chutant, tiers présent)", "Demander l'accord du CODIS pour toucher la victime"], "expli": "L'analyse des risques (RIOFE) doit précéder tout contact physique pour éviter le suraccident."},
        {"q": "Le RNAC précise que le CA doit 'nuancer le dysfonctionnement'. Qu'est-ce que cela signifie pour une bouteille d'O2 à 50 bars ?", "r": "Le matériel est indisponible pour une intervention longue", "options": ["Le matériel est parfaitement opérationnel", "Le matériel est indisponible pour une intervention longue", "Il faut jeter la bouteille"], "expli": "Le CA doit mesurer l'impact d'une autonomie réduite sur la capacité opérationnelle réelle."},

        # --- BILAN ET RÉGULATION (ABCDE / PESTE) ---
        {"q": "Lors du bilan ABCDE, vous notez une détresse circulatoire (C) et une suspicion de fracture du fémur. Quelle est la priorité du CA ?", "r": "Traiter la détresse circulatoire avant l'immobilisation du membre", "options": ["Poser l'attelle immédiatement", "Traiter la détresse circulatoire avant l'immobilisation du membre", "Passer le bilan radio avant tout soin"], "expli": "La hiérarchie des bilans impose de traiter les menaces vitales (C) avant les lésions traumatiques localisées."},
        {"q": "Votre équipier met 5 minutes à prendre une tension. Quelle compétence du RIOFE devez-vous appliquer ?", "r": "Réajuster l'action de l'équipier pour respecter les délais", "options": ["Le laisser finir pour qu'il apprenne", "Prendre la tension à sa place sans rien dire", "Réajuster l'action de l'équipier pour respecter les délais"], "expli": "Le CA doit 'Faire réaliser' dans un temps compatible avec l'urgence."},
        {"q": "Le médecin régulateur vous demande une saturation en O2 que vous n'arrivez pas à prendre. Que dites-vous ?", "r": "Annoncer l'impossibilité technique et décrire les signes cliniques (cyanose, sueurs)", "options": ["Inventer un chiffre plausible (95%)", "Annoncer l'impossibilité technique et décrire les signes cliniques (cyanose, sueurs)", "Raccrocher et retenter la mesure"], "expli": "La fiabilité de la transmission (RIOFE) est plus importante qu'une valeur chiffrée incertaine."},

        # --- SITUATIONS SPÉCIFIQUES ET INTERFACES ---
        {"q": "Sur une AVP, la Gendarmerie vous demande de déplacer le VSAV pour libérer une voie. Vous n'avez pas fini le bilan. Que décidez-vous ?", "r": "Refuser si cela compromet la sécurité ou le soin, proposer une alternative", "options": ["Obéir immédiatement car ils ont l'autorité", "Refuser si cela compromet la sécurité ou le soin, proposer une alternative", "Ignorer la demande"], "expli": "Le CA est responsable de sa zone de travail et doit coordonner avec les partenaires sans compromettre la victime."},
        {"q": "Un témoin agressif entrave votre action. Selon le cadre de vos compétences, quelle est votre priorité ?", "r": "Demander un renfort FDO et mettre l'équipe en sécurité", "options": ["Tenter de maîtriser physiquement le témoin", "Demander un renfort FDO et mettre l'équipe en sécurité", "Continuer les soins comme si de rien n'était"], "expli": "La sauvegarde de l'équipage est une compétence transversale majeure du CA."},
        {"q": "Dans une situation de 'Multi-victimes', quel est l'élément clé du message d'ambiance du CA ?", "r": "L'estimation du nombre de victimes et le besoin en renfort", "options": ["Le nom de la première victime identifiée", "L'estimation du nombre de victimes et le besoin en renfort", "La liste précise de tout le matériel utilisé"], "expli": "Le CA 1 équipe doit donner une vision globale pour permettre au CODIS d'ajuster les secours."},

        # --- ÉVALUATION ET LIVRET RIOFE ---
        {"q": "Le niveau 'NA' (Non Acquis) est prononcé lors d'une MSP si :", "r": "Une erreur majeure met en cause la sécurité ou la survie", "options": ["L'équipier a oublié de dire 'Bonjour'", "Une erreur majeure met en cause la sécurité ou la survie", "Le stagiaire est arrivé avec 2 minutes de retard"], "expli": "Les critères d'exclusion en évaluation CA sont souvent liés à la sécurité (RIOFE)."},
        {"q": "Quelle est la différence entre une 'Habileté' et une 'Attitude' selon le RNAC ?", "r": "L'habileté est un savoir-faire technique, l'attitude est un savoir-être", "options": ["C'est la même chose", "L'habileté est un savoir-faire technique, l'attitude est un savoir-être", "L'habileté est théorique, l'attitude est pratique"], "expli": "Le CA est évalué sur sa capacité à se comporter en chef (Attitude) autant que sur sa technique (Habileté)."},

        # --- TECHNIQUE SUAP AVANCÉE ---
        {"q": "Pourquoi le CA doit-il superviser l'installation du défibrillateur (DSA) ?", "r": "Pour garantir la sécurité électrique et la continuité des compressions", "options": ["Parce que l'équipier n'a pas le droit d'allumer l'appareil", "Pour garantir la sécurité électrique et la continuité des compressions", "Pour noter l'heure exacte sur sa montre"], "expli": "La coordination du MCE/DSA est un point critique de survie géré par le CA."},
        {"q": "Un patient refuse son transport après un bilan alarmant. Quelle est la démarche légale du CA ?", "r": "Informer le patient, contacter le médecin régulateur et demander une signature", "options": ["Forcer le patient à monter dans le VSAV", "Partir immédiatement car il a refusé", "Informer le patient, contacter le médecin régulateur et demander une signature"], "expli": "Le CA gère le cadre juridique du refus de soin en lien avec la régulation médicale."},
        {"q": "Lors d'un accouchement imminent, quelle est la mission prioritaire du CA 1 équipe ?", "r": "Préparer l'accueil du nouveau-né et guider l'équipier", "options": ["Pratiquer l'accouchement seul", "Préparer l'accueil du nouveau-né et guider l'équipier", "Attendre le SMUR sans toucher la maman"], "expli": "Le CA anticipe les besoins (température, matériel) et dirige les gestes de l'équipier."},

        # --- LOGISTIQUE ET ADMINISTRATION ---
        {"q": "Quelle mention est obligatoire sur la fiche bilan pour un patient traumatisé ?", "r": "Les circonstances précises du mécanisme lésionnel", "options": ["Le numéro de plaque d'immatriculation", "Les circonstances précises du mécanisme lésionnel", "La météo au moment de l'accident"], "expli": "La cinétique (vitesse, choc) aide le médecin à suspecter des lésions internes non visibles."},
        {"q": "Le CA constate qu'une attelle à dépression fuit. Quelle action est attendue ?", "r": "Signaler l'anomalie et identifier une solution alternative (ex: attelle alu-mousse)", "options": ["Mettre l'attelle quand même", "Signaler l'anomalie et identifier une solution alternative (ex: attelle alu-mousse)", "Demander au conducteur de la réparer avec du scotch"], "expli": "Capacité à gérer les dégradations de matériel en intervention."},
        {"q": "Comment le CA doit-il gérer le secret médical en intervention ?", "r": "En isolant la victime des regards et des oreilles indiscrètes", "options": ["En criant le bilan à la radio", "En isolant la victime des regards et des oreilles indiscrètes", "En racontant l'intervention aux voisins"], "expli": "Le respect de la dignité et du secret est une compétence évaluée (RIOFE)."},
        {"q": "Lors du reconditionnement, le CA s'aperçoit qu'il manque un dispositif médical. Que doit-il faire ?", "r": "Informer le chef de garde et noter l'indisponibilité partielle", "options": ["Ne rien dire en espérant que personne ne remarque", "Informer le chef de garde et noter l'indisponibilité partielle", "Accuser l'équipier"], "expli": "La transparence sur l'état de l'agrès est vitale pour la chaîne de secours."},
        {"q": "Le CA doit 'maintenir sa capacité opérationnelle'. Cela inclut :", "r": "La formation continue et le maintien des acquis de son équipe", "options": ["Le sport uniquement", "La formation continue et le maintien des acquis de son équipe", "La lecture de romans"], "expli": "Le CA est moteur de la formation de son équipe en garde."},
        {"q": "En fin d'intervention, quel est le dernier rôle du CA vis-à-vis de son équipe ?", "r": "Effectuer un débriefing rapide (Points positifs/négatifs)", "options": ["Rentrer se coucher directement", "Effectuer un débriefing rapide (Points positifs/négatifs)", "Critiquer l'équipier devant tout le monde"], "expli": "Le retour d'expérience (RETEX) immédiat fait partie des savoir-être de commandement."}
    ]

import random # Assure-toi que cette ligne est bien tout en haut du fichier

# --- LOGIQUE DU QUIZ ---

if st.session_state.current_q < len(st.session_state.quiz_data):
    item = st.session_state.quiz_data[st.session_state.current_q]
    
    st.subheader(f"Question {st.session_state.current_q + 1} / {len(st.session_state.quiz_data)}")
    st.info(item["q"])
    
    # --- MÉLANGE DES RÉPONSES ---
    # On crée une copie des options pour ne pas modifier la liste originale
    options_melangees = list(item["options"])
    # Si on n'a pas encore mélangé pour cette question précise
    if f"options_{st.session_state.current_q}" not in st.session_state:
        random.shuffle(options_melangees)
        st.session_state[f"options_{st.session_state.current_q}"] = options_melangees
    
    current_options = st.session_state[f"options_{st.session_state.current_q}"]

    # --- FORMULAIRE ---
    with st.form(key=f"form_{st.session_state.current_q}"):
        reponse = st.radio("Ta réponse :", current_options)
        valider = st.form_submit_button("Valider la réponse")
        
        if valider:
            if reponse == item["r"]:
                st.success(f"✅ Bravo ! {item['expli']}")
                st.session_state.score += 1
            else:
                st.error(f"❌ Raté... La réponse était : {item['r']}")
                st.warning(f"💡 {item['expli']}")
            
            st.session_state.answered = True # Marque que la réponse est donnée
            st.write("Cliquez sur 'Question suivante' pour continuer.")

    # Bouton pour passer à la suite
    if st.button("Passer à la question suivante ➡️"):
        st.session_state.current_q += 1
        st.rerun()

else:
    # --- FIN DU QUIZ ---
    st.balloons()
    st.success(f"🏆 Quiz terminé ! Ton score final : {st.session_state.score} / {len(st.session_state.quiz_data)}")
    
    if st.button("Recommencer le test"):
        # On vide aussi les options mélangées stockées
        for key in list(st.session_state.keys()):
            if key.startswith("options_"):
                del st.session_state[key]
        st.session_state.current_q = 0
        st.session_state.score = 0
        st.rerun()
