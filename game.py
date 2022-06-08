from pygame.locals import * 
import pygame

class Player:
    x = 500
    y = 500
    def up(self):
        self.y -= 1
    def down(self):
        self.y += 1
    def left(self):
        self.x -= 1
    def right(self):
        self.x += 1

class SnakeGame:
    # window size is 1000x1000
    windowHeight = 1000
    windowWidth = 1000
    player = Player()

    def __init__(self):
        self._running = True
        self._display_surface = None
        self._image_surface = None
    
    def after_init(self):
        pygame.init()
        self._running = True
        self._display_surface = pygame.display.set_mode((self.windowWidth,self.windowHeight),pygame.HWSURFACE)
        pygame.display.set_caption("Python Snake Game")
        self._image_surface = pygame.image.load("snake.jpg").convert()
    
    def render(self):
        self._display_surface.fill((50,50,100))
        self._display_surface.blit(self._image_surface,(self.player.x,self.player.y))
        pygame.display.flip()

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
            self.render()
        self.quit()

if __name__ == "__main__":
    snakegame = SnakeGame()
    snakegame.on_execute()