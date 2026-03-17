import time


def parse(exp_input):
    for x in exp_input.lower().split():
        if x in ["add", "remove", "edit"]:
            fun = x
        elif x.isdigit():
            amount = x
        else:
            category = x
    return fun, amount, category


class Expenses:
    def __init__(self, name):
        self.name = name
        self.time = time.time()
        self.arr = [
            {"id": 1, "fun": "add", "category": "coffee", "amount": 20},
            {"id": 2, "fun": "add", "category": "rent", "amount": 300},
        ]

    def add_expense(self):
        exp_input = input("Please enter your expenses: (coffee 50): ")
        # Takes input from the user for their expenses
        fun, amount, category = parse(exp_input)
        self.arr.append({"fun": fun, "category": category, "amount": amount})

        for dic in self.arr:
            for y in dic:
                print(dic[y])

        # self.list.append({'Expense': })

    def edit_expense(self):
        pass

    def remove_expense(self):
        inp = int(input("Select the expense number for deleting: "))
        for i, x in enumerate(self.arr):
            if inp == x["id"]:
                self.arr.pop(i)

    def menu(self):
        while True:
            menu_item = ["Add Expense", "Edit Expense", "Remove Expense"]
            for i, x in enumerate(menu_item):
                print(f"{i+1} {x}")
            choice = input("Enter your choice: ").strip().lower().split()[0]
            if choice in ["1", "add"]:
                print()
                self.add_expense()
            elif choice in ["2", "edit"]:
                self.edit_expense()
            elif choice in ["3", "remove"]:
                self.show_expense()
                self.remove_expense()
            else:
                print("Quitting: ")
                break

    def show_expense(self):
        i = 0
        for dict in self.arr:
            print(f"{dict["id"]}) {dict["fun"]} {dict["category"]} {dict["amount"]}")


d1 = Expenses("Sanjal")


d1.menu()
