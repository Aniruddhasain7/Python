from pygame.locals import *
import pygame
import time
from random import randint
class Player:
    x=0
    y=0
    d=0
    positions=[]
    length=5
class Apple:
    x=0
    y=0
class Game:
    game_width=10
    game_height=10
    grid_size=44
    def iscollision(self,x1,y1,x2,y2,bsize):
        if x1>=x2 and x1<=x2+bsize:
            if y1>=y2 and y1<=y2 +bsize:
                return True
        return False
    def __init__(self):
        self._running=True
        self.player=Player()
        self.apple=Apple()
        self.apple.x=randint(0,self.game_width)*self.grid_size
        self.apple.y=randint(0,self.game_height)*self.grid_size
    def on_init(self):
        pygame.init()
        self._display_surf=pygame.display.set_mode((840,600),pygame.HWSURFACE)
        pygame.display.set_caption("SNAKE GAME")
        self._my_image=pygame.image.load("snake.png").convert()
        self._my_image2=pygame.image.load("apple.png").convert()
    def on_render(self):
        self._display_surf.fill((0,0,0))
       # self._display_surf.blit(self._my_image,(self.player.x,self.player.y))
        for pos in self.player.positions:
            self._display_surf.blit(self._my_image,(pos[0],pos[1]))
        
        self._display_surf.blit(self._my_image2,(self.apple.x,self.apple.y))
        pygame.display.flip()
        

    def on_cleanup(self):
        pygame.quit()
    def on_execute(self):
        if self.on_init()==False:
            self._running=False
        while self._running:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self._running=False
            keys=pygame.key.get_pressed()
            if(keys[K_RIGHT]):
                self.player.d=0
            if(keys[K_LEFT]):
                self.player.d=1
            if(keys[K_UP]):
                self.player.d=2
            if(keys[K_DOWN]):
                self.player.d=3
            if self.player.d==0:
                self.player.x+=44
            elif self.player.d==1:
                self.player.x-=44
            elif self.player.d==2:
                self.player.y-=44
            elif self.player.d==3:
                self.player.y+=44
            if len(self.player.positions)<(self.player.length):
                self.player.positions.append((self.player.x,self.player.y))
            else:
                self.player.positions.pop(0)
                self.player.positions.append((self.player.x,self.player.y))
            if self.iscollision(self.player.x,self.player.y,self.apple.x,self.apple.y,44):
                print("COLLIDES")
                self.apple.x=randint(0,self.game_width)*self.grid_size
                self.apple.y=randint(0,self.game_height)*self.grid_size
                self.player.length+=1
            if len(self.player.positions)>(self.player.length):
                for i in range(0,self.player.length-1):
                    #print(f"{self.player.positions[i][0]},{self.player.positions[i][1]},{self.player.x},{self.player.y}")
                    if self.iscollision(self.player.x,self.player.y,self.player.positions[i][0],self.player.positions[i][1],40):
                        print("GAME OVER")
                        exit()

            self.on_render()
            time.sleep(0.1)
        self.on_cleanup()
if __name__=="__main__":
    game=Game()
    game.on_execute()