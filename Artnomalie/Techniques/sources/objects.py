import pygame

class Tableau(pygame.sprite.Sprite):
    """Classe pour les tableaux"""
    def __init__(self): # ce qui va se passer lors du lancement du jeu
        """Initialise un nouveau tableau"""
        super().__init__() #indispensable
        self.anomaly = False
        self.image = pygame.image.load("../data/Tableau/joconde_lowquality.png")
        self.rect=self.image.get_rect() # avoir les coordonnée du tableau (pratique pour une anomalie où il faudra le déplacer)
        self.rect.x = 0 #position x absolu
        self.rect.y = 0 #position y absolu
        self.rect.width = 0 #hitbox en largeur
        self.rect.height =0 #hitbox en hauteur
        
class Background(pygame.sprite.Sprite):
    """Classe pour les fonds"""
    def __init__(self):
        """Initialise un nouveau fond"""
        super().__init__()
        self.image = pygame.image.load("../data/Tableau/joconde_lowquality.png")
        self.rect=self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.width = 0

class Button(pygame.sprite.Sprite):
    """Classe pour les boutons"""
    def __init__(self):
        """Initialise un nouveau bouton"""
        super().__init__()
        self.image = pygame.image.load("../data/UI/fleche_salle.png")
        self.rect=self.image.get_rect()
        self.rect.x = 0 #position x absolu
        self.rect.y = 0 #position y absolu
        self.rect.width = 0 #hitbox en largeur
        self.rect.height =0 #hitbox en hauteur

class Texte():
    """Classe pour les textes"""
    def __init__(self):
        """Initialise un nouveau texte"""
        super().__init__()
        self.fontSize = 30
        self.police = pygame.font.Font("../data/Font/RasterForge.ttf", self.fontSize)
        self.pos = (0,0)
        self.text = "NaN"
        self.display = self.police.render(str(self.text),1,(255,255,255))


