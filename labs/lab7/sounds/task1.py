import pygame
import math
import time

pygame.init()
screen = pygame.display.set_mode((1400, 1050))
fon = (255, 255, 255)
screen.fill(fon)
img = pygame.image.load("images/mickeyclock.jpeg")
leftHand = pygame.image.load("images/left.jpg")
rightHand = pygame.image.load("images/right.jpg")
# img = pygame.transform.scale(img, (300, 300))
isDone = True

def rotateHand(image, angle, rad, additional):
    rotatedImage = pygame.transform.rotate(image, -angle) # rotate image
    angleInRadian = math.radians(angle - 90)
    newXCoordinate = rad * math.cos(angleInRadian) + additional[0]
    newYCoordinate = rad * math.sin(angleInRadian) + additional[1]
    rotateRect = rotatedImage.get_rect(center=(newXCoordinate, newYCoordinate))
    screen.blit(rotatedImage, rotateRect)

while isDone:
    screen.fill(fon)
    screen.blit(img, (0, 0))
    screen.blit(leftHand, (500, 320))
    screen.blit(rightHand, (850, 350))
    pygame.display.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isDone = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                rotateHand(leftHand, 20, 150, (700, 525))
                pygame.display.update()
                time.sleep(5)