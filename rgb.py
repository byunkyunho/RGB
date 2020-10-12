import pygame as pg

pg.init()

screen = pg.display.set_mode((1000, 500))
pg.display.set_caption("RGB")
RGB = [255,255,255]
running = True
small_font = pg.font.SysFont("arial", 30)
big_font = pg.font.SysFont("arial", 90)
font_color = (0,0,0)
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pg.mouse.get_pos()
            for a in range(3):
                if mouse_y > 330+a*50 and mouse_y < 360+a*50:
                    if mouse_x <= 50:
                        mouse_x = 50
                    if mouse_x >= 815:
                        mouse_x = 815
                    RGB[a] = (mouse_x - 50)//3
    screen.fill(RGB)
    color_change = 0
    for a in range(255):
        pg.draw.line(screen, (a, 0,0),(50+a*3, 330), (50+a*3,360), 3)
        pg.draw.line(screen, (0, a,0),(50+a*3, 380), (50+a*3,410), 3)
        pg.draw.line(screen, (0, 0,a),(50+a*3, 430), (50+a*3,460), 3)
    for a in enumerate(["R : ", "G : ", "B : "]):
        screen.blit(small_font.render("{}{}".format(a[1], RGB[a[0]]), True, font_color), (850, 330 + a[0] * 50) )
        pg.draw.polygon(screen, (127,127,127),((49+RGB[a[0]]*3, 330 + a[0] *50), (49+RGB[a[0]]*3 - 5, 320 + a[0] *50),(49+RGB[a[0]]*3 + 5, 320 + a[0] *50)))
        if RGB[a[0]] < 127:
            color_change += 1
    if color_change == 3:
        font_color = (255,255,255)
    else:
        font_color = (0,0,0)
    screen.blit(big_font.render("RGB : ({}, {} ,{})".format(RGB[0], RGB[1], RGB[2]), True, font_color), (100, 100))
    pg.display.update()