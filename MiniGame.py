from bangtal import *
from random import randint
import random
import time

setGameOption(GameOption.INVENTORY_BUTTON,False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON,False)
setGameOption(GameOption.ROOM_TITLE, False)

mainScene = Scene("main","Images/배경.png")
samePictureScene = Scene("같은 그림 찾기", "images/배경.png")
samePicturePauseScene = Scene("같은 그림 찾기","Images/배경.png")
snakeScene = Scene("지렁이게임","Images/배경.png")
snakePauseScene = Scene("뱀게임","Images/배경.png")
wormScene = Scene("지렁이게임","Images/배경.png")
dinoScene = Scene("공룡게임","Images/배경.png")

samePictureStart = Object("Images/같은그림찾기.png")
samePictureStart.locate(mainScene,500,550)
samePictureStart.show()

snakeStart = Object("Images/뱀게임.png")
snakeStart.locate(mainScene,500,400)
snakeStart.show()

wormStart = Object("Images/지렁이게임.png")
wormStart.locate(mainScene,500,250)
wormStart.show()

dinoStart = Object("Images/공룡게임.png")
dinoStart.locate(mainScene,500,100)
dinoStart.show()

record1 = Object("Images/record.png")
record1.setScale(0.5)
record1.locate(mainScene,770,580)
record1.show()

record2 = Object("Images/record.png")
record2.setScale(0.5)
record2.locate(mainScene,770,430)
record2.show()

record3 = Object("Images/record.png")
record3.setScale(0.5)
record3.locate(mainScene,770,280)
record3.show()

record4 = Object("Images/record.png")
record4.setScale(0.5)
record4.locate(mainScene,770,130)
record4.show()

def record1_onMouseAction(x,y,action):
    if(record_time==0):
        showMessage("기록 없음")
    else:
        showMessage(format(record_time,".2f")+"초")
record1.onMouseAction = record1_onMouseAction

def record2_onMouseAction(x,y,action):
    if(record_score==-1):
        showMessage("기록 없음")
    else:
        showMessage(format(record_score,"d")+"점")       
record2.onMouseAction = record2_onMouseAction

def record3_onMouseAction(x,y,action):
    if(worm_record_score==-1):
        showMessage("기록 없음")
    else:
        showMessage(format(worm_record_score,"d")+"점")       
record3.onMouseAction = record3_onMouseAction

def record4_onMouseAction(x,y,action):
    if(dino_record_score==-1):
        showMessage("기록 없음")
    else:
        showMessage(format(dino_record_score,"d")+"점")       
record4.onMouseAction = record4_onMouseAction

def samePictureStart_onMouseAction(x,y,action):
    samePictureScene.enter()
    samePictureStartFunction()
samePictureStart.onMouseAction = samePictureStart_onMouseAction

def snakeStart_onMouseAction(x,y,action):
    snakeScene.enter()
    snakeStartFunction()
snakeStart.onMouseAction = snakeStart_onMouseAction

def wormStart_onMouseAction(x,y,action):
    wormScene.enter()
    wormStartFunction()
wormStart.onMouseAction = wormStart_onMouseAction

def dinoStart_onMouseAction(x,y,action):
    dinoScene.enter()
    dinoStartFunction()
dinoStart.onMouseAction = dinoStart_onMouseAction

mainMenu = Object("Images/main.png")
newGameMenu = Object("Images/newGame.png")
snakeNewGameMenu = Object("Images/newGame.png")
wormNewGameMenu = Object("Images/newGame.png")
dinoNewGameMenu = Object("Images/newGame.png")
endMenu = Object("Images/end.png")

mainMenu.setScale(1.3)
newGameMenu.setScale(1.3)
snakeNewGameMenu.setScale(1.3)
wormNewGameMenu.setScale(1.3)
dinoNewGameMenu.setScale(1.3)
endMenu.setScale(1.3)

mainMenu.locate(samePictureScene,570,450)
newGameMenu.locate(samePicturePauseScene,570,350)
snakeNewGameMenu.locate(snakeScene,570,350)
wormNewGameMenu.locate(wormScene,570,350)
dinoNewGameMenu.locate(dinoScene,570,350)
endMenu.locate(samePictureScene,570,250)

next = Object("Images/SamePicture/next.png")
samePicturePause = Object("Images/SamePicture/pause.png")
snakePause = Object("Images/Snake/pause.png")

samePicturePause.setScale(0.4)
snakePause.setScale(0.4)

next.locate(samePictureScene,400,200)
samePicturePause.locate(samePictureScene,1200,650)
snakePause.locate(snakeScene,1200,650)

pic0 = Object("Images/SamePicture/카드뒷면.png")
pic1 = Object("Images/SamePicture/카드뒷면.png")
pic2 = Object("Images/SamePicture/카드뒷면.png")
pic3 = Object("Images/SamePicture/카드뒷면.png")
pic4 = Object("Images/SamePicture/카드뒷면.png")
pic5 = Object("Images/SamePicture/카드뒷면.png")
pic6 = Object("Images/SamePicture/카드뒷면.png")
pic7 = Object("Images/SamePicture/카드뒷면.png")
pic8 = Object("Images/SamePicture/카드뒷면.png")
pic9 = Object("Images/SamePicture/카드뒷면.png")
pic10 = Object("Images/SamePicture/카드뒷면.png")
pic11 = Object("Images/SamePicture/카드뒷면.png")
pic12 = Object("Images/SamePicture/카드뒷면.png")
pic13 = Object("Images/SamePicture/카드뒷면.png")
pic14 = Object("Images/SamePicture/카드뒷면.png")
pic15 = Object("Images/SamePicture/카드뒷면.png")

picture0 = Object("Images/SamePicture/카드뒷면.png")
picture1 = Object("Images/SamePicture/카드뒷면.png")
picture2 = Object("Images/SamePicture/카드뒷면.png")
picture3 = Object("Images/SamePicture/카드뒷면.png")
picture4 = Object("Images/SamePicture/카드뒷면.png")
picture5 = Object("Images/SamePicture/카드뒷면.png")
picture6 = Object("Images/SamePicture/카드뒷면.png")
picture7 = Object("Images/SamePicture/카드뒷면.png")
picture8 = Object("Images/SamePicture/카드뒷면.png")
picture9 = Object("Images/SamePicture/카드뒷면.png")
picture10 = Object("Images/SamePicture/카드뒷면.png")
picture11 = Object("Images/SamePicture/카드뒷면.png")
picture12 = Object("Images/SamePicture/카드뒷면.png")
picture13 = Object("Images/SamePicture/카드뒷면.png")
picture14 = Object("Images/SamePicture/카드뒷면.png")
picture15 = Object("Images/SamePicture/카드뒷면.png")

pic = [pic0,pic1,pic2,pic3,pic4,pic5,pic6,pic7,pic8,pic9,pic10,pic11,pic12,pic13,pic14,pic15]
picture = [picture0,picture1,picture2,picture3,picture4,picture5,picture6,picture7,picture8,picture9,picture10,picture11,picture12,picture13,picture14,picture15]

count = [0] * 8
samePicturePause_clicked = False
duringsamePicturePause_time = 0
samePicturePause_time = 0
replay_time = 0
totalsamePicturePause_time = 0
random_num = 0
show = 0
click = [0] * 2
record_time = 0

def endMenu_onMouseAction(x,y,action):
    endGame()
endMenu.onMouseAction = endMenu_onMouseAction

level = 1
def mainMenu_onMouseAction(x,y,action):
    global level
    samePictureClearSetting()
    level = 1
    mainScene.enter()
mainMenu.onMouseAction = mainMenu_onMouseAction

def samePictureStartFunction():
    global level, start_time
    level = 1
    mainMenu.hide()
    samePicturePause.show()
    next.hide()
    newGameMenu.locate(samePicturePauseScene,570,350)
    newGameMenu.hide()
    endMenu.hide()
    levelPictureShow()
    samePictureClearSetting()
    start_time = time.time()
    samePicturePause.setImage("Images/SamePicture/pause.png")
    samePicturePause.locate(samePictureScene,1200,650)
    samePicturePause.show()
    levelPicShow()

def snakeStartFunction():
    global score,snake,apple_x,apple_y,random_apple_x,random_apple_y
    score = 0
    for i in range(len(snake)):
        snake[i].hide()
    snake.clear()
    mainMenu.hide()
    createApple()
    snakeNewGameMenu.locate(snakePauseScene,570,350)
    snakeNewGameMenu.hide()
    endMenu.hide()
    snake.append(Object("Images/Snake/snake.png"))
    snake[0].x = 620
    snake[0].y = 340
    snake[0].locate(snakeScene,snake[0].x,snake[0].y)
    snake[0].show()
    random_apple_x = randint(2,28)
    random_apple_y = randint(2,14)
    apple_x = random_apple_x * 40+20
    apple_y = random_apple_y * 40+20
    apple.locate(snakeScene,apple_x,apple_y)
    timer1.set(10000)
    timer1.start()

def wormStartFunction():
    global ball_x,ball_y,checkk,worm_score, chkk
    checkk = 1
    chkk = 0
    ball_x = 625
    ball_y = 200
    mainMenu.hide()
    wormNewGameMenu.locate(wormScene,570,350)
    wormNewGameMenu.hide()
    endMenu.hide()
    worm_score = 0
    ball.clear()
    ball.append(blackball)
    ball.append(blueball)
    ball.append(greenball)
    ball.append(redball)
    ball.append(yellowball)
    ball.append(whiteball)
    for i in range(6):
        ball[i].color = i
        ball[i].locate(wormScene,ball_x,ball_y-i*35)
        ball[i].show()
    for i in range(len(downball[1])):
        downball[1][i].hide()
    for i in range(len(downball[0])):
        downball[0][i].hide()
    randomBallCreate()
    timer5.stop()
    timer6.stop()
    timer4.set(0.05)
    timer4.start()

dinosaur = Object("Images/Dinosaur/dinosaur.png")
dinosaur_x = 100
dinosaur_y = 100
dinosaur.locate(dinoScene,dinosaur_x,dinosaur_y)
dinosaur.setScale(0.3)

cactus = Object("Images/Dinosaur/cactus.png")
cactus_x = 1200
cactus_y = 100
cactus.locate(dinoScene,800,100)
cactus.setScale(0.5)
def dinoStartFunction():
    global count,cactus_x,cactus_y,dino_score
    randomSpeed = 7
    mainMenu.hide()
    dinoNewGameMenu.hide()
    endMenu.hide()
    dino_score = 0
    cactus_x = 1200
    cactus_y = 100
    count = 0
    dinosaur.show()
    cactus.show()
    timer3.set(0.1)
    timer3.start()

def dinoNewGameMenu_onMouseAction(x,y,action):
    dinoStartFunction()
dinoNewGameMenu.onMouseAction = dinoNewGameMenu_onMouseAction

timer2 = Timer(10000)
timer3 = Timer(10000)
count = 0
def dinoScene_onKeyboard(key,pressed):
    global dinosaur_x,dinosaur_y,count
    if(key == 75 and count == 0):
        timer2.set(0.4)
        timer2.start()
        dinosaur.locate(dinoScene,dinosaur_x,dinosaur_y+150)
        dinosaur.show()
        count = 1
dinoScene.onKeyboard = dinoScene_onKeyboard

def timer2_onTimeout():
    global dinosaur_x,dinosaur_y,count
    dinosaur.locate(dinoScene,dinosaur_x,dinosaur_y)
    dinosaur.show()
    count = 0
timer2.onTimeout = timer2_onTimeout

dino_score = 0
dino_record_score = -1
randomSpeed = 7
def timer3_onTimeout():
    global cactus_x,cactus_y,count,dino_score,dino_record_score,randomSpeed
    timer3.set(randomSpeed/100)
    timer3.start()
    cactus_x -=50
    if(cactus_x<0):
        cactus_x = 1200
        dino_score += 10
        randomSpeed = randint(3,7)
    if((cactus_x==150 and count==0) or (cactus_x == 50 and count == 0)):
        timer2.stop()
        timer3.stop()
        count = 1
        if(dino_score>dino_record_score or dino_record_score == -1):
                dino_record_score = dino_score
                showMessage("점수는 "+str(dino_record_score)+"점입니다."+"\n최고 기록입니다.")
        else:
                showMessage("점수는 "+str(dino_score)+"점입니다.")
        mainMenu.locate(dinoScene,570,450)
        dinoNewGameMenu.locate(dinoScene,570,350)
        endMenu.locate(dinoScene,570,250)
        mainMenu.show()
        dinoNewGameMenu.show()
        endMenu.show()
    cactus.locate(dinoScene,cactus_x,cactus_y)
    cactus.show()
timer3.onTimeout = timer3_onTimeout

def levelPictureShow():
    count = [0]*8
    if(level == 1):
        x = y = 200
        for i in range(8):
            pic[i].setScale(0.5)
            picture[i].setScale(0.5)
            picture[i].random_num=0
            if(i<4):
                pic[i].locate(samePictureScene,x,450)
                picture[i].locate(samePictureScene,x,450)
                x = x + 250
            else:
                pic[i].locate(samePictureScene,y,150)
                picture[i].locate(samePictureScene,y,150)
                y = y + 250
    elif(level == 2):
        x = y = 100
        for i in range(12):
            pic[i].setScale(0.5)
            picture[i].setScale(0.5)
            picture[i].random_num=0
            if(i<6):
                pic[i].locate(samePictureScene,x,450)
                picture[i].locate(samePictureScene,x,450)
                x = x + 200
            else:
                pic[i].locate(samePictureScene,y,150)
                picture[i].locate(samePictureScene,y,150)
                y = y + 200
    elif(level == 3):
        x = y = 50
        for i in range(16):
            pic[i].setScale(0.5)
            picture[i].setScale(0.5)
            picture[i].random_num=0
            if(i<8):
                pic[i].locate(samePictureScene,x,450)
                picture[i].locate(samePictureScene,x,450)
                x = x + 150
            else:
                pic[i].locate(samePictureScene,y,150)
                picture[i].locate(samePictureScene,y,150)
                y = y + 150

def levelPicShow():
    global level
    next.hide()
    samePicturePause.show()
    if(level == 1):
        for i in range(8):
            pic[i].show()
    elif(level == 2):
        for i in range(12):
            pic[i].show()
    else:
        for i in range(16):
            pic[i].show()

def next_onMouseAction(x,y,action):
    global start_time, totalsamePicturePause_time, check, set, count, level
    level+=1
    samePictureClearSetting()
    levelPictureShow()
    samePicturePause.show()
    start_time = time.time()
    next.hide()
    levelPicShow()
next.onMouseAction = next_onMouseAction

def samePicturePause_onMouseAction(x,y,action):
    global duringsamePicturePause_time, samePicturePause_time, replay_time, totalsamePicturePause_time, samePicturePause_clicked
    samePicturePause_clicked = not samePicturePause_clicked
    if samePicturePause_clicked:
        samePicturePauseScene.enter()
        samePicturePause_time = time.time()
        samePicturePause.setImage("Images/SamePicture/play.png")
        samePicturePause.locate(samePicturePauseScene,1200,650)
        newGameMenu.locate(samePicturePauseScene,570,350)
        mainMenu.locate(samePicturePauseScene,570,450)
        endMenu.locate(samePicturePauseScene,570,250)
        newGameMenu.show()
        mainMenu.show()
        endMenu.show()
    else:
        timer1.set(10000)
        timer1.start()
        samePictureScene.enter()
        replay_time = time.time()
        samePicturePause.setImage("Images/SamePicture/pause.png")
        samePicturePause.locate(samePictureScene,1200,650)
        newGameMenu.locate(samePictureScene,570,350)
        mainMenu.locate(samePictureScene,570,450)
        endMenu.locate(samePictureScene,570,250)
        newGameMenu.hide()
        mainMenu.hide()
        endMenu.hide()
        duringsamePicturePause_time = replay_time - samePicturePause_time
        totalsamePicturePause_time = totalsamePicturePause_time + duringsamePicturePause_time
samePicturePause.onMouseAction = samePicturePause_onMouseAction

def newGameMenu_onMouseAction(x,y,action):
    samePictureScene.enter()
    samePictureStartFunction()
newGameMenu.onMouseAction = newGameMenu_onMouseAction

def snakeNewGameMenu_onMouseAction(x,y,action):
    snakeScene.enter()
    snakeStartFunction()
snakeNewGameMenu.onMouseAction = snakeNewGameMenu_onMouseAction

def wormNewGameMenu_onMouseAction(x,y,action):
    wormScene.enter()
    wormStartFunction()
wormNewGameMenu.onMouseAction = wormNewGameMenu_onMouseAction

def samePictureClearSetting():
    global show, random_num, check, start_time, end_time, duringsamePicturePause_time, totalsamePicturePause_time, click, set, count, samePicturePause_clicked
    samePicturePause_clicked = False
    show = 0
    random_num = 0
    check = 0
    start_time = 0
    end_time = 0
    duringsamePicturePause_time = 0
    totalsamePicturePause_time = 0
    click = [0]*2
    set = [False]*16
    count = [0]*8
    for i in range(16):
        pic[i].hide()
        picture[i].hide()

def changeCardImage(pic_num):
    global count, set, random_num, level
    if(level == 1):
        random_num = randint(0,3)
        if(count[random_num] == 2):
            while(count[random_num] == 2):
                random_num = randint(0,3)
        if(random_num == 0):
            picture[pic_num].setImage("Images/SamePicture/0.png")
        elif(random_num == 1):
            picture[pic_num].setImage("Images/SamePicture/1.png")
        elif(random_num == 2):
            picture[pic_num].setImage("Images/SamePicture/2.png")
        elif(random_num == 3):
            picture[pic_num].setImage("Images/SamePicture/3.png")
    elif(level == 2):
        random_num = randint(0,5)
        if(count[random_num] == 2):
            while(count[random_num] == 2):
                random_num = randint(0,5)
        if(random_num == 0):
            picture[pic_num].setImage("Images/SamePicture/0.png")
        elif(random_num == 1):
            picture[pic_num].setImage("Images/SamePicture/1.png")
        elif(random_num == 2):
            picture[pic_num].setImage("Images/SamePicture/2.png")
        elif(random_num == 3):
            picture[pic_num].setImage("Images/SamePicture/3.png")
        elif(random_num == 4):
            picture[pic_num].setImage("Images/SamePicture/4.png")
        else:
            picture[pic_num].setImage("Images/SamePicture/5.png")
    else:
        random_num = randint(0,7)
        if(count[random_num] == 2):
            while(count[random_num] == 2):
                random_num = randint(0,7)
        if(random_num == 0):
            picture[pic_num].setImage("Images/SamePicture/0.png")
        elif(random_num == 1):
            picture[pic_num].setImage("Images/SamePicture/1.png")
        elif(random_num == 2):
            picture[pic_num].setImage("Images/SamePicture/2.png")
        elif(random_num == 3):
            picture[pic_num].setImage("Images/SamePicture/3.png")
        elif(random_num == 4):
            picture[pic_num].setImage("Images/SamePicture/4.png")
        elif(random_num == 5):
            picture[pic_num].setImage("Images/SamePicture/5.png")
        elif(random_num == 6):
            picture[pic_num].setImage("Images/SamePicture/6.png")
        else:
            picture[pic_num].setImage("Images/SamePicture/7.png")
    picture[pic_num].random_num = random_num
    count[random_num] = count[random_num] + 1
    set[pic_num] = True

def picChanged(pic_num):
    if(set[pic_num] == False):
        changeCardImage(pic_num)

def picShow(pic_num):
    global show
    click[show] = pic_num
    picture[pic_num].show()
    show += 1

def pic0_onMouseAction(x,y,action):
    global show
    picChanged(0)
    if(show<2):
        picShow(0)
    samePictureFinish()
pic0.onMouseAction = pic0_onMouseAction

def pic1_onMouseAction(x,y,action):
    global show
    picChanged(1)
    if(show<2):
        picShow(1)
    samePictureFinish()
pic1.onMouseAction = pic1_onMouseAction

def pic2_onMouseAction(x,y,action):
    global show
    picChanged(2)
    if(show<2):
        picShow(2)
    samePictureFinish()
pic2.onMouseAction = pic2_onMouseAction

def pic3_onMouseAction(x,y,action):
    global show
    picChanged(3)
    if(show<2):
        picShow(3)
    samePictureFinish()
pic3.onMouseAction = pic3_onMouseAction

def pic4_onMouseAction(x,y,action):
    global show
    picChanged(4)
    if(show<2):
        picShow(4)
    samePictureFinish()
pic4.onMouseAction = pic4_onMouseAction

def pic5_onMouseAction(x,y,action):
    global show
    picChanged(5)
    if(show<2):
        picShow(5)
    samePictureFinish()
pic5.onMouseAction = pic5_onMouseAction

def pic6_onMouseAction(x,y,action):
    global show
    picChanged(6)
    if(show<2):
        picShow(6)
    samePictureFinish()
pic6.onMouseAction = pic6_onMouseAction

def pic7_onMouseAction(x,y,action):
    global show
    picChanged(7)
    if(show<2):
        picShow(7)
    samePictureFinish()
pic7.onMouseAction = pic7_onMouseAction

def pic8_onMouseAction(x,y,action):
    global show
    picChanged(8)
    if(show<2):
        picShow(8)
    samePictureFinish()
pic8.onMouseAction = pic8_onMouseAction

def pic9_onMouseAction(x,y,action):
    global show
    picChanged(9)
    if(show<2):
        picShow(9)
    samePictureFinish()
pic9.onMouseAction = pic9_onMouseAction

def pic10_onMouseAction(x,y,action):
    global show
    picChanged(10)
    if(show<2):
        picShow(10)
    samePictureFinish()
pic10.onMouseAction = pic10_onMouseAction

def pic11_onMouseAction(x,y,action):
    global show
    picChanged(11)
    if(show<2):
        picShow(11)
    samePictureFinish()
pic11.onMouseAction = pic11_onMouseAction

def pic12_onMouseAction(x,y,action):
    global show
    picChanged(12)
    if(show<2):
        picShow(12)
    samePictureFinish()
pic12.onMouseAction = pic12_onMouseAction

def pic13_onMouseAction(x,y,action):
    global show
    picChanged(13)
    if(show<2):
        picShow(13)
    samePictureFinish()
pic13.onMouseAction = pic13_onMouseAction

def pic14_onMouseAction(x,y,action):
    global show
    picChanged(14)
    if(show<2):
        picShow(14)
    samePictureFinish()
pic14.onMouseAction = pic14_onMouseAction

def pic15_onMouseAction(x,y,action):
    global show
    picChanged(15)
    if(show<2):
        picShow(15)
    samePictureFinish()
pic15.onMouseAction = pic15_onMouseAction

def picture0_onMouseAction(x,y,action):
    pictureToPic(0)
picture0.onMouseAction = picture0_onMouseAction

def picture1_onMouseAction(x,y,action):
    pictureToPic(1)
picture1.onMouseAction = picture1_onMouseAction

def picture2_onMouseAction(x,y,action):
    pictureToPic(2)
picture2.onMouseAction = picture2_onMouseAction

def picture3_onMouseAction(x,y,action):
    pictureToPic(3)
picture3.onMouseAction = picture3_onMouseAction

def picture4_onMouseAction(x,y,action):
    pictureToPic(4)
picture4.onMouseAction = picture4_onMouseAction

def picture5_onMouseAction(x,y,action):
    pictureToPic(5)
picture5.onMouseAction = picture5_onMouseAction

def picture6_onMouseAction(x,y,action):
    pictureToPic(6)
picture6.onMouseAction = picture6_onMouseAction

def picture7_onMouseAction(x,y,action):
    pictureToPic(7)
picture7.onMouseAction = picture7_onMouseAction

def picture8_onMouseAction(x,y,action):
    pictureToPic(8)
picture8.onMouseAction = picture8_onMouseAction

def picture9_onMouseAction(x,y,action):
    pictureToPic(9)
picture9.onMouseAction = picture9_onMouseAction

def picture10_onMouseAction(x,y,action):
    pictureToPic(10)
picture10.onMouseAction = picture10_onMouseAction

def picture11_onMouseAction(x,y,action):
    pictureToPic(11)
picture11.onMouseAction = picture11_onMouseAction

def picture12_onMouseAction(x,y,action):
    pictureToPic(12)
picture12.onMouseAction = picture12_onMouseAction

def picture13_onMouseAction(x,y,action):
    pictureToPic(13)
picture13.onMouseAction = picture13_onMouseAction

def picture14_onMouseAction(x,y,action):
    pictureToPic(14)
picture14.onMouseAction = picture14_onMouseAction

def picture15_onMouseAction(x,y,action):
    pictureToPic(15)
picture15.onMouseAction = picture15_onMouseAction

level1_time = 0
level2_time = 0
level3_time = 0
def samePictureFinish():
    global show, random_num, check, start_time, end_time, duringsamePicturePause_time, totalsamePicturePause_time, level, record_time, level1_time, level2_time, level3_time
    if(show==2 and picture[click[0]].random_num == picture[click[1]].random_num):
        for i in range(2):
            picture[click[i]].hide()
            pic[click[i]].hide()
        show = 0
        check = check + 1
    if(level == 1):
        if(check == 4):
            end_time = time.time()
            level1_time = end_time - start_time
            showMessage("1단계는 "+format(float(level1_time - totalsamePicturePause_time),".2f")+"초 걸렸습니다!")
            next.show()
            samePicturePause.hide()
    elif(level == 2):
        if(check == 6):
            end_time = time.time()
            level2_time = end_time - start_time
            showMessage("2단계는 "+format(float(level2_time - totalsamePicturePause_time),".2f")+"초 걸렸습니다!")
            next.show()
            samePicturePause.hide()
    else:
        if(check == 8):
            end_time = time.time()
            level3_time = end_time - start_time
            if(record_time>level1_time+level2_time+level3_time or record_time == 0):
                record_time = level1_time + level2_time + level3_time
                showMessage("3단계는 "+format(float(level3_time - totalsamePicturePause_time),".2f")+"초 걸렸습니다!\n"+"총 걸린 시간은 "+format(float(record_time),".2f")+"초입니다.\n최고 기록입니다.")
            else:
                showMessage("3단계는 "+format(float(level3_time - totalsamePicturePause_time),".2f")+"초 걸렸습니다!\n"+"총 걸린 시간은 "+format(float(level1_time+level2_time+level3_time),".2f")+"초입니다.")
            samePicturePause.hide()
            samePictureGameEnd()

def pictureToPic(pic_num):
    global show
    picture[pic_num].hide()
    show = show -1
    pic[pic_num].show()
    if(click[0] == pic_num):
        click[0] = click[1]

def samePictureGameEnd():
    mainMenu.locate(samePictureScene,570,450)
    mainMenu.show()
    newGameMenu.locate(samePictureScene,570,350)
    newGameMenu.show()
    endMenu.locate(samePictureScene,570,250)
    endMenu.show()

board = Object("Images/Snake/board.png")
board.locate(snakeScene,60,60)
board.show()

head = Object("Images/Snake/snake.png")
snake = []
snake.append(head)
snake[0].x = 620
snake[0].y = 340
snake[0].locate(snakeScene,snake[0].x,snake[0].y)
snake[0].show()

random_apple_x = 15
random_apple_y = 8
apple_x = 0
apple_y = 0
apple = Object("Images/Snake/apple.png")
chk = 0
def createApple(): 
    global random_apple_x, random_apple_y, apple_x, apple_y, snake,apple,score,chk
    chk=0
    while(chk==0):
        chk=1
        random_apple_x = randint(2,28)
        random_apple_y = randint(2,14)
        for i in range(len(snake)):
            if((snake[i].x-20)/40 == random_apple_x and (snake[i].y-20)/40 == random_apple_y):
                chk=0
    apple_x = random_apple_x * 40+20
    apple_y = random_apple_y * 40+20
    apple.locate(snakeScene,apple_x,apple_y)
    apple.show()

timer1 = Timer(10000)
inputkey = 0
score = 0
def snakeScene_onKeyboard(key, pressed):
    global inputkey
    if(key == 84):
        inputkey = 84
        timer1.set(0.08)
    elif(key == 85):
        inputkey = 85
        timer1.set(0.08)
    elif(key == 82):
        inputkey = 82
        timer1.set(0.08)
    elif(key == 83):
        inputkey = 83
        timer1.set(0.08)
snakeScene.onKeyboard = snakeScene_onKeyboard

def eatApple():
    global apple_x,apple_y,apple,score,snake,inputkey
    if(snake[0].x==apple_x and snake[0].y==apple_y):
        apple.hide()
        score += 10
        chk = 0
        while(chk==0):
            chk=1
            random_apple_x = randint(2,28)
            random_apple_y = randint(2,14)
            for i in range(len(snake)):
                if((snake[i].x-20)/40 == random_apple_x and (snake[i].y-20)/40 == random_apple_y):
                    chk=0
        apple_x = random_apple_x * 40+20
        apple_y = random_apple_y * 40+20
        apple.locate(snakeScene,apple_x,apple_y)
        apple.show()
        if(score>0):
            if(int(score/10)==1):
                snake.append(Object("Images/Snake/snake_body.png"))
                if(inputkey == 84):
                    snake[1].x = snake[0].x
                    snake[1].y = snake[0].y - 40
                elif(inputkey == 85):
                    snake[1].x = snake[0].x
                    snake[1].y = snake[0].y + 40
                elif(inputkey == 82):
                    snake[1].x = snake[0].x + 40
                    snake[1].y = snake[0].y
                elif(inputkey == 83):
                    snake[1].x = snake[0].x - 40
                    snake[1].y = snake[0].y
                snake[1].locate(snakeScene,snake[1].x,snake[1].y) 
                snake[1].show()
            else:
                snake.append(Object("Images/Snake/snake_body.png"))
                snake[int(score/10)].x = snake[int(score/10)-1].x + (snake[int(score/10)-1].x-snake[int(score/10)-2].x)
                snake[int(score/10)].y = snake[int(score/10)-1].y + (snake[int(score/10)-1].y-snake[int(score/10)-2].y)
                snake[int(score/10)].locate(snakeScene,snake[int(score/10)].x,snake[int(score/10)].y)
                snake[int(score/10)].show()
        

def crashBody():
    global snake,score,record_score
    for i in range(1,int(score/10)+1):
        if(snake[0].x == snake[i].x and snake[0].y == snake[i].y):
            timer1.stop()
            if(score>record_score or record_score == -1):
                record_score = score
                showMessage("몸통에 닿았습니다.\n점수는 "+str(record_score)+"점입니다."+"\n최고 기록입니다.")
            else:
                showMessage("몸통에 닿았습니다.\n점수는 "+str(score)+"점입니다")
            for i in range(len(snake)):
                snake[i].hide()
            mainMenu.locate(snakeScene,570,450)
            snakeNewGameMenu.locate(snakeScene,570,350)
            endMenu.locate(snakeScene,570,250)
            mainMenu.show()
            snakeNewGameMenu.show()
            endMenu.show()

record_score = -1
def timer1_onTimeout():
    global snake,inputkey,score,record_score
    if(inputkey == 84):
        if(score>0):
            for i in range(1,int(score/10)+1):
                snake[int(score/10)+1-i].x = snake[int(score/10)+1-i-1].x
                snake[int(score/10)+1-i].y = snake[int(score/10)+1-i-1].y
                snake[int(score/10)+1-i].locate(snakeScene,snake[int(score/10)+1-i].x,snake[int(score/10)+1-i].y)
                snake[int(score/10)+1-i].show()
        snake[0].y += 40
        snake[0].locate(snakeScene,snake[0].x,snake[0].y)
        snake[0].show()
        eatApple()
        if (snake[0].y<600):
            timer1.set(0.08)
            timer1.start()
        else:
            if(score>record_score or record_score == -1):
                record_score = score
                showMessage("벽에 닿았습니다.\n점수는 "+str(record_score)+"점입니다."+"\n최고 기록입니다.")
            else:
                showMessage("벽에 닿았습니다.\n점수는 "+str(score)+"점입니다.")
            for i in range(len(snake)):
                snake[i].hide()
            mainMenu.locate(snakeScene,570,450)
            snakeNewGameMenu.locate(snakeScene,570,350)
            endMenu.locate(snakeScene,570,250)
            mainMenu.show()
            snakeNewGameMenu.show()
            endMenu.show()
        crashBody()
    elif(inputkey == 85):
        if(score>0):
            for i in range(1,int(score/10)+1):
                snake[int(score/10)+1-i].x = snake[int(score/10)+1-i-1].x
                snake[int(score/10)+1-i].y = snake[int(score/10)+1-i-1].y
                snake[int(score/10)+1-i].locate(snakeScene,snake[int(score/10)+1-i].x,snake[int(score/10)+1-i].y)
                snake[int(score/10)+1-i].show()
        snake[0].y -= 40
        snake[0].locate(snakeScene,snake[0].x,snake[0].y)
        snake[0].show()
        eatApple()
        if (snake[0].y>80):
            timer1.set(0.08)
            timer1.start()
        else:
            if(score>record_score or record_score == -1):
                record_score = score
                showMessage("벽에 닿았습니다.\n점수는 "+str(record_score)+"점입니다."+"\n최고 기록입니다.")
            else:
                showMessage("벽에 닿았습니다.\n점수는 "+str(score)+"점입니다.")
            for i in range(len(snake)):
                snake[i].hide()
            mainMenu.locate(snakeScene,570,450)
            snakeNewGameMenu.locate(snakeScene,570,350)
            endMenu.locate(snakeScene,570,250)
            mainMenu.show()
            snakeNewGameMenu.show()
            endMenu.show()
        crashBody()
    elif(inputkey == 82):
        if(score>0):
            for i in range(1,int(score/10)+1):
                snake[int(score/10)+1-i].x = snake[int(score/10)+1-i-1].x
                snake[int(score/10)+1-i].y = snake[int(score/10)+1-i-1].y
                snake[int(score/10)+1-i].locate(snakeScene,snake[int(score/10)+1-i].x,snake[int(score/10)+1-i].y)
                snake[int(score/10)+1-i].show()
        snake[0].x -= 40
        snake[0].locate(snakeScene,snake[0].x,snake[0].y)
        snake[0].show()
        eatApple()
        if (snake[0].x>80):
            timer1.set(0.08)
            timer1.start()
        else:
            if(score>record_score or record_score == -1):
                record_score = score
                showMessage("벽에 닿았습니다.\n점수는 "+str(record_score)+"점입니다."+"\n최고 기록입니다.")
            else:
                showMessage("벽에 닿았습니다.\n점수는 "+str(score)+"점입니다.")
            for i in range(len(snake)):
                snake[i].hide()
            mainMenu.locate(snakeScene,570,450)
            snakeNewGameMenu.locate(snakeScene,570,350)
            endMenu.locate(snakeScene,570,250)
            mainMenu.show()
            snakeNewGameMenu.show()
            endMenu.show()
        crashBody()
    elif(inputkey == 83):
        if(score>0):
            for i in range(1,int(score/10)+1):
                snake[int(score/10)+1-i].x = snake[int(score/10)+1-i-1].x
                snake[int(score/10)+1-i].y = snake[int(score/10)+1-i-1].y
                snake[int(score/10)+1-i].locate(snakeScene,snake[int(score/10)+1-i].x,snake[int(score/10)+1-i].y)
                snake[int(score/10)+1-i].show()
        snake[0].x += 40
        snake[0].locate(snakeScene,snake[0].x,snake[0].y)
        snake[0].show()
        eatApple()
        if (snake[0].x<1160):
            timer1.set(0.08)
            timer1.start()
        else:
            if(score>record_score or record_score == -1):
                record_score = score
                showMessage("벽에 닿았습니다.\n점수는 "+str(record_score)+"점입니다."+"\n최고 기록입니다.")
            else:
                showMessage("벽에 닿았습니다.\n점수는 "+str(score)+"점입니다.")
            for i in range(len(snake)):
                snake[i].hide()
            mainMenu.locate(snakeScene,570,450)
            snakeNewGameMenu.locate(snakeScene,570,350)
            endMenu.locate(snakeScene,570,250)
            mainMenu.show()
            snakeNewGameMenu.show()
            endMenu.show()
        crashBody()
timer1.onTimeout = timer1_onTimeout

black = Object("Images/Worm/black.png")
blue = Object("Images/Worm/blue.png")
green = Object("Images/Worm/green.png")
red = Object("Images/Worm/red.png")
yellow = Object("Images/Worm/yellow.png")

blackball = Object("Images/Worm/blackball.png")
blueball = Object("Images/Worm/blueball.png")
greenball = Object("Images/Worm/greenball.png")
redball = Object("Images/Worm/redball.png")
yellowball = Object("Images/Worm/yellowball.png")
whiteball = Object("Images/Worm/whiteball.png")

blackballl = Object("Images/Worm/blackball.png")

downball=[[blackballl,],[blackballl,]]
def createBall(num):
    temp = 0
    if num>9:
        num-=5
    if num==0:
        temp = Object("Images/Worm/blackball.png")
        temp.color=0
    elif num == 1:
        temp = Object("Images/Worm/blueball.png")
        temp.color=1
    elif num == 2:
        temp = Object("Images/Worm/greenball.png")
        temp.color=2
    elif num == 3:
        temp = Object("Images/Worm/redball.png")
        temp.color=3
    elif num == 4:
        temp = Object("Images/Worm/yellowball.png")
        temp.color=4
    elif num == 5:
        temp = Object("Images/Worm/black.png")
        temp.color=5
    elif num == 6:
        temp = Object("Images/Worm/blue.png")
        temp.color=6
    elif num == 7:
        temp = Object("Images/Worm/green.png")
        temp.color=7
    elif num == 8:
        temp = Object("Images/Worm/red.png")
        temp.color=8
    elif num == 9:
        temp = Object("Images/Worm/yellow.png")
        temp.color=9
    if(num < 5):
        temp.setScale(0.1)
    else:
        temp.setScale(1.5)
    return temp

blackball.setScale(0.15)
blueball.setScale(0.15)
greenball.setScale(0.15)
redball.setScale(0.15)
yellowball.setScale(0.15)
whiteball.setScale(0.15)

ball_x = 625
ball_y = 200
ball = [blackball,blueball,greenball,redball,yellowball,whiteball]

for i in range(6):
    ball[i].color = i
    ball[i].locate(wormScene,ball_x,ball_y-i*35)


chkk=0
downball0_y = 650
downball1_y = 650

def randomBallCreate():
    global chkk, downball0_y, downball1_y
    for i in range(len(downball[chkk])):
        downball[chkk][i].hide()
    downball[chkk].clear()
    if chkk==0:
        downball0_y=650
    elif chkk==1:
        downball1_y=650
    countt = randint(2,4)
    numlist = [0,1,2,3,4]
    s = random.sample(numlist, countt)
    for i in range(countt):
        random_num = randint(0,14)
        random_num1 = s[i]
        downball[chkk].append(createBall(random_num))
        downball[chkk][i].y=chkk
        
        if (random_num < 5):
            downball[chkk][i].x = 430 + random_num1 * 100
            downball[chkk][i].locate(wormScene,430 + random_num1 * 100,650)
        else:
            downball[chkk][i].x = 400 + random_num1 * 100
            downball[chkk][i].locate(wormScene,400 + random_num1 * 100,650)
        downball[chkk][i].show()
 
def wormScene_onKeyboard(key, pressed):
    global ball_x,ball_y,checkk
    if(key == 82 and pressed==True and checkk == 1):
        if(ball_x>450):
            for i in range(len(ball)):
                ball[i].locate(wormScene,ball_x - 100, ball_y - i * 35)
            ball_x = ball_x - 100
    elif(key == 83 and pressed==True and checkk == 1):
        if(ball_x<800):
            for i in range(len(ball)):
                ball[i].locate(wormScene,ball_x + 100, ball_y - i * 35)
            ball_x = ball_x + 100
wormScene.onKeyboard = wormScene_onKeyboard

timer4 = Timer(10000)
timer5 = Timer(10000)
color_y = 700

location=0
timing=0
def timer_chkk0_onTimeout():
    global downball0_y, chkk, ball_x, location,worm_record_score,worm_score, timing
    timer4.set(0.05)
    timer4.start()
    timing=0
    for i in range(len(downball[0])):
        downball[0][i].locate(wormScene,downball[0][i].x,downball0_y)
    downball0_y -= 30    
    if downball0_y==320:
        chkk=1
        randomBallCreate()
        timer5.set(0.05)
        timer5.start()
    elif downball0_y==170:
        meet=False
        location=0
        for i in range(len(downball[0])):
            if downball[0][i].x==ball_x+5 or downball[0][i].x==ball_x-25 :
                location=i
                meet=True
                break
        if meet==True:
            if downball[0][location].color<5:
                ball.insert(0, createBall(downball[0][location].color))
                ball[0].setScale(0.15)
                for i in range(len(ball)):
                    ball[i].locate(wormScene,ball_x,ball_y-i*35)
                    ball[i].show()
            else:
                if len(ball)==1:
                    timer4.stop()
                    timer5.stop()
                    timer6.stop()
                    if(worm_score>worm_record_score or worm_record_score == -1):
                        worm_record_score = worm_score
                        showMessage("점수는 "+str(worm_record_score)+"점입니다."+"\n최고 기록입니다.")
                    else:
                        showMessage("점수는 "+str(worm_score)+"점입니다.")
                    mainMenu.locate(wormScene,570,450)
                    wormNewGameMenu.locate(wormScene,570,350)
                    endMenu.locate(wormScene,570,250)
                    mainMenu.show()
                    wormNewGameMenu.show()
                    endMenu.show()
                elif downball[0][location].color-5 == ball[0].color:
                    ball[0].hide()
                    ball.pop(0)
                    worm_score += 10
                    for i in range(len(ball)):
                        ball[i].locate(wormScene,ball_x,ball_y-i*35)
                else:
                    timer5.stop()
                    timer4.stop()
                    chkk=0
                    timer6.set(0.1)
                    timer6.start()

        for i in range(len(downball[0])):
            downball[0][i].hide()
            
timer4.onTimeout = timer_chkk0_onTimeout

timer6 = Timer(10000)

def timer_chkk1_onTimeout():
    global downball1_y, chkk, location,worm_record_score,worm_score, timing
    timing=1
    timer5.set(0.05)
    timer5.start()
    for i in range(len(downball[1])):
        downball[1][i].locate(wormScene,downball[1][i].x,downball1_y)
    downball1_y -= 30
    if downball1_y==320:
        chkk=0
        randomBallCreate()
        timer4.set(0.05)
        timer4.start()
    elif downball1_y==170:
        location=0
        meet1=False
        for i in range(len(downball[1])):
            if downball[1][i].x==ball_x+5 or downball[1][i].x==ball_x-25 :
                location=i
                meet1=True
                break
        if meet1==True:
            if downball[1][location].color<5:
                ball.insert(0, createBall(downball[1][location].color))
                ball[0].setScale(0.15)
                for i in range(len(ball)):
                    ball[i].locate(wormScene,ball_x,ball_y-i*35)
                    ball[i].show()

            else:
                if len(ball)==1:
                    timer4.stop()
                    timer5.stop()
                    timer6.stop()
                    if(worm_score>worm_record_score or worm_record_score == -1):
                        worm_record_score = worm_score
                        showMessage("점수는 "+str(worm_record_score)+"점입니다."+"\n최고 기록입니다.")
                    else:
                        showMessage("점수는 "+str(worm_score)+"점입니다.")
                    mainMenu.locate(wormScene,570,450)
                    wormNewGameMenu.locate(wormScene,570,350)
                    endMenu.locate(wormScene,570,250)
                    mainMenu.show()
                    wormNewGameMenu.show()
                    endMenu.show()
                elif downball[1][location].color-5 == ball[0].color:
                    ball[0].hide()
                    ball.pop(0)
                    worm_score += 10
                    for i in range(len(ball)):
                        ball[i].locate(wormScene,ball_x,ball_y-i*35)
                else:
                    timer4.stop()
                    timer5.stop()
                    chkk=1
                    timer6.set(0.1)
                    timer6.start()

        for i in range(len(downball[1])):
            downball[1][i].hide()
timer5.onTimeout = timer_chkk1_onTimeout
checkk = 1
worm_score = 0
worm_record_score = -1
def timer6_onTimeout():
    global location,checkk,worm_record_score,worm_score, chkk
    checkk = 0
    if downball[chkk][location].color-5 != ball[0].color:
        
        if len(ball)==1:
            timer4.stop()
            timer5.stop()
            timer6.stop()
            if(worm_score>worm_record_score or worm_record_score == -1):
                worm_record_score = worm_score
                showMessage("점수는 "+str(worm_record_score)+"점입니다."+"\n최고 기록입니다.")
            else:
                showMessage("점수는 "+str(worm_score)+"점입니다.")
            mainMenu.locate(wormScene,570,450)
            wormNewGameMenu.locate(wormScene,570,350)
            endMenu.locate(wormScene,570,250)
            mainMenu.show()
            wormNewGameMenu.show()
            endMenu.show()
        else:
            ball[0].hide()
            ball.pop(0)
            worm_score += 10
            for i in range(len(ball)):
                ball[i].locate(wormScene,ball_x,ball_y-i*35)
            timer6.set(0.1)
            timer6.start()
    else:
        timer6.stop()
        ball[0].hide()
        ball.pop(0)
        worm_score += 10
        for i in range(len(ball)):
            ball[i].locate(wormScene,ball_x,ball_y-i*35)
        timer4.start()
        timer5.start()
        checkk = 1
timer6.onTimeout = timer6_onTimeout

timer1.start()
timer2.start()
timer3.start()
timer4.start()
timer5.start()
timer6.start()
startGame(mainScene)