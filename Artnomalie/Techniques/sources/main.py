import pygame
pygame.init()
from game import Game
import random
from fonctions import*

anomalyluck = 50 #Pourcentage de chance d'avoir une anomalie
anomaly = False
anomalyid = 0 #Contient le numero de l'anomalie
score = 0
win = False
game.bestscores = read_csv("../data/hs.csv") #Récupère les scores stockés dans le fichier csv
warningremoval = 0 #Initialisation du compteur de temps pour le warning
music("../data/music/Bolero.mp3", True) #Lancement de la musique du menu dans une boucle infinie

loadmap([game.backgroundini,game.fade])
fade_out(game.fade)
pygame.time.delay(3000)
fade_in(game.fade)
pygame.time.delay(1000)
loadmap(menu)
fade_out(game.fade)

while running: #Boucle principale (évite que la page se ferme toute seule)
    pygame.time.delay(16) #Force le jeu en 60 images par secondes

    if game.warning in  game.drawed:
        warningremoval += 16
        if warningremoval >=13000: #Enleve le "warning" après 5 secondes
             game.warning.image.set_alpha(0)
        else:
            game.warning.image.set_alpha(255)
    draw() #dessine les objets se trouvant dans la liste "draw"

    if win == True : #S'active si on gagne
        game.restart_button.image.set_alpha(0)
        game.paycheck.image.set_alpha(0)
        music("../data/music/victorysound.mp3", False)
        win = False
        fade_in(game.fade)
        loadmap(end_room)
        game.score = -1
        game.ScoreDisplay.text = "0"
        fade_out(game.fade)
        fade_in(game.paycheck)
        pygame.time.delay(500)
        cleantext("you win !", game.gotext)
        pygame.time.delay(2000)
        fade_in(game.restart_button)



    for event in pygame.event.get(): #Récupère tout les évènement du joueur
  
        if event.type == pygame.QUIT: #S'active si le joueur appuis sur la croix
            lose() #Sauvegarde le score a jour
            running=False
            pygame.quit()
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and  game.background1 in game.drawed: #Détecte si on appuis sur "échap" pendant que l'on joue (fonctionne suelement dans la salle principale)
                lose() #update le score
                game.ScoreDisplay.pos = (500,30) #Recentre le score une fois arrivé à 10 points
                fade_in(game.fade)
                loadmap(menu)
                fade_out(game.fade)
        elif event.type == pygame.MOUSEBUTTONDOWN: #S'active si le joueur clique sur l'un des bouttons

               #------------------MENU--------------------------------
            if IsClicked(event, game.playButton):      #------Permet de voir si on clique sur le bouton "Play"

                loadmap(mode_menu)
                fade_out(game.fade)
                pygame.event.clear()

            elif IsClicked(event, game.credits):           #--------- Affiche les crédits
                 loadmap(menu_credit)                    # Affiche la croix pour quitter les crédits
                 pygame.event.clear()

            elif IsClicked(event, game.RetourCredits):
                 loadmap(menu)
                 pygame.event.clear()

            elif IsClicked(event, game.scorebutton):
                game.bestscores = read_csv("../data/hs.csv") #Lis le fichier csv contenant les 5 meilleurs scores
                game.bestscores = [[int(game.bestscores[0][0]),int(game.bestscores[0][1]),int(game.bestscores[0][2]),int(game.bestscores[0][3]),int(game.bestscores[0][4])]]
                game.bestscores[0].sort(reverse=True)
                game.Top1.text = f"Top 1: {game.bestscores[0][0]}" #Met les scores à jour si nécessaire
                game.Top2.text = f"Top 2: {game.bestscores[0][1]}"
                game.Top3.text = f"Top 3: {game.bestscores[0][2]}"
                game.Top4.text = f"Top 4: {game.bestscores[0][3]}"
                game.Top5.text = f"Top 5: {game.bestscores[0][4]}"
                loadmap(menu_score)
                pygame.event.clear()


            elif IsClicked(event, game.Leave):
                running = False
                pygame.quit()
                break
            elif IsClicked(event, game.continuebutton): #Bouton continuer
                fade_in(game.fade)
                pygame.time.delay(1000)
                if anomaly == False: #Donne un point si il n'y a pas d'anomalie, met le score à 0 si il y en a une
                    game.score += 1
                    if game.score >= 10 and game.mode == "Infinite" :
                        game.ScoreDisplay.pos = (485,30)
                    elif game.score == 10 and game.mode == "Story" : #Active la variable victoire
                        win = True
                        loadmap([game.fade]) #Rend l'écran noir
                        draw()

                else:
                    lose()
                    game.ScoreDisplay.pos = (500,30)
                    if game.mode == "Story":
                        gameover()
                        pass

                if ( not anomaly or game.mode == "Infinite" )and win == False: #Relance la salle sauf si on gagne ou que l'on perd
                    game.ScoreDisplay.text = game.score #Modifie le score
                    anomaly = random.randint(1,100) <= anomalyluck #creer ou non une anomalie avec une probabilité de 50%
                    loadmap(first_room)
                    anomalyid = anomalies(anomaly) #Choisi l'anomalie si elle existe, la dessine et dessine tout les autres elements
                    fade_out(game.fade)
                    pygame.event.clear()

            elif IsClicked(event, game.button_retour): #Bouton retour
                fade_in(game.fade) #Doit tout le temps être la première ligne
                pygame.time.delay(1000)
                loadmap(first_room) #Temporaire, dépend de là où nous sommes
                if game.mode == "Story" and game.score == -1 and game.exitbutton in game.drawed:
                    game.drawed.remove(game.exitbutton)
                    game.drawed.insert(-1, game.indicator)
                fade_out(game.fade)
                pygame.event.clear() #Doit être la dernière ligne juste après le fade out
            elif IsClicked(event, game.restart_button):
                lose()
                game.skullbottom.rect.y = 0
                game.gotext.text=""
                anomaly = False
                warningremoval = 0
                anomalyid = -1
                fade_in(game.fade)
                loadmap(first_room)
                if game.mode == "Story":
                    game.score = -1
                    game.ScoreDisplay.text = "0"
                    game.drawed.remove(game.exitbutton)
                    game.drawed.insert(-1, game.indicator)
                draw()
                fade_out(game.fade)
                music("../data/music/Für_Elise.mp3", True)
                pygame.event.clear()
            elif IsClicked(event, game.exitbutton): #Bouton anomalie

                fade_in(game.fade) #Doit tout le temps être la première ligne
                pygame.time.delay(1000)
                loadmap(first_room)
                if anomaly == False: #Donne un point si il y a une anomalie, met le scoreà 0 sinon
                    lose()
                    game.ScoreDisplay.pos = (500,30)
                    if game.mode == "Story":
                        gameover()
                        pass
                else:
                    game.score += 1
                    if game.score >= 10 and game.mode == "Infinite" :
                        game.ScoreDisplay.pos = (485,30)
                    elif game.score == 10 and game.mode == "Story" :
                        win = True
                        loadmap([game.fade])
                        draw()

                if (game.mode == "Infinite" or anomaly) and win == False:
                    game.ScoreDisplay.text = game.score #change le score
                    anomaly = random.randint(1,100) <= anomalyluck #creer ou non une anomalie avec une probabilité de 50%
                    loadmap(first_room)
                    anomalyid = anomalies(anomaly) #Génère l'anomalie
                    fade_out(game.fade)
                    pygame.event.clear() #Doit être la dernière ligne juste après le fade out
            elif IsClicked(event, game.rules):
                loadmap(rulesmenu)
                
               #--------Choix du mode de jeu---------------
            elif IsClicked(event, game.storybutton):
                game.mode = "Story"
                fade_in(game.fade)
                pygame.time.delay(1000)
                game.score = -1
                loadmap(first_room)
                game.ScoreDisplay.text = 0
                anomaly = False
                anomalyid = anomalies(anomaly)
                game.drawed.remove(game.exitbutton)
                game.drawed.insert(-1, game.indicator)
                game.drawed.insert(-1, game.warning) #Pour mettre le "warning" en avant dernier
                fade_out(game.fade)
            elif IsClicked(event, game.infinite_button):
                game.mode = "Infinite"
                fade_in(game.fade)
                game.score = 0
                game.ScoreDisplay.text = 0
                anomaly = random.randint(1,100) <= anomalyluck
                anomalyid = anomalies(anomaly)
                pygame.time.delay(1000)
                loadmap(first_room)
                fade_out(game.fade)
                
                #--------Tableau et autres objet cliquable------------
            elif IsClicked(event, game.joconde): #Vérifie si on clique sur "La joconde" et si c'est un clique gauche
                fade_in(game.fade)
                pygame.time.delay(1000)
                zoom(game.joconde_zoom)
                if anomalyid == 2:
                    music("../data/music/creepy_sound.mp3", True)
                fade_out(game.fade)
                pygame.event.clear()

            elif IsClicked(event, game.delacroix): #Vérifie si on clique sur "La liberté guidant le peuple et si c'est un clique gauche
                fade_in(game.fade)
                pygame.time.delay(1000)
                zoom(game.delacroix_zoom)
                fade_out(game.fade)
                pygame.event.clear()

            elif IsClicked(event, game.vermeer): #Vérifie si on clique sur "la jeune fille à la perle" et si c'est un clique gauche
                fade_in(game.fade)
                pygame.time.delay(1000)
                zoom(game.vermeer_zoom)
                fade_out(game.fade)
                pygame.event.clear()

            elif IsClicked(event, game.vangogh): #Vérifie si on clique sur "La nuit étoilée" et si c'est un clique gauche
                fade_in(game.fade)
                pygame.time.delay(1000)
                zoom(game.vangogh_zoom)
                fade_out(game.fade)
                pygame.event.clear()

            
            elif IsClicked(event, game.cri): #Vérifie si on clique sur "le cri" et si c'est un clique gauche
                fade_in(game.fade)
                pygame.time.delay(1000)
                zoom(game.cri_zoom)
                fade_out(game.fade)
                pygame.event.clear()
                
            elif IsClicked(event, game.picasso): #Vérifie si on clique sur la "Guernica" et si c'est un clique gauche
                fade_in(game.fade)
                pygame.time.delay(1000)
                zoom(game.picasso_zoom)
                fade_out(game.fade)
                pygame.event.clear()
                
            elif IsClicked(event, game.monet): #Vérifie si on clique sur "Impression soleil levant" et si c'est un clique gauche
                fade_in(game.fade)
                pygame.time.delay(1000)
                zoom(game.monet_zoom)
                fade_out(game.fade)
                pygame.event.clear()
                
            elif IsClicked(event, game.matisse): #Vérifie si on clique sur "La Tristesse du roi" et si c'est un clique gauche
                fade_in(game.fade)
                pygame.time.delay(1000)
                zoom(game.matisse_zoom)
                fade_out(game.fade)
                pygame.event.clear()
                
            elif IsClicked(event, game.table):  #Vérifie si on clique sur la table basse et si c'est un clique gauche
                if anomalyid == 1:
                    game.table.image = pygame.image.load("../data/Tableau/table_basse_ouverte_anomaly.png")
                else:
                    game.table.image = pygame.image.load("../data/Tableau/table_basse_ouverte.png")


