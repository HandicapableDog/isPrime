def start():
	firstInput = raw_input("1: Check Number\n2: Count Up From Number\n3: Count Up From 2\n4: Loop from Number\nInput Here: ")
	if (firstInput == "1"):
		firstInput = int(firstInput)
		checker()
	elif (firstInput == "2"):
		firstInput = int(firstInput)
		countUp(firstInput)
	elif (firstInput == "3"):
		firstInput = int(firstInput)
		countUp(firstInput)
	elif (firstInput == "4"):
		firstInput = int(firstInput)
		countUp(firstInput)
	else:
		start()
		
def count(chk):
	cont = True
	while (cont == True):
		prime = 0
		print "Number : Modulus" 
		while (prime == 0):
			listPos = 0
			output = 0
			cycleNum = chk - 1
			ls = [1];
			while (cycleNum > 0):
				output = chk%cycleNum
				ls.append(output)
				print str(cycleNum + 1) + " : " + str(ls[listPos])
				listPos += 1
				cycleNum -= 1
			del ls[-1]
			if (0 in ls):
				print str(chk) + " is not a prime"
				print "Checking" + " " + str(chk + 1)
				prime = 0
			else:
				print str(chk) + " is a prime"
				print "Checking" + " " + str(chk + 1)
				prime = 1
			chk += 1
		incorrect = 1
		while (incorrect == 1):
			cont = raw_input("Would you like to continue onto %d (t/f)?" %(chk))
			if (cont == "t"):
				cont = True
				incorrect = 0
				prime = 0
			elif (cont == "f"):
				cont = False
				incorrect = 0
				print "Thank you!"
			else:
				print "Try again"
					
def solver(chk, intType):
	#intType defines whether or not lists will be recreated, for types 2 and 3 only
	listPos = 0
	output = 0
	cycleNum = chk - 1
	if (intType == 1):
		ls = [1];
		print "Number : Modulus"
		while (cycleNum > 0):
			output = chk%cycleNum
			ls.append(output)
			print str(cycleNum + 1) + " : " + str(ls[listPos])
			listPos += 1
			cycleNum -= 1
		del ls[-1]
		if (0 in ls):
			print "Not a Prime"
		else:
			print "Prime"
	elif (intType == 2):
		count(chk)
	elif (intType == 3):
		count(chk)
	# Make array to save each answer, .find(0) later
	# listPos must update opposite cycleNumber in order to accurately assign numbers to the list

def checker():
	intType = 1
	chk = input("Input number to be checked here: ")
	if (chk >= 2):
		solver(chk,intType)
	else:
		print "Number must be greater than 1"
		checker()

def loop(chk, loopNum):
	cont = True
	while (cont == True):
		loopList = [0];
		del loopList[0]
		prime = 0
		print "Number : Modulus" 
		while (prime == 0):
			listPos = 0
			output = 0
			cycleNum = chk - 1
			ls = [1];
			while (cycleNum > 0):
				output = chk%cycleNum
				ls.append(output)
				print str(cycleNum + 1) + " : " + str(ls[listPos])
				listPos += 1
				cycleNum -= 1
			del ls[-1]
			if (0 in ls):
				print str(chk) + " is not a prime"
				print "Checking" + " " + str(chk + 1)
				prime = 0
			else:
				print str(chk) + " is a prime"
				print "Checking" + " " + str(chk + 1)
				loopList.append(chk)
				if (len(loopList) == loopNum):
					prime = 1
					print "These are the %d requested prime numbers " %(loopNum) + str(loopList)
				else:
					prime = 0
			chk += 1
		incorrect = 1
		while (incorrect == 1):
			cont = raw_input("Would you like to continue onto %d (t/f)?" %(chk))
			if (cont == "t"):
				cont = True
				incorrect = 0
				prime = 0
			elif (cont == "f"):
				cont = False
				incorrect = 0
				print "Thank you!"
			else:
				print "Try again"

def countUp(firstInput):
	if (firstInput == 2):
		solver(2, 2)
	elif (firstInput == 4):
		correct = 0
		while (correct == 0):
			chk = input("Insert number to be started from here: ")
			if (chk >= 2):
				loopNum = input("Insert number of loops between check: ")
				if (loopNum <= 500):
					if (loopNum >= 2):
						loop(chk, loopNum)
						correct = 1
					else:
						print "Number of loops must be greater than 1"
				else:
					print "Number of loops cannot be greater than 500"
			else:
				print "Number must be greater than 1"
				correct = 0
	else:
		intType = 3
		chk = input("Insert number to be started from here: ")
		if (chk >= 2):	
			solver(chk, intType)
		else:
			print "Number must be greater than 1"
			countUp(firstInput)

start()
