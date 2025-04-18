import pygame
import datetime


pygame.init()


CLOCK_PATH = r"C:\Users\Kobylandy\Desktop\New Folder\labs\lab7\images\mickeyclock.jpeg"
LEFT_ARM_PATH = r"C:\Users\Kobylandy\Desktop\New Folder\labs\lab7\images\leftarm.png"
RIGHT_ARM_PATH = r"C:\Users\Kobylandy\Desktop\New Folder\labs\lab7\images\rightarm.png"


WIDTH, HEIGHT = 450, 400
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")


clock_img = pygame.image.load(CLOCK_PATH)
left_arm_img = pygame.image.load(LEFT_ARM_PATH)
right_arm_img = pygame.image.load(RIGHT_ARM_PATH)


clock_img = pygame.transform.scale(clock_img, (clock_img.get_width() // 3, clock_img.get_height() // 3))
left_arm_img = pygame.transform.scale(left_arm_img, (20, left_arm_img.get_height() // 3 - 20))
right_arm_img = pygame.transform.scale(right_arm_img, (right_arm_img.get_width() // 3, right_arm_img.get_height() // 3))

last_minute = -1

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  

    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    second = datetime.datetime.now().second
    
    if minute != last_minute:
        pygame.mixer.Sound(r"C:\Users\Kobylandy\Desktop\New Folder\labs\lab8\sounds\coinsound.mp3").play()
        last_minute = minute

    
    screen.fill(WHITE)
    screen.blit(clock_img, (0, 0))

    
    left_arm_angle = second * (-6)    
    right_arm_angle = minute * (-6)
    hour_arm_angle = hour * (-6)  

    

    left_rotated = pygame.transform.rotate(left_arm_img, left_arm_angle)
    left_rect = left_rotated.get_rect(center=(230, 175))

    right_rotated = pygame.transform.rotate(right_arm_img, right_arm_angle)
    right_rect = right_rotated.get_rect(center=(230, 175))

    hour_rotated = pygame.transform.rotate(left_arm_img, hour_arm_angle)
    hour_rect = hour_rotated.get_rect(center=(230,175))

    screen.blit(hour_rotated, hour_rect.topleft)
    screen.blit(left_rotated, left_rect.topleft)
    screen.blit(right_rotated, right_rect.topleft)

    
    pygame.display.update()
    
    
    pygame.time.delay(1000 // 60)  


pygame.quit()
