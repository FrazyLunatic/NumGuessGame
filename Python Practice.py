import random
import time

easy_chances = 10
med_chances = 5
hard_chances = 3

play_again = "y"

print("\nWelcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
print("\n")

while play_again == "y":
    attempts = 0
    rand_num = random.randint(1, 100)
    
    print("\nPlease select your difficulty level:")
    print("\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)")

    diff_chosen = input("\nEnter Your Choice: ").strip().lower()
    
    valid_choice = True

    if diff_chosen == "1" or diff_chosen == "easy":
        chances = easy_chances
        print("\nGreat! You have chosen the Easy level. Let's Start!")
    elif diff_chosen == "2" or diff_chosen == "medium":
        chances = med_chances
        print("\nAlright! You have chosen the Medium level. Let's Start!")
    elif diff_chosen == "3" or diff_chosen == "hard":
        chances = hard_chances
        print("\nWow! You have chosen the Hard level. Let's Start!")
    else:
        print("\nInvalid input. Please enter 1, 2, 3 or Easy/Medium/Hard.")
        valid_choice = False 

    if not valid_choice:
        continue  

    start_time = time.time()

    while attempts < chances:
        guess = int(input("\nEnter your guess: "))
        attempts += 1

        if guess == rand_num:
            print(f"\nCongratulations! You guessed the correct number in {attempts} attempts.")
            break
        elif guess < rand_num:
            print(f"\nAlmost! Number is greater than {guess}")
        else:
            print(f"\nAlmost! Number is less than {guess}")

    end_time = time.time()
    duration = end_time - start_time

    if attempts == chances and guess != rand_num:
        print(f"\nSorry! You ran out of chances. The number was {rand_num}.")

    print(f"You took {round(duration, 2)} seconds to finish the game.")

    play_again = input("\nDo you want to play again? (y/n): ").strip().lower()

    if play_again == "n":
        print("\nGoodbye")
        exit