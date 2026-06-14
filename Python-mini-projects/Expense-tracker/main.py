import json 

Expense_file = "expenses.txt"


def load_expenses():
    try:
        with open(Expense_file,"r") as file:
            data = file.read()
            if data:
                return json.loads(data)
            return []
    except FileNotFoundError:
        return []
    
