from replit import clear
import random

from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

from hangman_art import logo
print(logo)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Угадайте букву: ").lower()

    clear()
  
    if guess in display:
        print(f"Вы уже угадали букву {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter

    
    if guess not in chosen_word:
      
        print(f"Вы ввели {guess}, но такой буквы нет в слове. У вас уменьшилась жизнь.")
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("Вы проиграли :(.")
            print(f"Слово было\n{chosen_word}")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("Вы выиграли!.")

    from hangman_art import stages
    print(stages[lives])
