import pygame

#creer une classe pour les tableaux
class Tableau(pygame.sprite.Sprite):
    def __init__(self): # ce qui va se passer lors du lancement du jeu
        super().__init__() #indispensable
        self.anomaly = False
        self.image = pygame.image.load("Textures/Tableau/joconde_lowquality.png")
        self.rect=self.image.get_rect() # avoir les coordonnée du tableau (pratique pour une anomalie où il faudra le déplacer)
        self.rect.x = 0 #position x absolu
        self.rect.y = 0 #position y absolu
        self.rect.width = 0 #hitbox en largeur
        self.rect.height =0 #hitbox en hauteur
        
class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Textures/Tableau/joconde_lowquality.png")
        self.rect=self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.width = 0

class Button(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Textures/UI/fleche_salle.png")
        self.rect=self.image.get_rect()
        self.rect.x = 0 #position x absolu
        self.rect.y = 0 #position y absolu
        self.rect.width = 0 #hitbox en largeur
        self.rect.height =0 #hitbox en hauteur

class Texte():
    def __init__(self):
        super().__init__()
        self.fontSize = 30
        self.police = pygame.font.Font("Textures/Font/RasterForge.ttf", self.fontSize)
        self.pos = (0,0)
        self.text = "NaN"
        self.display = self.police.render(str(self.text),1,(255,255,255))


