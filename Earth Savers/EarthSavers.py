import pygame
import time
import random

pygame.init()

CAPTION = "Earth Savers"
ICON = pygame.transform.scale(pygame.image.load('./Assets/icons/GREAT.png'), (50, 50))
width = 1200
height = 900

screen = pygame.display.set_mode((width, height))
pygame.display.set_icon(ICON)
pygame.display.set_caption(CAPTION)

clock = pygame.time.Clock()


class thing:
    def __init__(self, x, y, Bin):
        self.x = x
        self.y = y
        self.Bin = Bin


def main_menu():
    music = pygame.mixer.music.load('./music/Chill.mp3')
    pygame.mixer.music.play(-1)

    main_menuIMG = pygame.image.load("./Assets/main_menu.png")

    run = True
    while run:
        screen.blit(main_menuIMG, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()


def main():
    TrashSpeed = 5
    ProgressSpeed = 0.1
    lastX = 0

    music = pygame.mixer.music.load('./music/ingame_music.mp3')
    pygame.mixer.music.play(-1)

    BG = pygame.image.load("./Assets/backgrounds/background100%.png")

    trash = [0] * 10
    for i in range(0, 10):
        trash[i] = thing((1200 + (i * 250)), 780, random.randint(1, 3))
    main_font = pygame.font.SysFont("MV Boli", 45)

    GlassBinIMG = pygame.image.load("./Assets/bins/GlassBin.png")
    PaperBinIMG = pygame.image.load("./Assets/bins/PaperBin.png")
    PlasticMetalBinIMG = pygame.image.load("./Assets/bins/PlasticMetalBin.png")
    GreatIMG = pygame.image.load("./Assets/icons/GREAT.png")
    TerribleIMG = pygame.image.load("./Assets/icons/TERRIBLE.png")

    GlassBottleIMG = pygame.image.load("./Assets/trash/glass_bottle.png")
    BoxIMG = pygame.image.load("./Assets/trash/box.png")
    BagIMG = pygame.transform.scale(pygame.image.load("./Assets/trash/plastic_bag.png"), (90, 90))

    points = 0
    progress = 100
    BarColor = (33, 194, 27)

    def drawing():

        screen.blit(BG, (0, 0))
        screen.blit(GlassBinIMG, (220, 470))
        screen.blit(PaperBinIMG, (480, 470))
        screen.blit(PlasticMetalBinIMG, (740, 470))
        pygame.draw.rect(screen, BarColor, [80, 30, progress * 3, 30])
        pygame.draw.rect(screen, (0, 0, 0), [80, 30, 300, 30], 3)
        Score_display = main_font.render(f"Player score : {points}", 1, (0, 0, 0))
        screen.blit(Score_display, (700, 20))

        for i in range(0, 10):
            if (trash[i].Bin == 1):
                screen.blit(GlassBottleIMG, (trash[i].x, trash[i].y))
            if (trash[i].Bin == 2):
                screen.blit(BoxIMG, (trash[i].x, trash[i].y))
            if (trash[i].Bin == 3):
                screen.blit(BagIMG, (trash[i].x, trash[i].y))

        pygame.draw.rect(screen, (0, 0, 0), [180, 770, 200, 100], 5)
        pygame.draw.rect(screen, (0, 0, 0), [0, 770, 1200, 100], 2)
        screen.blit(GreatIMG, (380, 15))
        screen.blit(TerribleIMG, (30, 15))
        pygame.display.update()

    running = 1
    while (running == 1):

        progress -= ProgressSpeed
        drawing()

        lastX = max(trash[0].x, trash[1].x, trash[2].x, trash[3].x, trash[4].x, trash[5].x, trash[6].x, trash[7].x,
                    trash[8].x)

        for i in range(0, 10):
            trash[i].x = trash[i].x - TrashSpeed
            if trash[i].x <= -80:
                trash[i].x = 2500
                trash[i].Bin = random.randint(1, 3)

        if progress < 10:
            BG = pygame.image.load("./Assets/backgrounds/background10%.png")

        if progress < 20 and progress > 10:
            BG = pygame.image.load("./Assets/backgrounds/background20%.png")

        if progress < 30 and progress > 20:
            BG = pygame.image.load("./Assets/backgrounds/background30%.png")

        if progress < 40 and progress > 30:
            BG = pygame.image.load("./Assets/backgrounds/background40%.png")

        if progress < 50 and progress > 40:
            BG = pygame.image.load("./Assets/backgrounds/background50%.png")

        if progress < 60 and progress > 50:
            BG = pygame.image.load("./Assets/backgrounds/background60%.png")

        if progress < 70 and progress > 60:
            BG = pygame.image.load("./Assets/backgrounds/background70%.png")

        if progress < 80 and progress > 70:
            BG = pygame.image.load("./Assets/backgrounds/background80%.png")

        if progress < 90 and progress > 80:
            BG = pygame.image.load("./Assets/backgrounds/background90%.png")

        if progress > 90:
            BG = pygame.image.load("./Assets/backgrounds/background100%.png")

        if progress == 0:
            break

        if progress > 100:
            progress = 100

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = 0

        keys = pygame.key.get_pressed()

        for i in range(0, 10):
            if (trash[i].x > 180 and trash[i].x < 380):
                if keys[pygame.K_1]:
                    if (trash[i].Bin == 1):
                        trash[i].x = lastX + 480
                        progress += 6
                        points += 10
                if keys[pygame.K_2]:
                    if (trash[i].Bin == 2):
                        trash[i].x = lastX + 480
                        progress += 6
                        points += 10
                if keys[pygame.K_3]:
                    if (trash[i].Bin == 3):
                        trash[i].x = lastX + 480
                        progress += 6
                        points += 10
            if keys[pygame.K_ESCAPE]:
                ProgressSpeed = 0
                TrashSpeed = 0

            else:
                ProgressSpeed = 0.1
                TrashSpeed = 5
        clock.tick(60)


main_menu()
