import pygame
from pygame import time
def main():

    pygame.init()

    pygame.display.set_caption("UwU game is sleep")

    DisplayRes = pygame.display.set_mode((720, 600))

    GameState = True

    image = pygame.image.load("face.jpg")

    faceX = pygame.mouse.get_pos()
    faceY = pygame.mouse.get_pos()
    framaes = pygame.time.Clock.get_ticks / 60

    while GameState:

        #DisplayRes.fill(33, 44, 55)
        while frames < 1000000:
            DisplayRes.blit(image, (faceX, faceY))
            pygame.display.flip() 

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                GameState == False

if __name__ == "__main__":
    main()