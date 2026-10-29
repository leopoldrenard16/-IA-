import streamlit as st, random, secrets, string
st.set_page_config(page_title="ChatIA Pro", page_icon="🤖")

# --- ASTUCE POUR QUE LES COMPTES ET LA MÉMOIRE S'ENREGISTRENT POUR TOUJOURS ---
@st.cache_resource
def obtenir_base_de_donnees():
    return {
        "users": {"leopold": "1234"}, # Base des comptes enregistrés
        "mem": {} # Mémoire de l'IA à long terme
    }

db = obtenir_base_de_donnees()

# --- INITIALISATION DES AUTRES VARIABLES ---
if "nv" not in st.session_state: st.session_state.nv = 1
if "user" not in st.session_state: st.session_state.user = None
if "q_fr" not in st.session_state:
    fr = [{"v": "manger", "p": "Nous", "f": "ons", "ph": "Nous mangeons"}, {"v": "jouer", "p": "Tu", "f": "es", "ph": "Tu joues"}, {"v": "chanter", "p": "Ils", "f": "ent", "ph": "Ils chantent"}]
    random.shuffle(fr); st.session_state.q_fr = fr
if "nombre_mystere" not in st.session_state:
    st.session_state.nombre_mystere = random.randint(1, 100)

clean = lambda t: "".join(c for c in t.lower() if c.isalnum() or c.isspace()).strip()

# --- ESPACE CONNEXION ---
st.sidebar.title("🔐 Espace Membre")
if st.session_state.user is None:
    act = st.sidebar.selectbox("Action", ["Se connecter", "Créer un compte"])
    p = st.sidebar.text_input("Pseudo")
    m = st.sidebar.text_input("Mot de passe", type="password")
    if st.sidebar.button("Valider"):
        if act == "Se connecter" and db["users"].get(p) == m:
            st.session_state.user = p; st.rerun()
        elif act == "Créer un compte" and p.strip() and p not in db["users"]:
            db["users"][p] = m; st.sidebar.success("Compte créé et enregistré !")
        else: st.sidebar.error("Erreur")
else:
    st.sidebar.write(f"🟢 Connecté : **{st.session_state.user}**")
    if st.sidebar.button("Déconnexion"): st.session_state.user = None; st.rerun()

menu = st.sidebar.radio("Menu", ["Accueil", "🧠 Apprentissage", "🎰 Machine à nombre", "🏆 calcul-GAME", "🧮 Calculatrice", "📚 Quiz Maths", "🇫🇷 Quiz Français", "🔐 Mot de passe"])

# --- ACCUEIL ---
if menu == "Accueil":
    st.title(f"🤖 ChatIA ({st.session_state.user or 'Invité'})")
    txt = st.text_input("Discute avec l'IA :")
    if txt:
        t = clean(txt)
        if "bonjour" in t or "salut" in t: st.success("🤖 Salut ! Prêt à jouer avec moi ?")
        elif "ca va" in t: st.success("🤖 Tout tourne parfaitement dans mes circuits ! Et toi ?")
        elif "qui t a cree" in t: st.success("🤖 C'est le grand développeur Leopold qui a écrit mon code !")
        elif "blague" in t: st.success(f"🤖 {random.choice(['Pourquoi les robots n\'ont pas peur ? Ils ont des nerfs d\'acier !', 'Qu\'est-ce qu\'un ordinateur qui chante ? Un disque dur !'])}")
        elif t in db["mem"] and st.session_state.user is not None:
            # L'IA ne répond avec sa mémoire QUE si on est connecté (pas en invité)
            st.success(f"🤖 {db['mem'][t]}")
        else: st.warning("🤖 Je ne sais pas ! Va dans 'Apprentissage' pour m'aider (connecte-toi d'abord) !")

# --- APPRENTISSAGE ---
elif menu == "🧠 Apprentissage":
    st.title("🧠 Apprentissage")
    if st.session_state.user is None:
        st.error("⚠️ Tu dois te connecter à un compte à gauche pour pouvoir apprendre des choses à l'IA !")
    else:
        st.write(f"En tant que membre connecté (**{st.session_state.user}**), tu peux donner de la mémoire à l'IA.")
        q_in = st.text_input("Quand j'écris (ex: couleur preferee) :")
        r_in = st.text_input("Tu dois répondre :")
        if st.button("Enregistrer") and q_in.strip() and r_in.strip():
            db["mem"][clean(q_in)] = r_in; st.success("🧠 Enregistré pour toujours ! Même si tu recharges la page, je m'en souviendrai !")

# --- LA GRANDE MACHINE À NOMBRE ---
elif menu == "🎰 Machine à nombre":
    st.code("01001010101010101010101000000101010100110010")
    st.subheader("🎰 LA GRANDE MACHINE A NOMBRE 🎰")
    st.code("01010101011010101010100111001010101110101001")
    st.write("Devine le nombre que j'ai en tête entre 1 et 100 !")
    bonjour = st.number_input("Ta proposition :", min_value=1, max_value=100, step=1, value=50)
    if st.button("Lancer la machine"):
        chifre = st.session_state.nombre_mystere
        if bonjour == chifre:
            st.balloons(); st.success("🎉 Bravo, tu as trouvé ! La grande machine s'est arrêtée.")
            st.session_state.nombre_mystere = random.randint(1, 100)
        else:
            st.error(f"❌ Dommage, ce n'est pas ça ! Le nombre mystère change...")
            st.session_state.nombre_mystere = random.randint(1, 100)

# --- JEU CALCUL-GAME ---
elif menu == "🏆 calcul-GAME":
    st.title("🏆 calcul-GAME (120 Niveaux)")
    if st.session_state.nv <= 120:
        n = st.session_state.nv
        exp = f"{10+n} + {5+n}" if n <= 30 else (f"{60-n} - 2" if n <= 60 else f"{n-60} * 2")
        st.info(f"🌟 **NIVEAU {n} / 120** | Combien font : **{exp}** ?")
        rep = st.text_input("Ta réponse :", key=f"g{n}")
        if st.button("Valider"):
            if rep.strip() and int(rep.strip()) == eval(exp):
                st.balloons(); st.success("🎉 Bravo !"); st.session_state.nv += 1
            else: st.error("❌ Ce n'est pas ça !")
    else: st.success("🥇 TU AS FINI LES 120 NIVEAUX !"); st.session_state.nv = 1

# --- CALCULATRICE ---
elif menu == "🧮 Calculatrice":
    st.title("🧮 Super Calculatrice")
    c = st.text_input("Entre ton calcul :")
    if c and all(char in "0123456789+-*/.()" for char in c.replace(" ", "")):
        try: st.success(f"Résultat : {eval(c)}")
        except: st.error("Calcul invalide.")

# --- QUIZ MATHS ---
elif menu == "📚 Quiz Maths":
    st.title("📚 Cours & Quiz Maths")
    st.write("📖 **PEMDAS :** On fait toujours `*` et `/` AVANT `+` et `-` !")
    rep1 = st.text_input("🔴 Combien font 10 - 4 / 2 ?")
    if rep1 and rep1.strip() == "8": st.success("Excellent ! 🌟")
    elif rep1: st.error("Faux ! La division était prioritaire.")

# --- QUIZ FRANÇAIS ---
elif menu == "🇫🇷 Quiz Français":
    st.title("🇫🇷 Cours & Quiz Français")
    st.write("**Présent des verbes en -ER :** Je -e, Tu -es, Il -e, Nous -ons, Vous -ez, Ils -ent.")
    for idx, q in enumerate(st.session_state.q_fr):
        rep = st.text_input(f"Question {idx+1} : ({q['v']}) -> {q['p']} ...... ?", key=f"f{idx}").strip().lower()
        if rep:
            if rep == q['f'] or rep == q['ph'].split()[-1].lower(): st.caption("Excellent ! ✨")
            else: st.caption(f"La phrase correcte est : {q['ph']}")

# --- MOT DE PASSE ---
elif menu == "🔐 Mot de passe":
    st.title("🔐 Générateur de Mot de Passe")
    longueur = st.number_input("Longueur (minimum 4) :", min_value=4, value=8)
    if st.button("Générer"):
        chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
        mp = [secrets.choice(string.ascii_lowercase), secrets.choice(string.ascii_uppercase), secrets.choice(string.digits), secrets.choice("!@#$%^&*()-_=+")]
        for _ in range(int(longueur) - 4): mp.append(secrets.choice(chars))
        random.shuffle(mp); st.success(f"Ton mot de passe : `{''.join(mp)}`")
