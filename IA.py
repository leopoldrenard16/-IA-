import random
import secrets
import string

# ========================================== #
# # FONCTIONS ET MODULES #
# ========================================== #

def nettoyer_texte(texte):
    """Met le texte en minuscules et retire la ponctuation de base sans coller les mots."""
    texte = texte.lower()
    for char in [".", ",", "?", "!", "-", "_", ";", ":", "'"]:
        texte = texte.replace(char, " ") # Remplace par un espace pour ne pas coller les mots
    return " ".join(texte.split()) # Supprime les espaces doubles

def generer_niveaux_game():
    """Génère la liste des 120 niveaux pour calcul-GAME."""
    niveaux = []
    # NIVEAUX 1 À 30
    for i in range(1, 16):
        niveaux.append((f"{10 + i} + {5 + i}", (10 + i) + (5 + i), "Additionne les unités puis les dizaines !"))
    for i in range(1, 16):
        niveaux.append((f"{30 - i} - 2", (30 - i) - 2, "Recule doucement sur la ligne des nombres."))
    
    # NIVEAUX 31 À 60
    for i in range(1, 16):
        niveaux.append((f"{i} x 2", i * 2, "Multiplier par 2, c'est trouver le double !"))
    for i in range(1, 16):
        niveaux.append((f"{i} x 5", i * 5, "Les résultats se terminent toujours par 0 ou 5."))
        
    # NIVEAUX 61 À 90
    for i in range(1, 16):
        niveaux.append((f"{5 + i} + {i} + 2", (5 + i) + i + 2, "Regroupe les nombres faciles en premier."))
    for i in range(1, 16):
        niveaux.append((f"40 - {i}", 40 - i, "Compte à rebours à partir de 40."))
        
    # NIVEAUX 91 À 120
    for i in range(1, 16):
        niveaux.append((f"{i} x 10", i * 10, "Ajoute simplement un zéro à droite du nombre !"))
    for i in range(1, 16):
        if i == 15:
            niveaux.append(("100 - 35", 65, "🔥 LE BOSS FINAL ! Enlève 30, puis encore 5 !"))
        else:
            niveaux.append((f"{50 + i} - 15", (50 + i) - 15, "Enlève 10, puis enleve 5."))
    return niveaux

def calcul_game():
    """Le grand défi des 120 niveaux."""
    liste_niveaux = generer_niveaux_game()
    total_niveaux = len(liste_niveaux)
    niveau_actuel = 1
    print("\n==================== 🏆 BIENVENUE DANS LE JEU : calcul-GAME 🏆 =====================")
    print("Trouve la réponse par toi-même et tape-la sur ton clavier.")
    print("(Tapez 'quitter' pour revenir sur ChatIA)\n")
    
    while niveau_actuel <= total_niveaux:
        intitule, solution, astuce = liste_niveaux[niveau_actuel - 1]
        print(f"🌟 NIVEAU {niveau_actuel} / {total_niveaux} | Combien font : {intitule} ?")
        
        while True:
            saisie = input("Ta réponse : ").strip()
            if saisie.lower() == "quitter":
                return
            try:
                reponse = int(saisie)
                break
            except ValueError:
                print("Oups ! Écris ta réponse avec des chiffres.")
                
        if reponse == solution:
            print("🎉 EXCELLENT ! Bonne réponse ! Niveau suivant.\n")
            niveau_actuel += 1
        else:
            print(f"❌ Ce n'est pas ça. Indice : {astuce}\n")
            
    print("🥇 FÉLICITATIONS ! TU AS FINI LES 120 NIVEAUX ! 🥇\n")

def super_calculatrice():
    """Lance directement la calculatrice libre."""
    print("\n--- MODE CALCULATRICE --- (Tapez 'quitter' pour sortir)")
    while True:
        expression = input("Entrez votre calcul : ")
        if expression.strip().lower() == "quitter":
            print("Fermeture de la calculatrice.\n")
            break
        try:
            if not all(c in "0123456789+-*/.()" for c in expression.replace(" ", "")):
                print("Erreur : Caractères non autorisés.")
                continue
            print(f"Résultat : {eval(expression)}")
        except ZeroDivisionError:
            print("Erreur : Division par zéro impossible.")
        except Exception:
            print("Erreur : Calcul invalide.")

def menu_maths():
    """Menu pour les cours et quiz de maths."""
    print("\n==================== BIENVENUE DANS LE COURS DE MATHS DE ChatIA =====================")
    print("1. Suivre la leçon sur les priorités de calcul")
    print("2. Lancer le Quiz de Calcul Mental")
    print("3. Lancer le jeu calcul-GAME")
    choix = input("\nQue voulez-vous faire ? (1, 2 ou 3) : ").strip()
    
    if choix == "1":
        print("\n📖 LEÇON : Les priorités opératoires (PEMDAS)")
        print("Dans un calcul sans parenthèses, on effectue TOUJOURS les multiplications")
        print("et les divisions AVANT les additions et les soustractions.")
        print("Exemple : 5 + 2 * 3 = ? -> 2 * 3 = 6, puis 5 + 6 = 11.")
        try:
            rep1 = input("\n🔴 Test : Combien font 10 - 4 / 2 ? ")
            if int(rep1) == 8:
                print("Excellent ! 🌟")
            else:
                print("Faux ! La division était prioritaire. 4 / 2 = 2, puis 10 - 2 = 8.")
        except ValueError:
            print("Entrée invalide.")
            
    elif choix == "2":
        print("\n--- MODE QUIZ DE MATHS (5 questions) ---")
        score = 0
        for i in range(1, 6):
            a, b = random.randint(1, 12), random.randint(1, 12)
            op = random.choice(["+", "-", "*"])
            sol = a + b if op == "+" else (a - b if op == "-" else a * b)
            try:
                rep = input(f"Question {i} : Combien font {a} {op} {b} ? ")
                if int(rep) == sol:
                    print("Bravo ! 🌟")
                    score += 1
                else:
                    print(f"Dommage... La réponse était {sol}.")
            except ValueError:
                print(f"Ce n'est pas un nombre ! La réponse était {sol}.")
        print(f"\n📚 Score : {score}/5")
        
    elif choix == "3":
        calcul_game()

def cours_de_francais():
    print("\n==================== BIENVENUE DANS LE COURS DE FRANÇAIS DE ChatIA =====================")
    print("Le présent des verbes en -ER : Je -e, Tu -es, Il -e, Nous -ons, Vous -ez, Ils -ent.")
    input("\nAppuyez sur Entrée pour démarrer le Quiz... ")
    
    questions = [
        {"v": "manger", "p": "Nous", "f": "ons", "ph": "Nous mangeons"},
        {"v": "jouer", "p": "Tu", "f": "es", "ph": "Tu joues"},
        {"v": "chanter", "p": "Ils", "f": "ent", "ph": "Ils chantent"},
        {"v": "aimer", "p": "J'", "f": "e", "ph": "J'aime"},
        {"v": "regarder", "p": "Vous", "f": "ez", "ph": "Vous regardez"}
    ]
    random.shuffle(questions)
    score = 0
    
    for i, q in enumerate(questions, 1):
        rep = input(f"\nQuestion {i} : ({q['v']}) -> {q['p']} ...... ? ").strip().lower()
        
        # Le verbe complet attendu (ex: "mangeons", "joues") se trouve à la fin de la phrase exemple
        verbe_complet = q['ph'].split()[-1].lower()
        
        # On valide si l'utilisateur donne la bonne terminaison seule OU le verbe complet correctement conjugué
        if rep == q['f'] or rep == verbe_complet:
            print("Excellent ! ✨")
            score += 1
        else:
            print(f"Dommage... La phrase correcte est : {q['ph']}")
            
    print(f"\n📝 Score : {score}/5")

def generateur_mot_de_passe():
    print("\n--- Générateur de Mot de Passe Sécurisé ---")
    try:
        saisie = input("Longueur (minimum 4) : ")
        longueur = int(saisie)
        if longueur < 4:
            print("Erreur : Minimum 4.")
            return
            
        chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
        mp = [
            secrets.choice(string.ascii_lowercase),
            secrets.choice(string.ascii_uppercase),
            secrets.choice(string.digits),
            secrets.choice("!@#$%^&*()-_=+")
        ]
        for _ in range(longueur - 4):
            mp.append(secrets.choice(chars))
        random.shuffle(mp)
        print(f"Votre mot de passe : {''.join(mp)}\n")
    except ValueError:
        print("Erreur de saisie.\n")

# ========================================== #
# # BOUCLE PRINCIPALE DU CHATBOT #
# ========================================== #

print("==================================================")
print("BIENVENUE DANS CHATIA")
print("Tapez 'quitter' pour fermer le programme.")
print("==================================================")

while True:
    user_input = input("\nVous : ")
    if not user_input.strip():
        continue
        
    prompt = nettoyer_texte(user_input)
    
    if prompt in ["quitter", "exit", "quit"]:
        print("\nIA : Au revoir !")
        break
        
    # ACCÈS DIRECT AU JEU
    if any(m in prompt for m in ["jeu", "game", "calcul game", "calculgame"]):
        calcul_game()
        continue
        
    # LANCE DIRECTEMENT LA CALCULATRICE
    if any(m in prompt for m in ["calcul", "calculatrice"]):
        super_calculatrice()
        continue
        
    # LANCE LE COURS / MENU DE MATHS
    if any(m in prompt for m in ["math", "maths", "cours de math", "cours de maths"]):
        menu_maths()
        continue
        
    if any(m in prompt for m in ["francais", "conjugaison", "cours de francais", "conjuguer"]):
        cours_de_francais()
        continue
        
    if any(m in prompt for m in ["mot de passe", "generateur", "pass", "pwd"]):
        generateur_mot_de_passe()
        continue
        
    if "comment tu fonctionne" in prompt or "intelligence artificielle fonctionne" in prompt:
        print("IA : L'intelligence artificielle (IA) fonctionne en analysant de grandes quantités de données grâce à des algorithmes et à des modèles mathématiques, sans posséder de conscience ou de vraie réflexion.")
        continue
        
    # RÉPONSES AUX PETITS MOTS ET POLITESSE
    if any(m in prompt for m in ["bonjour", "salut", "hello", "coucou", "hey"]):
        print("IA : " + random.choice(["Bonjour !", "Salut !", "Hello !"]))
    elif any(m in prompt for m in ["comment ca va", "comment va", "ca va", "tu vas bien"]):
        print("IA : Mon code tourne à merveille ! Et vous ?")
