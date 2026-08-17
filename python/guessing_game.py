from random import randint

def guessing_game():
    number_to_guess = randint(1, 50)
    tries = 0

    while True:
        guess_number = int(input("Guess the random number from 1 through 50\n"))

        if guess_number > 50 or guess_number < 1:
            print("Invalid number. Try again")
            continue

        tries += 1

        if number_to_guess == guess_number:
            print("Congrats! You found the number!")
            print(f"It took you {tries} tries")
            break

        if abs(number_to_guess - guess_number) <= 5:
            print("Hotter! Try again!\n")
        else:
            print("Colder! Try again!")

    try_again = input("Ya wanna try again? (yes/no): ").lower()
    if try_again == "yes":
        print("Sweet! Good luck:3")
        guessing_game()
    else:
        print("Alright:3 Bye!")

guessing_game()       