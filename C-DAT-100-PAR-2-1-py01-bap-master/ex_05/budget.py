import json

class Budget:
    def __init__(self, filePath = None):        
        self.__transactions = {}
        with open(filePath) as json_file:
            self.__transactions = json.load(json_file)
    
    def show_transactions(self, category = None):
        list = self.__transactions['transactions']
        for i in list:
            # display transactions'category
            if i['category'] == category:
                if isinstance(i['value'], int) or isinstance(i['value'], float):        
                    if i['value'] > 0:
                        print(f"you received " + {str(i['value'])} + " euros")
                    else:
                        print("you spent " + str(abs(i['value'])) + " euros")
            # display all transactions
            elif category == None:
                if isinstance(i['value'], int) or isinstance(i['value'], float):        
                    if i['value'] > 0:
                        print("you received " + str(i['value']) + " euros")
                    else:
                        print("you spent " + str(abs(i['value'])) + " euros")

    def add_transactions(self, *dicts):                          
        for i in dicts:
            with open('./data.json', "r") as json_file:
                self.__transactions = json.load(json_file)            
            self.__transactions["transactions"].append(i)
            with open('./data.json', "w") as json_file:
                json.dump(self.__transactions, json_file)
        
    def get_categories(self):
        categories = []
        for i in self.__transactions['transactions']:
            categories.append(i['category'])
        return categories

    def get_balance(self):
        balance = 0
        for i in self.__transactions['transactions']:
            balance = balance + i['value']
        print(f"Your balance: {balance} €")

    def get_last_transaction(self):
        last = self.__transactions['transactions'][-1]
        if last['value'] > 0:            
            print(f"Your last transaction: you received {(abs(last['value']))} euros")
        else:
            print(f"Your last transaction: you spent {(abs(last['value']))} euros")

budget = Budget("./data.json")

budget.get_last_transaction()

def chooseAction():
    print("Choose between :")
    print("1 - consult my balance")
    print("2 - add new transaction")
    print("3 - consult your transactions history")
    print("4 - quit")

    input_action = input("")
    if input_action == "1":
        budget.get_balance()
        input("----Go to menu: press Enter----")
        chooseAction()
    elif input_action == "2":
        input_value = input("Value: ")
        input_category = input("Category: ")    
        new_transaction = {'value': int(input_value), 'category': input_category}    
        budget.add_transactions(new_transaction)
        chooseAction() 
    elif input_action == "3":
        budget.show_transactions()
        input("----Go to menu: press Enter----")
        chooseAction()
    elif input_action == "4":
        print("Goodbye !")
    else:
        print("Wrong input !")
        chooseAction()

chooseAction()
