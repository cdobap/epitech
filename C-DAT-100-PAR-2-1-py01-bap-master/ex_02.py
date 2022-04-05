class Budget:
    def __init__(self):        
      self.__transactions = []

    def show_transactions(self):
        list = self.__transactions
        for i in list:
            if isinstance(i, int) or isinstance(i, float):        
                if i > 0:
                    print("you received " + str(i) + " euros")
                else:
                    print("you spent " + str(abs(i)) + " euros")
            
    def add_transactions(self, *param):                     
        for i in param:
            if isinstance(i, int) or isinstance(i, float):
                self.__transactions.append(i)                
            else:
                raise Exception("wrong params")          

""" 
if __name__ == '__main__':
    myBudget = Budget()
    myBudget.add_transactions(512 , 42.08 , -12)
    myBudget.show_transactions()
"""