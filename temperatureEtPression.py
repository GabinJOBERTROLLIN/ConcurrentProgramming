#---------------------------------------------------------
# Créateur : CHRONOWSKI Amaury / JOBERT--ROLLIN Gabin
# Crée le : 10/06/2022
# Programme : Control de la température et de la pression via un système multiprocessing
#---------------------------------------------------------

# Bibliothèques classiques
import time,multiprocessing,random


# Initialisation du verrou
mutex=multiprocessing.Lock()

# Initialisation des variable partagées
go_pompe=multiprocessing.Value('i',False) # Variable qui met en route/arrête la pompe (True/False)
go_chauffage=multiprocessing.Value('i',False) # Variable qui met en route/arrête le chauffage (True/False)
T=multiprocessing.Value('f',25) # Variable qui stocke la dernière température relevée (Float)
P=multiprocessing.Value('f',1013) # Variable qui stocke la dernière pression relevée (Float)
on=multiprocessing.Value('i',True) # Variable qui indique si les processus s'arrêtent en fonction du controleur (True/False)


def Control(T_ref,P_ref): 
# Programme du controleur, met en route/arrête le chauffage et la pompe en fonction de la température
# et de la pression et arrete tout les processus au bout d'un certain temps en fonction de boucle 
# (le nombre de boucle que fait le programme de controle)
# En entré : T_ref , la température voulue
#          :P_ref, la pression voulue

    boucle=250

    mutex.acquire()
    while on.value:
        mutex.release()
        time.sleep(0.2)
        mutex.acquire()

        if T.value>T_ref: 
            go_chauffage.value=False
            if P.value>P_ref: 
                go_pompe.value=True
            else: 
                go_pompe.value=False


        elif T.value<T_ref: 
            go_chauffage.value=True
            if P.value>P_ref: 
                go_pompe.value=True
            else: 
                go_pompe.value=False


        elif T.value==T_ref: 
            go_chauffage.value=False
            if P.value>P_ref: 
                go_pompe.value=True
            else: 
                go_pompe.value==False


        if boucle==0:
            on.value=False
        else:
            boucle-=1
    mutex.release()




def Chauffer():
# Programme du chauffage, augmente la température quand elle est trop faible
    mutex.acquire()
    while on.value:
        mutex.release()
        time.sleep(0.1)
        mutex.acquire()
        if go_chauffage.value:
            T.value+=0.5
    mutex.release()




def Pomper():
# Programme de la pompe, diminue la pression quand elle est trop faible
    mutex.acquire()
    while on.value:
        mutex.release()
        time.sleep(0.1)
        mutex.acquire()
        if go_pompe.value:
            P.value-=2
    mutex.release()




def Temp():
# Programme qui relève la temprérature, en réalité il simule une diminution aléatoire de température que l'on pourrait relever
    mutex.acquire()
    while on.value:
        mutex.release()
        time.sleep(0.5)
        mutex.acquire()
        T.value-=0.5*random.random()
    mutex.release()




def Pres():
# Programme qui relève la pression, en réalité il simule une augmentation aléatoire de pression que l'on pourrait relever
    mutex.acquire()
    while on.value:
        mutex.release()
        time.sleep(0.5)
        mutex.acquire()
        P.value+=2*random.random()
    mutex.release()


def Screen():
# Programme qui réstitue les données à l'utilisateur, il affiche la température et la pression pour un instant T
    mutex.acquire()
    while on.value:
        mutex.release()
        time.sleep(1)
        mutex.acquire()
        print("La température est de "+str(T.value)+" °C")
        print("La pression est de "+str(P.value)+" pa")




def run():
# Programme principale

    # Saisie de la température et pression voulues
    T_ref=input("Veuiller rentrer la température voulue (superieur ou égale à 25°C) :\n")
    saisi_protegé=True
    
    while saisi_protegé :
        try:
            T_ref=int(T_ref)
        except:
            T_ref=input("Entrer incorecte. Veuiller rentrer la température voulue (superieur ou égale à 25°C) :\n")
        if T_ref>=25:
             saisi_protegé=False
        else:
            T_ref=input("Entrer incorecte. Veuiller rentrer la température voulue (superieur ou égale à 25°C) :\n")
            try:
                T_ref=int(T_ref)
            except:
                T_ref=input("Entrer incorecte. Veuiller rentrer la température voulue (superieur ou égale à 25°C) :\n")

    P_ref=int(input("Veuiller rentrer la pression voulue (inferieur ou égale à 1013 Pa et superieur à 0 Pa) :\n"))

    saisi_protegé=True
    
    while saisi_protegé :
        try:
            P_ref=int(P_ref)
        except:
            P_ref=input("Entrer incorecte. Veuiller rentrer la pression voulue (inferieur ou égale à 1013 Pa et superieur à 0 Pa) :\n")
        if P_ref>0 and P_ref<=1013:
            saisi_protegé=False
        else:
            P_ref=input("Entrer incorecte. Veuiller rentrer la pression voulue (inferieur ou égale à 1013 Pa et superieur à 0 Pa) :\n")
            try:
                P_ref=int(P_ref)
            except:
                P_ref=input("Entrer incorecte. Veuiller rentrer la pression voulue (inferieur ou égale à 1013 Pa et superieur à 0 Pa) :\n")
            

    # Initialisation des processus
    Controleur=multiprocessing.Process(target=Control,args=(T_ref,P_ref,)) # Process pour le controleur qui gère la température et pression (Entrée = T_ref : Température voulue, P_ref : Pression voulue)
    Chauffage=multiprocessing.Process(target=Chauffer,args=()) # Process pour le chauffage
    Pompe=multiprocessing.Process(target=Pomper,args=()) # Process Pour la pompe
    Température=multiprocessing.Process(target=Temp,args=()) # Process qui récupère la température
    Pression=multiprocessing.Process(target=Pres,args=()) # Process  qui récupère la pression
    Ecran=multiprocessing.Process(target=Screen,args=()) # Process qui affiche la température et la pression à un instant T

    # Lancement des processus
    Controleur.start()
    Chauffage.start()
    Pompe.start()
    Température.start()
    Pression.start()
    Ecran.start()

    Controleur.join()
    Chauffage.join()
    Pompe.join()
    Température.join()
    Pression.join()
    Ecran.join()

# Main qui permet de lancer directement le programme 
if __name__=='__main__':
    run()