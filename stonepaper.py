import random 

while True:
	
	list_choice = ["rock","paper","scissor"]
	print("Hope you all played Rock-Paper-Scissor Game")
	print("Lets start")
	user =input("please enter rock || paper || scissor: ").lower()
	#print(user)

	if user in list_choice:
		pass
	else :
		print("Please choose valid option ")
		print("\n")
		continue

	#using random to choose from list
	comp = random.choice(list_choice)
	#print(comp)
	print("\n")
	print("Yours choose",user)
	print("Computer choose",comp)

	print("\n")
	print("Result")


	#main game part
	if user == "rock" and comp == "rock":
				print("Draw")
	elif user == "rock" and comp == "paper":
				print("Computer WIN")
	elif user == "rock" and comp == "scissor":
				print("You WIN")
	elif user == "paper" and comp == "rock":
				print("You WIN")
	elif user == "paper" and comp == "paper":
				print("Draw")
	elif user == "paper" and comp == "scissor":
				print("Computer WIN")
	elif user == "scissor" and comp == "rock":
				print("Computer WIN")
	elif user == "scissor" and comp == "paper":
				print("You WIN")
	elif user == "scissor" and comp == "scissor":
				print("Draw")
	
	print("\n")

	end = input("Do you want to play again ? (Y/N)").upper()

	if end == "Y":
		continue
	else:
		exit()
		#break


				
