# Puissance 4 — IA en Python

Implémentation du Puissance 4 avec plusieurs algorithmes d'intelligence artificielle : Minimax, Alpha-Beta et MCTS.

---

## Algorithmes IA

- **Minimax** — explore l'arbre de jeu en anticipant les coups adverses, maximise le score du joueur courant et minimise celui de l'adversaire
- **Alpha-Beta** — version optimisée de Minimax qui élagage les branches non prometteuses, réduisant drastiquement le nombre de noeuds explorés
- **MCTS (Monte Carlo Tree Search)** — simule des parties aléatoires pour estimer la valeur de chaque coup, sans nécessiter de fonction d'évaluation explicite

---

## Structure

```
├── ai/           # Implémentation des algorithmes (Minimax, Alpha-Beta, MCTS)
├── game/         # Logique du jeu (plateau, règles, détection de victoire)
├── interface/    # Interface graphique
├── tests/        # Tests unitaires
├── main.py       # Point d'entrée
└── requirements.txt
```

---

## Installation & Lancement

```bash
pip install -r requirements.txt
python main.py
```

---

## Prérequis

- Python 3.8+
