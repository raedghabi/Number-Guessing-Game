import random 
number = random.randint(1, 100)
while True:
    try : 
        user_guess = int(input("Guess a number between 1 and 100: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 100.")
        continue
    if user_guess  == number:
        print("Congratulations! You guessed the correct number.")
        break
    elif user_guess < number:
        print("Too low! Try again.")
    elif user_guess  > number:
        print("Too high! Try again.")
    else:
        print("Invalid input. Please enter a number between 1 and 100.")
        continue