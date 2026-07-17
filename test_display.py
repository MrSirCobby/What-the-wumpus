import pygame
import settings
import rooms
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption(settings.TITLE)

running = True

test_room = rooms.Room()
test_room.change_active()
test_room.update_walls()
#print(test_room.walls_list)
while running:
    settings.event_get = pygame.event.get()
    for event in settings.event_get:
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255,255,255))

    test_room.display_room(screen)


pygame.quit()