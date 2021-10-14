#%%
import pygame
import setting
from start_button import *
from number_button import *
from controller import *
#%%
class Game(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pygame.init()
        pygame.display.set_caption(title)
        self.screen=pygame.display.set_mode(screen_size)
        self.clock=pygame.time.Clock()
        self.start_screen()
    
    def start_screen(self):
        self.start_button=Start_Button()
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            self.start_button.update()
            self.screen.fill('black')
            self.start_button.draw(self.screen)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    
                if event.type==pygame.MOUSEBUTTONDOWN:
                    self.mouse_pos=pygame.mouse.get_pos()
                    if self.start_button.collision(self.mouse_pos):
                        print('click',self.mouse_pos)
                        waiting = False
                        self.game_start()
            
            pygame.display.update()
    
    def game_start(self):
        self.controller=Controller()
        self.loop()
    
    def loop(self):
        self.playing=True
        while self.playing:
            self.event()
            self.update()
            self.draw()
            pygame.display.update()
    
    def event(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.playing=False
                
            if event.type==self.controller.countdown_timer and self.controller.game_start==False:
                self.controller.countdown_time+=1
                if self.controller.countdown_time>=3:
                    self.controller.game_start=True
                    self.controller.countdown_time=0
                    self.controller.hidden_time=0
            if event.type==self.controller.hidden_timer and self.controller.game_start:
                self.controller.hidden_time+=1
                if self.controller.hidden_time>=self.controller.hidden_countdown:
                    self.controller.hidden=True
                    self.controller.hidden_time=0
    
    def text(self):
        if self.controller.game_start==False:
            self.countdown_font=pygame.font.SysFont(None,200)
            self.countdown_text=self.countdown_font.render(str(3-self.controller.countdown_time),True,'black')
            self.countdown_text_rect=self.countdown_text.get_rect(center=(screen_width/2,screen_height/2))
            self.screen.blit(self.countdown_text,self.countdown_text_rect)
        else:
            self.level_font=pygame.font.SysFont(None,40)
            self.level_text=self.level_font.render(f'LEVEL {str(self.controller.level).rjust(2)}',True,'black')
            self.level_text_rect=self.level_text.get_rect(right=screen_width-55,bottom=screen_height-10)
            self.screen.blit(self.level_text,self.level_text_rect)
    
    def update(self):
        self.controller.update(self.screen)
    
    def draw(self):
        self.screen.fill('white')
        self.controller.draw(self.screen)
        self.text()

my=Game()
pygame.quit()