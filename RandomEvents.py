import random
import time
prompt = "READY>"

def chosen(strings):
    time.sleep(5)
    return random.choose(strings)

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

def roll(n):
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
            n = int(input("How many dice would you like to roll?"))
            return(roll(n))
        elif keyboardinput == "choose":
            inputed = True
            n = 1
            strings = []
            while inputed:
                inputed = input("string #" + str(n))
                n += 1
                strings.append(inputed)
            return(chosen(strings))
        elif keyboardinput == "stop":
            return("Goodbye")
        else:
            return("I don't understand")

def welcome():
    print("Random Event Progam:")
    print("----------------------")
    print("Type flip to flip a coin")
    print("Type roll dice to roll some die")
    print("Type choose to choose from a list")
    print("Type stop to quit the program.")

def main():
    #try:
    if True:
        welcome()
        while True:
            returned = loop()
            print(returned)
            if returned == "Goodbye":
                break
    #except:
        #print("sorry")
           

if __name__ == "__main__":
    main()
