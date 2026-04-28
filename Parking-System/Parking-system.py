# - Utopia Parking
print("Welcome to Utopia Parking.")
while True:  # Main LOOP----->
    print("Menu: \n1) View Rates\n2) Check in and out\n3) Exit")
    while True:  # loop for checking the input value of the option only
        try:
            choice = int(input("Choose the option: "))
            print("--------------------")
            break
        except ValueError:
            print("The value must be integer")

    # Main Control Begins here
    if choice == 1:
        print("0-1 hours \t $19")
        print("1-2 hours \t $29")
        print("2-3 hours \t $79")
        print("3-24 hours \t $89")
        print("--------------------\n")

    elif choice == 2:
        while True:  # loop for checking the input values of the in and out hours
            try:
                print("Enter your Check in time: ")
                hour_in = int(input("Enter the hour(0-23): "))
                minute_in = int(input("Enter the minute(0-59): "))
                print("\nEnter your Check out time: ")
                hour_out = int(input("Enter the hour(0-23): "))
                minute_out = int(input("Enter the minute(0-59): "))
                if (0 <= minute_in < 60 and 0 <= minute_out < 60) and (
                    0 <= hour_out < 24 and 0 <= hour_in < 24
                ):  # Minute Boundary checker
                    break
                print("\nPlease enter Valid Hour and Minutes\n")

            except ValueError:
                print("\nPlease enter an integer value")

        total_minutes = (hour_out * 60 + minute_out) - (hour_in * 60 + minute_in)
        if total_minutes < 0:
            total_minutes += 24 * 60

        total_hour = total_minutes // 60
        total_minute = total_minutes % 60

        print(f"\nParking Time: {total_hour} hours and {total_minute} minutes")
        if total_minutes <= 60:
            due = 19
            print(f"Total Due: {due}$")
        elif total_minutes <= 120:
            due = 29
            print(f"Total Due: {due}$")
        elif total_minutes <= 180:
            due = 79
            print(f"Total Due: {due}$")
        else:
            due = 89
            print(f"Total Due: {due}$")
        collected_amount = 0  # No amount collected from the user yet
        while collected_amount < due:  # Run till collected_amount is less than due
            try:
                cash_inp = int(
                    input("Insert cash amount((1, 2, 5, 10, 20, 50, 100 only): ")
                )
                if (
                    cash_inp != 1
                    and cash_inp != 2
                    and cash_inp != 5
                    and cash_inp != 10
                    and cash_inp != 20
                    and cash_inp != 50
                    and cash_inp != 100
                ):
                    print(
                        "Please Enter the cash in only ((1, 2, 5, 10, 20, 50, 100)"
                    )  # exception handling for only required cash
                    continue
            except ValueError:
                print("Please Enter an Integer Value")
                continue
            collected_amount = collected_amount + cash_inp
            remaining_balance = due - collected_amount
            print("Remaining Balance:", remaining_balance)
        if collected_amount > due:  # In case of change needed
            change_amount = collected_amount - due
            print("\nHeres your change!!:", change_amount)
        print("Thank you for parking with us:)\n")
        break

    elif choice == 3:
        print("Thank you for using Utopia Parking :)")
        break
    else:
        print("\nThere is no such Option :(\n")
