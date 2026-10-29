import streamlit as st, random
st.set_page_config(page_title="ChatIA Pro", page_icon="🤖")

if "nv" not in st.session_state: st.session_state.nv = 1
if "users" not in st.session_state: st.session_state.users = {"leopold": "1234"}
if "user" not in st.session_state: st.session_state.user = None
if "mem" not in st.session_state: st.session_state.mem = {}

clean = lambda t: "".join(c for c in t.lower() if c.isalnum() or c.isspace()).strip()

st.sidebar.title("🔐 Espace Membre")
if st.session_state.user is None:
    act = st.sidebar.selectbox("Action", ["Se connecter", "Créer un compte"])
    p = st.sidebar.text_input("Pseudo")
    m = st.sidebar.text_input("Mot de passe", type="password")
    if st.sidebar.button("Valider"):
        if act == "Se connecter" and st.session_state.users.get(p) == m:
            st.session_state.user = p
            st.rerun()
        elif act == "Créer un compte" and p.strip() and p not in st.session_state.users:
            st.session_state.users[p] = m
            st.sidebar.success("Compte créé !")
        else: st.sidebar.error("Erreur")
else:
    st.sidebar.write(f"🟢 Connecté : **{st.session_state.user}**")
    if st.sidebar.button("Déconnexion"): st.session_state.user = None; st.rerun()

menu = st.sidebar.radio("Menu", ["Accueil", "🧠 Lui apprendre des choses", "🏆 calcul-GAME", "🧮 Calculatrice"])

if menu == "Accueil":
    st.title(f"🤖 ChatIA ({st.session_state.user or 'Invité'})")
    txt = st.text_input("Discute avec l'IA :")
    if txt:
        t = clean(txt)
        if "bonjour" in t or "salut" in t: st.success("🤖 Salut ! Prêt à jouer avec moi ?")
        elif "ca va" in t: st.success("🤖 Tout tourne parfaitement dans mes circuits ! Et toi ?")
        elif "qui t a cree" in t: st.success("🤖 C'est le grand développeur Leopold qui a écrit mon code !")
        elif "blague" in t: st.success(f"🤖 {random.choice(['Pourquoi les robots n\'ont pas peur ? Ils ont des nerfs d\'acier !', 'Qu\'est-ce qu\'un ordinateur qui chante ? Un disque dur !'])}")
        elif t in st.session_state.mem: st.success(f"🤖 {st.session_state.mem[t]}")
        else: st.warning("🤖 Je ne sais pas ! Va dans 'Lui apprendre des choses' pour m'aider !")

elif menu == "🧠 Lui apprendre des choses":
    st.title("🧠 Apprentissage")
    q_in = st.text_input("Quand j'écris (ex: couleur preferee) :")
    r_in = st.text_input("Tu dois répondre :")
    if st.button("Enregistrer") and q_in.strip() and r_in.strip():
        st.session_state.mem[clean(q_in)] = r_in
        st.success("🧠 Enregistré ! Teste ta phrase sur l'Accueil !")

elif menu == "🏆 calcul-GAME":
    st.title("🏆 calcul-GAME")
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

elif menu == "🧮 Calculatrice":
    st.title("🧮 Calculatrice")
    c = st.text_input("Entre ton calcul :")
    if c and all(char in "0123456789+-*/.()" for char in c.replace(" ", "")):
        try: st.success(f"Résultat : {eval(c)}")
        except: st.error("Calcul invalide.")
