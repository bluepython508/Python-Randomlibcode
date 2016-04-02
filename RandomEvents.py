import random
def flipcoin():
    flip = random.random()
    if flip > 0.5:
        return("heads")
    elif flip < 0.5:
        return("tails")
    else:
        return("invalid")

def roll():
    return random.randint(1, 6)

def main():
    keyboardinput = input()
    if keyboardinput:
        if keyboardinput == "flip":
            return(flipcoin())
        elif keyboardinput =="roll dice":
            return(roll())
        elif keyboardinput == "stop":
            return("Goodbye")

def welcome():
    print("Random Event Progam:")
    print("----------------------")
    print("Type flip to flip a coin.")
    print("Type roll dice to roll a die")
    print("Type stop to quit the program.")
           

if __name__ == "__main__":
    welcome()
    while True:
        returned = main()
        print(returned)
        if returned == "Goodbye":
            break
