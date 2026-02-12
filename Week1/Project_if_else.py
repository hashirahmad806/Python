import random

no_of_chances = 1
random_number = random.randint(1, 10)

print("**************************************")
print("***** Welcome to Number Guessing Game *****")
print("**************************************")
print("You have 5 chances to guess the correct number")

while no_of_chances <= 5:
    guess_no = int(input("Guess a number between 1 and 10: "))

    if guess_no == random_number:
        print(" Congratulations! You won the game ")
        break
    else:
        print(" Wrong guess, try again")

    no_of_chances += 1

if no_of_chances > 5:
    print("\n *** You lost the game. Better luck next time! *** \n")

print("The random number was:", random_number)
