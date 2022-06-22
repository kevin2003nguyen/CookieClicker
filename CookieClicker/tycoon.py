
import math
import pygame
from pygame import mixer

pygame.mixer.init()
WHITE = 255,255,255
BLACK = 0,0,0
GREEN = 12,13,34
# importing sounds
mixer.music.load('sounds/crunch.wav')
# importing images
bg = pygame.image.load('sprites/background_img.png')
building_bg = pygame.image.load('sprites/wooden_background.png')
wood = pygame.image.load('sprites/wooden_bar.png')

back_cookie = pygame.image.load('sprites/backgroundCookie.png')
cookie_img = pygame.image.load('sprites/cookie.png')
cursor_img = pygame.image.load('sprites/cursor_img.png')
grandma_img = pygame.image.load('sprites/grandma_img.png')
farm_img = pygame.image.load('sprites/farm_img.png')
mine_img = pygame.image.load('sprites/mine_img.png')
factory_img = pygame.image.load('sprites/factory_img.png')
bank_img = pygame.image.load('sprites/bank_img.png')
temple_img = pygame.image.load('sprites/temple_img.png')
wizard_tower_img = pygame.image.load('sprites/wizard_tower_img.png')

cursor_icon = pygame.image.load('sprites/icons/cursor_icon.png')
grandma_icon = pygame.image.load('sprites/icons/grandma_icon.png')
farm_icon = pygame.image.load('sprites/icons/farm_icon.png')
mine_icon = pygame.image.load('sprites/icons/mine_icon.png')
factory_icon = pygame.image.load('sprites/icons/factory_icon.png')
bank_icon = pygame.image.load('sprites/icons/bank_icon.png')
temple_icon = pygame.image.load('sprites/icons/temple_icon.png')
wizard_tower_icon = pygame.image.load('sprites/icons/wizard_tower_icon.png')

class Player:
    def __init__(self):
        self.score = 0
        self.total_cps = 0

# Class (building)
class Cookie:
    def __init__(self,x_pos,y_pos,image,scale):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.height = 250
        self.length = 250
        self.image = pygame.transform.scale(image,(int(self.length * scale),int(self.height)))
        self.rect = self.image.get_rect()

        self.clicked = False

        self.count = 0
    def update(self):

            if self.count > 0:
                cookie_scaled = pygame.transform.scale(cookie_img, (int(0.9*self.length), int(0.9*self.height)))
                screen.blit(cookie_scaled, (cookie_scaled.get_rect(  center=(int(self.x_pos + self.length/2), int(self.y_pos + self.height/2))  )))
                self.count -= 1
            else:
                screen.blit(cookie_img, (cookie_img.get_rect(center=(int(self.x_pos + self.length/2), int(self.y_pos + self.height/2)))))

        # return action
    def collidepoint(self, point):
            return pygame.Rect(self.x_pos, self.y_pos, self.length, self.height).collidepoint(point)
# the upgrades
class Upgrade(pygame.sprite.Sprite):
    def __init__(self,picture_path, name, x_pos, y_pos, image, icon, base_cost, increase_per_purchase, cps):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect.center = [x_pos,y_pos]
        self.length = 300
        self.height = 64

        self.image = image
        self.icon = icon
        
        self.quantity = 0
        self.base_cost = base_cost
        self.increase_per_purchase = increase_per_purchase
        self.cps = cps

        self.created = 0
    def collidepoint(self,point):
        # get mouse position
        return pygame.Rect(self.x_pos - 150, self.y_pos - 30, self.length, self.height).collidepoint(point)

    def getTotalCost(self):
        return math.ceil(self.base_cost * self.increase_per_purchase**(self.quantity))

    def draw(self):
        store_cost_font = pygame.font.Font('Font/ChelseaMarket-Regular.ttf', 17)
        store_quantity_font = pygame.font.Font('Font/ChelseaMarket-Regular.ttf', 36)
        
        text_cost = store_cost_font.render(f'{self.getTotalCost()}',True, BLACK)
        screen.blit(text_cost,[self.x_pos +  self.length - 360, self.y_pos + self.height - 61])
        
        text_quantity = store_quantity_font.render(f"{self.quantity}",True,WHITE)
        screen.blit(text_quantity,[self.x_pos + self.length - 190, self.y_pos - 22])

class Background_cookie:
    def __init__(self,x_pos,y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.length = 40
        self.height = 40

    def draw(self):
        screen.blit(back_cookie, (self.x_pos,self.y_pos))

    def update(self):
        self.y_pos += 5

        if self.y_pos > screen.get_height():
            list_of_cookies.remove(fallen_cookie)
# General setup
pygame.init()
clock = pygame.time.Clock()

# Define the dimension
screen_width = 1000
screen_hight = 600
screen = pygame.display.set_mode((screen_width,screen_hight))

pygame.display.set_caption('Tycoon')

wood_top = screen.get_height() - wood.get_height()
wood_left = screen.get_width()/2 - wood.get_width()/2

bg_top = screen.get_height() - bg.get_height()
bg_left = screen.get_width()/2 - bg.get_width()/2

building_bg_top = screen.get_height() - building_bg.get_height()
building_bg_left = screen.get_width()/2 - building_bg.get_width()/2

screen.blit(building_bg,(building_bg_left,building_bg_top))
screen.blit(bg, (bg_left,bg_top))
screen.blit(wood,(wood_left,wood_top))

#  Varaibles
cookie = Cookie(50,180,cookie_img,1)
user = Player()

#used to be at 32
store_y = 72

cursor = Upgrade('sprites/cursor_img.png', 'Cursor', 850, store_y, cursor_img, cursor_icon, base_cost=15, increase_per_purchase=1.15, cps=0.1)
grandma = Upgrade('sprites/grandma_img.png', 'Grandma', 850, store_y + 64*1, grandma_img, grandma_icon, base_cost=100, increase_per_purchase=1.15, cps=1)
farm = Upgrade('sprites/grandma_img.png', 'Farm', 850, store_y + 64*2, farm_img, farm_icon, base_cost=1100, increase_per_purchase=1.15, cps=8)
mine = Upgrade('sprites/grandma_img.png', 'Mine', 850, store_y + 64*3, mine_img, mine_icon, base_cost=12000, increase_per_purchase=1.15, cps=47)
factory = Upgrade('sprites/grandma_img.png', 'Factory', 850, store_y + 64*4, factory_img, factory_icon, base_cost=130000, increase_per_purchase=1.15, cps=260)
bank = Upgrade('sprites/grandma_img.png', 'Bank', 850, store_y + 64*5, bank_img, factory_icon, base_cost=1400000, increase_per_purchase=1.15, cps=1400)
temple = Upgrade('sprites/grandma_img.png', 'Temple', 850, store_y + 64*6, temple_img, temple_icon, base_cost=20000000, increase_per_purchase=1.15, cps=7800)
wizard_tower = Upgrade('sprites/grandma_img.png', 'Wizard Tower', 850, store_y + 64*7, wizard_tower_img, wizard_tower_icon, base_cost=330000000, increase_per_purchase=1.15, cps=311080)

list_of_buildings = [cursor, grandma, farm, mine, factory, bank, temple, wizard_tower]

list_of_cookies = []

upgrade_group = pygame.sprite.Group()
upgrade_group.add(cursor , grandma, farm, mine, factory, bank, temple, wizard_tower)

background_cookie_group = pygame.sprite.Group()


cps = 0

run = True

cursors = []
grandmas = []
farms = []
mines = []
factories = []
banks = []
temples = []
wizard_towers = []

counter = 1000 # in ms == one second
# Game loop
while run:

    screen.blit(bg,(0,0))
    screen.blit(building_bg,(700,0))
    screen.blit(wood,(685,0))
    cookie.update()
    
    eta = clock.tick(60)
    counter -= eta
    if counter < 0:
        counter += 1000
        user.score += cps

    for event in pygame.event.get():
        # Check for QUIT event
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if cookie.collidepoint(mouse_pos):
                user.score = user.score + 1
                cookie.count = 1
                list_of_cookies.append(Background_cookie(mouse_pos[0],mouse_pos[1]))
                mixer.music.play()
            for building in list_of_buildings:
                if building.collidepoint(mouse_pos) and user.score >= building.getTotalCost():
                    
                    if building == cursor:
                        cursors.append(1)
                        cps += 0.1
                        user.score -= building.getTotalCost()
                        cursor.quantity += 1
                    elif building == grandma:
                        grandmas.append(1)
                        cps += 1
                        user.score -= building.getTotalCost()
                        grandma.quantity += 1
                    elif building == farm:
                        farms.append(1)
                        cps += 8
                        user.score -= int(building.getTotalCost())
                        farm.quantity += 1
                    elif building == mine:
                        mines.append(1)
                        cps += 47
                        user.score -= building.getTotalCost()
                        mine.quantity += 1
                    elif building == factory:
                        factories.append(1)
                        cps += 260
                        user.score -= building.getTotalCost()
                        factory.quantity += 1
                    elif building == bank:
                        banks.append(1)
                        cps += 1400
                        user.score -= building.getTotalCost()
                        bank.quantity += 1
                    elif building == temple:
                        temples.append(1)
                        cps += 7800
                        user.score -= building.getTotalCost()
                        temple.quantity += 1
                    elif building == wizard_tower:
                        wizard_towers.append(1)
                        cps += 44000 
                        user.score -= building.getTotalCost()
                        wizard_tower.quantity += 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                user.score += 1000000000000000000000
                print(cookie.count)
            
            if event.key == pygame.K_q:
                print(pygame.mouse.get_pos())

  
    upgrade_group.draw(screen)

    for fallen_cookie in list_of_cookies:
        fallen_cookie.draw()
        fallen_cookie.update()

    cursor.draw()
    grandma.draw()
    farm.draw()
    mine.draw()
    factory.draw()
    bank.draw()
    temple.draw()
    wizard_tower.draw()
    

    # Drawing Text
    font = pygame.font.SysFont('Aharoni', 40,True,False)
    text_cookies_score = font.render(f"Cookies: {int(user.score)} ",True,BLACK)
    text_cps = font.render(f"CPS: {round(cps,2)}",True, BLACK)
    screen.blit(text_cps,[100,90])
    screen.blit(text_cookies_score,[100,50])
    
    background_cookie_group.draw(screen)
    pygame.display.flip()

    # Fill the background
    screen.fill(WHITE)


pygame.quit()
        