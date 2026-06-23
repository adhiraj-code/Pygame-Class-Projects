import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))

# fill the screen with white color

screen.fill((255,255,255))

# Define colors

GREEN = (0, 255, 0)

# Draw solid circle

pygame.draw.circle(screen, GREEN, (300, 300), 50)

# Draw outlined circle

pygame.draw.circle(screen, GREEN, (100, 100), 50, 3)

# Draw the surface object to the screen

pygame.display.update()

done = False

while not done:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            done = True


    pygame.display.flip()

pygame.quit()