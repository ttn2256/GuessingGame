#  File: GuessingGame.py

#  Description: Guessing the numbers you are thinking 

#  Student Name: Tuan Nguyen 

def main():
	# print Guessing Game
	print("Guessing Game \n")
	# prompt user
	print("Think of a number between 1 and 100 inclusive. \nAnd I will guess what it is in 7 tries or less. \n")
 
	# ask if user is ready
	question = input("Are you ready? (y/n): ")
 
	# if user does not enter y or n, prompt the user is ready again
	while ((question != "y") and (question != "n")):
		question = input("Are you ready? (y/n): ")
 
	# print bye if the answer is n 
	if (question == "n"):
		print("\nBye")
 
	# guess number if user enter y 
	if (question == "y"):
		lo = 0
		hi = 100
		for i in range(1,8):
			print("\nGuess", i, ": The number you thought was", (hi + lo)//2)
			guess = input("Enter 1 if my guess was high, -1 if low, and 0 if correct: ")

			# prompt the user to enter guess again if guess was not 0, 1 or -1

			while((guess != "0") and (guess != "1") and (guess != "-1")):
				guess = input("Enter 1 if my guess was high, -1 if low, and 0 if correct: ")
 
			# convert what user enter from string to int
			guess = int(guess)
 
			if (guess == 0):
				print("\nThank you for playing the Guessing Game.")
				break
 
			else:	
				if (guess == 1):
					hi = (hi + lo) // 2
				elif (guess == -1):
					lo = (lo + hi) // 2
 
		if (guess != 0):
                        # print if the 7th guess the user still enter 1 or -1 
			print("\nEither you guessed a number out of range or you had an incorrect entry")
 
 
main()
