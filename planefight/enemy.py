#coding=utf8
'''
Created on 2017年11月2日
@author: 李超
'''
import random
import pygame

#敌机类
class Enemy(object):
    def __init__(self):
        self.image = pygame.image.load('images/enemy.png').convert_alpha()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.init()
    
    def init(self):
        self.x = random.randint(0,400-self.width) 
        self.y = -self.height
        self.speed = random.randint(0,5)+2
        
    def move(self,time_passed_second):
        self.y += self.speed * time_passed_second
        if self.y > 650 :
            self.init() 
    
    def draw(self,screen):
        screen.blit(self.image,(self.x,self.y))        
        
    def shootBy(self,bullet):
        bx = bullet.x
        by = bullet.y
        
        return (self.x <bx< (self.x+self.width)) and (self.y <by< (self.y+self.height))
        
        
            