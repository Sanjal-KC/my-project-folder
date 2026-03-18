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
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        self.time = time.time()


class ExpenseTracker:
    def __init__(self, list=None):
        if list is None:
            list = []
        self.list = list

    def add_expense(self):
        exp_input = input("Please enter your expenses: (coffee 50): ").lower().split()
        # Takes input from the user for their expenses
        name, amount = exp_input
        self.list.append((Expenses(name, amount)))

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
            pass


d1 = ExpenseTracker()
d1.menu()
