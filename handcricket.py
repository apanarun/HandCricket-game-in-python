from random import randint,choice
def com():
    return randint(0,10)
def hum():
    flag = 1
    while(flag!=0):
        tmp = input("Enter your value : ")
        if(int(tmp)>10):
            print("Wrong Value,Try between (0-10)")
        else:
            flag = 0
    return int(tmp)
def toss():
    print("It's Toss time!!!")
    tosschoice = input("Enter your choice(odd/even) : ")
    cchoice = randint(0,10)
    hchoice = hum()
    print("COmputer's choice : ",cchoice)
    if(((cchoice+hchoice)%2==0 and tosschoice=="even") or ((cchoice+hchoice)%2==1 and tosschoice=="odd")):
        toss = 1
        print("You won the toss")
    else:
        toss = 0
        print("You lost the toss")
    return toss
lis = ["bat","bowl"]
def batorbowl():
    optionh = ""
    if(toss()==1):
        flag = 0
        while(flag != 1):
            print("Choose your play")
            choicex = input("Enter your choice (bat/bowl) : ")
            if(choicex == "bat"):
                print("You chose to bat")
                flag=1
                optionh = "bat"
            elif(choicex == "bowl"):
                flag=1
                optionh = "bowl"
            else:
                print("Wrong choice, Try again")
    else:
        choicex = choice(lis)
        if(choicex=="bat"):
            print("Computer chose to Bat")
            optionh = "bowl"
        else:
            print("Computer chose to Bowl")
            optionh = "bat"
    return optionh

def cbat():
    hscore = 0
    cscore = 0
    hscoreboard = []
    cscoreboard = []
    flag = 0
    overs = int(input("Enter no of overs : "))
    wicketchoice = int(input("Enter no of wickets : ")) 
    balls = 1
    wickets = 1
    print("Its Bowling Time!!!")
    while(flag!=1):
        c = com()
        h = hum()
        print("Computer's value is ",c)
        if(c==h):
            if(wickets==wicketchoice):
                flag = 1
                print("I am Out")
                break
            else:
                wickets+=1
                cscoreboard.append("w")
                print("I lost a wicket ")
                print("Wickets remaining : ",wicketchoice-wickets+1)
        elif(balls==overs*6):
            cscore+=c
            cscoreboard.append(c)
            flag = 1
            print("Overs completed!!")
            break
        else:
            balls+=1
            cscore+=c
            cscoreboard.append(c)

    print("Your Target is ...",cscore)

    
    print("Its Batting Time!!!")
    flag = 0
    balls= 1
    wickets=1
    while(flag!=1):
        if(hscore>cscore):
            break
        c = com()
        h = hum()
        print("Computer's value is ",c)
        if(c==h):
            if(wickets==wicketchoice):
                flag = 1
                print("You are Out")
                break
            else:
                wickets+=1
                hscoreboard.append("w")
                print("You lost a wicket ")
                print("Wickets remaining : ",wicketchoice-wickets+1)
        elif(balls==overs*6):
            hscore+=h
            hscoreboard.append(h)
            flag = 1
            print("Overs completed!!")
            break
        else:
            balls+=1
            hscore+=h
            hscoreboard.append(h)
    return(hscore,cscore,hscoreboard,cscoreboard)
def hbat():
    hscore = 0
    cscore = 0
    hscoreboard = []
    cscoreboard = []
    flag=0
    overs = int(input("Enter no of overs : "))
    wicketchoice = int(input("Enter no of wickets : ")) 
    balls=1
    wickets=1
    print("Its Batting Time!!!")
    while(flag!=1):
        c = com()
        h = hum()
        print("Computer's value is ",c)
        if(c==h):
            if(wickets==wicketchoice):
                flag = 1
                print("You are Out")
                break
            else:
                wickets+=1
                cscoreboard.append("w")
                print("You lost a wicket ")
                print("Wickets remaining : ",wicketchoice-wickets+1)
        elif(balls==overs*6):
            hscore+=h
            hscoreboard.append(h)
            flag = 1
            print("Overs completed!!")
            break
        else:
            balls+=1
            hscore+=h
            hscoreboard.append(h)
    flag=0
    balls=1
    wickets=1

    print("Your Score is ...",hscore)

    
    print("Its Bowling Time")
    while(flag!=1):
        if(cscore>hscore):
            break
        c = com()
        h = hum()
        print("Computer's value is ",c)
        if(c==h):
            if(wickets==wicketchoice):
                flag = 1
                print("I am Out")
                break
            else:
                wickets+=1
                hscoreboard.append("w")
                print("I lost a wicket ")
                print("Wickets remaining : ",wicketchoice-wickets+1)
        elif(balls==overs*6):
            cscore+=c
            cscoreboard.append(c)
            flag = 1
            print("Overs completed!!")
            break
        else:
            balls+=1
            cscore+=c
            cscoreboard.append(c)

    return(hscore,cscore,hscoreboard,cscoreboard)
def output(result):
    hscore = result[0]
    cscore = result[1]
    hscoreboard = result[2]
    cscoreboard = result[3]
    if(hscore==cscore):
        print("Game is Tied")
    elif(hscore>cscore):
        print("You won the Game!!")
    else:
        print("You lost the Game")
    print("Scoreboard")
    print("Your score : ",hscore)
    j=0
    for i in hscoreboard:
        if(j%6==0):
            print("")
        j+=1
        print(i,end=" ")
    print("")
    j=0
    print("Computer Score : ",cscore)
    for i in cscoreboard:
        if(j%6==0):
            print("")
        j+=1
        print(i,end=" ")
    print("")
print("Welcome to Hand Cricket")
replay=1
while (replay!=0):
    hgameplay = batorbowl()
    if(hgameplay=="bat"):
        result = hbat()
    else:
        result = cbat()
    output(result)
    x = input("Do you want to Play again(y/n) : ")
    if(x=="n" or x=="N" or x=="no" or x=="No"):
        replay=0
        break



            
    
    
    
        
