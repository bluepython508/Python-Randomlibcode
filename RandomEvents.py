import random
import time
prompt = ">>>"

def string_from_list(list_name):
    string = ''''''
    for x in range(len(list_name)):
        tempstring = '''roll ''' + str(x + 1) + ''': ''' + str(list_name[x-1]) + '''
'''
        string = string + tempstring
    return(string)
def flipcoin():
    flip = random.random()
    time.sleep(0.5)
    if flip > 0.5:
        return("heads")
    elif flip < 0.5:
        return("tails")
    else:
        return("The coin escaped")

def roll():
    n = int(input("How many dice would you like to roll?"))
    rolled = []
    for x in range(n):
        rolled.append(random.randint(1,6))
        time.sleep(1)
    return(string_from_list(rolled))

def loop():
    keyboardinput = input(prompt)
    if keyboardinput:
        if keyboardinput == "flip":
            return(flipcoin())
        elif keyboardinput =="roll dice":
            return(roll())
        elif keyboardinput == "stop":
            return("Goodbye")
        else:
            return("I don't understand")

def welcome():
    print("Random Event Progam:")
    print("----------------------")
    print("Type flip to flip a coin.")
    print("Type roll dice to roll a die")
    print("Type stop to quit the program.")

def main():
    welcome()
    while True:
        returned = loop()
        print(returned)
        if returned == "Goodbye":
            break
           

if __name__ == "__main__":
    main()
