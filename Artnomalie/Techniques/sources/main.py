import pygame
pygame.init()
from game import Game
import random
from fonctions import*

anomalyluck = 50 #pourcentage d'avoir une anomaly
anomaly = False
anomalyid = 0 #peut etre utile pour coder certaine anomaly, elle contien le numero de l'anomalie precise
score = 0
win = False
game.bestscores = read_csv("../data/hs.csv") #récupère les scores stockés
warningremoval = 0 # le compteur de temps pour le warning
music("../data/music/Bolero.mp3", True) #Lance la musique dans une boucle infinie

loadmap([game.backgroundini,game.fade])
fade_out(game.fade)
pygame.time.delay(3000)
fade_in(game.fade)
pygame.time.delay(1000)
loadmap(menu)
fade_out(game.fade)

while running: #boucle principale (évite que la page se ferme toute seule)
    pygame.time.delay(16) #force le jeu en 60fps

    if game.warning in  game.drawed:
        warningremoval += 16
        if warningremoval >=15000: # pour enlever le warning après 5 secondes
             game.warning.image.set_alpha(0)
        else:
            game.warning.image.set_alpha(255)
    draw() #dessine les objets se trouvant dans draw

    if win == True : #ce qui s'active si on gagne
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

        if event.type == pygame.QUIT: #Si le joueur appuis sur la croix
            lose() #update le score
            running=False
            pygame.quit()
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and  game.background1 in game.drawed: #détecet si on appuis sur échap en pleine game (fonctionne suelement dans la salle principale)
                lose() #update le score
                game.ScoreDisplay.pos = (500,30) #replace le score si nécessaire
                fade_in(game.fade)
                loadmap(menu)
                fade_out(game.fade)
        elif event.type == pygame.MOUSEBUTTONDOWN: #si le joueur clique sur un des bouttons

               #------------------MENU--------------------------------

            if IsClicked(event, game.playButton):      #------Permer de voir si on clique sur le bouton "Play", Clickable == True permet de cliquer 1 seule fois dessus et éviter de cliquer dessus une fois qu'il a disparu
                fade_in(game.fade)
                pygame.time.delay(1000)

                loadmap(mode_menu)
                fade_out(game.fade)
                pygame.event.clear()

            elif IsClicked(event, game.credits):           #--------- Montre les crédits
                 loadmap(menu_credit)                    # Ajoute la crois de retour
                 pygame.event.clear()

            elif IsClicked(event, game.RetourCredits):
                 loadmap(menu)
                 pygame.event.clear()

            elif IsClicked(event, game.scorebutton):
                game.bestscores = read_csv("../data/hs.csv") #lis le fichier contenant les 5 meilleurs score
                game.bestscores = [[int(game.bestscores[0][0]),int(game.bestscores[0][1]),int(game.bestscores[0][2]),int(game.bestscores[0][3]),int(game.bestscores[0][4])]]
                game.bestscores[0].sort(reverse=True)
                game.Top1.text = f"Top 1: {game.bestscores[0][0]}" #update les scores si nécessaire
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
            elif IsClicked(event, game.continuebutton): #bouton continuer
                fade_in(game.fade)
                pygame.time.delay(1000)
                if anomaly == False: #donne un point si il n'y a pas d'anomalie, reset le score si il y en a une
                    game.score += 1
                    if game.score >= 10 and game.mode == "Infinite" :
                        game.ScoreDisplay.pos = (485,30)
                    elif game.score == 10 and game.mode == "Story" : #activer la victoire
                        win = True
                        loadmap([game.fade]) #pour rendre l'écran noir
                        draw()

                else:
                    lose()
                    game.ScoreDisplay.pos = (500,30)
                    if game.mode == "Story":
                        gameover()
                        pass

                if ( not anomaly or game.mode == "Infinite" )and win == False: # pour relancer la salle sauf si on gagne ou on gameover
                    game.ScoreDisplay.text = game.score #change le texte du score
                    anomaly = random.randint(1,100) <= anomalyluck #creer ou nn une anomalie 1/2 chance
                    loadmap(first_room)
                    anomalyid = anomalies(anomaly) # choisi l'anomalie si elle existe et la dessine et dessine tout les elements
                    fade_out(game.fade)
                    pygame.event.clear()

            elif IsClicked(event, game.button_retour): #bouton retour
                fade_in(game.fade) # doit tout le temps être la première ligne
                pygame.time.delay(1000)
                loadmap(first_room) #temporaire, dépend de où nous sommes
                if game.mode == "Story" and game.score == -1 and game.exitbutton in game.drawed:
                    game.drawed.remove(game.exitbutton)
                    game.drawed.insert(-1, game.indicator)
                fade_out(game.fade)
                pygame.event.clear() #doit être la dernière juste après le fade out
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
            elif IsClicked(event, game.exitbutton): #bouton pour reculer si y a une anomalie

                fade_in(game.fade) # doit tout le temps être la première ligne
                pygame.time.delay(1000)
                loadmap(first_room)
                if anomaly == False: #donne un point si y une anomalie, reset le score si il y en a pas
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
                    game.ScoreDisplay.text = game.score #change le texte du score
                    anomaly = random.randint(1,100) <= anomalyluck #creer ou non une anomalie 1/2 chance
                    loadmap(first_room)
                    anomalyid = anomalies(anomaly) #génère l'anomalie
                    fade_out(game.fade)
                    pygame.event.clear() #doit être la dernière juste après le fade out
            elif IsClicked(event, game.rules):
                loadmap(rulesmenu)
               #--------------------------------------------------------
               #MODE MENU
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
                game.drawed.insert(-1, game.warning) # pour mettre le warning en avant dernier
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
                #OTHER

            elif IsClicked(event, game.joconde): #vérifie si on clique sur la joconde et si c'est un clique gauche
                fade_in(game.fade)
                pygame.time.delay(1000)
                zoom(game.joconde_zoom)
                if anomalyid == 2:
                    music("../data/music/creepy_sound.mp3", True)
                fade_out(game.fade)
                pygame.event.clear()

            elif IsClicked(event, game.cri): #vérifie si on clique sur la liberté guidant le peuple et si c'est un clique gauche
                fade_in(game.fade)
                pygame.time.delay(1000)
                zoom(game.cri_zoom)
                fade_out(game.fade)
                pygame.event.clear()

            elif IsClicked(event, game.delacroix): #vérifie si on clique sur la liberté guidant le peuple et si c'est un clique gauche
                fade_in(game.fade)
                pygame.time.delay(1000)
                zoom(game.delacroix_zoom)
                fade_out(game.fade)
                pygame.event.clear()

            elif IsClicked(event, game.vermeer): #vérifie si on clique sur la jaune fille a la perle et si c'est un clique gauche
                fade_in(game.fade)
                pygame.time.delay(1000)
                zoom(game.vermeer_zoom)
                fade_out(game.fade)
                pygame.event.clear()

            elif IsClicked(event, game.vangogh): #vérifie si on clique sur la nuit étoilée et si c'est un clique gauche
                fade_in(game.fade)
                pygame.time.delay(1000)
                zoom(game.vangogh_zoom)
                fade_out(game.fade)
                pygame.event.clear()
            elif IsClicked(event, game.picasso): #vérifie si on clique sur la nuit étoilée et si c'est un clique gauche
                fade_in(game.fade)
                pygame.time.delay(1000)
                zoom(game.picasso_zoom)
                fade_out(game.fade)
                pygame.event.clear()
            elif IsClicked(event, game.monet): #vérifie si on clique sur la nuit étoilée et si c'est un clique gauche
                fade_in(game.fade)
                pygame.time.delay(1000)
                zoom(game.monet_zoom)
                fade_out(game.fade)
                pygame.event.clear()
            elif IsClicked(event, game.matisse): #vérifie si on clique sur la nuit étoilée et si c'est un clique gauche
                fade_in(game.fade)
                pygame.time.delay(1000)
                zoom(game.matisse_zoom)
                fade_out(game.fade)
                pygame.event.clear()

            elif IsClicked(event, game.table):
                if anomalyid == 1:
                    game.table.image = pygame.image.load("../data/Tableau/table_basse_ouverte_anomaly.png")
                else:
                    game.table.image = pygame.image.load("../data/Tableau/table_basse_ouverte.png")


