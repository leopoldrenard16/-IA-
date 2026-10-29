import streamlit as st
import random
import secrets
import string

# Configuration de la page du site
st.set_page_config(page_title="ChatIA", page_icon="🤖", layout="centered")

# ========================================== #
#             FONCTIONS ET MODULES           #
# ========================================== #

def nettoyer_texte(texte):
    """Met le texte en minuscules et retire la ponctuation de base."""
    texte = texte.lower()
    for char in [".", ",", "?", "!", "-", "_", ";", ":", "'"]:
        texte = texte.replace(char, " ")
    return " ".join(texte.split())

def generer_niveaux_game():
    """Génère la liste des 120 niveaux pour calcul-GAME."""
    niveaux = []
    for i in range(1, 16):
        niveaux.append((f"{10 + i} + {5 + i}", (10 + i) + (5 + i), "Additionne les unités puis les dizaines !"))
    for i in range(1, 16):
        niveaux.append((f"{30 - i} - 2", (30 - i) - 2, "Recule doucement sur la ligne des nombres."))
    for i in range(1, 16):
        niveaux.append((f"{i} x 2", i * 2, "Multiplier par 2, c'est trouver le double !"))
    for i in range(1, 16):
        niveaux.append((f"{i} x 5", i * 5, "Les résultats se terminent toujours par 0 ou 5."))
    for i in range(1, 16):
        niveaux.append((f"{5 + i} + {i} + 2", (5 + i) + i + 2, "Regroupe les nombres faciles en premier."))
    for i in range(1, 16):
        niveaux.append((f"40 - {i}", 40 - i, "Compte à rebours à partir de 40."))
    for i in range(1, 16):
        niveaux.append((f"{i} x 10", i * 10, "Ajoute simplement un zéro à droite du nombre !"))
    for i in range(1, 16):
        if i == 15:
            niveaux.append(("100 - 35", 65, "🔥 LE BOSS FINAL ! Enlève 30, puis encore 5 !"))
        else:
            niveaux.append((f"{50 + i} - 15", (50 + i) - 15, "Enlève 10, puis enleve 5."))
    return niveaux

# Initialisation des variables cachées de Streamlit
if "niveau_actuel" not in st.session_state:
    st.session_state.niveau_actuel = 1
if "questions_fr" not in st.session_state:
    st.session_state.questions_fr = []

# ========================================== #
#            INTERFACE DU SITE               #
# ========================================== #

st.title("🤖 BIENVENUE DANS CHATIA")
st.write("Choisis une activité dans le menu de gauche 👈")

menu = st.sidebar.radio(
    "Menu Principal",
    ["Accueil", "🏆 calcul-GAME", "🧮 Super Calculatrice", "📚 Cours & Quiz de Maths", "🇫🇷 Cours de Français", "🔐 Générateur de Mot de Passe"]
)

# --- ACCUEIL ---
if menu == "Accueil":
    st.subheader("💬 Discute avec ChatIA !")
    texte_libre = st.text_input("Écris quelque chose à ton IA :")
    
    if texte_libre:
        texte_propre = nettoyer_texte(texte_libre)
        
        if "bonjour" in texte_propre or "salut" in texte_propre or "hello" in texte_propre:
            st.success("🤖 Salut à toi ! Prêt à faire chauffer tes neurones aujourd'hui ?")
        elif "ca va" in texte_propre or "comment tu vas" in texte_propre:
            st.success("🤖 Je vais super bien ! Mes circuits électroniques tournent à fond. Et toi ?")
        elif "tu fais quoi" in texte_propre:
            st.success("🤖 Je t'attends pour jouer ! Tu as testé le jeu calcul-GAME dans le menu à gauche ?")
        elif "quel age" in texte_propre or "ton age" in texte_propre:
            st.success("🤖 Je suis né il y a seulement quelques jours dans ton code Python ! Je suis un bébé robot super intelligent.")
        elif "qui t a cree" in texte_propre or "ton createur" in texte_propre:
            st.success("🤖 C'est le grand développeur Leopold ! Il a écrit mes lignes de code pour me donner vie.")
        elif "merci" in texte_propre:
            st.success("🤖 De rien ! C'est un plaisir de t'aider.")
        elif "blague" in texte_propre:
            blagues = [
                "Pourquoi les robots n'ont-ils jamais peur ? Parce qu'ils ont des nerfs d'acier ! 🤖",
                "Qu'est-ce qu'un ordinateur qui fait de la musique ? Un disque dur ! 🎵",
                "Que fait un geek quand il a froid ? Il ferme les fenêtres de Windows ! 🪟"
            ]
            st.success(f"🤖 {random.choice(blagues)}")
        elif "calculatrice" in texte_propre or "calcul" in texte_propre:
            st.info("🤖 Pour faire des calculs libres, utilise la 'Super Calculatrice' dans le menu de gauche !")
        else:
            st.success("🤖 Intéressant ! Je ne connais pas encore cette phrase, mais je la retiens.")

# --- JEU CALCUL-GAME ---
elif menu == "🏆 calcul-GAME":
    st.subheader("🏆 calcul-GAME : Le défi des 120 niveaux")
    liste_niveaux = generer_niveaux_game()
    total_niveaux = len(liste_niveaux)
    
    if st.session_state.niveau_actuel <= total_niveaux:
        intitule, solution, astuce = liste_niveaux[st.session_state.niveau_actuel - 1]
        st.info(f"🌟 **NIVEAU {st.session_state.niveau_actuel} / {total_niveaux}** | Combien font : **{intitule}** ?")
        saisie_game = st.text_input("Ta réponse :", key=f"game_{st.session_state.niveau_actuel}")
        if st.button("Valider la réponse"):
            if saisie_game.strip():
                try:
                    reponse = int(saisie_game.strip())
                    if reponse == solution:
                        st.balloons()
                        st.success("🎉 EXCELLENT ! Bonne réponse ! Clique à nouveau pour passer au niveau suivant.")
                        st.session_state.niveau_actuel += 1
                    else:
                        st.error(f"❌ Ce n'est pas ça. Indice : {astuce}")
                except ValueError:
                    st.warning("Oups ! Écris ta réponse avec des chiffres.")
    else:
        st.success("🥇 FÉLICITATIONS ! TU AS FINI LES 120 NIVEAUX ! 🥇")
        if st.button("Recommencer le jeu"):
            st.session_state.niveau_actuel = 1

# --- SUPER CALCULATRICE ---
elif menu == "🧮 Super Calculatrice":
    st.subheader("🧮 Super Calculatrice Libre")
    expression = st.text_input("Entrez votre calcul :")
    if expression:
        try:
            if not all(c in "0123456789+-*/.()" for c in expression.replace(" ", "")):
                st.error("Erreur : Caractères non autorisés.")
            else:
                st.success(f"Résultat : {eval(expression)}")
        except ZeroDivisionError:
            st.error("Erreur : Division par zéro impossible.")
        except Exception:
            st.error("Erreur : Calcul invalide.")

# --- COURS ET QUIZ MATHS ---
elif menu == "📚 Cours & Quiz de Maths":
    st.subheader("📚 Cours & Quiz de Maths")
    choix_maths = st.selectbox("Que veux-vous faire ?", ["Choisir...", "1. Leçon sur les priorités", "2. Quiz de Calcul Mental"])
    if choix_maths == "1. Leçon sur les priorités":
        st.markdown("### 📖 LEÇON : Les priorités opératoires (PEMDAS)")
        st.write("On effectue TOUJOURS les multiplications et les divisions AVANT les additions et les soustractions.")
        rep1 = st.text_input("🔴 Test : Combien font 10 - 4 / 2 ?")
        if rep1:
            try:
                if int(rep1) == 8:
                    st.success("Excellent ! 🌟")
                else:
                    st.error("Faux ! La division était prioritaire. 4 / 2 = 2, puis 10 - 2 = 8.")
            except ValueError:
                st.warning("Écris un nombre !")
    elif choix_maths == "2. Quiz de Calcul Mental":
        if "quiz_maths_questions" not in st.session_state:
            questions = []
            for _ in range(5):
                a, b = random.randint(1, 12), random.randint(1, 12)
                op = random.choice(["+", "-", "*"])
                sol = a + b if op == "+" else (a - b if op == "-" else a * b)
                questions.append((a, op, b, sol))
            st.session_state.quiz_maths_questions = questions
        for idx, (a, op, b, sol) in enumerate(st.session_state.quiz_maths_questions):
            rep = st.text_input(f"Question {idx+1} : Combien font {a} {op} {b} ?", key=f"qmath_{idx}")
            if rep:
                try:
                    if int(rep) == sol: st.caption("Correct ! ✨")
                    else: st.caption(f"Faux (réponse: {sol})")
                except ValueError: pass
        if st.button("Générer un nouveau Quiz"):
            del st.session_state.quiz_maths_questions

# --- COURS DE FRANÇAIS ---
elif menu == "🇫🇷 Cours de Français":
    st.subheader("🇫🇷 Cours de Français")
    st.markdown("**Le présent des verbes en -ER :** Je **-e**, Tu **-es**, Il **-e**, Nous **-ons**, Vous **-ez**, Ils **-ent**.")
    if not st.session_state.questions_fr:
        base_questions = [
            {"v": "manger", "p": "Nous", "f": "ons", "ph": "Nous mangeons"},
            {"v": "jouer", "p": "Tu", "f": "es", "ph": "Tu joues"},
            {"v": "chanter", "p": "Ils", "f": "ent", "ph": "Ils chantent"}
        ]
        random.shuffle(base_questions)
        st.session_state.questions_fr = base_questions
    for idx, q in enumerate(st.session_state.questions_fr):
        rep = st.text_input(f"Question {idx+1} : ({q['v']}) -> {q['p']} ...... ?", key=f"qfr_{idx}").strip().lower()
        verbe_complet = q['ph'].split()[-1].lower()
        if rep:
            if rep == q['f'] or rep == verbe_complet: st.caption("Excellent ! ✨")
            else: st.caption(f"La phrase correcte : {q['ph']}")
    if st.button("Recommencer le Quiz de Français"):
        st.session_state.questions_fr = []

# --- GÉNÉRATEUR DE MOT DE PASSE ---
elif menu == "🔐 Générateur de Mot de Passe":
    st.subheader("🔐 Générateur de Mot de Passe Sécurisé")
    longueur = st.number_input("Longueur du mot de passe (minimum 4) :", min_value=4, value=8)
    if st.button("Générer"):
        chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
        mp = [secrets.choice(string.ascii_lowercase), secrets.choice(string.ascii_uppercase), secrets.choice(string.digits), secrets.choice("!@#$%^&*()-_=+")]
        for _ in range(int(longueur) - 4): mp.append(secrets.choice(chars))
