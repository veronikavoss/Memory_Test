#%%
import pygame
from setting import *
from random import *
#%%
class Start_Button(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((120,120))
        self.rect=self.image.get_rect(center=(120,screen_height-120))
        self.font1=pygame.font.SysFont('Arcade Normal',20)
        self.font2=pygame.font.SysFont('Arcade Normal',80)
        
    def update(self):
        self.start_text=self.font1.render('START', True,'white')
        self.start_text_rect=self.start_text.get_rect(center=(120,screen_height-120))
        self.game_title=self.font2.render('MEMORY TEST', True,'white')
        self.game_title_rect=self.game_title.get_rect()
        self.game_title_rect.center=screen_width//2,screen_height//2
        
    def draw(self,display):
        pygame.draw.circle(display,'white',self.rect.center,60,5)
        display.blit(self.start_text,self.start_text_rect)
        display.blit(self.game_title,self.game_title_rect)
        
    def collision(self,m_pos):
        if self.rect.collidepoint(m_pos):
            return True
        else:
            return False