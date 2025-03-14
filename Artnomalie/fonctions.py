# Créé par Timéo, le 13/02/2025 en Python 3.7
import pygame
import random
from game import Game
from csv import *

#Merci d'écrire toute fonction dans ce document
def read_csv(filename): #lire n'importe quel csv
    DB = []
    with open(filename, mode='r') as file:
            csv_reader = reader(file)
            for row_index, row in enumerate(csv_reader):
                DB.append(row)
    return DB

def IsClicked(event, element):
    if element.rect.collidepoint(event.pos) and event.button ==1 and element in  game.drawed:
        return True
    return False

def cleantext(texte, element):
    for i in range(len(texte)):
        element.text = element.text+texte[i]
        game.gotext.pos = (170+random.randint(-10,10),30+random.randint(-10,10))
        draw()
        pygame.time.delay(100)


def gameover():
    music("Textures/music/blank.mp3", False)
    game.restart_button.image.set_alpha(0)
    game.drawed = gameover_menu
    fade_out(game.fade)
    cleantext("Game over", game.gotext)
    music("Textures/music/laugh.mp3", False)
    pygame.time.delay(300)
    for i in range(10):
        game.skullbottom.rect.y = 50
        draw()
        pygame.time.delay(100)
        game.skullbottom.rect.y = 0
        draw()
        pygame.time.delay(125)
    game.skullbottom.rect.y = 50
    fade_in(game.restart_button)

def loadmap(map):
    game.drawed = []
    for e in map:
        game.drawed.append(e)

def lose(): #la fonction lorsque on perd, sauvegarde le score
    #print(game.bestscores)
    if game.score > int(game.bestscores[0][4]):
        game.bestscores[0][4] = game.score
        game.bestscores = [[int(game.bestscores[0][0]),int(game.bestscores[0][1]),int(game.bestscores[0][2]),int(game.bestscores[0][3]),int(game.bestscores[0][4])]] #permet de rendre le sort fonctionnel vu que les valeurs sont des str pour le csv
        game.bestscores[0].sort(reverse=True) #permet de faire en sort que bestscores[0][4 soit toujours le plus petit score]
        #print(game.bestscores)
        with open("hs.csv", mode='w',newline='') as file:
            csv_writer = writer(file)
            csv_writer.writerows(game.bestscores)
    game.score = 0
    game.ScoreDisplay.pos = (500,30)

#WINDOW
pygame.display.set_caption("PORTRAIT")
screen=pygame.display.set_mode((1000,800))
running = True #Si c'est false, le jeu se ferme

game = Game()
game.fade.image.set_alpha(0)

#liste de toutes les anomalies possible contenant l'image a charger et celle a remplacer pour les tableau simple et zoomés
repertoire_annomalie = [
#Anomalie 1 : La musique change de la lettre à elise à Sonate au claire de lune
["empty space for song anomaly"],
#Anomalie 2 : Le tiroire de la table ne contient plus un bout de papier mais un couteau
["empty space for table anomaly"],
#Anomalie 3 : La tête de la jocode est remplacé par un autre visage
["Textures/Tableau/joconde_anomaly.png", game.joconde, "Textures/Tableau/joconde_anomaly_zoom.png", game.joconde_zoom, (848,263)],
#Anomalie 4 : Le fond de la libérté guidant le peuple est modifié
["Textures/Tableau/Eugene_delacroix_anomalie.png", game.delacroix, "Textures/Tableau/Eugene_delacroix_anomalie_big.png", game.delacroix_zoom],
#Anomalie 5 : La perle de la jeune fille a la perle disparait
["Textures/Tableau/Vermeer_anomalie.png", game.vermeer, "Textures/Tableau/Vermeer_anomalie_big.png", game.vermeer_zoom],
#Anomalie 6 : La lune est inversée sur la nuit étoilé
["Textures/Tableau/Van_gogh_anomalie.png", game.vangogh, "Textures/Tableau/Van_gogh_anomalie_big.png", game.vangogh_zoom],
#Anomalie 7 : quelqu'un dans le fond est en moins
["Textures/Tableau/cri.png", game.cri, "Textures/Tableau/cri_zoom_anomalie.png", game.cri_zoom],
#Anomalie 8 : Les couleurs sont inversés
["Textures/Tableau/picasso_anomaly.png", game.picasso, "Textures/Tableau/Picasso_zoom_anomaly.png", game.picasso_zoom],
#Anomalie 9 : Un bateau est ajouté
["Textures/Tableau/monet_anomalie.png", game.monet, "Textures/Tableau/Monet_anomalie_big.png", game.monet_zoom],
#Anomalie 10 : Des feuilles deviennent rouge
["Textures/Tableau/matisse_anomaly_small.png", game.matisse, "Textures/Tableau/Matisse_anomaly.png", game.matisse_zoom]]

#game.drawed contient tous les éléments à dessiner dans l'image
first_room =[game.background1, game.fond_score, game.joconde, game.delacroix, game.table, game.vermeer, game.vangogh, game.exitbutton, game.ScoreDisplay,
 game.continuebutton,game.cri, game.picasso, game.monet, game.matisse, game.fade] #Contient ce qu'il faut afficher pour la première salle

end_room =[game.backgroundend,game.paycheck, game.restart_button, game.gotext, game.fade]

#TOUJOURS DRAW LE FOND D'ABORD ET LE FADE EN DERNIER
menu = [game.menuBackground, game.playButton,game.credits, game.logo,game.Leave ,game.scorebutton, game.fade]
menu_credit = [game.menuBackground, game.textecredit ,game.RetourCredits,game.fade]
menu_score = [game.menuBackground,game.Top1,game.Top2,game.Top3,game.Top4,game.Top5 ,game.RetourCredits,game.fade]
mode_menu = [game.modeselect, game.storybutton, game.infinite_button, game.fade]
game.drawed = menu
gameover_menu = [game.restart_button, game.skullbottom, game.skulltop,game.gotext,  game.fade]



def change_rect(element,x,y,width,height):
    element.rect.x =x
    element.rect.y = y
    element.rect.width = width
    element.rect.height = height

def zoom(element):
    loadmap([game.zoombg, element,game.button_retour,game.fade])


def draw():#PERMET DE DESSINER LES OBJETS, IL N'UPDATE PAS L'ECRAN
    """Cette fonction sert a dessiner les objet et a écrire les texte sur l'écran"""
    screen.fill((0,0,0)) # clear l'écran
    for i in range(len(game.drawed)):
        if str(game.drawed[i].__class__.__name__) == "Texte": #permet de savoir si c'est un sprite ou du texte
            game.drawed[i].police = pygame.font.Font("Textures/Font/RasterForge.ttf", game.drawed[i].fontSize) # pour changer la font si nécessaire
            game.drawed[i].display = game.drawed[i].police.render(str(game.drawed[i].text),1,(255,255,255)) #changer le texte si nécessaire
            screen.blit(game.drawed[i].display, game.drawed[i].pos)

        else:
            if game.drawed[i].rect.x == 1002: #placer les indicateurs d'anomalie lors du tuto de story
                screen.blit(game.indicator.image, pygame.Rect(848, 290, 45, 45))
                screen.blit(game.indicator.image, pygame.Rect(901, 336, 45, 45))
                screen.blit(game.indicator.image, pygame.Rect(506, 590, 45, 45))
                screen.blit(game.indicator.image, pygame.Rect(740, 390, 45, 45))
                screen.blit(game.indicator.image, pygame.Rect(714, 279, 45, 45))
                screen.blit(game.indicator.image, pygame.Rect(288, 304, 45, 45))
                screen.blit(game.indicator.image, pygame.Rect(100, 332, 45, 45))
                screen.blit(game.indicator.image, pygame.Rect(160, 283, 45, 45))
                screen.blit(game.indicator.image, pygame.Rect(99, 217, 45, 45))
            else:
                screen.blit(game.drawed[i].image, game.drawed[i].rect) #ajoute les éléments dans l'écran, visible après le prochain update
    pygame.display.flip() #update l'écran


def anomalies(anomaly): #permet de choisir l'anomalie (elle ne permet pas de choisir si il y a une anomalie)
    """Cette fonction permet de choisir quel anomalie va apparaitre
       Attention cette fonction ne determine pas si il y a ou non une annomalie"""
    #reset la salle au cas où l'anomaly change de place
    game.joconde.image = pygame.image.load("Textures/Tableau/joconde.png")
    game.delacroix.image = pygame.image.load("Textures/Tableau/Eugene_delacroix.png")
    game.vermeer.image = pygame.image.load("Textures/Tableau/Vermeer.jpg")
    game.vangogh.image = pygame.image.load("Textures/Tableau/Van_gogh.jpg")
    game.joconde_zoom.image = pygame.image.load("Textures/Tableau/joconde_zoom.png")
    game.delacroix_zoom.image = pygame.image.load("Textures/Tableau/Eugene_delacroix_big.png")
    game.vermeer_zoom.image = pygame.image.load("Textures/Tableau/Vermeer_big.jpg")
    game.vangogh_zoom.image = pygame.image.load("Textures/Tableau/Van_gogh_big.jpg")
    game.table.image = pygame.image.load("Textures/Tableau/table_basse.png")
    game.cri_zoom.image = pygame.image.load("Textures/Tableau/cri_zoom.png")
    game.picasso.image = pygame.image.load("Textures/Tableau/picasso.png")
    game.matisse.image = pygame.image.load("Textures/Tableau/matisse.png")
    game.monet.image = pygame.image.load("Textures/Tableau/monet.png")
    game.matisse_zoom.image = pygame.image.load("Textures/Tableau/Matisse_big.png")
    game.monet_zoom.image = pygame.image.load("Textures/Tableau/Monet_big.jpg")
    game.picasso_zoom.image = pygame.image.load("Textures/Tableau/picasso_zoom.png")
    music("Textures\music\Für_Elise.mp3", True)
    #permet de choisir l'anomaly
    if anomaly:
        #print("ANOMALY")
        anomalyid = random.randint(0,len(repertoire_annomalie)-1) #remplacer le dernier chiffre par le nomdre d'anomaly (decaler de 1 pour une recherche correcte dans la liste)
        if anomalyid >= 2: #dans le cas ou les anomalies demande le même code
            repertoire_annomalie[anomalyid][1].image = pygame.image.load(repertoire_annomalie[anomalyid][0])      #affiche l'annomalie
            repertoire_annomalie[anomalyid][3].image = pygame.image.load(repertoire_annomalie[anomalyid][2])      #affiche l'annomalie dans le zoom
            if len(repertoire_annomalie[anomalyid]) != 4: #détecter si y a des infos supplémentaire ou pas pour des coordonnées
                repertoire_annomalie[anomalyid][1].rect.x = repertoire_annomalie[anomalyid][4][0]
                repertoire_annomalie[anomalyid][1].rect.y = repertoire_annomalie[anomalyid][4][1]
        elif anomalyid == 0: #anomaly musique
            music("Textures/music/Moonlight_Sonata_anomalie.mp3", True)
        elif anomalyid == 1: #anomaly table
            return anomalyid
        return anomalyid
    else: # pour changer anomalyid pour eviter certain bug
        anomalyid = -1
        return anomalyid

def music(music, loop):
    """Cette fonction gère la musique"""
    pygame.mixer.music.load(music)
    if loop:
        pygame.mixer.music.play(-1)
    else:
        pygame.mixer.music.play(0)

def fade_in(fade): #transition fondu au noir
    """Cette fonction réalise une transition au noir pour passer du jeu au fade_out"""
    for i in range(int(256/32)):
        fade.image.set_alpha(i*32)
        pygame.time.delay(16)
        draw()
    fade.image.set_alpha(255)
    draw()

def fade_out(fade): #transition fondu au noir inversé (on passe de noir au jeu)
    """Cette fonction réalise une transition au noir pour passer fade_in a une autre page du jeu"""
    for i in range(int(256/32)):
        fade.image.set_alpha(255-i*32)
        pygame.time.delay(16)
        draw()
    fade.image.set_alpha(0) #permet d'être sûr que l'image a bien disparu
    draw()
