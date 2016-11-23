#def
def settingsUpdate():
    print 'New Settings info: SX=' +str(sx) +str(' |SY=') +str(sy) +str(' |SR=') +str(wsx) +str('X') +str(wsy) + str(' |Mode=') +str(mode) +str(' |devMode=') +str(devMode) +str(' |renderer=') +str(renderer)

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
    grass_img = pygame.image.load("grass.png")
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
ver = 'alpha 1.0.3'
renderer = 'r1'

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
        except:
            print 'Error updating settings: SX=' +str(sx) +str(' |SY=') +str(sy) +str(' |SR=') +str(wsx) +str('X') +str(wsy) + str(' |Mode=') +str(mode) +str(' |devMode=') +str(devMode)


    if rendermode == 'new':
        main_back1=pygame.transform.scale(main_back1, (sx * 2, sy))
        screen.blit(main_back1,((mx-2655)/10,0))
        title_text = title_font.render(('Poly City'), True, black)
        screen.blit(title_text,(sx/2 - 250,10))
        screen.blit(menu1_img, (sx/2 - 250, 150))
        if mx > sx/2 - 200 and mx < sx/2 - 200 + 400 and my > 280 and my < 380:
            pygame.draw.rect(screen, gray, [sx/2 - 200, 280, 400, 100])
            play_text = menu_font.render(('Sandbox Mode'), True, black)
            screen.blit(play_text,(sx/2 - 200 ,280))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                rendermode = 'load sandbox'
        else:
            pygame.draw.rect(screen, gray2, [sx/2 - 200, 280, 400, 100])
            play_text = menu_font.render(('Sandbox Mode'), True, black)
            screen.blit(play_text,(sx/2 - 200 ,280))

        if mx > sx/2 - 200 and mx < sx/2 - 200 + 400 and my > 400 and my < 500:
            pygame.draw.rect(screen, gray, [sx/2 - 200, 400, 400, 100])
            play_text = menu_font.render(('Career Mode'), True, black)
            screen.blit(play_text,(sx/2 - 200 ,400))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                rendermode = 'load career'
        else:
            pygame.draw.rect(screen, gray2, [sx/2 - 200, 400, 400, 100])
            play_text = menu_font.render(('Career Mode'), True, black)
            screen.blit(play_text,(sx/2 - 200 ,400))

#    if rendermode == 'load':
#        screen.blit(main_back1,(loading_back_x, 0))
#        loading_back_x = loading_back_x - 5

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

    if rendermode == 'load':
            plus_text = menu_font.render((''+str(renderClock)+str('/')+str(size)), True, black)
            screen.blit(plus_text,(sx / 2 , sy - 100))        

    #load
    if rendermode == 'load':
        if renderClock < size:
            world.append(grass_img)
            worldSav.append('grass_img')
            worldSavAngle.append(0)
            renderClock = renderClock + 1
        else:
            rendermode = 'game'

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
                        if renderX + gamex > 0 and renderX + gamex < sx - 250 and renderY + gamey > 0 and renderY + gamey < sy - 250:
                            screen.blit(world[renderClock], (renderX + gamex, renderY + gamey))
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
                    place = grass_img
                    placeSav = grass_img

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
            play_text = menu_font.render(('Quit'), True, black)
            screen.blit(play_text,(sx/2 - 200 ,400))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                rendermode = 0
                pygame.time.delay(100)
        else:
            pygame.draw.rect(screen, gray2, [sx/2 - 200, 400, 400, 100])
            play_text = menu_font.render(('Quit'), True, black)
            screen.blit(play_text,(sx/2 - 200 ,400))

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
            if worldCreate[worldClock] == " 'grass_img'":
                worldPlace = grass_img
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