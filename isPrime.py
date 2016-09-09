import time
def start():
	firstInput = raw_input("1: Check Number\n2: Loop from Number\n3: Speed Check\n4: Speed Loop from Number\nInput Here: ")
	if (firstInput == "1"):
		firstInput = int(firstInput)
		checker()
	elif (firstInput == "4"):
		firstInput = int(firstInput)
		countUp(firstInput)
	elif (firstInput == "3"):
		firstInput = int(firstInput)
		countUp(firstInput)
	elif (firstInput == "2"):
		firstInput = int(firstInput)
		countUp(firstInput)
	else:
		start()
		
def count(chk):
	start = time.clock()
	cont = True
	while (cont == True):
		prime = 0
		print "Number : Modulus" 
		time.sleep(1.5)
		while (prime == 0):
			listPos, output = 0,0
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
				print "Completed in: " + str(time.clock() - start) + " seconds"
				print "Checking" + " " + str(chk + 1)
				prime = 1
			chk += 1
		incorrect = 1
		while (incorrect == 1):
			cont = raw_input("Would you like to continue onto %d (t/f)?" %(chk))
			if (cont == "t"):
				cont,incorrect,prime = True,0,0
			elif (cont == "f"):
				cont,incorrect = False,0
				print "Thank you!"
			else:
				print "Try again"
					
def solver(chk, intType):
	start = time.clock()
	#intType defines whether or not lists will be recreated, for types 2 and 3 only
	listPos,output = 0,0
	cycleNum = chk - 1
	if (intType == 1):
		ls = [1];
		print "Number : Modulus"
		time.sleep(1.5)
		while (cycleNum > 0):
			output = chk%cycleNum
			ls.append(output)
			print str(cycleNum + 1) + " : " + str(ls[listPos])
			listPos += 1
			cycleNum -= 1
		del ls[-1]
		print "Completed in: " + str(time.clock() - start) + " seconds"
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
	start = time.clock()
	cont = True
	while (cont == True):
		loopList = [0];
		del loopList[0]
		prime = 0
		print "Number : Modulus" 
		time.sleep(1.5)
		while (prime == 0):
			listPos,output = 0,0
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
					print "Completed in: " + str(time.clock() - start) + " seconds"
				else:
					prime = 0
			chk += 1
		incorrect = 1
		while (incorrect == 1):
			cont = raw_input("Would you like to continue onto %d (t/f)?" %(chk))
			if (cont == "t"):
				cont,incorrect,prime = True,0,0
			elif (cont == "f"):
				cont,incorrect = False,0
				print "Thank you!"
			else:
				print "Try again"

def divider(chk, chkNum, chkInt, start):
    found = 0
    while (found == 0):
        cycleNum = (chkNum - 1)/2
        nPrime, output = 0,0
        while (nPrime == 0):
            if (chkInt == 0):
                cycleNum -= 1
            elif (chkInt == 5):
                cycleNum -= 1
            elif (chkInt % 2 == 0):
                cycleNum -= 1
            else:
                output = chkNum%cycleNum
                if (output == 0):
                    nPrime = 1
                elif (cycleNum == 2):
                	nPrime = 2
                else:
                    cycleNum -= 1
        if (nPrime == 1):
            print str(chk) + " is not a Prime"
            found = 1
        elif (nPrime == 2):
            print str(chk) + " is a Prime"
            found = 1
        print "Completed in: " + str(time.clock() - start) + " seconds"

def nsolve(chk, chkNum):
    start = time.clock()
    chkLast = int(chk[-1])
    if (chkLast == 5):
        print "Not a Prime"
        print "Completed in: " + str(time.clock() - start) + " seconds"
    elif (chkLast % 2 == 0):
        print "Not a Prime"
        print "Completed in: " + str(time.clock() - start) + " seconds"
    elif (chkLast == 0):
        print "Not a Prime"
        print "Completed in: " + str(time.clock() - start) + " seconds"
    else:
        divider(chk, chkNum, chkLast, start)

def countUp(firstInput):
	if (firstInput == 2):
		correct = 0
		while (correct == 0):
			chk = input("Insert number to be started from here: ")
			if (chk > 2):
				loopNum = input("Insert number of loops between check: ")
				if (loopNum <= 5000):
					if (loopNum >= 2):
						loop(chk, loopNum)
						correct = 1
					else:
						print "Number of loops must be greater than 1"
				else:
					print "Number of loops cannot be greater than 5000"
			else:
				print "Number must be greater than 2"
				correct = 0
	elif (firstInput == 3):
		chk = raw_input("Input number to be checked here: ")
		chkNum = int(chk)
		if (chkNum > 2):
		    nsolve(chk, chkNum)
		else:
		    print "Number must be greater than 1"
		    countUp(3)
#	else:

start()
