import random

# A Number Guessing Game

print("Welcome to the number guessing game!\n")
print("I'm thinking of a number between 1 and 100.\n")

computer_guess = random.randint(1, 100)
tries = 10
while tries > 0:
    user_guess = int(input("Enter your guess: "))

    print(f"{computer_guess}")

    if user_guess > computer_guess:

        print("Lower!")
        tries -= 1

    elif user_guess < computer_guess:

        print("Higher!")
        tries -= 1

    else:
        print("Congratulation!")
        print(f"You guessed the number with {tries} trie(s) left!")

        break

if tries == 0:

    print("You ran out of tries!")
    print(f"The number was {computer_guess}")
