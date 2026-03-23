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
            # --- BLOC 1 : COMMANDEMENT ET POSTURE ---
            {"q": "Selon le RNAC, quelle est la mission principale du CA 1 équipe concernant son personnel ?", "r": "Commander et diriger l'équipe", "options": ["Réaliser les soins seul", "Commander et diriger l'équipe", "Attendre l'ordre de l'officier"], "expli": "Le CA doit assurer la direction de son équipe (L'équipier et le conducteur)."},
            {"q": "Quelle attitude est attendue du CA face à une situation complexe selon le RIOFE 74 ?", "r": "S'intégrer dans un dispositif et rendre compte", "options": ["Prendre le commandement de tout le secteur", "S'intégrer dans un dispositif et rendre compte", "Attendre sans agir"], "expli": "La capacité à s'intégrer et à rendre compte à la hiérarchie ou à la régulation est primordiale."},
            {"q": "Pour le CA, que signifie 'Superviser' selon le référentiel national ?", "r": "Contrôler la réalisation des tâches déléguées", "options": ["Faire le travail à la place des autres", "Contrôler la réalisation des tâches déléguées", "Ne rien faire et regarder"], "expli": "Le CA délègue l'exécution mais reste responsable du contrôle (ex: bilan, immobilisation)."},
            
            # --- BLOC 2 : SÉCURITÉ ---
            {"q": "Quelle est la priorité immédiate dès l'arrêt du véhicule ?", "r": "Assurer la sécurité et le balisage", "options": ["Prendre le sac de secours", "Assurer la sécurité et le balisage", "Appeler le CODIS"], "expli": "La sécurité (intervenants, victime, tiers) prime sur toute action de secours."},
            {"q": "Le CA doit s'assurer que son personnel porte ses EPI. Quel est son rôle vis-à-vis du contrôle ?", "r": "Réaliser ou faire réaliser des contrôles croisés", "options": ["Chacun est responsable de soi seul", "Réaliser ou faire réaliser des contrôles croisés", "Vérifier uniquement sa propre tenue"], "expli": "Le CA est garant de la sécurité collective via les contrôles croisés."},
            
            # --- BLOC 3 : BILANS ET TRANSMISSIONS ---
            {"q": "Selon le RIOFE, le CA doit être capable de transmettre son bilan à qui en priorité ?", "r": "Au CRRA (15) ou au CODIS", "options": ["À la famille de la victime", "Au CRRA (15) ou au CODIS", "Uniquement à son chef de centre"], "expli": "La transmission rapide et structurée vers la régulation est une compétence clé."},
            {"q": "Dans la gestion d'une intervention, le CA 1 équipe doit prioritairement :", "r": "Organiser le bilan de la victime", "options": ["Organiser le bilan de la victime", "Conduire le véhicule", "Remplir uniquement la partie administrative"], "expli": "L'organisation du bilan (recueil d'infos par l'équipier) est sous sa responsabilité."},
            
            # --- BLOC 4 : MATÉRIEL ET OPÉRATIONNALITÉ ---
            {"q": "Le CA doit signaler un matériel défectueux. Quelle est l'attitude attendue ?", "r": "Mesurer l'impact du dysfonctionnement sur la mission", "options": ["Ignorer si le matériel n'est pas vital", "Mesurer l'impact du dysfonctionnement sur la mission", "Arrêter l'intervention immédiatement"], "expli": "Le CA doit juger si l'anomalie empêche la mission ou si une alternative existe."},
            {"q": "Qui est responsable du reconditionnement du matériel après l'intervention ?", "r": "Le CA supervise le reconditionnement", "options": ["L'équipier seul", "Le CA supervise le reconditionnement", "Le mécanicien du groupement"], "expli": "Le CA s'assure que l'agrès est à nouveau opérationnel avant de se rendre disponible."},
            
            # --- BLOC 5 : ANALYSE DES RISQUES ---
            {"q": "Face à un danger immédiat non maîtrisé, quelle est la compétence du CA ?", "r": "Définir une zone d'exclusion", "options": ["Intervenir coûte que coûte", "Définir une zone d'exclusion", "Attendre les renforts sans rien baliser"], "expli": "Savoir identifier et délimiter les dangers fait partie des savoir-agir de sécurité."},
            {"q": "Le CA 1 équipe doit savoir s'extraire d'une zone de danger. C'est une compétence de :", "r": "Sauvegarde individuelle et collective", "options": ["Sauvegarde individuelle et collective", "Secourisme pur", "Logistique"], "expli": "La sauvegarde est une compétence transversale citée dans le RNAC."},
            
            # --- BLOC 6 : FORMATION ET ACCOMPAGNEMENT ---
            {"q": "Le livret de suivi (RIOFE 74) sert à valider des compétences. Que signifie le 'A' ?", "r": "Acquis", "options": ["Attendu", "Acquis", "À revoir"], "expli": "A = Acquis, ECA = En cours d'acquisition, NA = Non acquis."},
            {"q": "Le CA peut-il être tuteur d'un stagiaire dans le VSAV ?", "r": "Oui, il accompagne son développement", "options": ["Oui, il accompagne son développement", "Non, seul un officier peut le faire", "Uniquement si le stagiaire est déjà formé"], "expli": "Le CA participe à la formation de ses équipiers par l'accompagnement."},
            
            # --- BLOC 7 : CADRE RÉGLEMENTAIRE ---
            {"q": "Quelle est la date de la version du RNAC fournie ?", "r": "2019", "options": ["2015", "2019", "2022"], "expli": "Le référentiel national actuel date du 22/08/2019."},
            {"q": "Le RIOFE 74 s'applique spécifiquement pour quel type de SP ?", "r": "SPV (Volontaires)", "options": ["SPP uniquement", "SPV (Volontaires)", "JSP uniquement"], "expli": "Le document cible la formation d'intégration et de professionnalisation des SPV."},
            
            # --- BLOC 8 : COMPÉTENCES TRANSVERSALES ---
            {"q": "Parmi ces choix, lequel est une compétence transversale du CA ?", "r": "S'impliquer dans son emploi", "options": ["Savoir nager", "S'impliquer dans son emploi", "Connaître tous les hydrants"], "expli": "L'implication et le respect du cadre déontologique sont des compétences transversales."},
            {"q": "Comment le CA doit-il communiquer avec les autres services (Gendarmerie, SMUR) ?", "r": "De manière courtoise et efficace", "options": ["En leur donnant des ordres", "De manière courtoise et efficace", "Il ne doit pas leur parler"], "expli": "Le CA représente le service et doit coordonner ses actions avec les partenaires."},
            
            # --- BLOC 9 : SITUATIONS PARTICULIÈRES ---
            {"q": "En cas de nombreuses victimes, le CA doit :", "r": "Sectoriser et remonter les informations", "options": ["Traiter toutes les victimes seul", "Sectoriser et remonter les informations", "Demander à l'équipier de commander"], "expli": "Le CA aide à l'organisation du chantier en attendant les échelons supérieurs."},
            {"q": "Le CA doit savoir anticiper. Qu'est-ce que cela signifie en SUAP ?", "r": "Prévoir l'évolution de la victime et les besoins futurs", "options": ["Partir avant la fin des soins", "Prévoir l'évolution de la victime et les besoins futurs", "Deviner l'adresse de l'intervention"], "expli": "L'anticipation permet de demander les renforts (SMUR) au bon moment."},
            
            # --- BLOC 10 : ÉVALUATION ---
            {"q": "Une MSP (Mise en Situation Professionnelle) sert à :", "r": "Évaluer les compétences en situation réelle", "options": ["Faire du sport", "Évaluer les compétences en situation réelle", "Apprendre la théorie"], "expli": "La MSP est l'outil principal de validation du CA 1 équipe."},
    
            {"q": "Quelle est la fréquence de compression (MCE) ?", "r": "100-120/min", "options": ["80-100/min", "100-120/min", "120-140/min"], "expli": "Référence GNR ACR 2024."},
            {"q": "Que signifie le 'P' dans l'acronyme PESTE ?", "r": "Pouls", "options": ["Pression", "Pouls", "Pupilles"], "expli": "Examen circulatoire rapide."},
            {"q": "Quel est le débit d'O2 pour un ACR avec insufflateur ?", "r": "15 L/min", "options": ["9 L/min", "12 L/min", "15 L/min"], "expli": "Débit maximum pour remplir le réservoir."},
        ]

# --- LOGIQUE DU QUIZ ---

# On vérifie si on n'a pas dépassé le nombre de questions
if st.session_state.current_q < len(st.session_state.quiz_data):
    item = st.session_state.quiz_data[st.session_state.current_q]
    
    st.subheader(f"Question {st.session_state.current_q + 1} / {len(st.session_state.quiz_data)}")
    st.info(item["q"])
    
    # Formulaire pour éviter que la page se recharge à chaque clic
    with st.form(key=f"form_{st.session_state.current_q}"):
        reponse = st.radio("Ta réponse :", item["options"])
        valider = st.form_submit_button("Valider la réponse")
        
        if valider:
            if reponse == item["r"]:
                st.success(f"✅ Bravo ! {item['expli']}")
                st.session_state.score += 1
            else:
                st.error(f"❌ Raté... La réponse était : {item['r']}")
                st.warning(f"💡 {item['expli']}")
            
            # On prépare le passage à la question suivante
            st.session_state.current_q += 1
            st.write("Appuyez sur le bouton ci-dessous pour continuer.")

    # Bouton pour passer à la suite (en dehors du formulaire)
    if st.button("Passer à la question suivante ➡️"):
        st.rerun()

else:
    # --- FIN DU QUIZ ---
    st.balloons()
    st.success(f"🏆 Quiz terminé ! Ton score final : {st.session_state.score} / {len(st.session_state.quiz_data)}")
    
    if st.button("Recommencer le test"):
        st.session_state.current_q = 0
        st.session_state.score = 0
        st.rerun()
        st.session_state.current_q = 0
        st.session_state.score = 0
        st.rerun()
