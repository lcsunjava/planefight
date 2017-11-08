#coding=utf8
'''
Created on 2017年11月2日
@author: 李超
'''
import pygame
from planepanel import PlanePanel 

#主启动类
if __name__=='__main__':
    pygame.init()
    pygame.mixer.init()
    
    screen = pygame.display.set_mode((400,650),0,32)
    pygame.display.set_caption("飞机大战")
    pygame.mouse.set_visible(False)
    panel = PlanePanel()
    panel.run(screen)
    
    pygame.quit()
    
    



