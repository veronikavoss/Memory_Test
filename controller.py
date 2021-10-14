#%%
import pygame
from number_button import *
from random import *
#%%
class Controller:
    def __init__(self):
        self.number_sprite=pygame.sprite.Group()
        self.level=1
        self.opportunity=2
        self.game_start=False
        self.hidden=False
        self.next_level=False
        self.wrong=False
        self.game_over=False
        self.number_create()
        
        self.countdown_time=0
        self.hidden_countdown=0
        self.hidden_time=0
        self.wrong_delay=0
        self.game_over_time=0
        self.countdown_timer=pygame.USEREVENT+1
        pygame.time.set_timer(self.countdown_timer,1000)
        self.hidden_timer=pygame.USEREVENT+2
        pygame.time.set_timer(self.hidden_timer,1000)
        self.wrong_delay_timer=pygame.USEREVENT+3
        pygame.time.set_timer(self.wrong_delay_timer,1000)
        self.game_over_timer=pygame.USEREVENT+4
        pygame.time.set_timer(self.game_over_timer,1000)
        
        self.correct_sound=pygame.mixer.Sound('Sound/Magic Spell.wav')
        self.wrong_sound=pygame.mixer.Sound('Sound/B Elec Bass.wav')
    
    def number_create(self):
        self.row,self.column=5,9
        self.margin_l,self.margin_t=55,20
        self.cell_size=130
        cell_margin=10
        grid=[[0 for _ in range(self.column)] for _ in range(self.row)]
        
        num_count=self.level//3+5
        self.num_count=min(num_count,20)
        
        num=1
        while num<=self.num_count:
            self.row_idx=randrange(0,self.row)
            self.column_idx=randrange(0,self.column)
            if grid[self.row_idx][self.column_idx]==0:
                grid[self.row_idx][self.column_idx]=num
                
                x=self.margin_l+cell_margin+self.cell_size*self.column_idx
                y=self.margin_t+cell_margin+self.cell_size*self.row_idx
                
                num_pos=Number(x,y,num)
                self.number_sprite.add(num_pos)
                
                num+=1
    
    def collision(self,display):
        # if self.game_over==False:
        self.mouse_pos=pygame.mouse.get_pos()
        self.mouse=pygame.mouse.get_pressed()
        
        for b in self.number_sprite:
            b.text(display)
            if self.mouse[0]:
                self.hidden=True
                self.hidden_time=self.hidden_countdown
            if self.hidden:
                b.hidden_button()
                if b.rect.collidepoint(self.mouse_pos) and self.mouse[0]:
                    if b.index==self.num_count+1-len(self.number_sprite):
                        self.number_sprite.remove(b)
                    elif self.wrong==False:
                        self.opportunity-=1
                        self.wrong_sound.play()
                        self.wrong=True
    
    def update(self,display):
        hidden_countdown=5-(self.level//3)
        self.hidden_countdown=max(hidden_countdown,2)
        
        if self.game_start==True:
            self.collision(display)
        
        if len(self.number_sprite)==0:
            self.hidden=False
            self.game_start=False
            self.correct_sound.play()
            self.level+=1
            self.number_create()
    
    def grid(self,display):
        for i in range(self.row):
            for j in range(self.column):
                pygame.draw.rect(display,'black',(self.cell_size*j+self.margin_l,self.cell_size*i+self.margin_t,self.cell_size,self.cell_size),3)
    
    def draw(self,display):
        if self.game_start:
            self.grid(display)
            
        self.number_sprite.draw(display)