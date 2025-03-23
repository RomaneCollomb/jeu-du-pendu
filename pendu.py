import random

def pendu():
    # Liste de mots pour le jeu
    words = ['chat', 'chien', 'lapin', 'oiseau', 'girafe', 'koala']
    
    # Choisir un mot au hasard
    mot_a_deviner = random.choice(words)
    mot_deviné = ['_'] * len(mot_a_deviner)
    
    tentatives = 6  # Nombre de tentatives
    lettres_proposees = []

    print("Bienvenue dans le jeu du Pendu!")
    print("Le mot à deviner est : " + ' '.join(mot_deviné))
    
    # Boucle principale du jeu
    while tentatives > 0:
        proposition = input(f"Il vous reste {tentatives} tentatives. Entrez une lettre : ").lower()

        # Vérifier si l'utilisateur a déjà deviné la lettre
        if proposition in lettres_proposees:
            print(f"Vous avez déjà deviné la lettre '{proposition}'. Essayez une autre.")
            continue
        
        # Ajouter la lettre devinée à la liste des lettres déjà devinées
        lettres_proposees.append(proposition)

        # Vérifier si la lettre devinée est dans le mot
        if proposition in mot_a_deviner:
            print(f"Bien joué! La lettre '{proposition}' est dans le mot.")
            for i in range(len(mot_a_deviner)):
                if mot_a_deviner[i] == proposition:
                    mot_deviné[i] = proposition
        else:
            tentatives -= 1
            print(f"Désolé! La lettre '{proposition}' n'est pas dans le mot.")
        
        # Afficher l'état actuel du mot deviné
        print("Mot à deviner : " + ' '.join(mot_deviné))
        
        # Vérifier si le joueur a deviné le mot
        if ''.join(mot_deviné) == mot_a_deviner:
            print(f"Félicitations! Vous avez deviné le mot '{mot_a_deviner}'!")
            break
    else:
        print(f"Vous avez perdu! Le mot était '{mot_a_deviner}'.")

if __name__ == "__main__":
    pendu()
