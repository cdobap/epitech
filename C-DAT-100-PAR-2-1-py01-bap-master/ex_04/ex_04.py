from Finance import Budget


myBudget = Budget("./data.json")

for category in myBudget.get_categories():
    print(category)

myBudget.show_transactions('salary')

myBudget.add_transactions({'value': -5000, 'category': 'epitech' })

myBudget.show_transactions('epitech')
