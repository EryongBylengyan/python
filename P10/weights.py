# encoding:utf-8
__author__ = 'admin'
import pygame
import sys
import time
from pygame.locals import *
from random import randrange

class Weight(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = weight_image
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect.top = -self.rect.height
        self.rect.centerx = randrange(screen_size[0])

    def update(self):
        self.rect.top = self.rect.top + 1
        if self.rect.top>screen_size[1]:
            self.reset()

#初始化数据
pygame.init()
screen_size = 800,600
pygame.display.set_mode(screen_size,FULLSCREEN)
pygame.mouse.set_visible(0)

#载入图片
weight_image = pygame.image.load("weight.jpg")
weight_image = weight_image.convert()


#创建一个子图形组（sprite group），增加weight。
sprites =pygame.sprite.RenderUpdates()
sprites.add(Weight())


#获取屏幕表面，并且填充
screen = pygame.display.get_surface()
bg = (255,255,255)
screen.fill(bg)
pygame.display.flip()


#用于清楚子图形
def clear_callback(surf,rect):
    surf.fill(bg,rect)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN and event.key ==K_ESCAPE:
            sys.exit()
    time.sleep(0.001)
    sprites.clear(screen,clear_callback)
    sprites.update()
    updates = sprites.draw(screen)
    pygame.display.update(updates)


