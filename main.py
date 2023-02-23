#---------------------------------------------------------
# Créateur : CHRONOWSKI Amaury / JOBERT--ROLLIN Gabin
# Crée le : 10/06/2022
# Programme : Programme principal appelant les différents sous-programmes permettant de réaliser les exercices décrit dans la doc
#---------------------------------------------------------

if __name__== '__main__':


    # bibliothèques personelles
    
    import courseHippiqueBasique
    import calculMonteCarloPi
    import gameOfLife
    import gestionnaireDeBille
    import temperatureEtPression

#CHOIX DU PROGRAMME A LANCER
#   ALL = Tous
#   1   = Course Hippique
#   2   = Calcul de Pi par Monte-Carlo
#   3   = Gestionnaire de billes
#   4   = Jeu de la vie
#   5   = controle de température

    #programme principal
    LAUNCHER="3"


    #variables gameOfLife 
    TAILLE_GRILLE=20
    NBR_CYCLE=10
    DUREE_CYCLE=1

    #variables course hippique
    NBR_PROCESSH=2
    LONGEUR_COURSE=100

    #variables Monte Carlo calcul de Pi
    NOMBRE_POINTS=1000000
    NBR_PROCESS=4

    if LAUNCHER == "ALL":
        gameOfLife.run(TAILLE_GRILLE,NBR_CYCLE, DUREE_CYCLE)
        input("entrer une touche pour avancer au prochain programme")
        calculMonteCarloPi.run(NOMBRE_POINTS,NBR_PROCESS)
        input("entrer une touche pour avancer au prochain programme")
        courseHippiqueBasique.run(NBR_PROCESSH, LONGEUR_COURSE)
        input("entrer une touche pour avancer au prochain programme")
        gestionnaireDeBille.run()
        input("entrer une touche pour avancer au prochain programme")
        temperatureEtPression.run()

    elif LAUNCHER == "1":
        courseHippiqueBasique.run(NBR_PROCESSH, LONGEUR_COURSE)

    elif LAUNCHER == "2":
        calculMonteCarloPi.run(NOMBRE_POINTS,NBR_PROCESS)

    elif LAUNCHER == "3":
        gestionnaireDeBille.run()

    elif LAUNCHER == "4":
        gameOfLife.run(TAILLE_GRILLE,NBR_CYCLE,DUREE_CYCLE)

    elif LAUNCHER== "5":
        temperatureEtPression.run()
    
