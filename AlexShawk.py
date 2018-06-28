import random
import sys
import time 
#Settings
gameActive="yes"
balance = random.randint(0,500)
buyerNum= random.randint(0,1000)
supplyAlex = random.randint(10,30)
recivedMoney = 0
#Ingame Settings
SpellCheck = int(input("Would you like to enable Spell Check?(0/1): "))
print("For a more cinematic experience pick a speed")
speed = int(input("What speed would you like the repsonses? (0/1/2/3/4/5): "))

if speed == 1 or 2 or 3 or 4 or 5:
    if speed == 1:
        time.sleep(1)
    elif speed == 2:
        time.sleep(2)
    elif speed == 3:
        time.sleep(3)
    elif speed == 4:
        time.sleep(4)
    elif speed == 5:
        time.sleep(5)
while gameActive == "yes":
    if balance < 0:
        print("You have lost the game")
        print("Your game will now close")
        time.sleep(2)
        sys.exit(0)
    if supplyAlex > 0:
        print("Your Supply of Alexs to sell is", supplyAlex)
        print("Your balance is", "£", balance) 
        AlexShaw=input("How Much Is Alex Worth(You can purchase below or equal to your balance): £")
#Speed 1
        if speed == 1:
            time.sleep(1)
        elif speed == 2:
            time.sleep(2)
        elif speed == 3:
            time.sleep(3)
        elif speed == 4:
            time.sleep(4)
        elif speed == 5:
            time.sleep(5)      
        AlexShaw= int(AlexShaw)
        if AlexShaw > balance:
            while AlexShaw > balance:
                print("You can't buy your Alex Shaw with that money")
                AlexShaw=int(input("How Much Is Alex Worth(You can purchase below or equal to your balance): £"))
#Speed 2
        if speed == 1:
            time.sleep(1)
        elif speed == 2:
            time.sleep(2)
        elif speed == 3:
            time.sleep(3)
        elif speed == 4:
            time.sleep(4)
        elif speed == 5:
            time.sleep(5)          
        balance= balance-AlexShaw
        print("Your Alex Shaw is worth" ,"£",AlexShaw)
        if AlexShaw <= 100:
            buyerNum= random.randint(0,300)
        elif AlexShaw >= 200:
            buyerNum= random.randint(0,600)
        elif AlexShaw >= 300:
            buyerNum= random.randint(0,900)
        elif AlexShaw >= 400:
            buyerNum= random.randint(0,1200)
        elif AlexShaw >= 500:
            buyerNum= random.randint(0,1500)
        elif AlexShaw >= 1000:
            buyerNum= random.randint(0,3000)
        elif AlexShaw >= 1500:
            buyerNum= random.randint(0,4500)
        elif AlexShaw >= 2000:
            buyerNum= random.randint(0,6000)
        elif AlexShaw >= 3000:
            buyerNum= random.randint(0,9000)       
        elif AlexShaw >= 5000:
            buyerNum= random.randint(0,15000)
        else:
            print("An ERROR 01 Has Occured")
        print("A buyer wants to buy your Alex Shaw worth", "£", AlexShaw, "he wants to give you", "£",buyerNum)
        buy= str(input("Do you accept (Yes/No): "))
#Speed 3
        if speed == 1:
            time.sleep(1)
        elif speed == 2:
            time.sleep(2)
        elif speed == 3:
            time.sleep(3)
        elif speed == 4:
            time.sleep(4)
        elif speed == 5:
            time.sleep(5)    
        buy = buy.lower()
        if SpellCheck == 1:
            if "y" in buy:
                buy = "yes"
            elif "n" in buy:
                buy = "no"
            else:
                buy = "An ERROR 02 Has Occured"
        if buy == "yes":
            chance = random.randint(0,100)
            chanceMoney = random.randint(0,100)
            if chanceMoney >= 50:
                MoneyMaker = "Wallet"
            if chanceMoney < 50: 
                MoneyMaker = "Gold Bars"
            if chance >= 95:
                print("You found someones lost ", MoneyMaker, "on the floor and you picked it up")
                sell = str(input("Would you like to sell the "+ MoneyMaker + " (Yes/No): "))
                if SpellCheck == 1:
                    if "y" in sell:
                        sell = "yes"
                    elif "n" in sell:
                        sell = "no"
                    else:
                        sell = "An ERROR 03 Has Occured"
                if sell.upper() == "YES":
                    chanceWorth = random.randint(0,100)
                    if chanceWorth >= 50:
                        recivedMoney = 2000
                    if chanceWorth  < 50:
                        recivedMoney = 200

            print("Your new balance is now", "£", recivedMoney+balance+buyerNum-AlexShaw)
            recivedMoney = 0
            gameActive = str(input("Would you like to keep buying?(Yes/No): "))
#Speed 4
            if speed == 1:
                time.sleep(1)
            elif speed == 2:
                time.sleep(2)
            elif speed == 3:
                time.sleep(3)
            elif speed == 4:
                time.sleep(4)
            elif speed == 5:
                time.sleep(5)   
            if SpellCheck == 1:
                if "y" in gameActive:
                    gameActive = "yes"
                elif "n" in gameActive:
                    gameActive = "no"
                else:
                    buy = "An ERROR 03 Has Occured"
            balance = balance+buyerNum-AlexShaw
            gameActive = gameActive.lower()
            supplyAlex = supplyAlex-1
            if balance >= 5000:
                print("You now have enough money to buy some one to do this for you now gg!")
                gameActive = "no"
        elif buy == "no":
            chance = random.randint(0,100)
            if chance >= 50:
                print("Your Alex Shaw is now died you have lost your money")
                print("Your Balance is now £", balance-AlexShaw)
                balance = balance-AlexShaw
                supplyAlex= supplyAlex-1
            elif chance <= 49:
                print("Your balance has not changed")
            gameActive = str(input("Would you like to keep buying?(Yes/No): "))
#Speed 4
            if speed == 1:
                time.sleep(1)
            elif speed == 2:
                time.sleep(2)
            elif speed == 3:
                time.sleep(3)
            elif speed == 4:
                time.sleep(4)
            elif speed == 5:
                time.sleep(5)   
            if SpellCheck == 1:
                if "y" in gameActive:
                    gameActive = "yes"
                elif "n" in gameActive:
                    gameActive = "no"
                else:
                    buy = "An ERROR 03 Has Occured"
            balance = balance
            gameActive = gameActive.lower()
            if balance >= 5000:
                print("You now have enough money to buy some one to do this for you now gg!")
                gameActive = "no"
                         
        elif supplyAlex < 1:
            gameActive = "no"


