import datetime


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
    tracker_id = 0

    def __init__(self, name, amount):
        self.name = name
        Expenses.tracker_id += 1  # To track expenses number id
        self.tracker = Expenses.tracker_id
        self.amount = amount


class ExpenseTracker:
    def __init__(self, list=None):
        if list is None:
            self.list = []

    def add_expense(self):
        exp_input = input("Please enter your expenses: (coffee 50): ").lower().split()
        self.list.append((Expenses(*exp_input)))

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
            menu_item = ["Abdd Expense", "Edit Expense", "Remove Expense"]
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
        for x in self.list:
            print(f"{x.tracker}) {x.name}---{x.amount}")


d1 = ExpenseTracker()
d1.menu()
