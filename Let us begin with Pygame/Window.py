import pygame

pygame.init()

screen_width = 500
screen_height = 500
screen = pygame.diplay.set_mode((screen_width, screen_height))

def main_loop():
    running = True

    while running:
        for event in event.get():
            if event.type == pygame.QUIT:
                running = False

main_loop()