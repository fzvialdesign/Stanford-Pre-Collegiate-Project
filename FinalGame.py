import random, pygame, sys
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 840
WINDOWHEIGHT = 470

WHITE       = (255, 255, 255)
BLACK       = (  0,   0,   0)
RED         = (255,   0,   0)
GREEN       = (  0, 255,   0)
DARKGREEN   = (  0, 155,   0)
DARKGRAY    = ( 40,  40,  40)
BGCOLOR = BLACK

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

object1_selected = False
object2_selected = False
object3_selected = False
object4_selected = False
object5_selected = False
object6_selected = False
object7_selected = False
object8_selected = False
object9_selected = False
object10_selected = False

room = 0
maps = 0

backpack = False

inventory = []


def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT
    
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Final Game')
    
    
    
    showStartScreen()
    tutorial()
    
    while True:
        runGame()
        showGameOverScreen()
        
    


def runGame():
   global object1_selected
   global object2_selected
   global object3_selected
   global object4_selected
   global object5_selected
   global object6_selected
   global object7_selected
   global object8_selected
   global object9_selected
   global object10_selected
   global  room
   global maps
   global backpack
   
   pygame.mixer.music.load('soundtrack.wav')
   pygame.mixer.music.play(-1)
   
   while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()                          
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    settings()
        
        
        
        
        if room == 0:                        
            
            thread = "thread.png"
            torso = "torso.png"
            note = "note.png"
            
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            
            object1_pos_x = 719
            object1_pos_y = 223
            
            object2_pos_x = 104
            object2_pos_y = 350
            
            object3_pos_x = 408
            object3_pos_y = 210
            
            door_pos_x = 740
            door_pos_y = 0
            
            object1_size_x = 40
            object1_size_y = 40
            
            object2_size_x = 150
            object2_size_y = 80

            object3_size_x = 40
            object3_size_y = 40


            door_size_x = 100
            door_size_y = 680
            
            
            DISPLAYSURF.blit(pygame.image.load("kat.png"), (0,0))
            DISPLAYSURF.blit(pygame.transform.scale(pygame.image.load("fader.png"), (250,840)), (0, 0))
            
            if backpack:
                DISPLAYSURF.blit(pygame.image.load("inventory.png"), (0,60))
            
            roomNameFont = pygame.font.Font('freesansbold.ttf', 30)
            roomNameSurf = roomNameFont.render('Kathleen’s Room', True, WHITE)
            roomNameRect = roomNameSurf.get_rect()
            roomNameRect.midtop = (WINDOWWIDTH / 2, 10)
            
            DISPLAYSURF.blit(roomNameSurf, roomNameRect)  
            
            if object1_pos_x < mouse[0] <  object1_pos_x + object1_size_x and object1_pos_y < mouse[1] < object1_pos_y + object1_size_y:
                if click[0] == 1:  
                    inventory.append(thread)
                    object1_selected = True
                    print("Object 1")
                    print(inventory[0])
            
            elif object2_pos_x < mouse[0] <  object2_pos_x + object2_size_x and object2_pos_y < mouse[1] < object2_pos_y + object2_size_y:
                if click[0] == 1:  
                    inventory.append(torso)
                    object2_selected = True
                    print("Object 2")
                    print(inventory[0])
            
            elif object3_pos_x < mouse[0] <  object3_pos_x + object3_size_x and object3_pos_y < mouse[1] < object3_pos_y + object3_size_y:
                if click[0] == 1:  
                    inventory.append(note)
                    object3_selected = True
                    print("Object 3")
                    print(inventory[0])
            
            elif door_pos_x < mouse[0] <  WINDOWWIDTH and 0 < mouse[1] < WINDOWHEIGHT:
                doorSurf = BASICFONT.render("Bathroom", True, WHITE)
                doorRect = doorSurf.get_rect()
                doorRect.topleft = (700, 350)
                DISPLAYSURF.blit(doorSurf, doorRect)
                if click[0] == 1:
                    room = 1
            elif 0 < mouse[0] <  WINDOWWIDTH - door_pos_x and 100 < mouse[1] < WINDOWHEIGHT - 100:
                doorSurf = BASICFONT.render("Ubel’s Room", True, WHITE)
                doorRect = doorSurf.get_rect()
                doorRect.topleft = (60, 350)
                DISPLAYSURF.blit(doorSurf, doorRect)
                if click[0] == 1: 
                    room = 2
            
                
            if object1_selected == False:
                DISPLAYSURF.blit(pygame.transform.scale(pygame.image.load(thread), (object1_size_x, object1_size_y)), (object1_pos_x, object1_pos_y))
            elif object1_selected == True:
                None     
            
            if object2_selected == False:
                DISPLAYSURF.blit(pygame.transform.scale(pygame.image.load(torso), (object2_size_x, object2_size_y)), (object2_pos_x, object2_pos_y))
            elif object2_selected == True:
                None            
        
            if object3_selected == False:
                DISPLAYSURF.blit(pygame.transform.scale(pygame.image.load(note), (object3_size_x, object3_size_y)), (object3_pos_x, object3_pos_y))
            elif object3_selected == True:
                None            
        
        
            DISPLAYSURF.blit(pygame.transform.scale(pygame.image.load("vignette.png"), (840,470)), (0, 0))
            
            if backpack:                    
                if len(inventory) != 0:
                    pos = 75
                    for item in inventory:
                        DISPLAYSURF.blit(pygame.transform.scale(pygame.image.load(item), (25,25)), (10, pos))
                        pos += 35
           
        elif room == 1:                        
            
            dandruff = "dandruff.png"
            bullet = "bullet.png"
            alcohol = "alcohol.png"
            
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            
            object1_pos_x = 250
            object1_pos_y = 401
            
            object2_pos_x = 630
            object2_pos_y = 390
            
            object3_pos_x = 471
            object3_pos_y = 326
            
            door_pos_x = 740
            door_pos_y = 0
            
            object1_size_x = 40
            object1_size_y = 40
            
            object2_size_x = 40
            object2_size_y = 40

            object3_size_x = 40
            object3_size_y = 40


            door_size_x = 100
            door_size_y = 680
            
            
            DISPLAYSURF.blit(pygame.image.load("bath.png"), (0,0))
            DISPLAYSURF.blit(pygame.transform.scale(pygame.image.load("fader.png"), (250,840)), (0, 0))
            
            if backpack:
                DISPLAYSURF.blit(pygame.image.load("inventory.png"), (0,60))
            
            roomNameFont = pygame.font.Font('freesansbold.ttf', 30)
            roomNameSurf = roomNameFont.render('Bathroom', True, WHITE)
            roomNameRect = roomNameSurf.get_rect()
            roomNameRect.midtop = (WINDOWWIDTH / 2, 10)
            
            DISPLAYSURF.blit(roomNameSurf, roomNameRect)  
            
            if object1_pos_x < mouse[0] <  object1_pos_x + object1_size_x and object1_pos_y < mouse[1] < object1_pos_y + object1_size_y:
                if click[0] == 1:  
                    inventory.append(dandruff)
                    object4_selected = True
                    print("Object 4")
                    print(inventory[0])
            
            elif object2_pos_x < mouse[0] <  object2_pos_x + object2_size_x and object2_pos_y < mouse[1] < object2_pos_y + object2_size_y:
                if click[0] == 1:  
                    inventory.append(bullet)
                    object5_selected = True
                    print("Object 5")
                    print(inventory[0])
            
            elif object3_pos_x < mouse[0] <  object3_pos_x + object3_size_x and object3_pos_y < mouse[1] < object3_pos_y + object3_size_y:
                if click[0] == 1:  
                    inventory.append(alcohol)
                    object6_selected = True
                    print("Object 6")
                    print(inventory[0])
            elif 0 < mouse[0] <  WINDOWWIDTH - door_pos_x and 100 < mouse[1] < WINDOWHEIGHT - 100:
                doorSurf = BASICFONT.render('Kathleen’s Room', True, WHITE)
                doorRect = doorSurf.get_rect()
                doorRect.topleft = (60, 350)
                DISPLAYSURF.blit(doorSurf, doorRect)
                if click[0] == 1: 
                    room = 0
            
                
            if object4_selected == False:
                DISPLAYSURF.blit(pygame.transform.scale(pygame.image.load(dandruff), (object1_size_x, object1_size_y)), (object1_pos_x, object1_pos_y))
            elif object4_selected == True:
                None     
            
            if object5_selected == False:
                DISPLAYSURF.blit(pygame.transform.scale(pygame.image.load(bullet), (object2_size_x, object2_size_y)), (object2_pos_x, object2_pos_y))
            elif object5_selected == True:
                None            
        
            if object6_selected == False:
                DISPLAYSURF.blit(pygame.transform.scale(pygame.image.load(alcohol), (object3_size_x, object3_size_y)), (object3_pos_x, object3_pos_y))
            elif object6_selected == True:
                None            
        
        
            DISPLAYSURF.blit(pygame.transform.scale(pygame.image.load("vignette.png"), (840,470)), (0, 0))
            
            if backpack:                    
                if len(inventory) != 0:
                    pos = 75
                    for item in inventory:
                        DISPLAYSURF.blit(pygame.transform.scale(pygame.image.load(item), (25,25)), (10, pos))
                        pos += 35
           
        
        elif room == 2:                        
            hair = "hair.png"
            note = "note.png"
            
            
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            
            object1_pos_x = 650
            object1_pos_y = 310
            
            object2_pos_x = 415
            object2_pos_y = 258
            
            
            door_pos_x = 740
            door_pos_y = 0
            
            object1_size_x = 40
            object1_size_y = 40
            
            object2_size_x = 30
            object2_size_y = 30

            door_size_x = 100
            door_size_y = 680
            
            
            DISPLAYSURF.blit(pygame.image.load("ubelroom.png"), (0,0))
            DISPLAYSURF.blit(pygame.transform.scale(pygame.image.load("fader.png"), (250,840)), (0, 0))
            
            if backpack:
                DISPLAYSURF.blit(pygame.image.load("inventory.png"), (0,60))
            
            roomNameFont = pygame.font.Font('freesansbold.ttf', 30)
            roomNameSurf = roomNameFont.render("Ubel’s Room", True, WHITE)
            roomNameRect = roomNameSurf.get_rect()
            roomNameRect.midtop = (WINDOWWIDTH / 2, 10)
            
            DISPLAYSURF.blit(roomNameSurf, roomNameRect)  
            
            if object1_pos_x < mouse[0] <  object1_pos_x + object1_size_x and object1_pos_y < mouse[1] < object1_pos_y + object1_size_y:
                if click[0] == 1:  
                    inventory.append(hair)
                    object7_selected = True
                    print("Object 7")
                    print(inventory[0])
            
            elif object2_pos_x < mouse[0] <  object2_pos_x + object2_size_x and object2_pos_y < mouse[1] < object2_pos_y + object2_size_y:
                if click[0] == 1:  
                    inventory.append(note)
                    object8_selected = True
                    print("Object 8")
                    print(inventory[0])
            
            
            elif door_pos_x < mouse[0] <  door_pos_x + door_size_x and door_pos_y < mouse[1] < door_pos_y + door_size_y:
                doorSurf = BASICFONT.render("Kathleen’s Room", True, WHITE)
                doorRect = doorSurf.get_rect()
                doorRect.topleft = (650, 340)
                DISPLAYSURF.blit(doorSurf, doorRect)
                if click[0] == 1: 
                    room = 0
                    
            elif 0 < mouse[0] <  WINDOWWIDTH - door_pos_x and 100 < mouse[1] < WINDOWHEIGHT - 100:
                doorSurf = BASICFONT.render('Kitchen', True, WHITE)
                doorRect = doorSurf.get_rect()
                doorRect.topleft = (60, 350)
                DISPLAYSURF.blit(doorSurf, doorRect)
                if click[0] == 1: 
                    room = 3
            
                
            if object7_selected == False:
                DISPLAYSURF.blit(pygame.transform.scale(pygame.image.load(hair), (object1_size_x, object1_size_y)), (object1_pos_x, object1_pos_y))
            elif object7_selected == True:
                None     
            
            if object8_selected == False:
                DISPLAYSURF.blit(pygame.transform.scale(pygame.image.load(note), (object2_size_x, object2_size_y)), (object2_pos_x, object2_pos_y))
            elif object8_selected == True:
                None            

        
            DISPLAYSURF.blit(pygame.transform.scale(pygame.image.load("vignette.png"), (840,470)), (0, 0))
            
            if backpack:                    
                if len(inventory) != 0:
                    pos = 75
                    for item in inventory:
                        DISPLAYSURF.blit(pygame.transform.scale(pygame.image.load(item), (25,25)), (10, pos))
                        pos += 35
           
        
        elif room == 3:                        
            
            ink = "ink.png"
            note = "note.png"
            
            
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            
            object1_pos_x = 621
            object1_pos_y = 232
            
            object2_pos_x = 311
            object2_pos_y = 400
            
            
            door_pos_x = 740
            door_pos_y = 0
            
            object1_size_x = 40
            object1_size_y = 40
            
            object2_size_x = 30
            object2_size_y = 30

            door_size_x = 100
            door_size_y = 680
            
            
            DISPLAYSURF.blit(pygame.image.load("kitchen.png"), (0,0))
            DISPLAYSURF.blit(pygame.transform.scale(pygame.image.load("fader.png"), (250,840)), (0, 0))
            
            if backpack:
                DISPLAYSURF.blit(pygame.image.load("inventory.png"), (0,60))
            
            roomNameFont = pygame.font.Font('freesansbold.ttf', 30)
            roomNameSurf = roomNameFont.render("Kitchen", True, WHITE)
            roomNameRect = roomNameSurf.get_rect()
            roomNameRect.midtop = (WINDOWWIDTH / 2, 10)
            
            DISPLAYSURF.blit(roomNameSurf, roomNameRect)  
            
            if object1_pos_x < mouse[0] <  object1_pos_x + object1_size_x and object1_pos_y < mouse[1] < object1_pos_y + object1_size_y:
                if click[0] == 1:  
                    inventory.append(ink)
                    object9_selected = True
                    print("Object 9")
                    print(inventory[0])
            
            elif object2_pos_x < mouse[0] <  object2_pos_x + object2_size_x and object2_pos_y < mouse[1] < object2_pos_y + object2_size_y:
                if click[0] == 1:  
                    inventory.append(note)
                    object10_selected = True
                    print("Object 10")
                    print(inventory[0])
            
            
            elif door_pos_x < mouse[0] <  door_pos_x + door_size_x and door_pos_y < mouse[1] < door_pos_y + door_size_y:
                doorSurf = BASICFONT.render("Ubel’s Room", True, WHITE)
                doorRect = doorSurf.get_rect()
                doorRect.topleft = (700, 340)
                DISPLAYSURF.blit(doorSurf, doorRect)
                if click[0] == 1: 
                    room = 2
           
            
                
            if object9_selected == False:
                DISPLAYSURF.blit(pygame.transform.scale(pygame.image.load(ink), (object1_size_x, object1_size_y)), (object1_pos_x, object1_pos_y))
            elif object9_selected == True:
                None     
            
            if object10_selected == False:
                DISPLAYSURF.blit(pygame.transform.scale(pygame.image.load(note), (object2_size_x, object2_size_y)), (object2_pos_x, object2_pos_y))
            elif object10_selected == True:
                None            

        
            DISPLAYSURF.blit(pygame.transform.scale(pygame.image.load("vignette.png"), (840,470)), (0, 0))
            
            if backpack:                    
                if len(inventory) != 0:
                    pos = 75
                    for item in inventory:
                        DISPLAYSURF.blit(pygame.transform.scale(pygame.image.load(item), (25,25)), (10, pos))
                        pos += 35
           
        
        
        if maps == 1:
                DISPLAYSURF.blit(pygame.transform.scale(pygame.image.load("map.png"), (820,470)), (10, 10))
                if 84 < mouse[0] <  84 + 171 and 71 < mouse[1] < 71 + 141:
                    blocked()
                    if click[0] == 1: 
                        #pygame.time.wait(200)
                        #maps = 0
                        #room = 7
                        #lobby
                        None
                elif 264 < mouse[0] <  264 + 185 and 76 < mouse[1] < 76 + 140:
                    blocked()
                    if click[0] == 1:  
                        #pygame.time.wait(200)
                        #maps = 0
                        #room = 0
                        #bar
                        None
                elif 456 < mouse[0] <  456 + 173 and 74 < mouse[1] < 74 + 53:
                    blocked()
                    if click[0] == 1:  
                        #pygame.time.wait(200)
                        #maps = 0
                        #room = 6
                        #wine
                        None
                elif 457 < mouse[0] <  457 + 170 and 126 < mouse[1] < 126 + 83:
                    if click[0] == 1:  
                        #pygame.time.wait(200)
                        maps = 0
                        room = 3
                        #kitchen
                elif 81 < mouse[0] <  81 + 139 and 277 < mouse[1] < 277 + 111:
                    blocked()
                    if click[0] == 1:  
                        #pygame.time.wait(200)
                        #maps = 0
                        #room = 2
                        #Mia's 
                        None
                elif 224 < mouse[0] <  224 + 142 and 276 < mouse[1] < 276 + 110:
                    if click[0] == 1:  
                        #pygame.time.wait(200)
                        maps = 0
                        room = 2
                        #ubels
                elif 407 < mouse[0] <  407 + 138 and 277 < mouse[1] < 277 + 104:
                    if click[0] == 1:  
                        #pygame.time.wait(200)
                        maps = 0
                        room = 0
                        #kat's
                elif 552 < mouse[0] <  552 + 75 and 274 < mouse[1] < 274 + 109:
                    if click[0] == 1:  
                        #pygame.time.wait(200)
                        maps = 0
                        room = 1
                        #bath
                       
        
        
        DISPLAYSURF.blit(pygame.transform.scale(pygame.image.load("map_icon.png"), (30,30)), (10, 10))
        DISPLAYSURF.blit(pygame.transform.scale(pygame.image.load("backpack.png"), (50,50)), (5, 410))
        if maps == 1:
                if 0 < mouse[0] <  20 + 25 and 0 < mouse[1] < 20 + 25:
                    if click[0] == 1:  
                        #pygame.time.wait(200)
                        maps = 0
        else:
            if 0 < mouse[0] <  20 + 25 and 0 < mouse[1] < 20 + 25:
                    if click[0] == 1:  
                        #pygame.time.wait(200)
                        maps = 1
                        
        if backpack:
                 if 0 < mouse[0] <  50 and 0 < mouse[1] < 470:
                    if click[0] == 1: 
                        #pygame.time.wait(200)
                        backpack = False
        else:
                if 0 < mouse[0] <  5 + 50 and 0 < mouse[1] < 410 + 50:
                    if click[0] == 1: 
                        #pygame.time.wait(200)
                        backpack = True
                      
        if len(inventory) == 9:
            win()
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        
def win():
    DISPLAYSURF.blit(pygame.image.load("win.png"), (0,0))
    
def blocked():
    blockedFont = pygame.font.Font('freesansbold.ttf', 20)
    blockedSurf = blockedFont.render('Only Premium Users', True, WHITE)
    blockedRect = blockedSurf.get_rect()
    blockedRect.midtop = (WINDOWWIDTH / 2, 35) 
    
    DISPLAYSURF.blit(blockedSurf, blockedRect)  

    
    
def terminate():
    pygame.quit()
    sys.exit()

def tutorial():
    
   
            
    back = pygame.image.load("bar.png")
    DISPLAYSURF.blit(back, (0,0))
    i = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if (event.key == K_RETURN):
                    if i < 13:
                        i += 3
                        back = pygame.image.load("kat.png")
                        DISPLAYSURF.blit(back, (0,0))
                        cody = pygame.image.load("cody.png")
                        DISPLAYSURF.blit(pygame.transform.scale(cody, (420,630)), (540, 0))
                    else:
                        return
                    
                    
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        cody = pygame.image.load("cody.png")
        DISPLAYSURF.blit(pygame.transform.scale(cody, (420,630)), (540, 0))
        
        #subtitle = pygame.image.load("subtitle.png")
        #DISPLAYSURF.blit(pygame.transform.scale(subtitle, (300,150)), (400, 400))
        
        texts = ["I’m glad you could make it, Detective Halbert.", "We have quite the case on our hands here.", "",
                 "As you can see in front of you, gruesome as it is,", " there is a head on a spike here with a sign reading,","“For these their mind drowns in their liquor.”",
                 "As I’m sure you can tell, this is the sixth murder this","year to happen in such a manner. We are desperate", "here to solve these killings, and so we need your help.",
                 "So far we know that the victim has been identified", "as Kathleen Cerdwin, middle aged mother that was","supposed to perform here tomorrow with her upright bass.",
                 "It’s indiscernible where exactly she was killed but","it must have been in the hotel. She was checked in", "to the hotel earlier today and was last seen a few hours ago in this very bar.",
                 "So far, we have two potential suspects. You may","question them at your discretion. I trust you","know what to do, Detective Halbert."]
        
        line1 = texts[i]
        line2 = texts[i + 1]
        line3 = texts[i + 2]
        
        subtitleFont = pygame.font.Font('freesansbold.ttf', 20)
        
        subtitle1 = subtitleFont.render(line1, True, WHITE)
        subtitle1Rect = subtitle1.get_rect()
        subtitle1Rect.midtop = (WINDOWWIDTH / 2, 370)
        DISPLAYSURF.blit(subtitle1, subtitle1Rect)  
        subtitle2 = subtitleFont.render(line2, True, WHITE)
        subtitle2Rect = subtitle2.get_rect()
        subtitle2Rect.midtop = (WINDOWWIDTH / 2, 400)
        DISPLAYSURF.blit(subtitle2, subtitle2Rect)  
        subtitle3 = subtitleFont.render(line3, True, WHITE)
        subtitle3Rect = subtitle3.get_rect()
        subtitle3Rect.midtop = (WINDOWWIDTH / 2, 430)
        DISPLAYSURF.blit(subtitle3, subtitle3Rect) 
        
        
        #print(click[0])
        
        if 0 < mouse[0] <  WINDOWWIDTH and WINDOWHEIGHT/2 < mouse[1] < (WINDOWHEIGHT):
            if click[0] == 1: 
                if i < 13:
                                        
                    i += 3
                    DISPLAYSURF.blit(back, (0,0))
                    DISPLAYSURF.blit(pygame.transform.scale(cody, (420,630)), (540, 0))
                    pygame.display.update()
                else:
                    return
        
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def showStartScreen():
    back = pygame.image.load("back.png")
    DISPLAYSURF.blit(back, (0,0))
    i = 0
    while True:         
        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        button1_pos_x = 76
        button1_pos_y = 250
        
        button2_pos_x = 310
        button2_pos_y = 250
        
        button3_pos_x = 545
        button3_pos_y = 250
        
        size_x = 200
        size_y = 80
        
        bt1 = pygame.image.load("button1.png")
        bt1p = pygame.image.load("button1p.png")    
        bt2 = pygame.image.load("button2.png")
        bt2p = pygame.image.load("button2p.png")
        bt3 = pygame.image.load("button3.png")
        bt3p = pygame.image.load("button3p.png") 
        
        if button1_pos_x < mouse[0] <  button1_pos_x + size_x and button1_pos_y < mouse[1] < button1_pos_y + size_y:
            i = 0
            if click[0] == 1:
                DISPLAYSURF.blit(bt1, (button1_pos_x, button1_pos_y))
                DISPLAYSURF.blit(bt2p, (button2_pos_x, button2_pos_y))
                DISPLAYSURF.blit(bt3, (button3_pos_x, button3_pos_y))
                return 

        elif button2_pos_x < mouse[0] <  button2_pos_x + size_x and button2_pos_y < mouse[1] < button2_pos_y + size_y:
            i = 1
            if click[0] == 1:
                DISPLAYSURF.blit(bt1p, (button1_pos_x, button1_pos_y))
                DISPLAYSURF.blit(bt2, (button2_pos_x, button2_pos_y))
                DISPLAYSURF.blit(bt3, (button3_pos_x, button3_pos_y))
                settings()
        
        elif button3_pos_x < mouse[0] <  button3_pos_x + size_x and button3_pos_y < mouse[1] < button3_pos_y + size_y:
            i = 2
            if click[0] == 1:
                DISPLAYSURF.blit(bt1, (button1_pos_x, button1_pos_y))
                DISPLAYSURF.blit(bt2, (button2_pos_x, button2_pos_y))
                DISPLAYSURF.blit(bt3p, (button3_pos_x, button3_pos_y))
                terminate()
                
        
            
           
        if i == 0:
            DISPLAYSURF.blit(bt1p, (button1_pos_x, button1_pos_y))
            DISPLAYSURF.blit(bt2, (button2_pos_x, button2_pos_y))
            DISPLAYSURF.blit(bt3, (button3_pos_x, button3_pos_y))
        elif i == 1:
            DISPLAYSURF.blit(bt1, (button1_pos_x, button1_pos_y))
            DISPLAYSURF.blit(bt2p, (button2_pos_x, button2_pos_y))
            DISPLAYSURF.blit(bt3, (button3_pos_x, button3_pos_y))
        elif i == 2:
            DISPLAYSURF.blit(bt1, (button1_pos_x, button1_pos_y))
            DISPLAYSURF.blit(bt2, (button2_pos_x, button2_pos_y))
            DISPLAYSURF.blit(bt3p, (button3_pos_x, button3_pos_y))
           
        for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                if event.type == KEYDOWN:        
                         if (event.key == K_DOWN):
                           if i == 2:
                               i = 0
                           else: 
                               i += 1
                         if (event.key == K_UP):
                                   if i == 0:
                                       i = 2
                                   else: 
                                       i -= 1
                                 
                         if (event.key == K_RETURN) and i == 0:  
                             return 
                         elif (event.key == K_RETURN) and i == 1:
                                settings()
                         elif (event.key == K_RETURN) and i == 2:
                                terminate()
                       
        
        
        FPSCLOCK.tick(FPS)
        pygame.display.update() 
        
def settings():
    back = pygame.image.load("settings.png")
    DISPLAYSURF.blit(back, (0,0))
    i = 0
    while True:         
        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        button1_pos_x = 76
        button1_pos_y = 250
        
        button2_pos_x = 310
        button2_pos_y = 250
        
        button3_pos_x = 545
        button3_pos_y = 250
        
        size_x = 200
        size_y = 80
        
        bt1 = pygame.image.load("button1.png")
        bt1p = pygame.image.load("button1p.png")    
        bt2 = pygame.image.load("button2.png")
        bt2p = pygame.image.load("button2p.png")
        bt3 = pygame.image.load("button3.png")
        bt3p = pygame.image.load("button3p.png") 
        
        if button1_pos_x < mouse[0] <  button1_pos_x + size_x and button1_pos_y < mouse[1] < button1_pos_y + size_y:
            i = 0
            if click[0] == 1:
                DISPLAYSURF.blit(bt1, (button1_pos_x, button1_pos_y))
                DISPLAYSURF.blit(bt2p, (button2_pos_x, button2_pos_y))
                DISPLAYSURF.blit(bt3, (button3_pos_x, button3_pos_y))
                return 

        elif button2_pos_x < mouse[0] <  button2_pos_x + size_x and button2_pos_y < mouse[1] < button2_pos_y + size_y:
            i = 1
            if click[0] == 1:
                DISPLAYSURF.blit(bt1p, (button1_pos_x, button1_pos_y))
                DISPLAYSURF.blit(bt2, (button2_pos_x, button2_pos_y))
                DISPLAYSURF.blit(bt3, (button3_pos_x, button3_pos_y))
                settings()
        
        elif button3_pos_x < mouse[0] <  button3_pos_x + size_x and button3_pos_y < mouse[1] < button3_pos_y + size_y:
            i = 2
            if click[0] == 1:
                DISPLAYSURF.blit(bt1, (button1_pos_x, button1_pos_y))
                DISPLAYSURF.blit(bt2, (button2_pos_x, button2_pos_y))
                DISPLAYSURF.blit(bt3p, (button3_pos_x, button3_pos_y))
                terminate()
                
         
            
           
        if i == 0:
            DISPLAYSURF.blit(bt1p, (button1_pos_x, button1_pos_y))
            DISPLAYSURF.blit(bt2, (button2_pos_x, button2_pos_y))
            DISPLAYSURF.blit(bt3, (button3_pos_x, button3_pos_y))
        elif i == 1:
            DISPLAYSURF.blit(bt1, (button1_pos_x, button1_pos_y))
            DISPLAYSURF.blit(bt2p, (button2_pos_x, button2_pos_y))
            DISPLAYSURF.blit(bt3, (button3_pos_x, button3_pos_y))
        elif i == 2:
            DISPLAYSURF.blit(bt1, (button1_pos_x, button1_pos_y))
            DISPLAYSURF.blit(bt2, (button2_pos_x, button2_pos_y))
            DISPLAYSURF.blit(bt3p, (button3_pos_x, button3_pos_y))
           
        for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                if event.type == KEYDOWN:        
                         if (event.key == K_DOWN):
                           if i == 2:
                               i = 0
                           else: 
                               i += 1
                         if (event.key == K_UP):
                                   if i == 0:
                                       i = 2
                                   else: 
                                       i -= 1
                                 
                         if (event.key == K_RETURN) and i == 0:  
                             return 
                         elif (event.key == K_RETURN) and i == 1:
                                return
                         elif (event.key == K_RETURN) and i == 2:
                                terminate()
                       
        
        
        FPSCLOCK.tick(FPS)
        pygame.display.update() 

def checkForKeyPress():
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
        elif event.type == KEYUP:
            if event.key == K_ESCAPE:
                terminate
            else:
                return True



def drawPressKeyMsg():
    pressKeySurf = BASICFONT.render("Press any key to play...", True, DARKGRAY)
    pressKeyRect = pressKeySurf.get_rect() 
    pressKeyRect.bottomright = (WINDOWWIDTH - 10, WINDOWHEIGHT - 10)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

if __name__ == '__main__':
    main()