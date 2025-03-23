# Jeu du pendu - Python

Bienvenue dans le jeu du Pendu ! Ce projet consiste en un jeu interactif où l'utilisateur doit deviner un mot en proposant des lettres. À chaque mauvaise réponse, l'utilisateur perd une tentative. Le jeu se termine lorsque le joueur devine correctement le mot ou épuisé toutes ses tentatives.

## Description

Le jeu consiste à deviner un mot secret choisi aléatoirement parmi une liste de mots. Le joueur doit proposer des lettres et le jeu lui indiquera si la lettre fait partie du mot ou non. Le joueur a un maximum de 6 tentatives avant de perdre la partie.

### Fonctionnement

1. Le mot à deviner est choisi au hasard parmi une liste de mots prédéfinis.
2. Le joueur peut entrer une lettre à chaque tour.
3. Si la lettre est correcte, elle est ajoutée à la solution visible.
4. Si la lettre est incorrecte, une tentative est perdue.
5. Le jeu se termine lorsqu'un joueur devine le mot ou que le nombre d'essais est épuisé.

## Prérequis

- Python 3.x

## Comment jouer ?

1. Clonez ou téléchargez ce projet.
2. Exécutez le script Python : `python3 pendu.py`.
3. Suivez les instructions à l'écran.
4. Entrez une lettre à chaque tour jusqu'à ce que vous ayez trouvé le mot ou que vous ayez épuisé toutes vos tentatives.

## Exemple d'utilisation

```bash
Bienvenue dans le jeu du Pendu!
Le mot à deviner est : _ _ _ _

Il vous reste 6 tentatives. Entrez une lettre : c
Bien joué! La lettre 'c' est dans le mot.
Mot à deviner : c _ _ _

Il vous reste 6 tentatives. Entrez une lettre : h
Bien joué! La lettre 'h' est dans le mot.
Mot à deviner : c h _ _

...
```

## Auteur
Romane Collomb
