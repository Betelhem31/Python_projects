import random
print("Welcome to the Guess the Number game!")
print("i am thinking of a number between 1 and 100.")
difficulty_level = input("Choose a a difficulty. Type 'easy' or 'hard':\n")
right_number = random.randint(1, 100)
hard_guesses = 5
easy_guesses = 10
def hard_go():
    global hard_guesses
    while hard_guesses> 0:
        print(f"You have {hard_guesses} attempts to guess the number.")
        guesses_number = int(input("Make a guess: "))
        if(guesses_number > right_number):
            print("Too high. Try again.")
            hard_guesses -= 1
        elif(guesses_number < right_number):
            print("Too low. Try again.")
            hard_guesses -= 1
        else:
            print(f"You got it! The number was {right_number}.")
            return
    print(f" You've run out of guesses. The number was {right_number}.")
def easy_go():
    global easy_guesses
    while easy_guesses > 0:
        print(f"You have {easy_guesses} attempts to guess the number.")
        guesses_number = int(input("Make a guess: "))
        if(guesses_number > right_number):
            print("Too high. Try again.")
            easy_guesses -= 1
        elif(guesses_number < right_number):
            print("Too low. Try again.")
            easy_guesses -= 1
        else:
            print(f"You got it! The number was {right_number}.")
            return
    print(f" You've run out of guesses. The number was {right_number}.")

if difficulty_level == 'hard':
    hard_go()
elif difficulty_level == 'easy':
    easy_go()
else:
    print("Invalid difficulty level. Please restart the game and choose 'easy' or 'hard'.")


   
    
