class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = list()
        self.balance = 0

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.balance -= amount
        return self.check_funds(amount)

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)
        return self.check_funds(amount)

    def check_funds(self, amount):
        return amount <= self.balance

    def __str__(self):
        output = self.name.center(30, "*") + "\n"
        for items in range(0, len(self.ledger)):
            description = self.ledger[items]["description"]
            amount = self.ledger[items]["amount"]
            amount = "{:.2f}".format(amount)
            output += description.ljust(23, " ")[:23] + amount.rjust(7, " ") + "\n"
        total = self.get_balance()
        output += "Total: {:.2f}".format(total) + "\n"
        return output

def create_spend_chart(categories):
    withdrawls = list()
    for items in categories:
        total = abs(sum(values["amount"] for values in items.ledger if values["amount"] < 0))
        withdrawls.append(total)

    percents = map(lambda x: int(x / sum(withdrawls) * 10) * 10, withdrawls)

    data = dict()
    for items in range(0, len(categories)):
        data[categories[items].name] = percents[items]

    output = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        output += "{:>3}|".format(i)
        for items in data:
            if data[items] >= i: output += " o "
            else: output += "   "
        output += "\n"

    output += "    {dash}\n".format(dash = "-" * len(data) * 3)

    data_names = data.keys()
    max_len = max(len(ele) for ele in data_names)

    for i in range(0, max_len):
        output += " " * 4
        for j in range(0, len(data_names)):
            data_names[j] = data_names[j].ljust(max_len)
            output += " {letter} ".format(letter = data_names[j][i])
        output += "\n"

    return output
