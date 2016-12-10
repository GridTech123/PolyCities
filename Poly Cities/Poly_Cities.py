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
    import pygame 
    from pygame import *
    from pygame.locals import *
    import random
    import sys
    import pickle
    import time
    import os
    import pyError
    from Tkinter import *
    from tkFileDialog import*
    import random
except:
    try:
        import pyError
        pyError.newError('poly cities Error', 'There was an error on start', 'there was an issue importing something, make sure to use exe', 20, 20)
    except:
        print 'ERROR: pyError does not exist'

#colors
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
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
place = 'none'
placeSav = 'none'
saveLoad = 0
guiMenu = 'home'
angle = 0
cityName = ''
ver = 'alpha 1.0.4 pre-release'
renderer = 'r1'
renderTrees = True
selected = False
OpenMessage = False

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
    screen.fill(gray)
    clock.tick(200)
    mx, my = pygame.mouse.get_pos()

    if rendermode == 0:
        main_back1=pygame.transform.scale(main_back1, (sx * 2, sy))
        screen.blit(main_back1,((mx-2655)/10,0))
        title_text = title_font.render(('Poly City'), True, black)
        screen.blit(title_text,(sx/2 - 250,10))
        screen.blit(menu1_img, (sx/2 - 250, 150))
        if mx > sx/2 - 200 and mx < sx/2 - 200 + 400 and my > 160 and my < 260:
            pygame.draw.rect(screen, gray, [sx/2 - 200, 160, 400, 100])
            play_text = menu_font.render(('New'), True, black)
            screen.blit(play_text,(sx/2 - 200 ,160))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                rendermode = 'new'
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    pygame.time.delay(100) 
        else:
            pygame.draw.rect(screen, gray2, [sx/2 - 200, 160, 400, 100])
            play_text = menu_font.render(('New'), True, black)
            screen.blit(play_text,(sx/2 - 200 ,160))

        if mx > sx/2 - 200 and mx < sx/2 - 200 + 400 and my > 280 and my < 380:
            pygame.draw.rect(screen, gray, [sx/2 - 200, 280, 400, 100])
            play_text = menu_font.render(('Load'), True, black)
            screen.blit(play_text,(sx/2 - 200 ,280))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                saveLoad = 'load'
        else:
            pygame.draw.rect(screen, gray2, [sx/2 - 200, 280, 400, 100])
            play_text = menu_font.render(('Load'), True, black)
            screen.blit(play_text,(sx/2 - 200 ,280))

        if mx > sx/2 - 200 and mx < sx/2 - 200 + 400 and my > 400 and my < 500:
            pygame.draw.rect(screen, gray, [sx/2 - 200, 400, 400, 100])
            play_text = menu_font.render(('Settings'), True, black)
            screen.blit(play_text,(sx/2 - 200 ,400))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                rendermode = 'settings'
        else:
            pygame.draw.rect(screen, gray2, [sx/2 - 200, 400, 400, 100])
            play_text = menu_font.render(('Settings'), True, black)
            screen.blit(play_text,(sx/2 - 200 ,400))

        if mx > sx/2 - 200 and mx < sx/2 - 200 + 400 and my > 520 and my < 620:
            pygame.draw.rect(screen, gray, [sx/2 - 200, 520, 400, 100])
            play_text = menu_font.render(('Quit'), True, black)
            screen.blit(play_text,(sx/2 - 200 ,520))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                sys.exit()
        else:
            pygame.draw.rect(screen, gray2, [sx/2 - 200, 520, 400, 100])
            play_text = menu_font.render(('Quit'), True, black)
            screen.blit(play_text,(sx/2 - 200 ,520))

    if rendermode == 'settings':
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

            fs = menu_font.render('USE EXPERIMENTAL R2 RENDERER:', True, black)
            screen.blit(fs, (100, 390))
            if renderer == 'r2':
                screen.blit(checked_img, (700, 390))
                if mx > 700 and mx < 760 and my > 390 and my < 450:
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        renderer = 'r1'
                        settingsUpdate()
                        pygame.time.wait(100)
            else:
                screen.blit(unchecked_img, (700, 390))
                if mx > 700 and mx < 760 and my > 390 and my < 450:
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        renderer = 'r2'
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

            fs = menu_font.render('USE EXPERIMENTAL R2 RENDERER:', True, black)
            screen.blit(fs, (100, 390))
            if renderer == 'r2':
                screen.blit(checked_img, (700, 390))
                if mx > 700 and mx < 760 and my > 390 and my < 450:
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        renderer = 'r1'
                        settingsUpdate()
                        pygame.time.wait(100)
            else:
                screen.blit(unchecked_img, (700, 390))
                if mx > 700 and mx < 760 and my > 390 and my < 450:
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        renderer = 'r2'
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

        pygame.draw.rect(screen, gray3, [sx/2-580-50, 600, 650, 300])
        screen.blit(big_font.render(('Region Attributes'), True, black), (sx/2-580, 600))

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
        else:
            screen.blit(menu_font.render('-Pick a region', True, red), (sx/2-580, 680))

        #cs_text = big_font.render(('COMMING SOON'), True, red)
        #screen.blit(cs_text,(sx / 2 - 580 ,350))
        pygame.draw.rect(screen, gray3, [sx / 2 + 350, 160, 250, 320])
        gm_text = menu_font.render(('gamemode:'), True, black)
        screen.blit(gm_text,(sx / 2 + 370, 160))
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

        if mx > sx / 2 + 400 and mx < sx / 2 + 550 and my > 270 and my < 320:
            pygame.draw.rect(screen, gray, [sx / 2 + 400, 270, 150, 60])
            plus_text = menu_font.render(('Sandbox'), True, black)
            screen.blit(plus_text,(sx / 2 + 400 ,270))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                rendermode = 'load sandbox'
        else:
            pygame.draw.rect(screen, gray2, [sx / 2 + 400, 270, 150, 60])
            plus_text = menu_font.render(('Sandbox'), True, black)
            screen.blit(plus_text,(sx / 2 + 400, 270))

        if mx > sx / 2 + 400 and mx < sx / 2 + 550 and my > 370 and my < 420:
            pygame.draw.rect(screen, gray, [sx / 2 + 400, 370, 150, 60])
            plus_text = menu_font.render(('Career'), True, black)
            screen.blit(plus_text,(sx / 2 + 400 ,370))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                rendermode = 'load career'
        else:
            pygame.draw.rect(screen, gray2, [sx / 2 + 400, 370, 150, 60])
            plus_text = menu_font.render(('Career'), True, black)
            screen.blit(plus_text,(sx / 2 + 400, 370))

        if OpenMessage == True:
            message('choose a region', sx / 2 - 250, sy / 2 - 100, 500, 200)

    #if rendermode == 'load':
    #    screen.blit(main_back1,(loading_back_x, 0))
    #    loading_back_x = loading_back_x - 5

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

    if rendermode == 'load' or rendermode == 'load 2' or rendermode == 'load 3':
        if devMode == True:
            screen.blit(menu_font.render('you are in DevMode', True, black),(sx / 2 - 100, sy / 2))  
        else:
            main_back1=pygame.transform.scale(main_back1, (sx, sy))
            screen.blit(main_back1,(0,0))
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
                    try:
                        if renderX + gamex > 0 - 250 and renderX + gamex < sx and renderY + gamey > 0 - 250 and renderY + gamey < sy:
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

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PLUS:   
                size = size + 10

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_MINUS:   
                size = size - 10

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL:    
                reload()

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
        f = open(time.strftime('%I-%M-%S %p %m-%d-%y')+str('.sav'), 'w')
        f.write(''+str(worldSav)+str('\n')) 
        f.write(''+str(worldSavAngle)+str('\n'))
        f.write(''+str(gamex)+str('\n'))
        f.write(''+str(gamey)+str('\n'))
        f.write(''+str(cityName)+str('\n'))
        f.write(''+str(ver)+str('\n'))
        f.write('-'+str('\n'))
        f.write('Save info: SX=' +str(sx) +str(' |SY=') +str(sy) +str(' |SR=') +str(wsx) +str('X') +str(wsy) + str(' |Mode=') +str(mode) +str(' |devMode=') +str(devMode)+str('\n'))
        f.write('was saved on: '+str(time.strftime('%I:%M %p %m/%d/%y')+str('in version: ')+str(ver)))
        f.flush()
        f.close()
        saveLoad = ''
        os.chdir('..')
        rendermode = 'game'

    if saveLoad == 'load':
        os.chdir('saves')
        f = askopenfile(mode = 'r')
        lines = f.readlines()
        worldCreate = ['']
        worldCreate = lines[0]
        worldCreate.replace("'", ' ')
        worldCreate = worldCreate.split(',')
        worldSavAngle = ['']
        worldSavAngle = lines[1]
        worldSavAngle.replace("'", ' ')
        worldSavAngle.replace("[", ' ')
        worldSavAngle = worldSavAngle.split(',')
        worldSav = worldCreate
        worldClock = 1
        world = []
        while worldClock < len(worldCreate) - 1:
            worldCreate[worldClock].replace("[", '')
            #roads
            if worldCreate[worldClock] == " 'road_img'":
                worldPlace = road_img
            if worldCreate[worldClock] == " 'roadTurn_img'":
                worldPlace = roadTurn_img
            #terraforming
            if worldCreate[worldClock] == " 'grass1_img'":
                worldPlace = grass1_img
            if worldCreate[worldClock] == " 'water_img'":
                worldPlace = water_img
            worldSavAngle[worldClock].replace("[", '')
            worldSavAngle[worldClock].replace('"', '')
            worldSavAngle[worldClock].replace("'", '')
            worldPlace = pygame.transform.rotate(worldPlace, +int(worldSavAngle[worldClock]))
            world.append(worldPlace)
            worldClock = worldClock + 1
        gamex = +int(lines[2])
        gamey = +int(lines[3])
        cityName = lines[4]
        f.flush()
        f.close()
        saveLoad = ''
        os.chdir('..')
        rendermode = 'game'

    #print clock.get_fps()
    pygame.display.update()