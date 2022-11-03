import random
l=['Rock','Paper','Scissor']

while True:
    Usercount = 0 
    Computercount = 0
    userchoice = int(input('''
    Game starting.......
    1 Yes
    2 No ! exit 
                '''))

    if userchoice == 1 :
        for i in range(1,6):
            userinput=int(input('''
            Choice your input.....
            1 Rock
            2 Paper
            3 Scissor 
                    '''))

            if userinput == 1:
                Yourchoice = "Rock"
            elif userinput == 2:
                Yourchoice="Paper"
            elif userinput == 3:
                Yourchoice="Scissor"
            ComputerChoice = random.choice(l)
            if (Yourchoice == ComputerChoice) :
                print("Your choice" , Yourchoice)
                print("Computer Choice" , ComputerChoice)
                print ("Game Draw")
                Computercount = Computercount+1
                Usercount = Usercount+1

            elif (Yourchoice == 'Rock' and ComputerChoice == 'Scissor') or (Yourchoice == 'Paper' and ComputerChoice == 'Rock') or (Yourchoice == 'Scissor' and ComputerChoice == 'Paper'):
                print("Your choice" , Yourchoice)
                print("Computer Choice" , ComputerChoice)
                print ("You Win")
                Usercount = Usercount+1
            else:
                print("Your choice" , Yourchoice)
                print("Computer Choice" , ComputerChoice)
                print ("Computer Win")
                ComputerChoice = Computercount+1
        if Usercount == Computercount :
            print("Finaly Game Draw...")
            print("user score",Usercount)
            print("Computer score",Computercount)
        elif Usercount > Computercount :
            print("Finaly you win the game...")
            print("user score",Usercount)
            print("Computer score",Computercount)
        else:
            print("Finaly computer win the game...")
            print("user score",Usercount)
            print("Computer score",Computercount)
    else:
        break
