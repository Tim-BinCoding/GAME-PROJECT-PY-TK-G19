

from tkinter import*
from winsound import*
import winsound
import random
root = Tk()
root.resizable(0,0)
root.title("Creatby@Tim&Ulvy")
canvas = Canvas(width=1200, height=800)
################ IMAGES ###################################
bgGame = PhotoImage(file="images\space.gif")
displayBG = PhotoImage(file="images\MacBook.png")
rule = PhotoImage(file="images\scenario.png")
slid1 = PhotoImage(file="images\slid1.png")
slid2 = PhotoImage(file="images\sild2.png")
slid3 = PhotoImage(file="images\sild3.png")
player2 = PhotoImage(file="images\planefight.gif")
player1 = PhotoImage(file="images\plane4.gif")
enimies1 = PhotoImage(file="images\enymie.gif")
enimies2 = PhotoImage(file="images\Enimies.gif")
boom = PhotoImage(file="images\pbreakBoom.gif")
power = PhotoImage(file="images\super.gif.png")
well = PhotoImage(file="images\well.png")
################################### VIRIBALE ####################################################
Ax=0
Ay=0
positionEnimies=0
second=0
minut=0
blood=0
notEvent=False
nothingEnimies1=False
nothingEnimies2=False
nothingEnimies3=False
nothingEnimies4=False
players=player1
countEnimies=0
score=0
powerBullet='red'
######################### DISPLAY INTERFAC ########################
def displayGame():
    canvas.delete('all')
    winsound .PlaySound("Audioes\startGame.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
    canvas.create_image(600,320,image=displayBG)
    canvas.create_text(600,240,text="PLAY",font=('sansarif',28,'bold'),fill='red',tags='start')
    canvas.create_text(600,320,text="HELP",font=('sansarif',28,'bold'),fill='red',tags='rule')
    canvas.create_text(600,400,text="EXIT",font=('sansarif',28,'bold'),fill='red',tags='exit')
displayGame()

####### START GAME ######3
def startGame(event):
    canvas.delete('all')
    showSlid1()
    winsound .PlaySound("Audioes\space-war.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
def showSlid1():
    canvas.create_image(600,320,image=slid1)
    canvas.after(1000,showSlid2)
def showSlid2():
    canvas.create_image(600,320,image=slid2)
    canvas.after(1000,showSlid3)
def showSlid3():
    canvas.create_image(600,320,image=slid3)
    canvas.create_text(600,320,text="Loading...",font=('sansarif',28,'bold'),fill='red')
    canvas.after(2000,startPlay)
canvas.tag_bind('start',"<Button-1>",startGame)

######## SCENARIO GAME #######3
def scenarioGame(event):
    canvas.delete('all')
    canvas.create_image(600,300,image=rule)
    canvas.create_text(585,540,text="BACK",font=('sansarif',28,'bold'),fill='red',tags='back')
canvas.tag_bind('rule',"<Button-1>",scenarioGame)

################################ BACK DISPLAYGAME ##############################################
def backDisplay(event):
   displayGame()
canvas.tag_bind('back',"<Button-1>",backDisplay)

################################################ Play GAME #########################################
def startPlay():
    canvas.delete('all')
    global notEvent,nothingEnimies1,nothingEnimies2,nothingEnimies3,nothingEnimies4,minut,second,Ax,Ay,score
    notEvent=nothingEnimies1=nothingEnimies2=nothingEnimies3=nothingEnimies4=False
    if notEvent==False:  
        canvas.create_image(600,300,image=bgGame)
        addEnimies1()
        moveEnimies()
        playBullet()
        timeOfSTART()
        checkEvent()
        indentifyBlood()
        playerBorken()
        createBullet()
        planPlayer()
        minut=0
        second=0
        score=0
        countEnimies=0
        powerBullet='red'
        players=player1
############################## COUNT TIME ######################################################
def timeOfSTART():
    global second, minut,countLife,blood,notEvent,score
    if notEvent == False:
        canvas.delete('blood')
        canvas.delete('score')
        second+=1
        canvas.itemconfig('timer',text="Time : "+str(minut) + " : "+str(second))
        if second==60:
            minut+=1
            second=0
        if blood<=190:
            canvas.create_rectangle(1000,10,1190-blood,20,fill='red',tags='blood',outline='')
        canvas.create_text(1140,40,text=str(score),font=('sansarif',15,'bold'),fill='red',tags='score')
        canvas.after(1000,timeOfSTART)
    # canvas.create_text(590,240,text="SCORE : " +str(score),font=('sansarif',15,'bold'),fill='red')
################ CHECK BLOOD PLAYER #######
def indentifyBlood():
    canvas.create_rectangle(1000,10,1190,20,fill='white',outline='')
    canvas.create_rectangle(1090,25,1190,50,fill='cyan',outline='')
    canvas.create_text(1040,40,text='SCORE:',font=('sansarif',15,'bold'),fill='red')
    canvas.create_text(130,30,text='',font=('sansarif',25,'bold'),fill='white',tags='timer')
################################### PLAYER ###################################################
def planPlayer():
    global Ax,Ay,notEvent
    canvas.delete('player')
    if notEvent==False:
        canvas.create_image(600+Ax,550+Ay,image=players,tags='player')
      
#################################### CREATE BULLET #################################################
def createBullet():
    global notEvent,Ax,Ay,powerBullet
    if notEvent==False: 
        canvas.delete('bullet')
        canvas.create_rectangle(585+Ax,440+Ay,595+Ax,480+Ay,fill=powerBullet,tags="bullet",outline='')
        canvas.create_rectangle(600+Ax,440+Ay,610+Ax,480+Ay,fill=powerBullet,tags="bullet",outline='')
        canvas.after(500,createBullet)

############### SHOOT BULLET ##########
def playBullet():
    global notEvent
    if notEvent==False:
        canvas.move("bullet",0,-2)
        canvas.after(1,playBullet)
    
#################################### ADD ENIMIES #####################################3########
def addEnimies1():
    global notEvent
    if notEvent==False:
        positionEnimies=random.randrange(100,300)
        canvas.create_image(positionEnimies,10,image=random.choice([str(enimies1),str(enimies2)]),tags='enimies1')
        canvas.after(1500, addEnimies2)
def addEnimies2():
    global notEvent
    if notEvent==False:
        positionEnimies=random.randrange(350,550)
        canvas.create_image(positionEnimies,10,image=random.choice([str(enimies1),str(enimies2)]),tags='enimies2')
        canvas.after(2000, addEnimies3)
def addEnimies3():
    global notEvent
    if notEvent==False:
        positionEnimies=random.randrange(600,850)
        canvas.create_image(positionEnimies,40,image=random.choice([str(enimies1),str(enimies2)]),tags='enimies3')
        canvas.after(2500, addEnimies4)
def addEnimies4():
    global notEvent
    if notEvent==False:
        positionEnimies=random.randrange(550,950)
        canvas.create_image(positionEnimies,50,image=random.choice([str(enimies1),str(enimies2)]),tags='enimies4')
        canvas.after(3000, addEnimies1)
    
##################################### MOVE ENIMIES ###############################################
def moveEnimies():
    global notEvent
    if notEvent==False:
        canvas.move('enimies1',0,1)
        canvas.move('enimies2',0,1)
        canvas.move('enimies3',0,1)
        canvas.move('enimies4',0,1)
        canvas.after(40,moveEnimies)

############## CHECK EVENT #########################
def checkEvent():
    global nothingEnimies1,nothingEnimies2,nothingEnimies3,nothingEnimies4,countEnimies,players,player1,player2,notEvent,score,powerBullet
    ############# ENIMIES MEET BULLET ####################
    if not nothingEnimies1 and len(canvas.coords("enimies1"))!=0 and len(canvas.coords("bullet"))!=0:
        x1Bullet=canvas.coords('bullet')[0]
        x2Bullet=canvas.coords('bullet')[2]
        y1Bullet=canvas.coords('bullet')[1]
        y2Bullet=canvas.coords('bullet')[3]
        if not nothingEnimies1 and (x1Bullet-60<=canvas.coords("enimies1")[0] and x2Bullet+60>=canvas.coords("enimies1")[0]) and y1Bullet-150<=canvas.coords("enimies1")[1] :
            countEnimies+=1
            score+=1
            winsound .PlaySound("Audioes\system-break.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
            canvas.create_image(canvas.coords("enimies1")[0],canvas.coords("enimies1")[1],image=boom,tags='boom')
            canvas.delete("enimies1")
            canvas.delete('bullet')
            nothingEnimies1=True
    if len(canvas.coords("enimies1"))==0 and nothingEnimies1==True:
        nothingEnimies1=False
       
    ############# ENIMIES2 #############
    if not nothingEnimies2 and len(canvas.coords("enimies2"))!=0 and len(canvas.coords("bullet"))!=0:
        x1Bullet=canvas.coords('bullet')[0]
        x2Bullet=canvas.coords('bullet')[2]
        y1Bullet=canvas.coords('bullet')[1]
        y2Bullet=canvas.coords('bullet')[3]
        if not nothingEnimies2 and x1Bullet-60<=canvas.coords("enimies2")[0] and x2Bullet+60>=canvas.coords("enimies2")[0] and y1Bullet-150<=canvas.coords("enimies2")[1]:
            countEnimies+=1
            score+=1
            winsound .PlaySound("Audioes\system-break.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
            canvas.create_image(canvas.coords("enimies2")[0],canvas.coords("enimies2")[1],image=boom,tags='boom')
            canvas.delete("enimies2")
            canvas.delete('bullet')
            nothingEnimies2=True
    if len(canvas.coords("enimies2"))==0 and nothingEnimies2==True:
        nothingEnimies2=False
    ################ ENIMIES 3 & 4 ###################
    if not nothingEnimies3 and len(canvas.coords("enimies3"))!=0 and len(canvas.coords("bullet"))!=0:
        x1Bullet=canvas.coords('bullet')[0]
        x2Bullet=canvas.coords('bullet')[2]
        y1Bullet=canvas.coords('bullet')[1]
        y2Bullet=canvas.coords('bullet')[3]
        if not nothingEnimies1 and x1Bullet-60<=canvas.coords("enimies3")[0] and x2Bullet+60>=canvas.coords("enimies3")[0] and y1Bullet-150<=canvas.coords("enimies3")[1]:
            countEnimies+=1
            score+=1
            winsound .PlaySound("Audioes\system-break.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
            canvas.create_image(canvas.coords("enimies3")[0],canvas.coords("enimies3")[1],image=boom,tags='boom')  
            canvas.delete("enimies3")
            canvas.delete('bullet')
            nothingEnimies3=True
    if len(canvas.coords("enimies3"))==0 and nothingEnimies3==True:
        nothingEnimies3=False
    ############# ENIMIES 4 #############
    if not nothingEnimies2 and len(canvas.coords("enimies4"))!=0 and len(canvas.coords("bullet"))!=0:
        x1Bullet=canvas.coords('bullet')[0]
        x2Bullet=canvas.coords('bullet')[2]
        y1Bullet=canvas.coords('bullet')[1]
        y2Bullet=canvas.coords('bullet')[3]
        if not nothingEnimies4 and x1Bullet-60<=canvas.coords("enimies4")[0] and x2Bullet+60>=canvas.coords("enimies4")[0] and y1Bullet-150<=canvas.coords("enimies4")[1]:
            countEnimies+=1
            score+=1
            winsound .PlaySound("Audioes\system-break.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
            canvas.create_image(canvas.coords("enimies4")[0],canvas.coords("enimies4")[1],image=boom,tags='boom')
            canvas.delete("enimies4")
            canvas.delete('bullet')
            nothingEnimies4=True
        
    if len(canvas.coords("enimies4"))==0 and nothingEnimies4==True:
        nothingEnimies4=False
    if countEnimies==20:
        canvas.create_image(600,320,image=power,tags='power')
        powerBullet = 'blue'
        canvas.after(500,getPower)
        players=player2
    elif countEnimies==40:
        powerBullet='green'
        canvas.create_image(600,320,image=power,tags='power')
        canvas.after(500,getPower)
    if notEvent==False:
        canvas.after(200,checkEvent)
        canvas.after(900,removeBoom)
    
######### DELETE BOOM ##########3
def removeBoom():
    canvas.delete('boom')
    
############# GET POWER ###########
def getPower():
     canvas.delete('power')
     
############ ENIMIES MET PLAYER ##############3
def playerBorken():
    global notEvent,blood
    if len(canvas.coords("enimies1"))!=0 and len(canvas.coords('player'))!=0:
        if canvas.coords("enimies1")[0]-30<= canvas.coords('player')[0] and canvas.coords("enimies1")[0]+30 >= canvas.coords('player')[0] and canvas.coords("enimies1")[1]+30 >= canvas.coords('player')[1]:
            notEvent=True
            blood=190
            canvas.create_image(600,320,image=well,tags='well')
            canvas.delete('player')
            canvas.after(1000,finishedGame) 
    if len(canvas.coords("enimies2"))!=0 and len(canvas.coords('player'))!=0:
        if canvas.coords("enimies2")[0]-30<= canvas.coords('player')[0] and canvas.coords("enimies2")[0]+30 >= canvas.coords('player')[0] and canvas.coords("enimies2")[1]+30 >= canvas.coords('player')[1]:
            notEvent=True
            blood=190
            canvas.create_image(600,320,image=well,tags='well')
            canvas.delete('player')
            canvas.after(1000,finishedGame)
    if notEvent==False:
        canvas.after(500,playerBorken)
    
#################### THE FINISH OF GAME ############
def finishedGame():
    global score
    canvas.delete("all")
    canvas.create_image(600,320,image=displayBG)
    canvas.create_text(590,240,text="SCORE : " +str(score),font=('sansarif',15,'bold'),fill='red')
    canvas.create_text(600,320,text="RESTART",font=('sansarif',20,'bold'),fill='red',tags='back')
    canvas.create_text(600,400,text="EXIT",font=('sansarif',20,'bold'),fill='red',tags='exit')
    
############ BUTTON ######################
def moveRight(event):
    global Ax,Ay,notEvent
    if notEvent==False:
        if canvas.coords('player')[0]<1100: 
            Ax+=30
            planPlayer()
root.bind("<Right>",moveRight)
def moveLeft(event):
    global Ax,Ay,notEvent
    if notEvent==False:
        if canvas.coords('player')[0]>100: 
            Ax-=100
            planPlayer()
root.bind("<Left>",moveLeft)
def moveUp(event):
    global Ax,Ay,notEvent
    if notEvent==False:
        if canvas.coords('player')[1] > 100:
            Ay-=100
            planPlayer()
root.bind("<Up>",moveUp)
def moveDown(event):
    global Ax,Ay,notEvent
    if notEvent==False:
        if canvas.coords('player')[1] < 650:
            Ay+=100
            planPlayer()
root.bind("<Down>",moveDown)
############################ exit game ###################################
def exitedGame(event):
    root.quit()
canvas.tag_bind('exit',"<Button-1>",exitedGame)

canvas.pack()
root.mainloop()
