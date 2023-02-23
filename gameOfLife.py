#---------------------------------------------------------
# Créateur : CHRONOWSKI Amaury / JOBERT--ROLLIN Gabin
# Crée le : 10/06/2022
# Programme : Permet de faire le jeu de la vie avec les règles classiques rappelées dans la doc
#---------------------------------------------------------

# bibliothèques classiques
import multiprocessing as mp
from sqlite3 import TimestampFromTicks
import numpy as np
import os, time,math, random, sys, ctypes, signal

# bibliothèques personelles
from affichage import *


# variables globales
global TAILLE
global TEMPS
global DUREE
TAILLE=20

def initGrid(tab):
# Création de la Matrice de départ (case choisie aléatoirement)
    effacer_ecran()
    for i in range(20):
        for j in range(20):
            move_to(i+1,2*j+1)
            if random.randint(0,1)==0:
                print('□')
                tab[20*i+j]=0
            else:
                print('▣')
                tab[20*i+j]=1

def afficheGrid(tab):
    effacer_ecran()
    for i in range(20):
        for j in range(20):
            move_to(i+1,2*j+1)
            
            if tab[TAILLE*i+j]==0:
                
                print('□')
            else:
                print('▣')
            

def calculNombreVoisin(brouillonTab,i,j):
# calcul du nombre de voisin d'une case de cordonnées (i,j) du tableau brouillonTab

# fonctions utiles
    def dansGrid(x,y) :
    # renvoie un booléen : True si la cellule de coordonées (x,y) est dans le tableau
        return TAILLE>x>=0 and TAILLE>y>=0

    def estEnVie(x,y):
    # renvoie un boolée, : True di la cellule ed coordonée (x,y) est en vie
        return brouillonTab[TAILLE*x+y]==1

# calcul du nombre de voisin
    delta=[(-1,0), (-1, +1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
    nombreVoisin=0
    for (dx,dy) in delta :
        if dansGrid(i+dx, j+dy) and estEnVie(i+dx, j+dy) :
            nombreVoisin +=1
    return nombreVoisin
    


def actualise(tabT,numProcess,Q):
# effectue le résultat d'une génération
    tabTPLUS=tabT[:]
    for i in range((numProcess*TAILLE)//4,((numProcess+1)*TAILLE)//4):
        for j in range(TAILLE):
            nombreVoisin=calculNombreVoisin(tabT,i,j)
            if nombreVoisin < 2:
                tabTPLUS[TAILLE*i+j]=0
            elif nombreVoisin > 3:
                tabTPLUS[TAILLE*i+j]=0
            elif nombreVoisin == 3:
                tabTPLUS[TAILLE*i+j]=1
            else:
                pass
    Q.put((tabTPLUS,numProcess))
    


def decoupe(tabT):
# Crée des processus  et leurs attribuent des parties de la grille à actualiser
    #tabTPLUS1=tabi.copy()
    Q=mp.Queue()
    Lprocess=[]
    ids=[]
    tabTPLUS1=tabT
    for i in range(4):
        p = mp.Process(target=actualise,args=(tabT,i,Q))
        ids.append(p)
        p.start()
    for process in ids:
        Lprocess.append(Q.get())
    for (grid,numProcess) in Lprocess:
        for i in range((numProcess*TAILLE)//4,((numProcess+1)*TAILLE)//4):
            for j in range(TAILLE):
                tabTPLUS1[TAILLE*i+j]=grid[TAILLE*i+j]        
        
    afficheGrid(tabTPLUS1)
    return tabTPLUS1

def arret(s,frame):
# Fonction appelée quand on CTRL+C pour arreter le programme
    sys.exit("  Arret manuel")


def run(taille,temps,duree):
#programme principal
    TAILLE=taille
    TEMPS=temps
    DUREE=duree
    signal.signal(signal.SIGINT,arret)
    tab=[i for i in range(TAILLE*TAILLE)]
    initGrid(tab)
    
    time.sleep(DUREE)
    for i in range(TEMPS):
        
        effacer_ecran()
        tab=decoupe(tab)
        time.sleep(DUREE)
    

if __name__== '__main__':
    TAILLE_GRILLE=20
    NBR_CYCLE=10
    DUREE_CYCLE=1
    run(TAILLE_GRILLE,NBR_CYCLE, DUREE_CYCLE)
    