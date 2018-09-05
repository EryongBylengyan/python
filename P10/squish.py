# encoding:utf-8
__author__ = 'admin'
import os,sys,pygame
from pygame.locals import *
from random import randrange
import objects,config

"这个莫夸包括Squish游戏的主要游戏逻辑"

class State:
    """
    泛型游戏状态类，可以处理时间并在给定的表面上显示自身。
    """
    def handle(self,event):
        if event.type == QUIT or event.type =="ESC":
            sys.exit()
        if event.type ==KEYDOWN and event.type == K_ESCAPE:
            sys.exit()

    def firstDisplay(self,screen):
        """
        用户第一行显示状态。使用背景色填充屏幕
        """
        screen.fill(config.Background_color)
        pygame.display.flip()

    def display(self,screen):
        """
        用于在已经显示过一次状态后再次显示，默认的行为是什么都不做。
        """
        pass

class Level(State):
    """
    游戏等级，用户计算已经落下了多少物体，移动子图形以及其他和游戏逻辑相关的任务。
    """
    def __init__(self,number=1):
        self.number = number
        self.remaining = config.Weight_per_level

        speed = config.Drop_speed

        speed+=(self.number-1)*config.Speed_increase
        self.weight = objects.Weight(speed)
        self.banana = objects.Banana()

        both = self.weight,self.banana
        self.sprites = pygame.sprite.RenderUpdates(both)


    def update(self,game):
        "从前一帧更新游戏状态"
        #更新所有子图形
        self.sprites.update()
        #如果相机碰到了秤砣，那么告诉游戏切换到GameOver状态
        if self.banana.touch(self.weight):
            game.nextState = GameOver()
        #否则在秤砣落地式将其复位
        #如果本官内的所有秤砣都落下了，则让游戏切换到LevelClear状态；
        elif self.weight.landed:
            self.weight.reset()
            self.remaining-=1
            if self.remaining==0:
                game.nextState = LevelCleared(self.number)

    def display(self,screen):
        """
        在第一次显示后显示状态，与FirstDisplay不同，这个方法使用pygame.display.update对self.sprites.draw提供的、
        需要更新的矩形列表进行更新。
        """
        screen.fill(config.Background_color)
        updates = self.sprites.draw(screen)
        pygame.display.update(updates)


class Paused(State):
    """
    简单的暂停游戏状态，按下键盘上任意键活点击鼠标都会结束这个状态。
    """
    """
    """
    finished = 0
    image = None
    text = ""

    def handle(self,event):
        State.handle(self,event)
        if event.type in [MOUSEBUTTONDOWN,KEYDOWN]:
            self.finished = 1

    def update(self,game):
        if self.finished:
            game.nextState = self.nextState()

    def firstDisplay(self,screen):
        screen.fill(config.Background_color)
        font = pygame.font.Font(None,config.font_size)
        lines = self.text.strip().splitlines()

        height = len(lines)*font.get_linesize()

        center,top = screen.get_rect().center
        top -= height//2

        if self.image:
            image = pygame.image.load(self.image).convert()
            r = image.get_rect()
            top += r.height//2
            r.midbottom = center,top - 20

        antialias = 1
        black = 0,0,0


        for line in lines:
            text = font.render(line.strip(),antialias,black)
            r=text.get_rect()
            r.midtop = center,top
            screen.blit(text,r)
            top += font.get_linesize()

        pygame.display.flip()

class Info(Paused):
    nextState = Level
    text = """
    In this game you are a banana,
    trying to survive a course in
    self-defense against fruit,where the
    participants will "defend" themselves
    against you with a 16 tou weight."""


class StartUp(Paused):
    nextState = Info
    image = config.Splash_image
    text="""
        Welcome to Squish.
        the game of Fruit Self-Defence."""

class LevelCleared(Paused):

    def __init__(self,number):
        self.number= number
        self.text = """Level %i cleared
                Click to start next level"""%self.number


    def nextState(self):
        return Level(self.number+1)

class GameOver(Paused):

    nextState = Level
    text = """
        Game OVER
        Click to ReStart,Esc to quir."""


class Game:

    def __init__(self,*args):
        path = os.path.abspath(args[0])
        dir = os.path.split(path)[0]

        os.chdir(dir)
        self.state = None
        self.nextState = StartUp()

    def run(self):

        pygame.init()
        flag = 0

        if config.full_screen:
            flag = FULLSCREEN
        screen_size = config.Screen_size
        screen = pygame.display.set_mode(screen_size,flag)

        pygame.display.set_caption("Fruit Self Defense")
        pygame.mouse.set_visible(False)


        while True:
            if self.state!=self.nextState:
                self.state = self.nextState
                self.state.firstDisplay(screen)

            for event in pygame.event.get():
                self.state.handle(event)

            self.state.update(self)
            self.state.display(screen)


if __name__ == "__main__":
    game = Game(*sys.argv)
    game.run()