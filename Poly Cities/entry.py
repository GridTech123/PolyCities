def reset():
    clicked = False
    global text
    text = ''

def new(screen, defText, color1, color2, font, x, y, xl, yl):
    pygame.draw.rect(screen, color1, [xl, yl, x, y])
    if mx > 100 and mx < 160 and my > 2 and my < 260:
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            clicked = True
    if clicked == False:
        screen.blit(font.render(defText, True, color2), (xl, yl))  
    else:
        screen.blit(font.render(text, True, color2), (xl, yl))  