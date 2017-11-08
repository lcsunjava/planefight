#coding=utf8
'''
Created on 2017年11月2日
@author: 李超
'''
import pygame
from bullet import Bullet 

#英雄机类
class Hero(object):
    def __init__(self):
        self.images = []
        for i in range(0,2):
            self.images.append(pygame.image.load(('images/hero%d.png')%(i)).convert_alpha())
        self.image = self.images[0]
        self.x = 200
        self.y = 500
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.index = 0
        self.bullets = []
        self.life = 3
        
    def anim(self):
        self.image = self.images[(self.index)/20%len(self.images)]
        self.index += 1
            
    def move(self,mx,my):
        self.x = mx
        self.y = my
        
    def draw(self,screen):
        screen.blit(self.image,(self.x-self.width/2,self.y-self.height/2))    
        
    def shoot(self):
        bullet = Bullet(self.x,self.y)  
        self.bullets.append(bullet)
        
        return self.bullets
    
    def crash(self,enemy):
        x1 = enemy.x - self.width/2;
        x2 = enemy.x + enemy.width + self.width/2;
        y1 = enemy.y - self.height/2;
        y2 = enemy.y + enemy.height + self.height/2;  
      
        return (x1<self.x<x2)  and  (y1<self.y<y2)
      
      
      
      
      
      
      
      
      
      
        
        
        
        