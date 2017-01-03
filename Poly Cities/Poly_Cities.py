#def
def settingsUpdate():
    print 'New Settings info: SX=' +str(sx) +str(' |SY=') +str(sy) +str(' |SR=') +str(wsx) +str('X') +str(wsy) + str(' |Mode=') +str(mode) +str(' |devMode=') +str(devMode) +str(' |renderer=') +str(renderer)

def message(text, x, y, xs, ys):
    global OpenMessage
    OpenMessage = True
    if OpenMessage == True:
        pygame.draw.rect(screen, blue3, [x, y, xs, ys])
        screen.blit(menu_font.render(text, True, gray), (x, y))
        if mx > x and mx < x + 100 and my > y+70 and my < y+60+70:
            pygame.draw.rect(screen, gray, [x, y + 70, 100, 60])
            plus_text = menu_font.render(('Ok'), True, black)
            screen.blit(plus_text,(x, y + 70))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                OpenMessage = False
        else:
            pygame.draw.rect(screen, gray2, [x, y + 70, 100, 60])
            plus_text = menu_font.render(('Ok'), True, black)
            screen.blit(plus_text,(x, y + 70))

try:
    import os
    import pygame
    from pygame import *
    from pygame.locals import *
    import random
    import sys
    import pickle
    import time
    import pyError
    from Tkinter import *
    from tkFileDialog import*
    import random
except:
    os.chdir('html')
    os.startfile('missingModule.html')

try:
    import pyError
except:
    os.chdir('html')
    os.startfile('missingPyError.html')

clock = pygame.time.Clock()

#colors
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 150, 200)
blue2 = (44, 157, 201)
blue3 = (8, 140, 196)
blue4 = (40, 181, 166)
red = (255, 0, 0)
green = (0, 255, 0)
green2 = (0, 153, 0)
green3 = (0,100,0)
gray = (158, 156, 166)
gray2 = (69, 67, 68)
gray3 = (140, 138, 139)

#images
try:
    os.chdir('images')
    main_back1 = pygame.image.load("main_backround1.jpg")
    menu1_img = pygame.image.load("menu.png")
    mouse = pygame.image.load("mouse.png")
    mouse2 = pygame.image.load("mouse2.png")
    menu2_img = pygame.image.load("menuBack.png")
    checked_img = pygame.image.load("checked.png")
    unchecked_img = pygame.image.load("unchecked.png")
    grass1_img = pygame.image.load("grass1.png")
    logo = pygame.image.load('logo.png')
    GUIbar = pygame.image.load('GUIbar.png')
    roadGUI_img = pygame.image.load('roadGUI.png')
    roadGUI2_img = pygame.image.load('roadGUI2.png')
    road_img = pygame.image.load('road.png')
    backGUI_img = pygame.image.load('backGUI.png')
    outline_img = pygame.image.load('outline.png')
    roadTurnGUI_img = pygame.image.load('roadTurnGUI.png')
    roadTurn_img = pygame.image.load('roadTurn.png')
    terraformGUI_img = pygame.image.load('terraformGUI.png')
    waterGUI_img = pygame.image.load('waterGUI.png')
    water_img = pygame.image.load('water.png')
    grassGUI_img = pygame.image.load('grassGUI.png')
    topGuiBar_img = pygame.image.load('topGuiBar.png')
    topGuiBarData_img = pygame.image.load('topGuiData.png')
    topGuiBarMoney_img = pygame.image.load('topGuiLogoMoney.png')
    tree1_img = pygame.image.load('tree1.png')
    tree2_img = pygame.image.load('tree2.png')
    grass2_img = pygame.image.load('grass2.png')
    grass3_img = pygame.image.load('grass3.png')
    midwest_img = pygame.image.load('theMidwest.png')
    west_img = pygame.image.load('theWest.png')
    notheast_img = pygame.image.load('theNortheast.png')
    south_img = pygame.image.load('theSouth.png')
    midwestHover_img = pygame.image.load('theMidwestHover.png')
    westHover_img = pygame.image.load('theWestHover.png')
    notheastHover_img = pygame.image.load('theNortheastHover.png')
    southHover_img = pygame.image.load('theSouthHover.png')
    sand_img = pygame.image.load('sand.png')
    buildingsGUI = pygame.image.load('buildingsGUI.png')
    smallHouseGUI_img = pygame.image.load('smallHouseGUI.png')
    smallHouse_img = pygame.image.load('smallHouse.png')
    logo1_img = pygame.image.load('logo1.png')
    logo2_img = pygame.image.load('logo2.png')
    AButton_img = pygame.image.load('A_Button.png')
    BButton_img = pygame.image.load('B_Button.png')
    XButton_img = pygame.image.load('X_Button.png')
    YButton_img = pygame.image.load('Y_Button.png')
    #loading animation
    os.chdir('loading animation')
    loading1 = pygame.image.load("loading1.png")
    loading2 = pygame.image.load("loading2.png")
    loading3 = pygame.image.load("loading3.png")
    loading4 = pygame.image.load("loading4.png")
    loading5 = pygame.image.load("loading5.png")
    loading6 = pygame.image.load("loading6.png")
    loading7 = pygame.image.load("loading7.png")
    os.chdir('..')
    os.chdir('..')
except:
    pyError.newError('poly cities Error', 'There was an error on start', 'there was an issue getting images', 20, 20) 

#setup
clock = pygame.time.Clock()

#vars
rendermode = 0
show_mouse = 1
gamex = -3750
gamey = -3750
devMode = False
pickle_in = open('devMode.pcr', 'r')
devMode = pickle.load(pickle_in)
pickle_in = open('visualizations.pcr', 'r')
visualizations = pickle.load(pickle_in)
place = 'none'
placeSav = 'none'
saveLoad = 0
guiMenu = 'home'
angle = 0
cityName = ''
ver = 'alpha 1.1.0 pre-release'
renderer = 'r2'
renderTrees = True
selected = False
OpenMessage = False
benchmark = 'loading screens'
loadingPer = 0
loading = ''
loadingList = []
alphaMenu = True
customizeTrees = 50
customizeWater = 50
fpsMessage = True
mousex = 100
mousey = 100


#pygame start
try:
    from win32api import GetSystemMetrics
except:
    pyError.newError('poly cities Error', 'There was an error on start', 'there was an issue importing win32api(pywin32), make sure to use exe', 20, 20)   
try:  
    #print "Width =", GetSystemMetrics(0)
    #print "Height =", GetSystemMetrics(1)
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % ( GetSystemMetrics(0) / 4, 1)
    pygame.init()
    wsx = GetSystemMetrics(0)
    wsy = GetSystemMetrics(1)
    if devMode == True:
        print 'WARNING: You are in dev mode!'
        sx = wsx - 100
        sy = wsy - 100
        mode = RESIZABLE
    elif devMode == 'safeMode':
        print 'WARNING: You are in safe mode!'
        sx = wsx - 500
        sy = wsy - 500
        mode = RESIZABLE
    else:
        sx = wsx
        sy = wsy
        mode = FULLSCREEN
    screen = pygame.display.set_mode([sx,sy], mode)
    print 'Start info: SX=' +str(sx) +str(' |SY=') +str(sy) +str(' |SR=') +str(wsx) +str('X') +str(wsy) + str(' |Mode=') +str(mode) +str(' |devMode=') +str(devMode)
except:
    pyError.newError('poly cities Error', 'There was an error on start', 'We dont know what happened', 20, 20)   

#fonts
menu_font = pygame.font.SysFont('Calibri', 40)
hud_font = pygame.font.SysFont('Calibri', 40)
hud_font2 = pygame.font.SysFont('Calibri', 20)
big_font = pygame.font.SysFont('Calibri', 80)
title_font = pygame.font.SysFont('Calibri', 100)

#window settings
pygame.display.set_icon(logo)
pygame.display.set_caption("Poly City")

#joystick
pygame.joystick.init()
try:
    j = pygame.joystick.Joystick(0)
    j.init()
except pygame.error:
    print 'no joystick found.'

#first time
try:
    pickle_in = open('firstStart.pcr', 'r')
    rendermode = 0
except:
    pickle_out = open('firstStart.pcr', 'w')
    pickle.dump(True, pickle_out)
    pickle_out.close()
    rendermode = 0

#program
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==VIDEORESIZE:
            screen=pygame.display.set_mode(event.dict['size'], mode)
            sx, sy = screen.get_size()

    #settings
    fps_text = menu_font.render('FPS:' +str (clock.get_fps()), True, white)
    screen.fill(gray)
    clock.tick(200)
    mx, my = pygame.mouse.get_pos()


    if rendermode == 0:
        main_back1=pygame.transform.scale(main_back1, (sx * 2, sy))
        screen.blit(main_back1,((mx-2655)/10,0))
        screen.blit(logo1_img,(sx - 500, sy/2 - 470))
        pygame.draw.rect(screen, blue3, [sx - 500, sy/2 - 180, 400, 450])

        if mx > sx - 450 and mx < sx - 450 + 300 and my > sy / 2 - 150 and my < sy / 2 - 150 + 90:
            pygame.draw.rect(screen, blue, [sx - 450, sy / 2 - 150, 300, 90])
            play_text = menu_font.render(('New'), True, black)
            screen.blit(play_text,(sx - 450, sy / 2 - 150))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                rendermode = 'new'
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    pygame.time.delay(100) 
        else:
            pygame.draw.rect(screen, blue2, [sx - 450, sy / 2 - 150, 300, 90])
            play_text = menu_font.render(('New'), True, black)
            screen.blit(play_text,(sx - 450, sy / 2 - 150))

        if mx > sx - 450 and mx < sx - 450 + 300 and my > sy / 2 - 50 and my < sy / 2 - 50 + 90:
            pygame.draw.rect(screen, blue, [sx - 450, sy / 2 - 50, 300, 90])
            play_text = menu_font.render(('Load'), True, black)
            screen.blit(play_text,(sx - 450, sy / 2 - 50))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                saveLoad = 'load'
        else:
            pygame.draw.rect(screen, blue2, [sx - 450, sy / 2 - 50, 300, 90])
            play_text = menu_font.render(('Load'), True, black)
            screen.blit(play_text,(sx - 450, sy / 2 - 50))

        if mx > sx - 450 and mx < sx - 450 + 300 and my > sy / 2 + 50 and my < sy / 2 + 50 + 90:
            pygame.draw.rect(screen, blue, [sx - 450, sy / 2 + 50, 300, 90])
            play_text = menu_font.render(('Settings'), True, black)
            screen.blit(play_text,(sx - 450, sy / 2 + 50))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                rendermode = 'settings'
        else:
            pygame.draw.rect(screen, blue2, [sx - 450, sy / 2 + 50, 300, 90])
            play_text = menu_font.render(('Settings'), True, black)
            screen.blit(play_text,(sx - 450, sy / 2 + 50))

        if mx > sx - 450 and mx < sx - 450 + 300 and my > sy / 2 + 150 and my < sy / 2 + 150 + 90:
            pygame.draw.rect(screen, blue, [sx - 450, sy / 2 + 150, 300, 90])
            play_text = menu_font.render(('Quit'), True, black)
            screen.blit(play_text,(sx - 450, sy / 2 + 150))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                sys.exit()
        else:
            pygame.draw.rect(screen, blue2, [sx - 450, sy / 2 + 150, 300, 90])
            play_text = menu_font.render(('Quit'), True, black)
            screen.blit(play_text,(sx - 450, sy / 2 + 150))

        if pygame.joystick.get_count() > 0:
            screen.blit(AButton_img, (sx - 250, sy / 2 - 135))
            screen.blit(BButton_img, (sx - 250, sy / 2 - 35))
            screen.blit(XButton_img, (sx - 250, sy / 2 + 65))
            screen.blit(YButton_img, (sx - 250, sy / 2 + 165))
            if event.type == pygame.JOYBUTTONDOWN:
                 if event.button == 0:
                    rendermode = 'new'   
            if event.type == pygame.JOYBUTTONDOWN:
                 if event.button == 1:
                    saveLoad = 'load'  
            if event.type == pygame.JOYBUTTONDOWN:
                 if event.button == 2:
                    rendermode = 'settings'  
            if event.type == pygame.JOYBUTTONDOWN:
                 if event.button == 3:
                     sys.exit()


        #if alphaMenu == True:
        #    pygame.draw.rect(screen, blue3, [sx / 2 - 325, sy / 2 - 100, 650, 200])
        #    screen.blit(menu_font.render('Remember:', True, gray), (sx / 2 - 325, sy / 2 - 100))
        #    screen.blit(menu_font.render('Poly Cities is in alpha remember', True, gray), (sx / 2 - 325, sy / 2 - 100 + 30))
        #    screen.blit(menu_font.render('that there are bugs and there are', True, gray), (sx / 2 - 325, sy / 2 - 100 + 60))
        #    screen.blit(menu_font.render('lots to be added to the game.', True, gray), (sx / 2 - 325, sy / 2 - 100 + 90))
        #    if mx > sx / 2 - 325 + 10 and mx < sx / 2 - 325 + 10 + 100 and my > sy / 2 - 100 + 130 and my < sy / 2 - 100 + 130 + 60:
        #        pygame.draw.rect(screen, gray, [sx / 2 - 325 + 10, sy / 2 - 100 + 130, 100, 60])
        #        plus_text = menu_font.render(('Ok'), True, black)
        #        screen.blit(plus_text,(sx / 2 - 325 + 10, sy / 2 - 100 + 130))
        #        if event.type == MOUSEBUTTONDOWN and event.button == 1:
        #            alphaMenu = False
        #    else:
        #        pygame.draw.rect(screen, gray2, [sx / 2 - 325 + 10, sy / 2 - 100 + 130, 100, 60])
        #        plus_text = menu_font.render(('Ok'), True, black)
        #        screen.blit(plus_text,(sx / 2 - 325 + 10, sy / 2 - 100 + 130))

    if rendermode == 'firstStart':
        pygame.draw.rect(screen, blue3, [sx / 2 - 325, sy / 2 - 100, 650, 200])
        screen.blit(menu_font.render('It seems to be your first time here,', True, gray), (sx / 2 - 325, sy / 2 - 100))
        screen.blit(menu_font.render('would you like us to run a benchmark', True, gray), (sx / 2 - 325, sy / 2 - 100 + 30))
        screen.blit(menu_font.render('so we can select the best settings for', True, gray), (sx / 2 - 325, sy / 2 - 100 + 60))
        screen.blit(menu_font.render('your computer', True, gray), (sx / 2 - 325, sy / 2 - 100 + 90))
        if mx > sx / 2 - 325 + 10 and mx < sx / 2 - 325 + 10 + 100 and my > sy / 2 - 100 + 130 and my < sy / 2 - 100 + 130 + 60:
            pygame.draw.rect(screen, gray, [sx / 2 - 325 + 10, sy / 2 - 100 + 130, 100, 60])
            plus_text = menu_font.render(('Ok'), True, black)
            screen.blit(plus_text,(sx / 2 - 325 + 10, sy / 2 - 100 + 130))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                rendermode = 'benchmark'
        else:
            pygame.draw.rect(screen, gray2, [sx / 2 - 325 + 10, sy / 2 - 100 + 130, 100, 60])
            plus_text = menu_font.render(('Ok'), True, black)
            screen.blit(plus_text,(sx / 2 - 325 + 10, sy / 2 - 100 + 130))

        if mx > sx / 2 - 325 + 650 - 110 and mx < sx / 2 - 325 + 650 - 110 + 100 and my > sy / 2 - 100 + 130 and my < sy / 2 - 100 + 130 + 60:
            pygame.draw.rect(screen, gray, [sx / 2 - 325 + 650 - 110 , sy / 2 - 100 + 130, 100, 60])
            plus_text = menu_font.render(('No'), True, black)
            screen.blit(plus_text,(sx / 2 - 325 + 650 - 110, sy / 2 - 100 + 130))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                rendermode = 0
        else:
            pygame.draw.rect(screen, gray2, [sx / 2 - 325 + 650 - 110, sy / 2 - 100 + 130, 100, 60])
            plus_text = menu_font.render(('No'), True, black)
            screen.blit(plus_text,(sx / 2 - 325 + 650 - 110, sy / 2 - 100 + 130))

    if rendermode == 'benchmark':
        if devMode == True:
            screen.blit(menu_font.render('you are in DevMode', True, black),(sx / 2 - 100, sy / 2))  
        else:
            main_back1=pygame.transform.scale(main_back1, (sx, sy))
            screen.blit(main_back1,(0,0))
        pygame.draw.rect(screen, gray2, [100, sy - 270, 620, 60])
        pygame.draw.rect(screen, blue2, [110, sy - 260, loadingPer, 40])     
        pygame.draw.rect(screen, gray2, [100, sy - 200, 620, 60])
        screen.blit(menu_font.render('Benchmarking: '+str(loading), True, blue2),(110, sy - 190))

    if rendermode == 'benchmark':
        if benchmark == 'loading screens':
            if len(loadingList) < 11:
                loading = 'loading screens'
                loadingPer = 100
                loadingList.append(clock.get_fps())
            else:
                loadingFPS = (loadingList[1] + loadingList[2] + loadingList[3] + loadingList[4] + loadingList[5] + loadingList[6] + loadingList[7] + loadingList[8] + loadingList[9] + loadingList[10]) / 10
                loadingList = []
                benchmark = 'rendering'

    if rendermode == 'settings':
        #try:
            main_back1=pygame.transform.scale(main_back1, (sx * 2, sy))
            screen.blit(main_back1,((mx-2655)/10,0))
            menu2_img = pygame.transform.scale(menu2_img, (sx - 200, sy - 200))
            screen.blit(menu2_img, (100, 100))
            if mx > 100 and mx < 160 and my > 100 and my < 160:
                pygame.draw.rect(screen, gray, [100, 100, 60, 60])
                plus_text = menu_font.render(('<'), True, black)
                screen.blit(plus_text,(110 ,110))
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    rendermode = 0
            else:
                pygame.draw.rect(screen, gray2, [100, 100, 60, 60])
                plus_text = menu_font.render(('<'), True, black)
                screen.blit(plus_text,(110 ,110))
            res = menu_font.render('RES:', True, black)
            screen.blit(res, (100, 200))
            res = menu_font.render(''+str(sx)+str('X')+str(sy), True, black)
            screen.blit(res, (280, 200))
            if mx > 190 and mx < 260 and my > 200 and my < 260:
                pygame.draw.rect(screen, gray, [190, 200, 60, 60])
                plus_text = menu_font.render(('-'), True, black)
                screen.blit(plus_text,(210 ,210))
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    sx = sx - 100
                    sy = sy - 100
                    screen = pygame.display.set_mode([sx,sy], mode)
                    settingsUpdate()
                    pygame.time.wait(100)
            else:
                pygame.draw.rect(screen, gray2, [190, 200, 60, 60])
                plus_text = menu_font.render(('-'), True, black)
                screen.blit(plus_text,(210 ,210))
            if mx > 490 and mx < 550 and my > 200 and my < 260:
                pygame.draw.rect(screen, gray, [490, 200, 60, 60])
                plus_text = menu_font.render(('+'), True, black)
                screen.blit(plus_text,(510 ,210))
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    sx = sx + 100
                    sy = sy + 100
                    settingsUpdate()
                    screen = pygame.display.set_mode([sx,sy], mode)
                    pygame.time.wait(100)
            else:
                pygame.draw.rect(screen, gray2, [490, 200, 60, 60])
                plus_text = menu_font.render(('+'), True, black)
                screen.blit(plus_text,(510 ,210))

            fs = menu_font.render('FULLSCREEN:', True, black)
            screen.blit(fs, (100, 300))
            if mode == FULLSCREEN:
                screen.blit(checked_img, (350, 300))
                if mx > 350 and mx < 410 and my > 300 and my < 360:
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        mode = RESIZABLE
                        screen = pygame.display.set_mode([sx,sy], mode)
                        settingsUpdate()
                        pygame.time.wait(100)
            else:
                screen.blit(unchecked_img, (350, 300))
                if mx > 350 and mx < 410 and my > 300 and my < 360:
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        mode = FULLSCREEN
                        screen = pygame.display.set_mode([sx,sy], mode)
                        settingsUpdate()
                        pygame.time.wait(100)

            fs = menu_font.render('USE OLD R1 RENDERER:', True, black)
            screen.blit(fs, (100, 390))
            if renderer == 'r1':
                screen.blit(checked_img, (500, 390))
                if mx > 500 and mx < 560 and my > 390 and my < 450:
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        renderer = 'r2'
                        settingsUpdate()
                        pygame.time.wait(100)
            else:
                screen.blit(unchecked_img, (500, 390))
                if mx > 500 and mx < 560 and my > 390 and my < 450:
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        renderer = 'r1'
                        settingsUpdate()
                        pygame.time.wait(100)

            fs = menu_font.render('RENDER TREES:', True, black)
            screen.blit(fs, (100, 480))
            if renderTrees == True:
                screen.blit(checked_img, (380, 480))
                if mx > 380 and mx < 440 and my > 480 and my < 540:
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        renderTrees = False
                        settingsUpdate()
                        pygame.time.wait(100)
            else:
                screen.blit(unchecked_img, (380, 480))
                if mx > 380 and mx < 440 and my > 480 and my < 540:
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        renderTrees = True
                        settingsUpdate()
                        pygame.time.wait(100)

            if mx > 100 and mx < 370 and my > 570 and my < 630:
                pygame.draw.rect(screen, gray, [100, 570, 270, 60])
                plus_text = menu_font.render(('Find Joystick'), True, black)
                screen.blit(plus_text,(100, 570))
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    pygame.joystick.init()
                    try:
                        j = pygame.joystick.Joystick(0)
                        j.init()
                    except pygame.error:
                        print 'no joystick found.'
            else:
                pygame.draw.rect(screen, gray2, [100, 570, 270, 60])
                plus_text = menu_font.render(('Find Joystick'), True, black)
                screen.blit(plus_text,(100, 570))

        #except:
        #    print 'Error updating settings: SX=' +str(sx) +str(' |SY=') +str(sy) +str(' |SR=') +str(wsx) +str('X') +str(wsy) + str(' |Mode=') +str(mode) +str(' |devMode=') +str(devMode)

    if rendermode == 'settings from pause':
        try:
            main_back1=pygame.transform.scale(main_back1, (sx * 2, sy))
            screen.blit(main_back1,((mx-2655)/10,0))
            menu2_img = pygame.transform.scale(menu2_img, (sx - 200, sy - 200))
            screen.blit(menu2_img, (100, 100))
            if mx > 100 and mx < 160 and my > 100 and my < 160:
                pygame.draw.rect(screen, gray, [100, 100, 60, 60])
                plus_text = menu_font.render(('<'), True, black)
                screen.blit(plus_text,(110 ,110))
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    rendermode = 'pause'
            else:
                pygame.draw.rect(screen, gray2, [100, 100, 60, 60])
                plus_text = menu_font.render(('<'), True, black)
                screen.blit(plus_text,(110 ,110))
            res = menu_font.render('RES:', True, black)
            screen.blit(res, (100, 200))
            res = menu_font.render(''+str(sx)+str('X')+str(sy), True, black)
            screen.blit(res, (280, 200))
            if mx > 190 and mx < 260 and my > 200 and my < 260:
                pygame.draw.rect(screen, gray, [190, 200, 60, 60])
                plus_text = menu_font.render(('-'), True, black)
                screen.blit(plus_text,(210 ,210))
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    sx = sx - 100
                    sy = sy - 100
                    screen = pygame.display.set_mode([sx,sy], mode)
                    settingsUpdate()
                    pygame.time.wait(100)
            else:
                pygame.draw.rect(screen, gray2, [190, 200, 60, 60])
                plus_text = menu_font.render(('-'), True, black)
                screen.blit(plus_text,(210 ,210))
            if mx > 490 and mx < 550 and my > 200 and my < 260:
                pygame.draw.rect(screen, gray, [490, 200, 60, 60])
                plus_text = menu_font.render(('+'), True, black)
                screen.blit(plus_text,(510 ,210))
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    sx = sx + 100
                    sy = sy + 100
                    settingsUpdate()
                    screen = pygame.display.set_mode([sx,sy], mode)
                    pygame.time.wait(100)
            else:
                pygame.draw.rect(screen, gray2, [490, 200, 60, 60])
                plus_text = menu_font.render(('+'), True, black)
                screen.blit(plus_text,(510 ,210))

            fs = menu_font.render('FULLSCREEN:', True, black)
            screen.blit(fs, (100, 300))
            if mode == FULLSCREEN:
                screen.blit(checked_img, (350, 300))
                if mx > 350 and mx < 410 and my > 300 and my < 360:
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        mode = RESIZABLE
                        screen = pygame.display.set_mode([sx,sy], mode)
                        settingsUpdate()
                        pygame.time.wait(100)
            else:
                screen.blit(unchecked_img, (350, 300))
                if mx > 350 and mx < 410 and my > 300 and my < 360:
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        mode = FULLSCREEN
                        screen = pygame.display.set_mode([sx,sy], mode)
                        settingsUpdate()
                        pygame.time.wait(100)

            fs = menu_font.render('USE OLD R1 RENDERER:', True, black)
            screen.blit(fs, (100, 390))
            if renderer == 'r1':
                screen.blit(checked_img, (500, 390))
                if mx > 500 and mx < 560 and my > 390 and my < 450:
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        renderer = 'r2'
                        settingsUpdate()
                        pygame.time.wait(100)
            else:
                screen.blit(unchecked_img, (500, 390))
                if mx > 500 and mx < 560 and my > 390 and my < 450:
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        renderer = 'r1'
                        settingsUpdate()
                        pygame.time.wait(100)

            fs = menu_font.render('RENDER TREES:', True, black)
            screen.blit(fs, (100, 480))
            if renderTrees == True:
                screen.blit(checked_img, (380, 480))
                if mx > 380 and mx < 440 and my > 480 and my < 540:
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        renderTrees = False
                        settingsUpdate()
                        pygame.time.wait(100)
            else:
                screen.blit(unchecked_img, (380, 480))
                if mx > 380 and mx < 440 and my > 480 and my < 540:
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        renderTrees = True
                        settingsUpdate()
                        pygame.time.wait(100)
        except:
            print 'Error updating settings: SX=' +str(sx) +str(' |SY=') +str(sy) +str(' |SR=') +str(wsx) +str('X') +str(wsy) + str(' |Mode=') +str(mode) +str(' |devMode=') +str(devMode)


    if rendermode == 'new':
        main_back1=pygame.transform.scale(main_back1, (sx * 2, sy))
        screen.blit(main_back1,((mx-2655)/10,0))
        menu2_img = pygame.transform.scale(menu2_img, (sx - 200, sy - 200))
        screen.blit(menu2_img, (100, 100))
        if mx > sx/2-580 and mx < sx/2-580 + 210 and my > 200 and my < 200 + 280:
            screen.blit(westHover_img,(sx/2-580, 200))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                selected = 'west'
        else:
            screen.blit(west_img,(sx/2-580, 200))

        if mx > sx/2-351 and mx < sx/2-351 + 251 and my > 225 and my < 225 + 192:
            screen.blit(midwestHover_img,(sx/2-351, 225))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                selected = 'midwest'
        else:
            screen.blit(midwest_img,(sx/2-351, 225))

        if mx > sx/2-97 and mx < sx/2-97 + 127 and my > 220 and my < 220 + 134:
            screen.blit(notheastHover_img,(sx/2-97, 220))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                selected = 'northeast'
        else:
            screen.blit(notheast_img,(sx/2-97, 220))

        if mx > sx/2-355 and mx < sx/2-355 + 364 and my > 420 and my < 420 + 122:
            screen.blit(southHover_img,(sx/2-385, 350))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                selected = 'south'
        else:
            screen.blit(south_img,(sx/2-385, 350))

        pygame.draw.rect(screen, blue3, [sx/2-580-50, 600, 650, 200])
        screen.blit(big_font.render(('Region Attributes'), True, black), (sx/2-580, 600))

        if mx > sx/2-580-50 and mx < sx/2-580-50+170 and my > 530 and my < 590:
            pygame.draw.rect(screen, blue, [sx/2-580-50, 530, 170, 60])
            plus_text = menu_font.render(('Customize'), True, black)
            screen.blit(plus_text,(sx/2-580-50, 530))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                rendermode = 'customize'
        else:
            pygame.draw.rect(screen, blue2, [sx/2-580-50, 530, 170, 60])
            plus_text = menu_font.render(('Customize'), True, black)
            screen.blit(plus_text,(sx/2-580-50, 530))

        if not selected == False:
            if selected == 'west':
                screen.blit(westHover_img,(sx/2-580, 200))
                screen.blit(menu_font.render('-Mountains', True, gray), (sx/2-580, 680))
                screen.blit(menu_font.render('-Oceans', True, gray), (sx/2-580, 710))
                screen.blit(menu_font.render('-Plains', True, gray), (sx/2-580, 740))
            if selected == 'midwest':
                screen.blit(midwestHover_img,(sx/2-351, 225))
                screen.blit(menu_font.render('-Rolling hills', True, gray), (sx/2-580, 680))
                screen.blit(menu_font.render('-Plains', True, gray), (sx/2-580, 710))
                screen.blit(menu_font.render('-Forests', True, gray), (sx/2-580, 740))
                screen.blit(menu_font.render('-Rivers', True, gray), (sx/2-580, 770))
            if selected == 'northeast':
                screen.blit(notheastHover_img,(sx/2-97, 220))
                screen.blit(menu_font.render('-Coastal Plains', True, gray), (sx/2-580, 680))
                screen.blit(menu_font.render('-Mountains', True, gray), (sx/2-580, 710))
                screen.blit(menu_font.render('-Forests', True, gray), (sx/2-580, 740))
            if selected == 'south':
                screen.blit(southHover_img,(sx/2-385, 350))
                screen.blit(menu_font.render('-Oceans', True, gray), (sx/2-580, 680))
                screen.blit(menu_font.render('-Rivers', True, gray), (sx/2-580, 710))
                screen.blit(menu_font.render('-Deserts', True, gray), (sx/2-580, 740))
            if selected == 'custom':
                screen.blit(southHover_img,(sx/2-385, 350))
                screen.blit(menu_font.render('-Custom', True, gray), (sx/2-580, 680))
        else:
            screen.blit(menu_font.render('-Pick a region', True, red), (sx/2-580, 680))

        #cs_text = big_font.render(('COMMING SOON'), True, red)
        #screen.blit(cs_text,(sx / 2 - 580 ,350))
        pygame.draw.rect(screen, blue3, [sx / 2 + 350, 160, 250, 320])
        gm_text = menu_font.render(('gamemode:'), True, black)
        screen.blit(gm_text,(sx / 2 + 370, 160))
        if mx > 100 and mx < 160 and my > 100 and my < 160:
            pygame.draw.rect(screen, blue, [100, 100, 60, 60])
            plus_text = menu_font.render(('<'), True, black)
            screen.blit(plus_text,(110 ,110))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                rendermode = 0
        else:
            pygame.draw.rect(screen, blue2, [100, 100, 60, 60])
            plus_text = menu_font.render(('<'), True, black)
            screen.blit(plus_text,(110 ,110))

        if mx > sx / 2 + 400 and mx < sx / 2 + 550 and my > 270 and my < 320:
            pygame.draw.rect(screen, blue, [sx / 2 + 400, 270, 150, 60])
            plus_text = menu_font.render(('Sandbox'), True, black)
            screen.blit(plus_text,(sx / 2 + 400 ,270))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                rendermode = 'load sandbox'
        else:
            pygame.draw.rect(screen, blue2, [sx / 2 + 400, 270, 150, 60])
            plus_text = menu_font.render(('Sandbox'), True, black)
            screen.blit(plus_text,(sx / 2 + 400, 270))

        if mx > sx / 2 + 400 and mx < sx / 2 + 550 and my > 370 and my < 420:
            pygame.draw.rect(screen, blue, [sx / 2 + 400, 370, 150, 60])
            plus_text = menu_font.render(('Career'), True, black)
            screen.blit(plus_text,(sx / 2 + 400 ,370))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                rendermode = 'load career'
        else:
            pygame.draw.rect(screen, blue2, [sx / 2 + 400, 370, 150, 60])
            plus_text = menu_font.render(('Career'), True, black)
            screen.blit(plus_text,(sx / 2 + 400, 370))

        if OpenMessage == True:
            message('choose a region', sx / 2 - 250, sy / 2 - 100, 500, 200)

    #if rendermode == 'load':
    #    screen.blit(main_back1,(loading_back_x, 0))
    #    loading_back_x = loading_back_x - 5

    if rendermode == 'customize':
        main_back1=pygame.transform.scale(main_back1, (sx * 2, sy))
        screen.blit(main_back1,((mx-2655)/10,0))
        menu2_img = pygame.transform.scale(menu2_img, (sx - 200, sy - 200))
        screen.blit(menu2_img, (100, 100))
        if mx > 100 and mx < 160 and my > 100 and my < 160:
            pygame.draw.rect(screen, gray, [100, 100, 60, 60])
            plus_text = menu_font.render(('<'), True, black)
            screen.blit(plus_text,(110 ,110))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                rendermode = 'new'
        else:
            pygame.draw.rect(screen, gray2, [100, 100, 60, 60])
            plus_text = menu_font.render(('<'), True, black)
            screen.blit(plus_text,(110 ,110))

        screen.blit(menu_font.render(('Tree spawning:'), True, black),(100,200))
        if mx > 350 and mx < 350 + 60 and my > 200 and my < 260:
            pygame.draw.rect(screen, gray, [350, 200, 60, 60])
            plus_text = menu_font.render(('-'), True, black)
            screen.blit(plus_text,(365 ,210))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if customizeTrees > 0:
                    customizeTrees = customizeTrees - 10
        else:
            pygame.draw.rect(screen, gray2, [350, 200, 60, 60])
            plus_text = menu_font.render(('-'), True, black)
            screen.blit(plus_text,(365 ,210))

        screen.blit(menu_font.render((str(customizeTrees)+'/100'), True, black),(420,200))

        if mx > 550 and mx < 550 + 60 and my > 200 and my < 260:
            pygame.draw.rect(screen, gray, [550, 200, 60, 60])
            plus_text = menu_font.render(('+'), True, black)
            screen.blit(plus_text,(565 ,210))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if customizeTrees < 100:
                    customizeTrees = customizeTrees + 10
        else:
            pygame.draw.rect(screen, gray2, [550, 200, 60, 60])
            plus_text = menu_font.render(('+'), True, black)
            screen.blit(plus_text,(565 ,210))

        screen.blit(menu_font.render(('Water spawning:'), True, black),(100,300))
        if mx > 350 and mx < 350 + 60 and my > 300 and my < 360:
            pygame.draw.rect(screen, gray, [350, 300, 60, 60])
            plus_text = menu_font.render(('-'), True, black)
            screen.blit(plus_text,(365 ,310))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if customizeWater > 0:
                    customizeWater = customizeWater - 10
        else:
            pygame.draw.rect(screen, gray2, [350, 300, 60, 60])
            plus_text = menu_font.render(('-'), True, black)
            screen.blit(plus_text,(365 ,310))

        screen.blit(menu_font.render((str(customizeWater)+'/100'), True, black),(420,300))

        if mx > 550 and mx < 550 + 60 and my > 300 and my < 360:
            pygame.draw.rect(screen, gray, [550, 300, 60, 60])
            plus_text = menu_font.render(('+'), True, black)
            screen.blit(plus_text,(565 ,310))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if customizeWater < 100:
                    customizeWater = customizeWater + 10
        else:
            pygame.draw.rect(screen, gray2, [550, 300, 60, 60])
            plus_text = menu_font.render(('+'), True, black)
            screen.blit(plus_text,(565 ,310))

        if mx > 350 and mx < 350 + 170 and my > 400 and my < 490:
            pygame.draw.rect(screen, gray, [350, 400, 170, 60])
            plus_text = menu_font.render(('Finish'), True, black)
            screen.blit(plus_text,(350, 400))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                rendermode = 'new'
                selected = 'custom'
        else:
            pygame.draw.rect(screen, gray2, [350, 400, 170, 60])
            plus_text = menu_font.render(('Finish'), True, black)
            screen.blit(plus_text,(350, 400))


    if rendermode == 'load sandbox':
        size = 900
        renderClock = 0
        loading_animation = 1
        loading_back_x = 0
        world = ['']
        worldSav = ['']
        worldSavAngle = ['']
        rendermode = 'load'
        population = 0
        money = 'unlimited'
        SplashFile = open('splashTxt.txt', 'r')
        SplashFile = SplashFile.readlines()
        SplashFile = SplashFile[random.randint(0,len(SplashFile) - 1)]

    if rendermode == 'load career':
        size = 900
        renderClock = 0
        loading_animation = 1
        loading_back_x = 0
        world = ['']
        worldSav = ['']
        worldSavAngle = ['']
        rendermode = 'load'
        population = 0
        money = 100000
        SplashFile = open('splashTxt.txt', 'r')
        SplashFile = SplashFile.readlines()
        SplashFile = SplashFile[random.randint(0,len(SplashFile) - 1)]

    #load
    if rendermode == 'load':
        if selected == 'west':
            if renderClock < size:
                loadRandom = random.randint(0,4)
                if loadRandom == 0:
                    world.append(grass1_img)
                    loading = 'grass1_img'
                    worldSav.append('grass1_img')
                    worldSavAngle.append(0)
                if loadRandom == 1:
                    world.append(grass2_img)
                    loading = 'grass2_img'
                    worldSav.append('grass2_img')
                    worldSavAngle.append(0)
                if loadRandom == 2:
                    world.append(grass3_img)
                    loading = 'grass3_img'
                    worldSav.append('grass3_img')
                    worldSavAngle.append(0)
                if loadRandom == 3:
                    world.append(water_img)
                    loading = 'water_img'
                    worldSav.append('water_img')
                    worldSavAngle.append(0)
                if loadRandom == 4:
                    world.append(water_img)
                    loading = 'water_img'
                    worldSav.append('water_img')
                    worldSavAngle.append(0)
                renderClock = renderClock + 1
            else:
                rendermode = 'load 2'
        elif selected == 'midwest':
            if renderClock < size:
                loadRandom = random.randint(0,4)
                if loadRandom == 0:
                    world.append(grass1_img)
                    loading = 'grass1_img'
                    worldSav.append('grass1_img')
                    worldSavAngle.append(0)
                if loadRandom == 1:
                    world.append(grass2_img)
                    loading = 'grass2_img'
                    worldSav.append('grass2_img')
                    worldSavAngle.append(0)
                if loadRandom == 2:
                    world.append(grass3_img)
                    loading = 'grass3_img'
                    worldSav.append('grass3_img')
                    worldSavAngle.append(0)
                if loadRandom == 3:
                    world.append(grass3_img)
                    loading = 'grass3_img'
                    worldSav.append('grass3_img')
                    worldSavAngle.append(0)
                if loadRandom == 4:
                    world.append(water_img)
                    loading = 'water_img'
                    worldSav.append('water_img')
                    worldSavAngle.append(0)
                renderClock = renderClock + 1
            else:
                rendermode = 'load 2'
        elif selected == 'northeast':
            if renderClock < size:
                loadRandom = random.randint(0,4)
                if loadRandom == 0:
                    world.append(grass1_img)
                    loading = 'grass1_img'
                    worldSav.append('grass1_img')
                    worldSavAngle.append(0)
                if loadRandom == 1:
                    world.append(grass2_img)
                    loading = 'grass2_img'
                    worldSav.append('grass2_img')
                    worldSavAngle.append(0)
                if loadRandom == 2:
                    world.append(grass3_img)
                    loading = 'grass3_img'
                    worldSav.append('grass3_img')
                    worldSavAngle.append(0)
                if loadRandom == 3:
                    world.append(water_img)
                    loading = 'water_img'
                    worldSav.append('water_img')
                    worldSavAngle.append(0)
                if loadRandom == 4:
                    world.append(water_img)
                    loading = 'water_img'
                    worldSav.append('water_img')
                    worldSavAngle.append(0)
                renderClock = renderClock + 1
            else:
                rendermode = 'load 2'
        elif selected == 'south':
            if renderClock < size:
                loadRandom = random.randint(0,5)
                if loadRandom == 0:
                    world.append(sand_img)
                    loading = 'sand_img'
                    worldSav.append('sand_img')
                    worldSavAngle.append(0)
                if loadRandom == 1:
                    world.append(sand_img)
                    loading = 'sand_img'
                    worldSav.append('sand_img')
                    worldSavAngle.append(0)
                if loadRandom == 2:
                    world.append(sand_img)
                    loading = 'sand_img'
                    worldSav.append('sand_img')
                    worldSavAngle.append(0)
                if loadRandom == 3:
                    world.append(grass2_img)
                    loading = 'grass2_img'
                    worldSav.append('grass2_img')
                    worldSavAngle.append(0)
                if loadRandom == 4:
                    world.append(grass1_img)
                    loading = 'grass1_img'
                    worldSav.append('grass1_img')
                    worldSavAngle.append(0)
                if loadRandom == 5:
                    world.append(water_img)
                    loading = 'water_img'
                    worldSav.append('water_img')
                    worldSavAngle.append(0)
                renderClock = renderClock + 1
            else:
                rendermode = 'load 2'
        elif selected == 'custom':
            if renderClock < size:
                loadRandom = random.randint(0,100)
                if loadRandom <= customizeWater:
                    world.append(water_img)
                    loading = 'water_img'
                    worldSav.append('water_img')
                    worldSavAngle.append(0)
                else:
                    world.append(grass1_img)
                    loading = 'grass1_img'
                    worldSav.append('grass1_img')
                    worldSavAngle.append(0)
                renderClock = renderClock + 1
            else:
                rendermode = 'load 2'
        else:
            rendermode = 'new'
            OpenMessage = True

    if rendermode == 'load 2':
        loading = 'starting load 2'
        trees = ['']
        treeOffsetY = [0]
        treeOffsetX = [0]
        rendermode = 'load 3'

    if rendermode == 'load 3':
        if selected == 'west':
            if renderClock < size * 2:
                loadRandom = random.randint(0,3)
                if loadRandom == 0:
                    trees.append('none')
                    treeOffsetX.append((random.randint(0,50)))
                    treeOffsetY.append((random.randint(0,100)))
                    loading = 'tree_none'
    #                worldSavTree.append('tree1')
                if loadRandom == 1:
                    trees.append(tree2_img)
                    treeOffsetX.append((random.randint(0,50)))
                    treeOffsetY.append((random.randint(0,100)))
                    loading = 'tree2'
    #                worldSavTree.append('tree1')
                if loadRandom == 2:
                    trees.append('none')
                    treeOffsetX.append((random.randint(0,50)))
                    treeOffsetY.append((random.randint(0,100)))
                    loading = 'tree_none'
    #                worldSavTree.append('tree1')
                if loadRandom == 3:
                    trees.append('none')
                    treeOffsetX.append((random.randint(0,50)))
                    treeOffsetY.append((random.randint(0,100)))
                    loading = 'tree_none'
    #                worldSavTree.append('tree1')
                renderClock = renderClock + 1
            else:
                rendermode = 'game'
        if selected == 'midwest':
            if renderClock < size * 2:
                loadRandom = random.randint(0,3)
                if loadRandom == 0:
                    trees.append('none')
                    treeOffsetX.append((random.randint(0,50)))
                    treeOffsetY.append((random.randint(0,100)))
                    loading = 'tree_none'
    #                worldSavTree.append('tree1')
                if loadRandom == 1:
                    trees.append(tree1_img)
                    treeOffsetX.append((random.randint(0,50)))
                    treeOffsetY.append((random.randint(0,100)))
                    loading = 'tree1'
    #                worldSavTree.append('tree1')
                if loadRandom == 2:
                    trees.append(tree1_img)
                    treeOffsetX.append((random.randint(0,50)))
                    treeOffsetY.append((random.randint(0,100)))
                    loading = 'tree1'
    #                worldSavTree.append('tree1')
                if loadRandom == 3:
                    trees.append(tree1_img)
                    treeOffsetX.append((random.randint(0,50)))
                    treeOffsetY.append((random.randint(0,100)))
                    loading = 'tree1'
    #                worldSavTree.append('tree1')
                renderClock = renderClock + 1
            else:
                rendermode = 'game'
        if selected == 'northeast':
            if renderClock < size * 2:
                loadRandom = random.randint(0,3)
                if loadRandom == 0:
                    trees.append('none')
                    treeOffsetX.append((random.randint(0,50)))
                    treeOffsetY.append((random.randint(0,100)))
                    loading = 'tree_none'
    #                worldSavTree.append('tree1')
                if loadRandom == 1:
                    trees.append(tree1_img)
                    treeOffsetX.append((random.randint(0,50)))
                    treeOffsetY.append((random.randint(0,100)))
                    loading = 'tree1'
    #                worldSavTree.append('tree1')
                if loadRandom == 2:
                    trees.append(tree1_img)
                    treeOffsetX.append((random.randint(0,50)))
                    treeOffsetY.append((random.randint(0,100)))
                    loading = 'tree1'
    #                worldSavTree.append('tree1')
                if loadRandom == 3:
                    trees.append(tree1_img)
                    treeOffsetX.append((random.randint(0,50)))
                    treeOffsetY.append((random.randint(0,100)))
                    loading = 'tree1'
    #                worldSavTree.append('tree1')
                renderClock = renderClock + 1
            else:
                rendermode = 'game'

        if selected == 'south':
            if renderClock < size * 2:
                loadRandom = random.randint(0,4)
                if loadRandom == 0:
                    trees.append('none')
                    treeOffsetX.append((random.randint(0,50)))
                    treeOffsetY.append((random.randint(0,100)))
                    loading = 'tree_none'
    #                worldSavTree.append('tree1')
                if loadRandom == 1:
                    trees.append(tree2_img)
                    treeOffsetX.append((random.randint(0,50)))
                    treeOffsetY.append((random.randint(0,100)))
                    loading = 'tree2'
    #                worldSavTree.append('tree1')
                if loadRandom == 2:
                    trees.append('none')
                    treeOffsetX.append((random.randint(0,50)))
                    treeOffsetY.append((random.randint(0,100)))
                    loading = 'tree_none'
    #                worldSavTree.append('tree1')
                if loadRandom == 3:
                    trees.append('none')
                    treeOffsetX.append((random.randint(0,50)))
                    treeOffsetY.append((random.randint(0,100)))
                    loading = 'tree_none'
    #                worldSavTree.append('tree1')
                if loadRandom == 4:
                    trees.append('none')
                    treeOffsetX.append((random.randint(0,50)))
                    treeOffsetY.append((random.randint(0,100)))
                    loading = 'tree_none'
    #                worldSavTree.append('tree1')
                renderClock = renderClock + 1
            else:
                rendermode = 'game'        

        if selected == 'custom':
            if renderClock < size * 2:
                loadRandom = random.randint(customizeTrees,100)
                if loadRandom <= customizeTrees:
                    trees.append(tree2_img)
                    treeOffsetX.append((random.randint(0,50)))
                    treeOffsetY.append((random.randint(0,100)))
                    loading = 'tree2'
                else:
                    trees.append('none')
                    treeOffsetX.append((random.randint(0,50)))
                    treeOffsetY.append((random.randint(0,100)))
                    loading = 'tree_none'                    
                renderClock = renderClock + 1
            else:
                rendermode = 'game'

        if selected == 'both':
            if renderClock < size * 2:
                loadRandom = random.randint(0,2)
                if loadRandom == 0:
                    trees.append('none')
                    treeOffsetX.append((random.randint(0,50)))
                    treeOffsetY.append((random.randint(0,100)))
                    loading = 'tree_none'
    #                worldSavTree.append('tree1')
                if loadRandom == 1:
                    trees.append(tree1_img)
                    treeOffsetX.append((random.randint(0,50)))
                    treeOffsetY.append((random.randint(0,100)))
                    loading = 'tree1'
    #                worldSavTree.append('tree1')
                if loadRandom == 2:
                    trees.append(tree1_img)
                    treeOffsetX.append((random.randint(0,50)))
                    treeOffsetY.append((random.randint(0,100)))
                    loading = 'tree2'
    #                worldSavTree.append('tree1')
                renderClock = renderClock + 1
            else:
                rendermode = 'game'

    if rendermode == 'load' or rendermode == 'load 2' or rendermode == 'load 3':
        screen.fill(blue2)
        screen.blit(logo2_img,(sx/2 - 200, sy/2 - 300))
        screen.blit(big_font.render(str(SplashFile[0:len(SplashFile)-1]), True, blue3), (sx/2-len(SplashFile) * 16, sy - 350))
        pygame.draw.rect(screen, gray2, [100, sy - 270, 620, 60])
        pygame.draw.rect(screen, blue2, [110, sy - 260, renderClock/3, 40])     
        pygame.draw.rect(screen, gray2, [100, sy - 200, 620, 60])
        screen.blit(menu_font.render('Creating map tiles: '+str(loading), True, blue2),(110, sy - 190))

    #game
    if rendermode == 'game':
        if renderer == 'r1':
            render = True
            renderX = 0
            xClock = 0
            renderY = 0
            renderClock = 1
            while render == True:
                    try:
                        screen.blit(world[renderClock], (renderX + gamex, renderY + gamey))
                        if not trees[renderClock] == 'none':
                            if renderTrees == True:
                                if world[renderClock] == grass1_img:
                                    screen.blit(trees[renderClock], ((renderX + gamex)+treeOffsetX[renderClock], (renderY + gamey)+treeOffsetY[renderClock]))
                                elif world[renderClock] == grass2_img:
                                    screen.blit(trees[renderClock], ((renderX + gamex)+treeOffsetX[renderClock], (renderY + gamey)+treeOffsetY[renderClock]))
                                elif world[renderClock] == grass3_img:
                                    screen.blit(trees[renderClock], ((renderX + gamex)+treeOffsetX[renderClock], (renderY + gamey)+treeOffsetY[renderClock]))
                        if not place == 'none':
                            if mx > renderX + gamex and mx < renderX + gamex + 250 and my > renderY + gamey and my < renderY + gamey + 250:
                                screen.blit(outline_img,(renderX + gamex, renderY + gamey))
                                if event.type == MOUSEBUTTONDOWN and event.button == 1:   
                                    if not my > sy - 100:
                                        world[renderClock] = place
                                        worldSav[renderClock] = ''+str(placeSav)
                                        worldSavAngle[renderClock] = angle
                        renderX = renderX + 250
                        xClock = xClock + 1
                        renderClock = renderClock + 1
                        if xClock == 30:
                            renderX = 0
                            xClock = 0
                            renderY = renderY + 250
                    except:
                        render = False

        if renderer == 'r2':
            render = True
            renderX = 0
            xClock = 0
            renderY = 0
            renderClock = 1
            while render == True:
                if visualizations == True:
                    try:
                        if renderX + gamex > 250 - 250 and renderX + gamex < sx - 250 and renderY + gamey > 250 and renderY + gamey < sy - 250:
                            screen.blit(world[renderClock], (renderX + gamex, renderY + gamey))
                            if not trees[renderClock] == 'none':
                                if renderTrees == True:
                                    if world[renderClock] == grass1_img:
                                        if (renderX + gamex)+treeOffsetX[renderClock] > 250 - 250 and (renderX + gamex)+treeOffsetX[renderClock] < sx - 250 and (renderY + gamey)+treeOffsetY[renderClock] > 250 - 250 and (renderY + gamey)+treeOffsetY[renderClock] < sy - 250:
                                            screen.blit(trees[renderClock], ((renderX + gamex)+treeOffsetX[renderClock], (renderY + gamey)+treeOffsetY[renderClock]))
                                    elif world[renderClock] == grass2_img:
                                        if (renderX + gamex)+treeOffsetX[renderClock] > 250 - 250 and (renderX + gamex)+treeOffsetX[renderClock] < sx - 250 and (renderY + gamey)+treeOffsetY[renderClock] > 250 - 250 and (renderY + gamey)+treeOffsetY[renderClock] < sy - 250:
                                            screen.blit(trees[renderClock], ((renderX + gamex)+treeOffsetX[renderClock], (renderY + gamey)+treeOffsetY[renderClock]))
                                    elif world[renderClock] == grass3_img:
                                        if (renderX + gamex)+treeOffsetX[renderClock] > 250 - 250 and (renderX + gamex)+treeOffsetX[renderClock] < sx - 250 and (renderY + gamey)+treeOffsetY[renderClock] > 250 - 250 and (renderY + gamey)+treeOffsetY[renderClock] < sy - 250:
                                            screen.blit(trees[renderClock], ((renderX + gamex)+treeOffsetX[renderClock], (renderY + gamey)+treeOffsetY[renderClock]))
                            if not place == 'none':
                                if mx > renderX + gamex and mx < renderX + gamex + 250 and my > renderY + gamey and my < renderY + gamey + 250:
                                    screen.blit(outline_img,(renderX + gamex, renderY + gamey))
                                    if event.type == MOUSEBUTTONDOWN and event.button == 1:   
                                        if not my > sy - 100:
                                            world[renderClock] = place
                                            worldSav[renderClock] = ''+str(placeSav)
                                            worldSavAngle[renderClock] = angle
                        world[renderClock]
                        renderX = renderX + 250
                        xClock = xClock + 1
                        renderClock = renderClock + 1
                        if xClock == 30:
                            renderX = 0
                            xClock = 0
                            renderY = renderY + 250
                    except:
                        render = False
                else:
                    try:
                        if renderX + gamex > 0 - 250 and renderX + gamex < sx and renderY + gamey > 0 - 250 and renderY + gamey < sy:
                            screen.blit(world[renderClock], (renderX + gamex, renderY + gamey))
                            if not trees[renderClock] == 'none':
                                if renderTrees == True:
                                    if world[renderClock] == grass1_img:
                                        if (renderX + gamex)+treeOffsetX[renderClock] > 0 - 250 and (renderX + gamex)+treeOffsetX[renderClock] < sx and (renderY + gamey)+treeOffsetY[renderClock] > 0 - 250 and (renderY + gamey)+treeOffsetY[renderClock] < sy:
                                            screen.blit(trees[renderClock], ((renderX + gamex)+treeOffsetX[renderClock], (renderY + gamey)+treeOffsetY[renderClock]))
                                    elif world[renderClock] == grass2_img:
                                        if (renderX + gamex)+treeOffsetX[renderClock] > 0 - 250 and (renderX + gamex)+treeOffsetX[renderClock] < sx and (renderY + gamey)+treeOffsetY[renderClock] > 0 - 250 and (renderY + gamey)+treeOffsetY[renderClock] < sy:
                                            screen.blit(trees[renderClock], ((renderX + gamex)+treeOffsetX[renderClock], (renderY + gamey)+treeOffsetY[renderClock]))
                                    elif world[renderClock] == grass3_img:
                                        if (renderX + gamex)+treeOffsetX[renderClock] > 0 - 250 and (renderX + gamex)+treeOffsetX[renderClock] < sx and (renderY + gamey)+treeOffsetY[renderClock] > 0 - 250 and (renderY + gamey)+treeOffsetY[renderClock] < sy:
                                            screen.blit(trees[renderClock], ((renderX + gamex)+treeOffsetX[renderClock], (renderY + gamey)+treeOffsetY[renderClock]))
                            if not place == 'none':
                                if mx > renderX + gamex and mx < renderX + gamex + 250 and my > renderY + gamey and my < renderY + gamey + 250:
                                    screen.blit(outline_img,(renderX + gamex, renderY + gamey))
                                    if event.type == MOUSEBUTTONDOWN and event.button == 1:   
                                        if not my > sy - 100:
                                            world[renderClock] = place
                                            worldSav[renderClock] = ''+str(placeSav)
                                            worldSavAngle[renderClock] = angle
                        world[renderClock]
                        renderX = renderX + 250
                        xClock = xClock + 1
                        renderClock = renderClock + 1
                        if xClock == 30:
                            renderX = 0
                            xClock = 0
                            renderY = renderY + 250
                    except:
                        render = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:   
                gamey = gamey + 10

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:   
                gamey = gamey - 10

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:   
                gamex = gamex + 10

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:   
                gamex = gamex - 10

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:   
                rendermode = 'pause'

        if pygame.joystick.get_count() > 0:
            if j.get_axis(0) < -.1:
                gamex = gamex - j.get_axis(0) * 15             
            if j.get_axis(0) > .1:
                gamex = gamex - j.get_axis(0) * 15     
            if j.get_axis(1) < -.1:
                gamey = gamey - j.get_axis(1) * 15             
            if j.get_axis(1) > .1:
                gamey = gamey - j.get_axis(1) * 15   
            if event.type == pygame.JOYBUTTONDOWN:
                 if event.button == 6:
                    rendermode = 'pause'         

        if not place == 'none':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:   
                    outline_img = pygame.transform.rotate(outline_img, -90)
                    place = pygame.transform.rotate(place, -90)
                    angle = angle - 90
                    pygame.time.delay(100)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:   
                    outline_img = pygame.transform.rotate(outline_img, +90)
                    place = pygame.transform.rotate(place, +90)
                    angle = angle + 90
                    pygame.time.delay(100)                  
        
        GUIbar = pygame.transform.scale(GUIbar, (sx, 200))
        screen.blit(GUIbar, (0, sy - 100))
        screen.blit(topGuiBar_img, (sx / 2 - 450, 0))
        screen.blit(topGuiBarData_img, (sx / 2 - 405, 5))
        screen.blit(menu_font.render(''+str(money), True, blue2), (sx / 2 - 330, 20))
        screen.blit(topGuiBarMoney_img, (sx / 2 - 400, 10))
        screen.blit(topGuiBarData_img, (sx / 2 - 105, 5))
        screen.blit(menu_font.render(''+str(population), True, blue2), (sx / 2 - 30, 20))
        screen.blit(topGuiBarMoney_img, (sx / 2 - 100, 10))
        if guiMenu == 'home':
            screen.blit(roadGUI_img, (10, sy - 95))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:   
                if mx > 10 and mx < 100 and my > sy - 95 and my < sy - 5:
                    guiMenu = 'road'
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        pygame.time.delay(100)
            screen.blit(terraformGUI_img, (110, sy - 95))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:   
                if mx > 110 and mx < 200 and my > sy - 95 and my < sy - 5:
                    guiMenu = 'terraform'
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        pygame.time.delay(100)  
            screen.blit(buildingsGUI, (210, sy - 95))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:   
                if mx > 210 and mx < 300 and my > sy - 95 and my < sy - 5:
                    guiMenu = 'buildings'
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        pygame.time.delay(100)
        elif guiMenu == 'road':
            screen.blit(backGUI_img, (10, sy - 95))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:   
                if mx > 10 and mx < 100 and my > sy - 95 and my < sy - 5:
                    guiMenu = 'home'
                    place = 'none'
                    placeSav = 'none'
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        pygame.time.delay(100) 
            screen.blit(roadGUI2_img, (110, sy - 95))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:   
                if mx > 110 and mx < 200 and my > sy - 95 and my < sy - 5:
                    place = road_img
                    placeSav = 'road_img'
            screen.blit(roadTurnGUI_img, (210, sy - 95))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:   
                if mx > 210 and mx < 300 and my > sy - 95 and my < sy - 5:
                    place = roadTurn_img
                    placeSav = 'roadTurn_img'
        elif guiMenu == 'terraform':
            screen.blit(backGUI_img, (10, sy - 95))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:   
                if mx > 10 and mx < 100 and my > sy - 95 and my < sy - 5:
                    guiMenu = 'home'
                    place = 'none'
                    placeSav = 'none'
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        pygame.time.delay(100)
            screen.blit(waterGUI_img, (110, sy - 95))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:   
                if mx > 110 and mx < 200 and my > sy - 95 and my < sy - 5:
                    place = water_img
                    placeSav = 'water_img'
            screen.blit(grassGUI_img, (210, sy - 95))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:   
                if mx > 210 and mx < 300 and my > sy - 95 and my < sy - 5:
                    place = grass1_img
                    placeSav = grass1_img
        elif guiMenu == 'buildings':
            screen.blit(backGUI_img, (10, sy - 95))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:   
                if mx > 10 and mx < 100 and my > sy - 95 and my < sy - 5:
                    guiMenu = 'home'
                    place = 'none'
                    placeSav = 'none'
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        pygame.time.delay(100) 
            screen.blit(smallHouseGUI_img, (110, sy - 95))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:   
                if mx > 110 and mx < 200 and my > sy - 95 and my < sy - 5:
                    place = smallHouse_img
                    placeSav = 'smallHouse_img'
        if clock.get_fps() < 10:
            if fpsMessage == True:
                rendermode = 'pause'
                os.chdir('html')
                os.startfile('lowFPS.html')
                fpsMessage = False

    if rendermode == 'pause':
        main_back1=pygame.transform.scale(main_back1, (sx * 2, sy))
        screen.blit(main_back1,((mx-2655)/10,0))
        title_text = title_font.render(('Paused'), True, black)
        screen.blit(title_text,(sx/2 - 250,10))
        screen.blit(menu1_img, (sx/2 - 250, 150))
        if mx > sx/2 - 200 and mx < sx/2 - 200 + 400 and my > 160 and my < 260:
            pygame.draw.rect(screen, gray, [sx/2 - 200, 160, 400, 100])
            play_text = menu_font.render(('Unpause'), True, black)
            screen.blit(play_text,(sx/2 - 200 ,160))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                rendermode = 'game'
                pygame.time.delay(100)
        else:
            pygame.draw.rect(screen, gray2, [sx/2 - 200, 160, 400, 100])
            play_text = menu_font.render(('Unpause'), True, black)
            screen.blit(play_text,(sx/2 - 200 ,160))

        if mx > sx/2 - 200 and mx < sx/2 - 200 + 400 and my > 280 and my < 380:
            pygame.draw.rect(screen, gray, [sx/2 - 200, 280, 400, 100])
            play_text = menu_font.render(('Save'), True, black)
            screen.blit(play_text,(sx/2 - 200 ,280))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                saveLoad = 'save'
                pygame.time.delay(100)
        else:
            pygame.draw.rect(screen, gray2, [sx/2 - 200, 280, 400, 100])
            play_text = menu_font.render(('Save'), True, black)
            screen.blit(play_text,(sx/2 - 200 ,280))

        if mx > sx/2 - 200 and mx < sx/2 - 200 + 400 and my > 400 and my < 500:
            pygame.draw.rect(screen, gray, [sx/2 - 200, 400, 400, 100])
            play_text = menu_font.render(('Settings'), True, black)
            screen.blit(play_text,(sx/2 - 200 ,400))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                rendermode = 'settings from pause'
                pygame.time.delay(100)
        else:
            pygame.draw.rect(screen, gray2, [sx/2 - 200, 400, 400, 100])
            play_text = menu_font.render(('Settings'), True, black)
            screen.blit(play_text,(sx/2 - 200 ,400))

        if mx > sx/2 - 200 and mx < sx/2 - 200 + 400 and my > 520 and my < 620:
            pygame.draw.rect(screen, gray, [sx/2 - 200, 520, 400, 100])
            play_text = menu_font.render(('Quit'), True, black)
            screen.blit(play_text,(sx/2 - 200 ,520))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                rendermode = 0
                pygame.time.delay(100)
        else:
            pygame.draw.rect(screen, gray2, [sx/2 - 200, 520, 400, 100])
            play_text = menu_font.render(('Quit'), True, black)
            screen.blit(play_text,(sx/2 - 200 ,520))

    if saveLoad == 'save':
        os.chdir('saves')
        fpsMessage = False
        f = open(time.strftime('%I-%M-%S %p %m-%d-%y')+str('.sav'), 'w')
        saveClock = 0
        saveList = []
        while saveClock < len(world):
            if world[saveClock] == grass1_img:
                saveList.append('grass1_img')
            if world[saveClock] == grass2_img:
                saveList.append('grass2_img')
            if world[saveClock] == grass3_img:
                saveList.append('grass3_img')
            if world[saveClock] == water_img:
                saveList.append('water_img')
            if world[saveClock] == sand_img:
                saveList.append('sand_img')
            if world[saveClock] == smallHouse_img:
                saveList.append('smallHouse_img')
            saveClock = saveClock + 1
        else:
            f.write(str(saveList))
            f.write('\n')
            f.write('\n')
            f.write(str(gamex))
            f.write('\n')
            f.write(str(gamey))
            f.write('\n')
            f.write(str(money))
            f.write('\n')
            f.write(str(population))
            os.chdir('..')
            f.close()
            saveLoad = ''
            rendermode = 'game'

    if saveLoad == 'load':
        os.chdir('saves')
        try:
            f = askopenfile(mode = 'r')
            lines = f.readline()
            loadClock = 0
            loadCurSTR = ''
            loadSTR = ''
            try:
                while not loadCurSTR == '\n':
                    loadSTR = loadSTR + lines[loadClock]
                    loadCurStr = lines[loadClock]
                    loadClock = loadClock + 1
            except:
                loadSTR = loadSTR.split(',')
                try:
                    loadClock = 0
                    world = ['']
                    while True:
                        if loadSTR[loadClock] == (" 'grass1_img'"):
                            world.append(grass1_img)
                        elif loadSTR[loadClock] == (" 'grass2_img'"):
                            world.append(grass2_img)        
                        elif loadSTR[loadClock] == (" 'grass3_img'"):
                            world.append(grass3_img)            
                        elif loadSTR[loadClock] == (" 'sand_img'"):
                            world.append(sand_img)    
                        elif loadSTR[loadClock] == (" 'water_img'"):
                            world.append(water_img)   
                        elif loadSTR[loadClock] == (" 'smallHouse_img'"):
                            world.append(smallHouse_img)   
                        loadClock = loadClock + 1
                except:       
                    lines = f.readlines()
                    gamex = int(lines[1].replace('\n', ''))
                    gamey = int(lines[2].replace('\n', ''))
                    money = lines[3].replace('\n', '')
                    population = lines[4].replace('\n', '')
                    size = len(world)
            os.chdir('..')
            saveLoad = ''
            SplashFile = open('splashTxt.txt', 'r')
            SplashFile = SplashFile.readlines()
            SplashFile = SplashFile[random.randint(0,len(SplashFile) - 1)]
            renderClock = 0
            selected = 'both'
            rendermode = 'load 2'
        except:
            saveLoad = 0
            os.chdir('..')

    if devMode == True:
        screen.blit(fps_text, (0,0))

    #if pygame.joystick.get_count() > 0:
    #    if j.get_axis(4) < -.1:
    #        mousex = mousex + j.get_axis(4) * 15    
    #    if j.get_axis(4) > .1:
    #        mousex = mousex + j.get_axis(4) * 15    
    #    if j.get_axis(3) < -.1:
    #        mousey = mousey + j.get_axis(3) * 15  
    #    if j.get_axis(3) > .1:
    #        mousey = mousey + j.get_axis(3) * 15    
    #    pygame.mouse.set_pos(mousex,mousey)

    pygame.HWSURFACE
    pygame.display.update()