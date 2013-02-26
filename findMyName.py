'''
This is a game for MCA 2012-2015 batch (Give a name yaar to this batch ... ) yeah...
In this you have to play against computer.. the computer will guess a name from our batch and you have to guess it.. atmost only 5 invalid guesses are allowed if you are able to guess then walla you won else you loose... 
'''

import random
import string

def loadme():
	print ""
	print ""
	print "*********************** WAIT MCA 2012-2015 BATCH NAMES ARE LOADING ***********************"
	inFile = open("names.txt",'r',0)
	line = inFile.readline()
	namelist = string.split(line)
	print " ", len(namelist), "names loaded..."
	print " "
	print " "
	print "<------------------------THE GAME BEGINS-------------------------->"
	return namelist

namelist = loadme()

def guessed(secretName,nameGuessed):
	for char in secretName:
		if char not in nameGuessed:
			return False
	return True

def guessedWord(secretName,nameGuessed):
	name=''
	for char in secretName:
		if char in nameGuessed:
			name += char + ' '
		else:
			name += '_ '
	return name

def play(secretName):
	print ""
	print "            Welcome to BHUJHO TO JAANO :D :D "
	print ""
	print "Hmmmm to ham ek naaam soch liyee hai .... ye nahi jaante hai ki wo ladka hai ki ladki  but its  of ", len(secretName) , " letters long.....:) :)"
	nameGuessed=[]
	chances = 5
	while(True):
		print " "
		print "***************************"
		print " "
		print "AApke pass " ,chances ," chances baaaki hai...hahahah :P.."
		guess = raw_input("Guess one letter : ").lower()
		if guess in nameGuessed:
			print "Aaailaaa ... tune pehle hi ye letter guess kar chukaa hai re baba :/ "
		else:
			nameGuessed.append(guess)
			if guess in secretName:
				print ""
				print "Ye hui naaa baat                                             : " + guessedWord(secretName,nameGuessed)
				if guessed(secretName,nameGuessed):
					print " "
					print "**********************"
					print "Badhaai hooo aaap  jeet chuke hai... chal ab party de ...:P."
					if secretName == 'niranjan':
						print "YOU HAVE JUST GUESSED OF THE NAME OF DEVELOPER..CORRECTLY. CONGRATS :D :D"
					print "Thnks fro paliyng.."
						
					break;
			else:
				
				print ""
				print "ooohoooo ye letter nahi hai yaar naaam mai ...try again..    : " + guessedWord(secretName,nameGuessed)
				chances -= 1
				if chances ==0:
					print " "
					print "************************************************"
					print "Aaap ye game haar chuke hai...you ran out of guesses...soo naaam ye thaa..  " + secretName
					break;

secretName=(random.choice(namelist)).lower()
play(secretName)
