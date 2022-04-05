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
                        print("you received " + str(i['value']) + " euros")
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
            self.__transactions['transactions'].append(i)
    
    def get_categories(self):
        categories = []
        for i in self.__transactions['transactions']:
            categories.append(i['category'])
        return categories
