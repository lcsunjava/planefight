#coding=utf8
'''
Created on 2017年11月2日
@author: 李超
'''
from sys import exit
import pygame
from enemy import Enemy 
from hero import Hero

WHITE = (255, 255, 255)

#界面类
class PlanePanel(object):
    def __init__(self):
        self.background = pygame.image.load('images/background.png').convert_alpha()
        self.gameover = pygame.image.load('images/gameover.png').convert_alpha()
        self.hero = Hero()
        self.enemies = []
        self.initEnemy()
        self.bullets = []
        self.bullet_index = 0
        self.over = False
        self.running = True
        self.score = 0
        self.f = pygame.font.Font("font/verdana.ttf", 18)
        self.initMusic()
        self.bullet_sound = pygame.mixer.Sound("sound/bullet.wav")
        self.bullet_sound.set_volume(0.2)
        
    def initMusic(self):
        pygame.mixer.music.load("sound/game_music.ogg")
        pygame.mixer.music.set_volume(0.2)    
        
    def initEnemy(self):
        cnt = 0
        while True:
            self.enemies.append(Enemy())
            cnt += 1
            if cnt == 5:
                break    
        
    def draw(self,screen):
        screen.blit(self.background,(0,0)) 
          
        if not self.hero.life:
            screen.blit(self.gameover,(0,0))  
            
        score_text = self.f.render('Score : %s' % str(self.score), True, WHITE)
        life_text = self.f.render("Life : %s" % str(self.hero.life), True, WHITE)
        screen.blit(score_text,(10,5)) 
        screen.blit(life_text,(10,25))
        self.hero.draw(screen)
        
        for enemy in self.enemies:
            enemy.draw(screen)
            
        for bullet in self.bullets:
            bullet.draw(screen)  
        
        pygame.display.update()                
    
    def explode(self,bullet):
        j = -1
        for i in range(0,len(self.enemies)):
            enemy = self.enemies[i]
            if enemy.shootBy(bullet):
                self.score += 1
                j = i
                break
        
        if j > -1:
            e = self.enemies[j]
            e.init()
            bullet.init(self.hero)
    
    def isOver(self):
        for i in range(0,len(self.enemies)):
            enemy = self.enemies[i]
            j = -1
            if self.hero.crash(enemy):
                self.hero.life -= 1
                j = i
            
            if j > -1:
                en = self.enemies[j]
                en.init()    
        
        return self.hero.life < 0    
            
    def run(self,screen):
        pygame.mixer.music.play(-1)
        clock = pygame.time.Clock()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    exit()
                elif event.type == pygame.MOUSEMOTION:
                    if (self.bullet_index%20)==0:
                        self.bullet_sound.play()
                        self.bullets = self.hero.shoot()   
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.running = True  
                                   
            if not self.over:
                self.move(screen, clock)
    
    def move(self,screen,clock):
        mx,my = pygame.mouse.get_pos()
        self.hero.move(mx, my)
        self.hero.anim()
        self.draw(screen)
        self.bullet_index += 1
        
        time_passed = clock.tick(100)
        time_passed_second = time_passed/20.0        
        for enemy in self.enemies:
            enemy.move(time_passed_second)
            
        for bullet in self.bullets:
            bullet.move()
            self.explode(bullet)
        
        if self.isOver():
            pygame.mixer.music.stop()
            pygame.mixer.stop()
            self.over = True  
            self.running = False
                