import pygame

class Alien(pygame.sprite.Sprite):
    def __init__(self, tier, x, y):
        super().__init__()
        file_path = './aliens/' + tier + '.png'
        self.image = pygame.image.load(file_path).convert_alpha()
        self.rect =  self.image.get_rect(topleft = (x,y ))

        if tier == 'een': self.value = 100
        elif tier == 'twee': self.value = 200
        elif tier == 'drie': self.value = 300
        elif tier == 'vier': self.value = 400
        else: self.value = 500

    def update(self, direction):
        self.rect.x += direction

class miniboss(pygame.sprite.Sprite):
    def __init__(self,side,screen_width):
        super().__init__()
        self.image = pygame.image.load('./aliens/vier.png')
        if side == 'right':
            x = screen_width + 50
            self.speed = -3
        else:
            x = - 50
            self.speed = 3
        self.rect =self.image.get_rect(topleft = (x,80))

    def update(self):
        self.rect.x += self.speed