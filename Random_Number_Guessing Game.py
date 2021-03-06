#Random Number Guessing Game Simulator
import random        # A Random number is generated by the system b using this "random" library...
print('-----------------------------------------------------------------')
print('----------Welcome To The Number Guessing Game Simulator----------')
print('-----------------------------------------------------------------')
print('\n\n')
count=0
temp=0
if(count==0):
    players=int(input('---Please Enter The Number Of Players: '))    #You can enter no.of players to play
    if(players>=1 and players<=6):
        lowlm=int(input('---Enter The Lower Limit: '))
        highlm=int(input('---Enter The Higher Limit: '))       #Enter the higher and lower limits which the ramdom number will be generated in between them...
        if(lowlm>=0 and highlm<=10000):
            plyno=1
            ran=random.randint(lowlm,highlm)         #Random number is generated
            while(plyno==1):     # loop continues to give chances for all players again after each round, if no player won in first round...
                for i in range(1,players+1):      # this loop iterates by giving all players 1 chance for 1 round...
                    if(plyno>=1 and plyno<=players):
                        ply=int(input("---'Player-"+str(plyno)+"' --Enter Your Guess--: "))
                        if(ply>=lowlm and ply<=highlm):      
                            if(ply<ran):
                                print("'---Player-"+str(plyno)+"' --Your Guess Was LESSER Than Expected--")
                                plyno+=1
                            elif(ply>ran):
                                print("---'Player-"+str(plyno)+"'--Your Guess Was HIGHER Than Expected--")
                                plyno+=1
                            else:
                                print("--- CONGRATULATIONS---  'Player-"+str(plyno)+"' Has Won The Game By Guessing The Correct Number ---")
                                print('-----------------------------------------------------------------')
                                print("------------------------   GAME-OVER   ------------------------")
                                print('-----------------------------------------------------------------')
                                plyno+=7      # As I gave limit 6 for no.of players, by incrementing "plyno", by 7 the loop will be terminated and next round will be started...
                                count+=1
                                temp+=1
                        else:
                            print("----------Please Enter Your Guess Between "+str(lowlm)+" and "+str(highlm)+" ----------")
                    else:
                        plyno+=7        # Here "plyno" is incremented by 7, if  the "no.of players" condition is not satisfied and prompts user again to start... 
                if(temp==1):
                    plyno=0        # if any one of the players won in any round, all the iterations will be terminated and  the program ends...
                else:
                    plyno=1
            if(plyno>players):
                count+=1    # Here "count" is incremented to terminate the loop if the player number exceeds the No.of players limit..(just in case...)
        else:
            print("---------- Please Enter Lower And Higher Limit Between '0-10000' ----------")     # As i gave a range for both higher and lower limits, if u enter out of range, user will be prompted to start the game again....
    else:
        print("---------- Only Upto 6 Players Can Play This Game ------------")
        print("---------- Please Enter Number-Of-Players Between '1-6' --------")        # Same as i gave a limit "6" for no.of players, if u enter out of range, user will be prompted to start the game again... 