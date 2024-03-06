#!/usr/bin/python3
import random

def getLines():
	linelist=[]
	while len(linelist) < 5:
	
		with open("hmw.txt", "r") as f:
    			lines = f.readlines()
    			if lines not in linelist:
    				linelist.append(random.choice(lines))
	return linelist


def questANDanswer():
	db = {}
	for el in getLines():
		x = el.index("?")
		db[el[:x+1]] = el[x+1:-1]
	return db

name = input("Enter your name: ")
def game():
	count = 0
	for k,v in questANDanswer().items():
		print(k)
		ls = v.split(",")
		correct = ls[0]
		random.shuffle(ls)
		tmp = ",".join(ls)
		print(tmp)
		answer = input("Enter your answer: ")
		if answer.lower() == correct.lower():
			print("Correct")
			count += 1
		else:
			print("Wrong. The correct answer was:", correct)
	return count

def write(fname):
	
	f = open(fname, "a")
	f.write(name + " - " + str(game()) + "\n")
	
	f.close()
write("result.txt")

def readdd():
	f = open('result.txt')
	return f.readlines()

def makeDict():
	md = {}
	for el in readdd():
		k,v = el.split(" - ")
		md[k] = v[:-1]
	return md
	
def sortedDict():
	dictt = makeDict()
	ml = list(dictt.items())
	ml.sort(key=lambda x: x[1], reverse = True)
	return ml
	
def writeIntoFile(fname):
	with open(fname, "a") as f:
		for m,j in sortedDict():
			f.write(m + " - " + str(j) + "\n")
writeIntoFile("result.txt")

	

		
		
		
		
		
		
