from game.puissance4 import Puissance4
from ai.minimax import minimax
from ai.alphabeta import alpha_beta
from ai.mcts import mcts
import sys

def afficher_grille_et_resultat(jeu):
    jeu.afficher_grille()
    if jeu.est_victoire():
        print(f"Victoire du joueur {jeu.joueur_actuel} !")
        return True
    elif jeu.est_pleine():
        print("Match nul !")
        return True
    return False

def jouer_joueur_vs_joueur():
    jeu = Puissance4()
    print("\n--- Joueur vs Joueur ---")
    while True:
        jeu.afficher_grille()
        try:
            col = int(input(f"Joueur {jeu.joueur_actuel}, choisissez une colonne (0-6) : "))
        except ValueError:
            print("Veuillez entrer un nombre.")
            continue

        if not jeu.jouer(col):
            print("Coup invalide. Réessayez.")
            continue

        if afficher_grille_et_resultat(jeu):
            break

        jeu.changer_joueur()

def jouer_joueur_vs_ia(choix_ia):
    jeu = Puissance4()
    print("\n--- Joueur vs IA ---")
    while True:
        jeu.afficher_grille()
        if jeu.joueur_actuel == 'X':
            try:
                col = int(input("Votre coup (0-6) : "))
            except ValueError:
                print("Nombre invalide.")
                continue
        else:  # IA joue avec O
            print("IA réfléchit...")
            if choix_ia == "1":
                col = minimax(jeu, max_profondeur=4)
            elif choix_ia == "2":
                col = alpha_beta(jeu, max_profondeur=4)
            elif choix_ia == "3":
                col = mcts(jeu, budget=1000)
            else:
                print("IA non reconnue.")
                col = 0
                break

        if not jeu.jouer(col):
            print("Coup invalide.")
            continue

        if afficher_grille_et_resultat(jeu):
            break

        jeu.changer_joueur()

def jouer_ia_vs_ia(choix_ia1, choix_ia2):
    jeu = Puissance4()
    print(f"\n--- IA vs IA ---")

    # PARAMÈTRES IA 1 (X)
    if choix_ia1 == "1" or choix_ia1 == "2":
        profondeur_ia1 = int(input("Profondeur pour IA 1 (X) : "))
        budget_ia1 = None
    elif choix_ia1 == "3":
        budget_ia1 = int(input("Budget de simulations pour MCTS IA 1 (X) : "))
        profondeur_ia1 = None

    # PARAMÈTRES IA 2 (O)
    if choix_ia2 == "1" or choix_ia2 == "2":
        profondeur_ia2 = int(input("Profondeur pour IA 2 (O) : "))
        budget_ia2 = None
    elif choix_ia2 == "3":
        budget_ia2 = int(input("Budget de simulations pour MCTS IA 2 (O) : "))
        profondeur_ia2 = None

    print(f"IA 1 (X) = {'Minimax' if choix_ia1=='1' else 'Alpha-Beta' if choix_ia1=='2' else 'MCTS'}")
    print(f"IA 2 (O) = {'Minimax' if choix_ia2=='1' else 'Alpha-Beta' if choix_ia2=='2' else 'MCTS'}")

    while True:
        jeu.afficher_grille()
        print(f"[IA {jeu.joueur_actuel}] réfléchit...")

        if jeu.joueur_actuel == 'X':
            choix = choix_ia1
            profondeur = profondeur_ia1
            budget = budget_ia1
        else:
            choix = choix_ia2
            profondeur = profondeur_ia2
            budget = budget_ia2

        if choix == "1":
            col = minimax(jeu, max_profondeur=profondeur)
        elif choix == "2":
            col = alpha_beta(jeu, max_profondeur=profondeur)
        elif choix == "3":
            col, infos = mcts(jeu, budget=budget, collect_infos=True)
            print("[DEBUG MCTS] Infos arbre:", infos)
        else:
            print("IA non reconnue.")
            break

        if not jeu.jouer(col):
            print(f"[ERREUR] IA {jeu.joueur_actuel} a choisi une colonne invalide. Abandon.")
            break

        if afficher_grille_et_resultat(jeu):
            break

        jeu.changer_joueur()


def afficher_menu():
    print("\n--- Menu Puissance 4 ---")
    print("1. Joueur contre Joueur")
    print("2. Joueur contre IA")
    print("3. IA contre IA")
    print("0. Quitter")

def afficher_choix_ia():
    print("\n--- Choix de l'IA ---")
    print("1. Minimax")
    print("2. Alpha-Beta")
    print("3. MCTS")
    print("0. Retour")

def jouer_partie_console():
    while True:
        afficher_menu()
        choix = input("Choisissez une option : ")

        if choix == "1":
            jouer_joueur_vs_joueur()

        elif choix == "2":  # Joueur vs IA
            afficher_choix_ia()
            choix_ia = input("Choisissez votre IA : ")
            if choix_ia in ["1", "2", "3"]:
                jouer_joueur_vs_ia(choix_ia)
            else:
                print("Option IA invalide.")

        elif choix == "3":  # IA vs IA
            print("\nChoisir IA 1 :")
            afficher_choix_ia()
            choix_ia1 = input("Choisissez IA 1 : ")

            print("\nChoisir IA 2 :")
            afficher_choix_ia()
            choix_ia2 = input("Choisissez IA 2 : ")

            if choix_ia1 in ["1", "2", "3"] and choix_ia2 in ["1", "2", "3"]:
                jouer_ia_vs_ia(choix_ia1, choix_ia2)
            else:
                print("Option IA invalide.")

        elif choix == "0":
            print("Au revoir !")
            sys.exit(0)

        else:
            print("Option invalide.")
