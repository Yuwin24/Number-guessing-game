import random
chances = 0
n = random.randint(1, 99)
print("A game by R.L.Yuwin")
guess = int(input("Enter an integer from 1 to 99: "))
while n != "guess":
    print
    if guess < n:
        print("guess is low")
        guess = int(input("Enter an integer from 1 to 99: "))
    elif guess > n:
        print("guess is high")
        guess = int(input("Enter an integer from 1 to 99: "))
    else:
        print("you guessed it!")
        break

    chances = chances +1

    if chances > 5:
        print("Oops Try Again You Failed :(")

        break
