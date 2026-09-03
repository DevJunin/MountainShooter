import pygame

print("Setup start")
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print("Setup enter")

print("Setup Start")
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Quitiing')
            pygame.quit()  # close window
            quit()  # end pygame
