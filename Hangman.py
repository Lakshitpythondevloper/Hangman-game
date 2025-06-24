import random
import Hangman_words
stages = [r'''
    ___________
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
    _|___
    
    ''',r'''
     ___________
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
    _|___''',r'''
    ___________
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
    _|___''', r'''
    ___________
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
    _|___''', r'''
    ___________
     |/      |
     |      (_)
     |      \|
     |       
     |     
     |
    _|___''',r'''
    ___________
     |/      |
     |      (_)
     |       |
     |       
     |      
     |
    _|___
          ''',r'''
    ___________
     |/      |
     |      (_)
     |       
     |      
     |
    _|___
          ''',r'''
    ___________
     |/      |
     |      
     |      
     |       
     |      
     |
    _|___
          ''']
# Creating word by computer

lives = 7

Choosen_word = random.choice(Hangman_words.word_list).lower()
# Creating placeholder
length_of_word = len(Choosen_word)
placeholder = ""
for place in range(length_of_word):
    placeholder+="_"
print("Word to guess:",placeholder, "|---->" "Length of word:", length_of_word)

# Guessing number and checking
Game_over = False
correct_letters = []
while not Game_over:

    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You already guessed that letter.{guess}")

    display = ""

    for letter in Choosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display+= "_"
    print(display)


    if guess not in Choosen_word:
        lives -= 1
        print(stages[lives])
    if lives == 0:
        Game_over = True
        print("You lose")

    if "_" not in display:
        Game_over = True
        print("You win")

print(stages[lives])