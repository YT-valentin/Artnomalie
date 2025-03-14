import pygame
from objects import *

class Game: # MERCI DE INSTANCIER TOUTE OBJET ICI !

    def __init__(self):

        #On créer les tableau à partir de la classe Tableau
        self.joconde = Tableau()
        self.joconde.image = pygame.image.load("Textures/Tableau/joconde.png")
        self.joconde.rect.x = 852
        self.joconde.rect.y = 269
        self.joconde.rect.width = 38
        self.joconde.rect.height = 93

        self.delacroix = Tableau()
        self.delacroix.image = pygame.image.load("Textures/Tableau/Eugene_delacroix.png")
        self.delacroix.rect.x = 740
        self.delacroix.rect.y = 395
        self.delacroix.rect.width = 45
        self.delacroix.rect.height = 35

        self.vermeer  = Tableau()
        self.vermeer.image = pygame.image.load("Textures/Tableau/Vermeer.jpg")
        self.vermeer.rect.x = 260
        self.vermeer.rect.y = 263
        self.vermeer.rect.width = 106
        self.vermeer.rect.height = 118

        self.vangogh = Tableau()
        self.vangogh.image = pygame.image.load("Textures/Tableau/Van_gogh.jpg")
        self.vangogh.rect.x = 682
        self.vangogh.rect.y = 247
        self.vangogh.rect.width = 103
        self.vangogh.rect.height = 101

        self.cri = Tableau()
        self.cri.image = pygame.image.load("Textures/Tableau/cri.png")
        self.cri.rect.x = 893
        self.cri.rect.y = 279
        self.cri.rect.width = 60
        self.cri.rect.height = 156

        #section pour les tableaux zoomés
        self.joconde_zoom = Background()
        self.joconde_zoom.image = pygame.image.load("Textures/Tableau/joconde_zoom.png")
        self.joconde_zoom.rect.x = 250
        self.joconde_zoom.rect.y = 100

        self.delacroix_zoom = Background()
        self.delacroix_zoom.image = pygame.image.load("Textures/Tableau/Eugene_delacroix_big.png")
        self.delacroix_zoom.rect.x = 250
        self.delacroix_zoom.rect.y = 200

        self.vermeer_zoom = Background()
        self.vermeer_zoom.image = pygame.image.load("Textures/Tableau/Vermeer_big.jpg")
        self.vermeer_zoom.rect.x = 250
        self.vermeer_zoom.rect.y = 200

        self.vangogh_zoom = Background()
        self.vangogh_zoom.image = pygame.image.load("Textures/Tableau/Van_gogh_big.jpg")
        self.vangogh_zoom.rect.x = 250
        self.vangogh_zoom.rect.y = 200

        self.picasso_zoom = Background()
        self.picasso_zoom.image = pygame.image.load("Textures/Tableau/picasso_zoom.png")
        self.picasso_zoom.rect.x = 180
        self.picasso_zoom.rect.y = 220

        self.matisse_zoom = Background()
        self.matisse_zoom.image = pygame.image.load("Textures/Tableau/Matisse_big.png")
        self.matisse_zoom.rect.x = 180
        self.matisse_zoom.rect.y = 180

        self.monet_zoom = Background()
        self.monet_zoom.image = pygame.image.load("Textures/Tableau/Monet_big.jpg")
        self.monet_zoom.rect.x = 180
        self.monet_zoom.rect.y = 150

        self.cri_zoom = Background()
        self.cri_zoom.image = pygame.image.load("Textures/Tableau/cri_zoom.png")
        self.cri_zoom.rect.x = 250
        self.cri_zoom.rect.y = 100

        #table basse
        self.table = Tableau()
        self.table.image = pygame.image.load("Textures/Tableau/table_basse.png")
        self.table.rect.x = 412
        self.table.rect.y = 580
        self.table.rect.width = 222
        self.table.rect.height = 74
        #section des backgroud
        self.zoombg = Background()
        self.zoombg.image = pygame.image.load("Textures/Background/zoombg.png")
        self.background1 = Background()
        self.background1.image = pygame.image.load("Textures/Background/salle1.jpg")
        self.fade = Background()
        self.fade.image = pygame.image.load("Textures/Background/fade1.png")
        self.backgroundini = Background()
        self.backgroundini.image = pygame.image.load("Textures/UI/nytelogo.png")
        self.backgroundend = Background()
        self.backgroundend.image = pygame.image.load("Textures/Background/endbg.png")

        self.paycheck = Button()
        self.paycheck.rect.x = 100
        self.paycheck.rect.y = 200
        self.paycheck.image = pygame.image.load("Textures/UI/paycheck.png")

        #On initialise le score a zéro
        self.score = -1
        #On choisit le mode
        self.mode = "Story"
        #variable contenant tout les scores
        self.bestscores = []
        self.drawed = []

        #User Interface
            #logo
        self.logo = Button()
        self.logo.image = pygame.image.load("Textures/UI/artnomalielogo.png")
        self.logo.rect.x=10
        self.logo.rect.y= 30
        self.logo.rect.width = 0
        self.logo.rect.height = 0
            #bouton suivant

        self.continuebutton = Button()
        self.continuebutton.rect.x=810
        self.continuebutton.rect.y= 650
        self.continuebutton.rect.width = 200
        self.continuebutton.rect.height = 120
            #bouton retour
        self.button_retour = Button()
        self.button_retour.rect.x=50
        self.button_retour.rect.y= 650
        self.button_retour.image = pygame.image.load("Textures/UI/fleche_retour.png") #change l'image de base
        self.button_retour.rect.width = 200
        self.button_retour.rect.height = 120
            #exit (texture temporaire)
        self.exitbutton = Button()
        self.exitbutton.rect.x=50
        self.exitbutton.rect.y= 650
        self.exitbutton.image = pygame.image.load("Textures/UI/bouton_anomalies.png")
        self.exitbutton.rect.width = 150
        self.exitbutton.rect.height = 90
            #Fond du score
        self.fond_score = Background()
        self.fond_score.rect.x = 412
        self.fond_score.rect.y = -5
        self.fond_score.image = pygame.image.load("Textures/Background/fond_score.png")
            #Texte
        self.ScoreDisplay = Texte()
        self.ScoreDisplay.text = "0"
        self.ScoreDisplay.pos = (500,30)
        self.ScoreDisplay.fontSize = 50

            #Bouton Play
        self.playButton = Button()
        self.playButton.rect.x = 350
        self.playButton.rect.y = 600
        self.playButton.image = pygame.image.load("Textures/UI/playpainting.png")
        self.playButton.rect.width = 300
        self.playButton.rect.height = 180

            # Score
        self.scorebutton = Button()
        self.scorebutton.rect.x = 25
        self.scorebutton.rect.y = 400
        self.scorebutton.image = pygame.image.load("Textures/UI/scorepainting.png")
        self.scorebutton.rect.width = 300
        self.scorebutton.rect.height = 180

            # Credits
        self.credits = Button()
        self.credits.rect.x = 25
        self.credits.rect.y = 600
        self.credits.image = pygame.image.load("Textures/UI/creditpainting.png")
        self.credits.rect.width = 300
        self.credits.rect.height = 180

            #texte credit
        self.textecredit = Background()
        self.textecredit.image = pygame.image.load("Textures/Background/creditbg.png")

            # Croix retour credits
        self.RetourCredits = Button()
        self.RetourCredits.rect.x = 850
        self.RetourCredits.rect.y = 5
        self.RetourCredits.image = pygame.image.load("Textures/UI/retourpainting.png")
        self.RetourCredits.rect.width = 100
        self.RetourCredits.rect.height = 100

            #Leave Button
        self.Leave = Button()
        self.Leave.rect.x = 675
        self.Leave.rect.y = 600
        self.Leave.image = pygame.image.load("Textures/UI/exitpainting.png")
        self.Leave.rect.width = 300
        self.Leave.rect.height = 180

        self.menuBackground = Background()
        self.menuBackground.image = pygame.image.load("Textures/Background/menubg.png")
        self.menuBackground.rect.y = 0
        self.skulltop = Background()
        self.skulltop.image = pygame.image.load("Textures/UI/skulltop.png")
        self.skullbottom = Button()
        self.skullbottom.image = pygame.image.load("Textures/UI/skullbottom.png")
        self.skullbottom.rect.y = 0
        self.skullbottom.rect.x = 0
        self.skullbottom.rect.width = 0
        #highscore
        self.Top1 = Texte()
        self.Top1.text = "Top 1: 0"
        self.Top1.pos = (30,30)
        self.Top1.fontSize = 100

        self.Top2 = Texte()
        self.Top2.text = "Top 2: 0"
        self.Top2.pos = (30,130)
        self.Top2.fontSize = 100

        self.Top3 = Texte()
        self.Top3.text = "Top 3: 0"
        self.Top3.pos = (30,230)
        self.Top3.fontSize = 100

        self.Top4 = Texte()
        self.Top4.text = "Top 4: 0"
        self.Top4.pos = (30,330)
        self.Top4.fontSize = 100

        self.Top5 = Texte()
        self.Top5.text = "Top 5: 0"
        self.Top5.pos = (30,430)
        self.Top5.fontSize = 100

        # mode menu
        self.modeselect = Button()
        self.modeselect.image = pygame.image.load("Textures/UI/select_mode_menu.png")
        self.modeselect.rect.width = 0
        self.modeselect.rect.x = 200
        self.modeselect.rect.y = 150
        #story mode button
        self.storybutton = Button()
        self.storybutton.image = pygame.image.load("Textures/UI/story_button.png")
        self.storybutton.rect.width = 400
        self.storybutton.rect.height = 100
        self.storybutton.rect.x = 300
        self.storybutton.rect.y = 275

        #infinite mode button
        self.infinite_button = Button()
        self.infinite_button.image = pygame.image.load("Textures/UI/infinite_button.png")
        self.infinite_button.rect.width = 400
        self.infinite_button.rect.height = 100
        self.infinite_button.rect.x = 300
        self.infinite_button.rect.y = 410

        #warning
        self.warning = Button()
        self.warning.image = pygame.image.load("Textures/UI/warning_ui.png")
        self.warning.rect.width = 500
        self.warning.rect.height = 200
        self.warning.rect.x = 250
        self.warning.rect.y = 50

        self.restart_button = Button()
        self.restart_button.image = pygame.image.load("Textures/UI/restart_button.png")
        self.restart_button.rect.width = 263
        self.restart_button.rect.height = 85
        self.restart_button.rect.x = 356
        self.restart_button.rect.y = 552
        
        #game over text
        self.gotext = Texte()
        self.gotext.text = ""
        self.gotext.pos = (170,30)
        self.gotext.fontSize = 100
        #star symbol
        self.indicator = Button()
        self.indicator.image = pygame.image.load("Textures/UI/starsymbol.png")
        self.indicator.rect.height = 0
        self.indicator.rect.x = 1002


        self.picasso = Background()
        self.picasso.image = pygame.image.load("Textures/Tableau/picasso.png")
        self.picasso.rect.x = 91
        self.picasso.rect.y = 208
        self.picasso.rect.width = 54
        self.picasso.rect.height = 55

        self.matisse = Background()
        self.matisse.image = pygame.image.load("Textures/Tableau/matisse.png")
        self.matisse.rect.x = 158
        self.matisse.rect.y = 231
        self.matisse.rect.width = 53
        self.matisse.rect.height = 145

        self.monet = Background()
        self.monet.image = pygame.image.load("Textures/Tableau/monet.png")
        self.monet.rect.x = 92
        self.monet.rect.y = 278
        self.monet.rect.width = 59
        self.monet.rect.height = 165