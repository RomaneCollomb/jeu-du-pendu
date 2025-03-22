import random

def hangman():
    # Liste de mots pour le jeu
    words = ['chat', 'chien', 'lapin', 'oiseau', 'girafe', 'koala']
    
    # Choisir un mot au hasard
    word_to_guess = random.choice(words)
    guessed_word = ['_'] * len(word_to_guess)
    
    attempts = 6  # Nombre de tentatives
    guessed_letters = []

    print("Bienvenue dans le jeu du Pendu!")
    print("Le mot à deviner est : " + ' '.join(guessed_word))
    
    # Boucle principale du jeu
    while attempts > 0:
        guess = input(f"Il vous reste {attempts} tentatives. Entrez une lettre : ").lower()

        # Vérifier si l'utilisateur a déjà deviné la lettre
        if guess in guessed_letters:
            print(f"Vous avez déjà deviné la lettre '{guess}'. Essayez une autre.")
            continue
        
        # Ajouter la lettre devinée à la liste des lettres déjà devinées
        guessed_letters.append(guess)

        # Vérifier si la lettre devinée est dans le mot
        if guess in word_to_guess:
            print(f"Bien joué! La lettre '{guess}' est dans le mot.")
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1
            print(f"Désolé! La lettre '{guess}' n'est pas dans le mot.")
        
        # Afficher l'état actuel du mot deviné
        print("Mot à deviner : " + ' '.join(guessed_word))
        
        # Vérifier si le joueur a deviné le mot
        if ''.join(guessed_word) == word_to_guess:
            print(f"Félicitations! Vous avez deviné le mot '{word_to_guess}'!")
            break
    else:
        print(f"Vous avez perdu! Le mot était '{word_to_guess}'.")

if __name__ == "__main__":
    hangman()
