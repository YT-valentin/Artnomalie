# Créé par Timéo, le 13/02/2025 en Python 3.7
import pygame
import random
from game import Game
from csv import *

#Merci d'écrire toutes fonctions dans ce document

#WINDOW
pygame.display.set_caption("PORTRAIT")
screen=pygame.display.set_mode((1000,800))
running = True #Si c'est false, le jeu se ferme

game = Game()
game.fade.image.set_alpha(0) # fade est un écran noir pour les transitions, ceci le rend transparent pour qu'on puisse voir le jeu

#liste de toutes les anomalies possible contenant l'image a charger et celle a remplacer pour les tableau simple et zoomés
repertoire_annomalie = [
#Anomalie 1 : La musique change de la lettre à elise à Sonate au claire de lune
["empty space for song anomaly"],
#Anomalie 2 : Le tiroire de la table ne contient plus un bout de papier mais un couteau
["empty space for table anomaly"],
#Anomalie 3 : La tête de la jocode est remplacé par un autre visage
["../data/Tableau/joconde_anomaly.png", game.joconde, "../data/Tableau/joconde_anomaly_zoom.png", game.joconde_zoom, (848,263)],
#Anomalie 4 : Le fond de la libérté guidant le peuple est modifié
["../data/Tableau/Eugene_delacroix_anomalie.png", game.delacroix, "../data/Tableau/Eugene_delacroix_anomalie_big.png", game.delacroix_zoom],
#Anomalie 5 : La perle de la jeune fille a la perle disparait
["../data/Tableau/Vermeer_anomalie.png", game.vermeer, "../data/Tableau/Vermeer_anomalie_big.png", game.vermeer_zoom],
#Anomalie 6 : La lune est inversée sur la nuit étoilé
["../data/Tableau/Van_gogh_anomalie.png", game.vangogh, "../data/Tableau/Van_gogh_anomalie_big.png", game.vangogh_zoom],
#Anomalie 7 : quelqu'un dans le fond est en moins
["../data/Tableau/cri.png", game.cri, "../data/Tableau/cri_zoom_anomalie.png", game.cri_zoom],
#Anomalie 8 : Les couleurs sont inversés
["../data/Tableau/picasso_anomaly.png", game.picasso, "../data/Tableau/Picasso_zoom_anomaly.png", game.picasso_zoom],
#Anomalie 9 : Un bateau est ajouté
["../data/Tableau/monet_anomalie.png", game.monet, "../data/Tableau/Monet_anomalie_big.png", game.monet_zoom],
#Anomalie 10 : Des feuilles deviennent rouge
["../data/Tableau/matisse_anomaly_small.png", game.matisse, "../data/Tableau/Matisse_anomaly.png", game.matisse_zoom]]

#game.drawed contient tous les éléments à dessiner dans l'image
#TOUJOURS DRAW LE FOND D'ABORD ET LE FADE EN DERNIER
#LISTE DES SALLES
first_room =[game.background1, game.fond_score, game.joconde, game.delacroix, game.table, game.vermeer, game.vangogh, game.exitbutton, game.ScoreDisplay,
 game.continuebutton,game.cri, game.picasso, game.monet, game.matisse, game.fade] #Contient ce qu'il faut afficher pour la première salle
end_room =[game.backgroundend,game.paycheck, game.restart_button, game.gotext, game.fade]
menu = [game.menuBackground, game.playButton,game.credits, game.logo,game.Leave ,game.scorebutton,game.rules, game.fade]
menu_credit = [game.menuBackground, game.textecredit ,game.RetourCredits,game.fade]
menu_score = [game.menuBackground,game.Top1,game.Top2,game.Top3,game.Top4,game.Top5 ,game.RetourCredits,game.fade]
mode_menu = [game.modeselect, game.storybutton, game.infinite_button, game.fade]
game.drawed = menu
gameover_menu = [game.restart_button, game.skullbottom, game.skulltop,game.gotext,  game.fade]
rulesmenu = [game.menuBackground, game.rulestext, game.RetourCredits, game.fade]

def read_csv(filename): #Pour lire n'importe quel fichier csv
    """entrée : Un fichier csv
       effet : On lit le fichier csv entrée"""
    DB = []
    with open(filename, mode='r') as file:
            csv_reader = reader(file)
            for row_index, row in enumerate(csv_reader):
                DB.append(row)
    return DB

def IsClicked(event, element): #Vérifie si on clique sur l'image
    """entrée : 
       effet : """
    if element.rect.collidepoint(event.pos) and event.button ==1 and element in  game.drawed:
        return True
    return False

def cleantext(texte, element): #Fait bouger le texte légèrement de manière aléatoire
    """entrée : 
       effet : """
    for i in range(len(texte)):
        element.text = element.text+texte[i]
        game.gotext.pos = (170+random.randint(-10,10),30+random.randint(-10,10))
        draw()
        pygame.time.delay(100)


def gameover():
    """Cette fonction se _________ """
    music("../data/music/blank.mp3", False)
    game.restart_button.image.set_alpha(0)
    game.drawed = gameover_menu
    fade_out(game.fade)
    cleantext("Game over", game.gotext)
    music("../data/music/laugh.mp3", False)
    pygame.time.delay(300)
    for i in range(10): # animation de la bouche
        game.skullbottom.rect.y = 50
        draw()
        pygame.time.delay(100)
        game.skullbottom.rect.y = 0
        draw()
        pygame.time.delay(125)
    game.skullbottom.rect.y = 50
    fade_in(game.restart_button)

def loadmap(map): #pour éviter de modifier les listes contenants les elements dans les salles en voulant modifier drawed
    """entrée : 
       effet : """
    game.drawed = []
    for e in map:
        game.drawed.append(e)

def lose(): #la fonction lorsque on perd, sauvegarde le score (surtout utilisé dans le code pour sauvegarder le code plus que quand on perd en vrai)
    #print(game.bestscores)
    """__________________ """
    if game.score > int(game.bestscores[0][4]):
        game.bestscores[0][4] = game.score
        game.bestscores = [[int(game.bestscores[0][0]),int(game.bestscores[0][1]),int(game.bestscores[0][2]),int(game.bestscores[0][3]),int(game.bestscores[0][4])]] #permet de rendre le sort fonctionnel vu que les valeurs sont des str pour le csv
        game.bestscores[0].sort(reverse=True) #permet de faire en sort que bestscores[0][4 soit toujours le plus petit score]
        #print(game.bestscores)
        with open("../data/hs.csv", mode='w',newline='') as file:
            csv_writer = writer(file)
            csv_writer.writerows(game.bestscores)
    game.score = 0
    game.ScoreDisplay.pos = (500,30)

def zoom(element):
    loadmap([game.zoombg, element,game.button_retour,game.fade])

def draw():#PERMET DE DESSINER LES OBJETS, IL N'UPDATE PAS L'ECRAN
    """Cette fonction sert a dessiner les objet et a écrire les texte sur l'écran"""
    screen.fill((0,0,0)) # clear l'écran
    for i in range(len(game.drawed)):
        if str(game.drawed[i].__class__.__name__) == "Texte": #permet de savoir si c'est un sprite ou du texte
            game.drawed[i].police = pygame.font.Font("../data/Font/RasterForge.ttf", game.drawed[i].fontSize) # pour changer la font si nécessaire
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
    """entrée : ___________
       effet : 
       Attention cette fonction ne determine pas si il y a ou non une annomalie"""
    #reset la salle au cas où l'anomaly change de place
    game.joconde.image = pygame.image.load("../data/Tableau/joconde.png")
    game.delacroix.image = pygame.image.load("../data/Tableau/Eugene_delacroix.png")
    game.vermeer.image = pygame.image.load("../data/Tableau/Vermeer.jpg")
    game.vangogh.image = pygame.image.load("../data/Tableau/Van_gogh.jpg")
    game.joconde_zoom.image = pygame.image.load("../data/Tableau/joconde_zoom.png")
    game.delacroix_zoom.image = pygame.image.load("../data/Tableau/Eugene_delacroix_big.png")
    game.vermeer_zoom.image = pygame.image.load("../data/Tableau/Vermeer_big.jpg")
    game.vangogh_zoom.image = pygame.image.load("../data/Tableau/Van_gogh_big.jpg")
    game.table.image = pygame.image.load("../data/Tableau/table_basse.png")
    game.cri_zoom.image = pygame.image.load("../data/Tableau/cri_zoom.png")
    game.picasso.image = pygame.image.load("../data/Tableau/picasso.png")
    game.matisse.image = pygame.image.load("../data/Tableau/matisse.png")
    game.monet.image = pygame.image.load("../data/Tableau/monet.png")
    game.matisse_zoom.image = pygame.image.load("../data/Tableau/Matisse_big.png")
    game.monet_zoom.image = pygame.image.load("../data/Tableau/Monet_big.jpg")
    game.picasso_zoom.image = pygame.image.load("../data/Tableau/picasso_zoom.png")
    game.joconde.rect.x = 582
    game.joconde.rect.y = 269
    music("../data/music/Für_Elise.mp3", True)
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
            music("../data/music/Moonlight_Sonata_anomalie.mp3", True)
        elif anomalyid == 1: #anomaly table
            return anomalyid
        return anomalyid
    else: # pour changer anomalyid pour eviter certain bug
        anomalyid = -1
        return anomalyid

def music(music, loop):
    """entrée : la musique que l'on souhaite lire et _______
       effet : la musique choisie se joue"""
    pygame.mixer.music.load(music)
    if loop:
        pygame.mixer.music.play(-1)
    else:
        pygame.mixer.music.play(0)

def fade_in(fade):
    """entrée : 
       effet : Cette fonction réalise une transition au noir pour passer du jeu au fade_out"""
    for i in range(int(256/32)):
        fade.image.set_alpha(i*32)
        pygame.time.delay(16)
        draw()
    fade.image.set_alpha(255)
    draw()

def fade_out(fade): 
    """entrée : 
       effet : Cette fonction réalise une transition au noir pour passer du fade_in à une autre page du jeu"""
    for i in range(int(256/32)):
        fade.image.set_alpha(255-i*32)
        pygame.time.delay(16)
        draw()
    fade.image.set_alpha(0) #permet d'être sûr que l'image a bien disparu
    draw()
