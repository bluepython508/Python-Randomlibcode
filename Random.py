import random
def flipcoin():
    flip = random.random()
    if flip > 0.5:
        return("heads")
    elif flip < 0.5:
        return("tails")
    else:
            return("invalid")

def main():
    keyboardinput = input()
    if keyboardinput:
        if keyboardinput == "flip":
            return(flipcoin())
        elif keyboardinput == "stop":
            return("Goodbye")

def welcome():
    print("Coin Flipping Progam:")
    print("------------------------------------------------------")
    print("Type flip to flip a coin.")
    print("Type stop to quit the program.")
           

if __name__ == "__main__":
    welcome()
    while True:
        returned = main()
        print(returned)
        if returned == "Goodbye":
            break
