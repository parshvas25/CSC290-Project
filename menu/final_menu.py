import pygame
from pygame.locals import *

#Initialize Game Dimensions
screen_width = 800
screen_height = 800

#Initialize PyGame
pygame.init()
screen=pygame.display.set_mode((screen_width, screen_height))

#Create a dictionary of colors to be used in the menu

color_dict = {"black": (0,0,0), "yellow": (255,255,0), "green": (0,255,0)}

background_image = pygame.image.load("background.jpg")
bg = pygame.transform.scale(background_image, (800,800))

#Import Forque Font
forque = "Forque.ttf"

#Create Function that can adjust the game font

def game_font(text:str, font:str, size:int, textColor:tuple):
	return pygame.font.Font(font, size).render(text, 0, textColor)


def main():

	running = True
	current = "Start"
	while running:
		screen.blit(bg, (0,0))
		sokoban_title = game_font("Sokoban", forque, 100, color_dict["yellow"])
		start = game_font("Start", forque, 75, color_dict["green"])
		screen.blit(sokoban_title, (screen_width/2 - 150, 100))
		screen.blit(start, (screen_width/2 - 90, 300))
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					print("1")
				
		pygame.display.update()

main()
#


