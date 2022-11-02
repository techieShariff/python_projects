import random
import hangmanart
import hangmanword

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

print(logo)

word_list = ["sajidshariff","alfiyasyed","aamirul"]
end_of_game = False
random_word = random.choice(word_list)
print(f"Pssst The Solution is '{random_word}'")
lives = 6

word_length = len(random_word)

display = []

for _ in random_word:
        display += "_"
while not end_of_game:
    guess = input("Enter a letter ? : ").lower()

    for position in range(word_length):
        letter = random_word[position]

        if guess == letter:
            display[position] = letter

    if guess not in random_word:
        lives -= 1

        if lives == 0:
            end_of_game=True
            print("You lost")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You won")

print(display)
