import random
while True:
    try :
        print("1: Rock ")
        print("2: Paper ")
        print("3: Scissors")
        x=int(input ("Enter your choice to play   "))
        
        if x<0 or x>3:
            print ("Plz enter enter in given limit (1-3)")
        
        lst=["Rock","Paper","Scissors"]
        
        y= random.choice(lst)
        if y=="Rock" and x == 3:
            print("Ohoo! i choose rock and you lose ")
        elif y=="Paper" and x == 1:
            print("Ohoo! i choose paper and you lose ")
        elif y=="Scissors" and x == 2:
            print("Ohoo! i choose scissor and you lose ")
        elif y=="Rock" and x == 2:
            print("i choose rock  you win ")
        elif y=="Paper" and x ==3 :
            print("Ohoo! i choose paper  you win ")
        elif y=="Scissors" and x == 1:
            print("Ohoo! i choose scissors  you win ")
        elif y=="Rock" and x == 1:
            print("Ohoo! same choice ")
        elif y=="Paper" and x == 2:
            print("Ohoo! same choice ")
        elif y=="Scissors" and x == 3:
            print("Ohoo! same choice ")
            
            
    except:
        print("plz enter value in integers")