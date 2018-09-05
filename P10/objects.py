# encoding:utf-8
__author__ = 'admin'

import pygame,config,os
from random import randrange

"这个模块包括Squish的游戏对象"

class SquishSprite(pygame.sprite.Sprite):
    """
    Squish中所有的子图形的范型超类。构造函数负责载入图像，设置子图形的rect和area的属性。
    并且允许它在制定与去内进行移动，area由屏幕的大小和留白决定.
    """
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert()
        self.rect = self.image.get_rect()
        screen = pygame.display.get_surface()
        shrink = -config.margin * 2
        self.eara = screen.get_rect().inflate(shrink,shrink)

class Weight(SquishSprite):
    """
    落下的物体。它使用了SquishPrite构造函数设置她的图像，并且会以给定的速度左委构造函数的参数来设置下落的速度。
    """

    def __init__(self,speed):
        SquishSprite.__init__(self,config.Weight_image)
        self.speed = speed
        self.reset()

    def reset(self):
        x = randrange(self.eara.left,self.eara.right)
        self.rect.midbottom = x,0

    def update(self):
        self.rect.top += self.speed
        self.landed = self.rect.top >= self.eara.bottom

class Banana(SquishSprite):
    """
    绝望的香蕉。它使用了SquishPrite构造函数设置她的图像，并且会停留在屏幕底端。她的水平位置由当前的书表位置决定。
    """
    def __init__(self):
        SquishSprite.__init__(self,config.Banana_image)
        self.rect.bottom = self.eara.bottom
        self.pad_top = config.Banana_pad_top
        self.pad_side = config.Banana_pad_side

    def update(self):
        self.rect.centerx = pygame.mouse.get_pos()[0]
        self.rect = self.rect.clamp(self.eara)

    def touch(self,other):
        bounds = self.rect.inflate(-self.pad_side,-self.pad_top)
        bounds.bottom = self.rect.bottom
        return bounds.colliderect(other.rect)
