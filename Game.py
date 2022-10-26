from Sky import Sky
from Ship import Ship
from bullet import bullet
import pygame
import random

class Game:
    
    def __init__(self):
        
        self.width= 400
        self.height= 400
        
        self.mySky= Sky(self.width, self.height, 50)
        
        self.screen= pygame.display.set_mode((self.width, self.height))
        self.clock= pygame.time.Clock()
        self.fps= 60
        #Cargar la hoja de imágenes
        self.sprites= pygame.image.load("sprites.png")
        self.shipsprite= pygame.Surface((64,64)).convert()
        self.shipsprite.blit(self.sprites,(0,0),(250,436,64,64))
        self.myShip=Ship()
        #Cargar la imagen de las balas
        self.bulletsprite= pygame.image.load("balas.png").convert()
        self.bulletsprite.set_colorkey(0,0)
        
       

    def run(self):
        
        pygame.init()
        
        control=True
        while control:
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
            
            self.screen.fill((0,0,0))
            
            #Show the Sky
            
            for star in self.mySky.stars:
                r= random.randint(0, 255)
                g= random.randint(0, 255)
                b= random.randint(0, 255)
                pygame.draw.circle(self.screen,(r,g,b), star, 1)
                
            if self.myShip.x > self.width-64: self. myShip.x = self.width-64
            if self.myShip.x < 8: self.myShip.x= 8 
            if self.bullet.ybullet > self.height:
                self.bullet.ybullet =self.myShip.y
            

            
                
            self.mySky.move()            
            self.bullet.shoot()
            x=self.myShip.move(self.checkkeys())
            y=self.height/2
            self.screen.blit(self.shipsprite, (x,y))
            self.screen.blit(self.bulletsprite,(x,self. bullet. ybullet))
                
            pygame.display.flip()
            
            self.clock.tick(self.fps)
    
    def checkkeys(self):
        keys=pygame.key.get_pressed()

        if  keys[pygame.K_LEFT]:
            return "LEFT"

        if  keys[pygame.K_RIGHT]:
            return "RIGHT"
        if keys[pygame.K_w]: self.bullet.condition="Dispara"
        else: self.ship.direction="Stop"
            
            
myGame=Game()
myGame.run()
            