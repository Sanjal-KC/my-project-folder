import numpy as n

difficulty = {
    "E": {"attempt": 5, "max_guess": 5},
    "M": {"attempt": 5, "max_guess": 10},
    "D": {"attempt": 10, "max_guess": 15},
}
print(
    "Hello Welcome to the number guessing game: \nYou will have ten attempts. Each right answer gets you 10 points"
)
x = input("\nType 'Y' and press Enter to play (or just Enter to exit): ")

while True:
    if x.upper() == "Y":
        gp = 0
        print("Choose the Difficulty Level:\n")
        while True:
            level = input("Easy(E),Medium(M),Difficult(D):\t").upper()
            if level == "E" or level == "M" or level == "D":
                break
            else:
                print("Invalid Input! Please enter E,M or D.")

        attempt = difficulty[level]["attempt"]
        max_guess = difficulty[level]["max_guess"]
        max_points = attempt * 10

        for i in range(1, attempt + 1):
            auto_gen = n.random.randint(max_guess + 1)
            print(f"\n{'='*30}")
            print(f"Attempt {i}/{attempt}")
            while True:
                try:
                    guess = int(input(f"Guess a number between 0 to {max_guess}: "))
                    if 0 <= guess <= max_guess:
                        break
                    else:
                        print(f"Please enter 0-{max_guess} only!")
                except ValueError:
                    print("That's not a number! Try again.")

            if guess == auto_gen:
                print(f"\n\t \t✅ Congrats {guess} is the correct guess")
                gp = gp + 10
                print(f"\t \t🎯 Points:{gp}/{max_points}")
            else:
                print(f"\n \t \t❌ WRONG!!!")
                print(f"\t \t{auto_gen} was the correct guess")
                print(f"\t \t🎯 Point:{gp}/{max_points}")
        print(f"\nYour total Points is: {gp}/{max_points}")
        if gp == max_points:
            print("Killing it! You got the highest point")
        elif gp == 0:
            print("\n:( Better luck Next time")

        x = input("Press Y again for next game: ").upper()
        if not x == "Y":
            break
    else:
        break
