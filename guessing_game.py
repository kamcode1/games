import random

secret_number = random.randint(1,15)
while True:
    guess = int(input("please, guess (the number it has to be b/n 1 to 15): "))

    match guess:
        case _ if guess == secret_number:
            print("congratulations, you guessed it!")
            break
        case _ if guess > secret_number:
            print("Nope, your guess is a bit high. Give it another shot!")

        case _ if guess < secret_number:
            print("Nope, your guess is a bit low. Give it another shot!")
        case _: 
            print("please, Enter a valid number.")
        