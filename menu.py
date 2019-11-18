
import pygame
from pygame import*
from play import Sokoban

#Import Forque Font

def game_font(text:str, font:str, size:int, textColor:tuple):
    return pygame.font.Font(font, size).render(text, 0, textColor)



def main():
    forque = "menu/Forque.ttf"
    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 500
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Sokoban")


#Create a dictionary of colors to be used in the menu

    color_dict = {"black": (0,0,0), "yellow": (255,255,0), "green": (0,255,0)}

    background_image = pygame.image.load("menu/background.jpg") 
    bg = pygame.transform.scale(background_image, (SCREEN_WIDTH,SCREEN_HEIGHT))


    running = True
    current = "Start"
    while running:
        screen.blit(bg, (0,0))
        sokoban_title = game_font("Sokoban", forque, 100, color_dict["yellow"])
        start = game_font("Start", forque, 75, color_dict["green"])
        screen.blit(sokoban_title, (SCREEN_WIDTH/2 - 150, 100))
        screen.blit(start, (SCREEN_WIDTH/2 - 90, 300))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    sokoban = Sokoban()
                    sokoban.play()

        pygame.display.update()

main()
