import random
import time
import math
prompt = "READY>"

def string_from_list(list_name):
	string = ''''''
	for x in range(len(list_name)):
		tempstring = '''Roll ''' + str(x + 1) + ''': ''' + str(list_name[x-1]) + '''\n'''
		string = string + tempstring
	return(string)
def get_list():
	result = []
	element = 'bar'
	while element:
		element = input("Choice?")
		if element:
			result.append(element)
	return result


def choose(choices):
	return random.choice(choices)


def flipcoin():
	flip = random.random()
	time.sleep(0.5)
	if flip > 0.5:
		return("Heads")
	elif flip < 0.5:
		return("Tails")
	else:
		return("The coin escaped")

def roll(n):
	rolled = []
	for x in range(n):
		rolled.append(random.randint(1,6))
		#time.sleep(1)
	return(string_from_list(rolled))

def loop():
	keyboardinput = input(prompt)
	if keyboardinput:
		if keyboardinput == "flip":
			return(flipcoin())
		elif keyboardinput =="roll dice":
			n = int(round(float(input("How many dice would you like to roll?"))))
			return(roll(n))
		elif keyboardinput == "stop":
			return("Goodbye")
		elif keyboardinput == "help":
			welcome()
			return
		else:
			return("I don't understand")

def welcome():
	print("Random Event Progam:")
	print("----------------------")
	print("Type flip to flip a coin.")
	print("Type roll dice to roll a dice")
	print("Type help to show this help message.")
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
