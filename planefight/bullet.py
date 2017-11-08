#coding=utf8
'''
Created on 2017年11月2日
@author: 李超
'''
import pygame

#子弹类
class Bullet(object):
    def __init__(self,x,y):
        self.image = pygame.image.load('images/bullet.png').convert_alpha()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = x
        self.y = y
        self.speed = 10
    
    def move(self):
        self.y -= self.speed
    
    def init(self,hero):
        self.x = hero.x
        self.y = hero.y-hero.height/2
        self.speed = 10    
    
    def draw(self,screen):
        screen.blit(self.image,(self.x,self.y))
    
    
    
    
    
    
    
    
    
    
    
    
        