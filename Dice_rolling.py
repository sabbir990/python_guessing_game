import random

while True :
    choice = input("Choose that if you wanna dice (y/n)").lower()

    if choice == 'y':
        number1 = random.randint(1, 6)
        number2 = random.randint(1, 6)

        print(f"Your Dice is : {number1, number2}")

    elif choice == "n" :
        print("Thanks for playing!")
        break;

    else:
        print("Invalid Input")
        break;
