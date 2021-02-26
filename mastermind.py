import random


def run_game():
    
    #function creates random list 
    randomlist= []
    for i in range(0,4):
        n = random.randint(1,8)
        randomlist.append(n)
    # print (randomlist)
    print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.")
    

    correct = False
    tries = 12
    while not correct and tries > 0:
        userguess = input("Input 4 digit code:")
        if len(userguess) < 4 or len(userguess) > 4:
            print(" Please enter exactly 4 digits.")
            continue
        #takes apostrophes out of list
        guesslist = [int(d) for d in userguess]
        # print (guesslist)
        
        tries = tries - 1
        correctpos = 0
        incorrect = 0
        for i in range(0,4):
            if (guesslist[i] == randomlist[i]):
                correctpos = correctpos + 1
            if (guesslist[i] in randomlist):
                incorrect = incorrect + 1
        incorrect = incorrect - correctpos
        print(" Number of correct digits in correct place:    ",correctpos)
        print("Number of correct digits not in correct place:",incorrect)
        if tries != 0 and guesslist != randomlist:
            print("Turns left:",tries)
        elif guesslist == randomlist:
            print("Congratulations! You are a codebreaker!")
            print("The code was: ",*randomlist,sep="")
            break


if __name__ == "__main__":
    run_game()