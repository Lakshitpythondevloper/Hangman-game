# 🕹️ Hangman Game (Python Console Edition)
![Project Logo](https://cdn-icons-png.freepik.com/256/13338/13338262.png?semt=ais_hybrid)

Welcome to the classic **Hangman Game**, recreated in Python for the terminal! This is a beginner-friendly project that helps you understand loops, conditionals, string manipulation, and user input in Python.

## 📁 Project Structure

```
hangman-game/
├── hangman.py # Main Python game file
├── Hangman_words.py # Contains a list of words for random selection
├── README.md # This README file 
```

---

## 🚀 Features

- 🔠 **Random Word Selection**  
  The game pulls a random word from a predefined list in `Hangman_words.py`.

- 🧠 **Letter-by-Letter Guessing**  
  The user guesses the word one letter at a time.

- 🎨 **ASCII Art Hangman**  
  Each incorrect guess displays a new part of the stick figure — a visual representation of your remaining lives.

- ✅ **Repeated Guess Detection**  
  The game notifies the user if a letter has already been guessed.

- 🔄 **Live Word Update**  
  After each guess, the placeholder updates to reveal correct letters.

- ☠️ **Loss Condition**  
  The player loses if the hangman is fully drawn (7 incorrect guesses).

- 🏆 **Win Condition**  
  If the user guesses all the letters correctly before running out of lives, they win!

---

## 🛠 How to Run the Game

### Prerequisites

- Python 3.x must be installed on your machine.
- Intall editor Vs code or pycharm
- Download the .py files from the github of hangman.py etc.

## Explanation of Practice.py (Hangman Game Code)🐍
This file contains the core logic for a command-line Hangman game. Let's break down each section:👇

**1. Imports**💾

```
import random
import Hangman_words
```
- ```import random:``` This line imports the ```random``` module, which is necessary for choosing a random word from the ```word_list```.

- ```mport Hangman_words``` This imports a separate Python file named ```Hangman_words.py```. This file is expected to contain a variable, typically a list, named ```word_list```, which holds all the possible words for the Hangman game.📕
 
**2. Game Initialization** ⚙️

```
lives = 7

Choosen_word = random.choice(Hangman_words.word_list).lower()
print(Choosen_word) # This line is usually removed in final games for cheating prevention

length_of_word = len(Choosen_word)
placeholder = ""
for place in range(length_of_word):
    placeholder+="_"
print("Word to guess:",placeholder, " " "Length of word:", length_of_word)
```

- ```lives = 7``` : Initializes the number of lives the player has at the start of the game. ❤️

- ```Choosen_word = random.choice(Hangman_words.word_list).lower()```:
- ```random.choice(Hangman_words.word_list)```: Selects a single random word from the ```word_list``` defined in ```Hangman_words.py```. 🎯

- ```.lower():``` Converts the chosen word to lowercase, ensuring consistency regardless of how words are capitalized in the ```word_list```. 🔡
- ```print(Choosen_word)```: This line prints the chosen word at the start. While useful for debugging, it would typically be commented out or removed in the final game to prevent players from seeing the word. 🤫

- **Placeholder Creation:**

- ```length_of_word = len(Choosen_word)```: Gets the length of the chosen word. 📏

- ```placeholder = ""``` and the following ```for```loop: Creates a string of underscores (```_```) with the same length as the ```Choosen_word```.  This ```placeholder``` will be displayed to the user, showing how many letters are in the word and which ones have been guessed. _ _ _

- ```print("Word to guess:",placeholder, ...)```: Displays the initial placeholder (e.g., ```_ _ _ _```) and the length of the word to the player. ❓

**4. Game Loop** 🔄
```
Game_over = False
correct_letters = []
while not Game_over:
    # ... (code inside the loop)
```
     
- ```Game_over = False```: A boolean flag that controls the main game loop. The loop continues as long as ```Game_over``` is ```False```. 🟢

- ```correct_letters = []```: An empty list to store all the letters that the player has guessed correctly so far. ✅

- ```while not Game_over:```: This is the main game loop. The game continues to run, prompting for guesses, until ```Game_over``` becomes ```True``` (either by winning or losing). 🔁

**5. Player Input and Guess Checking** ✍️
```
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You already guessed that letter {guess}.")
```
- ```guess = input("Guess a letter: ").lower():```

- ```input("Guess a letter: ")```: Prompts the user to enter a letter and captures their input. ⌨️

- ```.lower()```: Converts the user's guess to lowercase for case-insensitive matching. 🅰️

- ```if guess in correct_letters:```: Checks if the letter the user just guessed is already in the correct_letters list. If it is, it informs the user that they've already guessed that letter. 🙅‍♀️

**6. Updating the Display** 📊
```
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
```

- ```display = "```": Initializes an empty string that will hold the current state of the word (guessed letters and underscores). 📝

- ```for letter in Choosen_word:```: This loop iterates through each letter in the Choosen_word. 🚶‍♀️

- ```if letter == guess:```: If the current letter from Choosen_word matches the guess made by the player:

- ```display += letter```: The actual letter is added to the display string.

- ```correct_letters.append(guess)```: The guessed letter is added to correct_letters so it's remembered for future turns and avoids duplicate incorrect guesses affecting lives. 🎉

- ```elif letter in correct_letters:```: If the current letter from Choosen_word has already been correctly guessed in a previous turn (it's in correct_letters):

- ```display += letter```: The actual letter is added to the display string.

- ```else:```: If the current letter has not been guessed yet:

- ```display+= "_"```: An underscore is added to display. 🤫

- ```print(display)```: Prints the display string, showing the player the progress (e.g., _ p p l _). 🌟

**7. Handling Incorrect Guesses and Lives** 💔
```
    if guess not in Choosen_word:
        lives -= 1
        print(stages[lives])
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
```

- ```if guess not in Choosen_word:```: Checks if the guessed letter is not present in the Choosen_word. ❌

- ```lives -= 1```: If the guess is incorrect, the player loses a life. 📉

- ```print(stages[lives])```: Prints the appropriate hangman ASCII art from the stages list, corresponding to the current number of lives remaining. 🖼️

- ```print(f"...")```: Provides feedback to the user that their guess was incorrect and they lost a life. 😔

**8. Win/Loss Conditions** 🏆
```
    if lives == 0:
        Game_over = True
        print("You lose bro! hangman is complete. The word was", Choosen_word+".")

    if "_" not in display:
        Game_over = True
        print("You win bro! The word is", Choosen_word+".")
```
**Loss Condition:**

- ```if lives == 0:```: Checks if the player has run out of lives. 💀

- ```Game_over = True```: Sets the flag to True, which will terminate the while loop. 🛑

- ```print(...)```: Informs the player that they lost and reveals the correct word. 😭

**Win Condition:**

- ```if "_" not in display:```: Checks if there are no more underscores left in the display string. This means all letters have been correctly guessed. ✨

- ```Game_over = True```: Sets the flag to True, terminating the while loop. 🛑

- ```print(...)```: Informs the player that they won and confirms the word. 🥳

**9. Final Hangman State 🏁**
```
print(stages[lives])

```
This line outside the ```while``` loop prints the final hangman stage. This will show either the fully drawn hangman (if the player lost) or the gallows without a hangman (if the player won). 🎭

## Here is ASCII art 🖌️🎨: -

```
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
```
