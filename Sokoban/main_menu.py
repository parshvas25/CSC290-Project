
import pygame
from pygame import*
import os


#
BLACK = (0,0,0) 
YELLOW = (255,255,0)
GREEN = (0,255,0)


cur_path = os.path.dirname(__file__)
new_path = os.path.relpath('..\\Resources', cur_path)
#Import Forque Font

def game_font(text:str, font:str, size:int, textColor:tuple):
    return pygame.font.Font(font, size).render(text, 0, textColor)

class Button:
    def __init__(self, rect, level):
        self.rect = pygame.Rect(rect)
        self.image = pygame.Surface(self.rect.size).convert()
        self.level = level
        self.text = str(level)

    def on_click(self, event):
        return self.rect.collidepoint(event.pos)

    def get_level(self):
        return self.level

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        font = pygame.font.SysFont('Comic Sans MS', 20)
        leveltext = font.render(self.text, False, YELLOW)
        screen.blit(leveltext, self.rect.move(20,10))

def main():
    
    forque = new_path + "\Fonts\Forque.ttf"
    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 500
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Sokoban")

    background_image = pygame.image.load(new_path + "\Images\\background.jpg") 
    bg = pygame.transform.scale(background_image, (SCREEN_WIDTH,SCREEN_HEIGHT))

    screen.blit(bg, (0,0))
    
    button_group = []
    for i in range(50,450, 80):
        temp_button = Button((i,350, 50, 50), (i-50)//80 + 1)
        button_group.append(temp_button)
    
    for x in button_group:
        x.draw(screen)

    sokoban_title = game_font("Sokoban", forque, 100, YELLOW)
    start = game_font("Start", forque, 75, GREEN)
    levels_label = game_font("Levels", forque, 50, YELLOW)

    screen.blit(sokoban_title, (SCREEN_WIDTH/2 - 150, 25))
    screen.blit(start, (SCREEN_WIDTH/2 - 80, 150))
    screen.blit(levels_label, (SCREEN_WIDTH/2 - 70, 275))

    level_choice = pygame.sprite.Group()

    running = True
    while running:
        
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for x in button_group:
                    if x.on_click(event):
                        return x.get_level()

            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return 1

        pygame.display.update()
