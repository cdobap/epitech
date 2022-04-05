def show_transactions(list):
    for i in list:
        if isinstance(i, int) or isinstance(i, float):        
            if i > 0:
                print("you received " + str(i) + " euros")
            else:
                print("you spent " + str(abs(i)) + " euros")

""" 
if __name__ == '__main__':
    show_transactions([512 , 42.08 , -12, "test", 0])
"""