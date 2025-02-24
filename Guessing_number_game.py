import random

guessed_number = random.randint(1, 100)

go_on = True

while go_on:
    try:
        input_number = int(input("Guess the number I've choose already and enter if you can, It's between 1 - 100 : "))
    
        if(input_number > guessed_number):
            print("Too High!")
            
        elif(input_number < guessed_number):
            print("Too Low!")
            
        elif(input_number == guessed_number):
            go_on = False
            print("You Guessed it Correct!")
            
        else:
            print("Invalid Input!")
    except:
        print("Invalid Input!")