from pygame.locals import * 
import pygame
import time
from random import randint

class Player:
    x = []
    y = []
    step = 10
    direction = 0
    length = 5
    updates = 0
    max_updates = 4
    score = 0
    def __init__(self,length):
        self.length = length
        for i in range(length):
            self.x.append(500),self.y.append(500)
        for i in range(1000):
            self.x.append(-100),self.y.append(-100)
    def status(self):
        self.updates += 1
        if self.updates > self.max_updates:
            if self.x[0] < 0:
                self.x[0] = 990
            elif self.x[0] > 1000:
                self.x[0] = 0
            elif self.y[0] < 0:
                self.y[0] = 990
            elif self.y[0] > 1000:
                self.y[0] = 0
            else:
                pass
            # set previous x and y to the previous index in their respective arrays
            for i in range(self.length-1,0,-1):
                self.x[i],self.y[i] = self.x[i-1],self.y[i-1]
        if self.direction == 0:
            self.y[0] -= self.step
        if self.direction == 1:
            self.y[0] += self.step
        if self.direction == 2:
            self.x[0] -= self.step
        if self.direction == 3:
            self.x[0] += self.step

    def up(self):
        if self.direction != 1:
            self.direction=0
    def down(self):
        if self.direction != 0:
            self.direction=1
    def left(self):
        if self.direction != 3:
            self.direction=2
    def right(self):
        if self.direction != 2:    
            self.direction=3
    
    def draw(self,background,image):
        for i in range(self.length):
            background.blit(image,(self.x[i],self.y[i]))

class Apple:
    x = 100
    y = 100
    step = 5

    def __init__(self,x,y):
        self.x = x*self.step
        self.y = y*self.step

    def draw(self,background,image):
        background.blit(image,(self.x,self.y))

class Game:
    def collision(self,xA,yA,xS,yS,size):
        if xA >= xS and xA <= xS+size:
            if yA >= yS and yA <= yS+size:
                return True
        return False

class SnakeGame:
    # window size is 1000x1000
    windowHeight = 1000
    windowWidth = 1000
    flags = DOUBLEBUF
    screen = pygame.display.set_mode((windowWidth,windowHeight), flags, 16)
    player = 0
    apple = 0

    def __init__(self):
        self._running = True
        self._display_surface = None
        self._image_surface = None
        self._apple_surface = None
        self.game = Game()
        self.player = Player(5)
        self.apple = Apple(100,100)
    
    def after_init(self):
        pygame.init()
        self._running = True
        self._display_surface = self.screen
        pygame.display.set_caption("Python Snake Game")
        self._image_surface = pygame.image.load("snake.jpg").convert()
        self._apple_surface = pygame.image.load("apple.jpg").convert()
    
    def render(self):
        self._display_surface.fill((50,50,100))
        self.player.draw(self._display_surface,self._image_surface)
        self.apple.draw(self._display_surface,self._apple_surface)
        font = pygame.font.SysFont(None,24)
        GREEN = (0,255,0)
        image = font.render(f"Score: {self.player.score}",True,GREEN)
        self._display_surface.blit(image,(900,30))
        pygame.display.flip()

    def loop(self):
        self.player.status()
        # collides with apple
        for i in range(self.player.length):
            if self.game.collision(self.apple.x,self.apple.y,self.player.x[i],self.player.y[i],1):
                self.apple.x,self.apple.y = (randint(50,940)//10)*10,(randint(50,940)//10)*10
                self.player.length += 1
                self.player.score += 1
        # collides with itself
        for i in range(4,self.player.length):
            if self.game.collision(self.player.x[0],self.player.y[0],self.player.x[i],self.player.y[i],1):
                print("You lost.")
                exit(0)

    def quit_event(self, event):
        if event == QUIT:
            self._running = False

    def quit(self):
        pygame.quit()

    def on_execute(self):
        if self.after_init() == False:
            self._running = False
        while ( self._running ):
            pygame.event.pump()
            keys = pygame.key.get_pressed()
            if keys[K_UP]:
                self.player.up()
            if keys[K_DOWN]:
                self.player.down()
            if keys[K_LEFT]:
                self.player.left()
            if keys[K_RIGHT]:
                self.player.right()
            if keys[K_ESCAPE]:
                self._running = False
            self.loop()
            self.render()
            if keys[K_q]:
                time.sleep(50.0/1000.0)
            else:
                time.sleep(150.0/1000.0)
        self.quit()

if __name__ == "__main__":
    snakegame = SnakeGame()
    snakegame.on_execute()