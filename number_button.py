#%%
import pygame
from setting import *
#%%
class Number(pygame.sprite.Sprite):
    def __init__(self,x,y,index):
        super().__init__()
        self.index=index
        self.button_size=110
        self.image=pygame.Surface((self.button_size,self.button_size))
        self.image.fill('white')
        self.rect=self.image.get_rect(x=x,y=y)
        self.surface_rect=self.rect
    
    def text(self,display):
        font=pygame.font.SysFont(None,150)
        self.image=font.render(str(self.index),True,'black')
        self.rect=self.image.get_rect(center=self.surface_rect.center)
    
    def hidden_button(self):
        self.image=pygame.Surface((self.button_size,self.button_size))
        self.rect=self.surface_rect
        self.image.fill('gray')