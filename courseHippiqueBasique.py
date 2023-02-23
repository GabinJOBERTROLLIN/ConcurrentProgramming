#---------------------------------------------------------
# Créateur : CHRONOWSKI Amaury / JOBERT--ROLLIN Gabin
# Crée le : 10/06/2022
# Programme : Control de la température et de la pression via un système multiprocessing
#---------------------------------------------------------

# Bibliothèques classiques
import multiprocessing as mp
import os, time,math, random, sys, ctypes, signal

# Bibliothèques personelles
from affichage import *


# initialisation variables
mutex=mp.Lock()
NBR_PROCESS=5
LONGEUR_COURSE = 100 
lyst_colors=[CL_WHITE, CL_RED, CL_GREEN, CL_BROWN , CL_BLUE, CL_MAGENTA, CL_CYAN, CL_GRAY, CL_DARKGRAY, CL_LIGHTRED, CL_LIGHTGREEN,  CL_LIGHTBLU, CL_YELLOW, CL_LIGHTMAGENTA, CL_LIGHTCYAN]
mes_process = [0 for i in range(NBR_PROCESS)]
global winner



def affichageNyan(mes_lignes, mon_num, col):
# Affichage d'un Cheval Nyan-cat sur 4 lignes 
# en entré : mes_lignes, tableau de 4 numéro de lignes où afficher le cheval Nyan-cat
#          : mon_num, numéro du participant
#          : col, distance par rapport au début

    mutex.acquire()
    move_to(mes_lignes[0]+1,col)         # pour effacer toute ma ligne
    erase_line_from_beg_to_curs()
    en_couleur(lyst_colors[mon_num %len(lyst_colors)])
    print('•.,¸,.•*`•.,¸¸,.•*¯╭━━━━╮')
    move_to(mes_lignes[1]+1,col)         # pour effacer toute ma ligne
    erase_line_from_beg_to_curs()
    en_couleur(lyst_colors[mon_num %len(lyst_colors)])
    print('•.,¸,.•*¯`•.,¸,.•*.|:::::/\__/\ ')
    move_to(mes_lignes[2]+1,col)         # pour effacer toute ma ligne
    erase_line_from_beg_to_curs()
    en_couleur(lyst_colors[mon_num %len(lyst_colors)])
    print("•.,¸,.•*¯`•.,¸,.•*<|::::(｡● ω● )")
    move_to(mes_lignes[3]+1,col)         # pour effacer toute ma ligne
    erase_line_from_beg_to_curs()
    en_couleur(lyst_colors[mon_num %len(lyst_colors)])
    mutex.release()
    print('•.,¸,.•¯•.,¸,.•╰ * し---し- Ｊ')



def un_cheval(mon_num : int, keep_running,list_col) : # ma_ligne commence à 0
# création d'un cheval, prends en entré son numéro ainsi que le tableau "list_col" qui est partagé
    
    col=1
    if mon_num ==0:
        mes_lignes=[1,2,3,4]
    else:
        mes_lignes=[mon_num*4+i for i in range(1,5)]

    while col < LONGEUR_COURSE and keep_running.value : 
        affichageNyan(mes_lignes,mon_num,col)
        col+=1

        list_col[mon_num ]=col
        try : # En cas d'interruption
            time.sleep(0.1 * random.randint(1,5))
        finally : 
            pass



def prise_en_compte_signaux(signum, frame) :
# Sous programme appelé en cas de CTRL+C

    move_to(NBR_PROCESS*4+11, 1)
    print(f"Il y a eu interruption No {signum} au clavier ..., on finit proprement")
    
    for i in range(NBR_PROCESS): 
        mes_process[i].terminate() 
    
    move_to(NBR_PROCESS*4+12, 1)
    curseur_visible()
    en_couleur(CL_WHITE)
    print("Fini")
    sys.exit(0)



def def_arbitre(liste,PREDICTION):
# création d'un arbitre qui affiche à tout moment le premier et dernier cheval
# à la fin affiche également si le joueur a gagné son pari
# En Entré : une liste contenant la distance parcourue par chaque cheval

    global winner
    winner=""
    longder=0
    while longder < LONGEUR_COURSE:
        col=liste[:]
        maxi=max(col)
        mini=min(col)
        top1=col.index(maxi)
        top20=col.index(mini)
        move_to(NBR_PROCESS*4+5,1)
        erase_line_from_beg_to_curs()
        print(chr(ord('A')+top1), "est premier")
        print(chr(ord('A')+top20), "est dernier")
        longder=mini
        if maxi==100 and winner=="":
            winner=chr(ord('A')+top1)

        try : 
            time.sleep(0.1 )
        finally : 
            pass

    # Affiche en fonction de notre prédiction
    if PREDICTION!=winner:
        move_to(NBR_PROCESS*4+12, 1)
        curseur_visible()
        print("Tu as perdu le gagnant etait",winner)
    else:
        move_to(NBR_PROCESS*4+12, 1)
        curseur_visible()        
        print("Tu as gagné le gagnant etait",winner)




def run(nb_process,longueur):
# programme principal

    NBR_PROCESS=nb_process
    LONGEUR_COURSE=longueur

    list_lettre=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    list_col=mp.Array('i',[0]*NBR_PROCESS)
    # On rentre notre prediction
    prediction=str(input("\nVeuillez rentrer votre prédiction (de "+list_lettre[0]+" à "+list_lettre[NBR_PROCESS-1]+") : \n"))
    prediction=prediction.upper()
    # On fait une saisi protegé pour bien rentrer se que l'on veut
    saisi_protegé=True
    while saisi_protegé :
        if prediction in list_lettre[0: NBR_PROCESS]:
            saisi_protegé=False
        else:
            prediction=input("Entrer incorecte. Veuillez rentrer votre prédiction (de "+list_lettre[0]+" à "+list_lettre[NBR_PROCESS-1]+") : \n")
            prediction=prediction.upper()

    
    keep_running=mp.Value(ctypes.c_bool, True)

    
    signal.signal(signal.SIGINT , prise_en_compte_signaux)
    #signal.signal(signal.SIGQUIT , prise_en_compte_signaux)

    effacer_ecran()
    curseur_invisible()

    for i in range(NBR_PROCESS):  # Lancer     Nb_process  processus
        mes_process[i] = mp.Process(target=un_cheval, args= (i,keep_running,list_col,))
        mes_process[i].start()

    arbitre=mp.Process(target=def_arbitre,args=(list_col,prediction,))
    arbitre.start()

    move_to(NBR_PROCESS*4+12, 1)
    print("tous lancés, Controle-C pour tout arrêter")


    # On attend la fin de la course
    for i in range(NBR_PROCESS): mes_process[i].join()
    arbitre.join()


    move_to(NBR_PROCESS*4+14, 1)
    curseur_visible()
    print("Fini")

# Main qui permet de lancer directement le programme 
if __name__=='__main__':
    #variables course hippique
    NBR_PROCESSH=2
    LONGEUR_COURSE=100
    run(NBR_PROCESSH, LONGEUR_COURSE)