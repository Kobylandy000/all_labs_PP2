import pygame, random, time, sys

def checkCoordinate(enemy, coordinateOfCoin):
    if enemy.rect.left < coordinateOfCoin < enemy.rect.right and enemy.rect.top < coordinateOfCoin < enemy.rect.bottom:
        return False
    return True


windowWidth = 400
windowHeight = 600
size = (windowWidth, windowHeight)
enemySpeed = 3
playerSpeed = 3
enemyCounter = 0
coinCounter = 0
pygame.init()
screen = pygame.display.set_mode(size)

white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
screen.fill(white)

backgroundImage = pygame.image.load(r"C:\Users\Kobylandy\Desktop\New Folder\labs\lab8\images\street.png")

bigFont = pygame.font.SysFont("Arial", 50)
smallFont = pygame.font.SysFont("Arial", 20)
gameOverText = bigFont.render("GAME OVER!!!", True, red)
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Kobylandy\Desktop\New Folder\labs\lab8\images\enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(45, windowWidth - 45), 0)

    def move(self):
        global enemyCounter
        self.rect.move_ip(0, enemySpeed)
        if self.rect.top > windowHeight:
            enemyCounter += 1
            self.rect.bottom = 0
            self.rect.center = (random.randint(45, windowWidth - 45), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Kobylandy\Desktop\New Folder\labs\lab8\images\player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (200, 520)

    def move(self):
        isPressed = pygame.key.get_pressed()  # казир кандай клавиш басылганына тексеру
        if self.rect.top > 0:
            if isPressed[pygame.K_UP]:
                self.rect.move_ip(0, -playerSpeed)
        if self.rect.bottom < windowHeight:
            if isPressed[pygame.K_DOWN]:
                self.rect.move_ip(0, playerSpeed)
        if self.rect.left > 0:
            if isPressed[pygame.K_LEFT]:
                self.rect.move_ip(-playerSpeed, 0)
        if self.rect.right < windowWidth:
            if isPressed[pygame.K_RIGHT]:
                self.rect.move_ip(playerSpeed, 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(r"C:\Users\Kobylandy\Desktop\New Folder\labs\lab8\images\coin.jpeg"), (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(45, windowWidth - 45), 0)

    def move(self):
        global enemyCounter
        self.rect.move_ip(0, enemySpeed)
        if self.rect.top > windowHeight:
            enemyCounter += 1
            self.rect.bottom = 0
            self.rect.center = (random.randint(45, windowWidth - 45), 0)
player = Player()
enemy = Enemy()
coin = Coin()

enemies = pygame.sprite.Group()
enemies.add(enemy)

coins = pygame.sprite.Group()
coins.add(coin)

sprites = pygame.sprite.Group()
sprites.add(player)
sprites.add(enemy)
sprites.add(coin)

newSpeed = 0.2 + pygame.USEREVENT

isDone = True
while isDone:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isDone = False
            pygame.quit()
        if event.type == newSpeed:
            enemySpeed += 2
    screen.blit(backgroundImage, (0, 0))
    enemyResultText = smallFont.render(f"Cars: {enemyCounter}", True, blue)
    coinResultText = smallFont.render(f"Coins: {coinCounter}", True, blue)
    screen.blit(coinResultText, (280, 20))
    screen.blit(enemyResultText, (280, 40))

    for sp in sprites:
        screen.blit(sp.image, sp.rect)
        sp.move()

    if pygame.sprite.spritecollideany(player, coins):
        
        coinCounter += 1
        coordinateOfEnemy = enemy.rect.center
        coordinateOfCoin = random.randint(30, windowWidth - 30)
        if checkCoordinate(enemy, coordinateOfCoin):
            coin.rect.center = (coordinateOfCoin, 0)
        else:
            if coordinateOfCoin + 60 < windowWidth:
                coin.rect.center = (coordinateOfCoin + 60, 0)
            else:
                coin.rect.center = (coordinateOfCoin - 60, 0)

    if pygame.sprite.spritecollideany(player, enemies):
        
        time.sleep(1)
        screen.fill(white)
        screen.blit(gameOverText, (windowWidth // 4, windowHeight // 2))
        for sp in sprites:
            sp.kill()
        
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    pygame.display.update()