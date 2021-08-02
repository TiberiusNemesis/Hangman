#Author: Tiberius Nemesis Dourado, 2021.2

import random
gallows = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def hangman(word):
        spaces = []
        mistakes = 0
        stored_guesses = []
        while mistakes <= 6:
            hit = 0
            print(gallows[mistakes], end="  ") #prints hangman and gallows
            for i in range(len(word)):
                if len(spaces) != len(word): #sets up _____'s if not setup already
                    spaces.append(word[i])
                    stored_guesses.append("_")
                print(stored_guesses[i],end="") #prints _________'s
            if stored_guesses == spaces:
                print(" was the word! \nYou win!")
                return()
            guess = input("\nGuess a letter: ")
            while not guess:
                guess = input("\nPlease enter your guess: ")
            guess = (guess[0:1]).lower()
            if guess not in stored_guesses:
                for i in range(len(word)): #checks if guess = any of the word's letters, if it is, sets hit to 1 to display "congrats! you got one right"
                    if guess == spaces[i]:
                        hit+=1
                        stored_guesses[i] = guess
                if hit == 0:
                    print(f'\nThere are no "{guess}"s.')
                    mistakes+=1
                else:
                    if hit == 1:
                        print(f'There is one "{guess}"! Good job.')
                    else:
                        print(f'\nThere are {hit} "{guess}"s! Nice.')
            else:
                print(f'You have already guessed {guess}! Try a different letter.')
        if mistakes > 5:
            print(gallows[6], end="  ")
            print(f'The word was {word}!\n You lose.')

gameState = "y"
while gameState == "y":
    word_list = ["inerente","peculiar","denegrir","respeito","genocida","sucinto","inferir","oriundo","contudo",
                 "austero","sensato","erudito","vigente","profano","hesitar","deferido","prudente","equidade",
                 "iminente","invasivo","pandemia","perspicaz","colapso","reiterar","alienado","abstrato","paradoxo",
                 "complexo","proceder","distinto","demagogo","alicerce","ativista","talarico","apologia","imparcial",
                 "inusitado","perspicaz","persuadir","vagabundo","mesquinho","impetuoso","cognitivo"," maturidade",
                 "precedente","subestimar","entretanto","significado","dissimulado","vicissitude","intensidade",
                 "integridade","austeridade","pragmatismo","subsequente","preconceito","facultativo","superestimar",
                 "literalmente","introvertido","eventualmente","peculiaridade","amor","bem","brasil","bom","brava",
                 "babaca","biodiversidade","danado","devasso","empatia","felicidade","gratuito","gentil","genocida",
                 "keynesianismo","lunar","luz","leviano","limiar","legado","linda","mito","marasmo","modesto",
                 "niilismo","nude","nobreza","negro","navio","namoro","oportunista","puta","quente","querida",
                 "queijo","sintomas","trem","urbano","zero","zoom"] #alter word list to whatever words you would like :)
    chosen_word = random.choice(word_list)
    hangman(chosen_word)
    gameState = (input("\nWould you like to play again? y/n\n")).lower()
