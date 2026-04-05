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
                if (
                    0 <= minute_in < 60 and 0 <= minute_out < 60
                ):  # Minute Boundary checker
                    break
                print("\nPlease enter Valid minutes\n")

            except ValueError:
                print("\nPlease enter an integer value")

        check_in = hour_in + (minute_in / 60)
        check_out = hour_out + (minute_out / 60)
        total_time = check_out - check_in
        if total_time < 0:
            temp = total_time + 24
            total_time = temp

        if (  # Only runs if check in and out are between 0 to 24 hours and total parking time is not negative
            check_in >= 0 and check_in < 24
        ) and (
            check_out >= 0 and check_out < 24
        ):
            total_hour = hour_out - hour_in
            if total_hour < 0:
                temp2 = total_hour + 24
                total_hour = temp2

            if minute_out > minute_in:
                total_minutes = minute_out - minute_in
            else:
                total_minutes = minute_in - minute_out

            print(f"\nParking Time: {total_hour} hours and {total_minutes} minutes")
            if total_time <= 1:
                print("Total Due: 19$")
                due = 19
            elif total_time <= 2:
                print("Total Due: 29$")
                due = 29
            elif total_time <= 3:
                print("Total Due: 79$")
                due = 39
            else:
                print("Total Due: 89$")
                due = 79
            collected_amount = 0  # No amount collected from the user yet
            while collected_amount < due:  # Run till collected_amount is less than due
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
                collected_amount = collected_amount + cash_inp
                remaining_balance = due - collected_amount
                print("Remaining Balance:", remaining_balance)
            if collected_amount > due:  # In case of change needed
                change_amount = collected_amount - due
                print("\nHeres your change!!:", change_amount)
            print("Thank you for parking with us:)\n")
            break
        else:
            print("\nYour Parking time is not valid.\n")
            break
    elif choice == 3:
        print("Thank you for using Utopia Parking :)")
        break
    else:
        print("\nThere is no such Option :(\n")
