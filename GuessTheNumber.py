print("name-:rahul biradar\nUSN-:1AY24AI087\nsec-:o")
import random

number = random.randint(1, 20)
print("I am thinking of a number between 1 and 20.")

guess_count = 0
while True:
    print("Take a guess.")
    guess = int(input())  
    guess_count += 1
    if guess < number:
        print("Your guess is too low.")
    elif guess > number:
        print("Your guess is too high.")
    else:
        print(f"Good job! You guessed my number in {guess_count} guesses!")
        break
