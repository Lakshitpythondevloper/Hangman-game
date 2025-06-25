import random
import Hangman_words
print(r''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                   ''')
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
print(Choosen_word)
# Creating placeholder
length_of_word = len(Choosen_word)
placeholder = ""
for place in range(length_of_word):
    placeholder+="_"
print("Word to guess:",placeholder, " " "Length of word:", length_of_word)

# Guessing number and checking
Game_over = False
correct_letters = []
while not Game_over:

    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You already guessed that letter {guess}.")

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
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
    if lives == 0:
        Game_over = True
        print("You lose bro! hangman is complete. The word was", Choosen_word+".")

    if "_" not in display:
        Game_over = True
        print("You win bro! The word is", Choosen_word+".")

print(stages[lives])