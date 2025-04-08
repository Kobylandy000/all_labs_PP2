import pygame, time 

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()
screen = pygame.display.set_mode((500, 500))
fon = (255, 255 ,255)
screen.fill(fon)
isDone = True
mainCoordX = 250
mainCoordY = 250
speed=0

while isDone:
    screen.fill(fon)
    pygame.draw.circle(screen, 'Red', (mainCoordX, mainCoordY), 25)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isDone = False
            pygame.quit()
       # elif event.type == pygame.KEYDOWN:
          #  if event.key == pygame.K_UP:
              #  if mainCoordY - 20 - 25 >= 0:
               #     mainCoordY -= 20
            #if event.key == pygame.K_DOWN:
             #   if mainCoordY + 20 + 25 <= 500:
              #      mainCoordY += 20
           # if event.key == pygame.K_RIGHT:
              #  if mainCoordX + 20 + 25 <= 500:
               #     mainCoordX += 20
            #   if mainCoordX - 20 - 25 >= 0:
             #       mainCoordX -= 20
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if mainCoordY - 20 - 25 >= 0:
            mainCoordY -= 20
    if keys[pygame.K_DOWN]:
        if mainCoordY + 20 + 25 <= 500:
            mainCoordY += 20
    if keys[pygame.K_RIGHT]:
        if mainCoordX + 20 + 25 <= 500:
            mainCoordX += 20
    if keys[pygame.K_LEFT]:
        if mainCoordX - 20 - 25 >= 0:
            mainCoordX -= 20
    FramePerSec.tick(FPS)
    