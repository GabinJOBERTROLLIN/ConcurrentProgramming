#---------------------------------------------------------
# Créateur : CHRONOWSKI Amaury / JOBERT--ROLLIN Gabin
# Crée le : 10/06/2022
# Programme : Calcul de Pi grâce à la méthode de monte-Carlo
#---------------------------------------------------------

# Bibliothèques classiques
import random,multiprocessing, time



# Création de la variable partagé et du verrou
mutex=multiprocessing.Lock()
nb_hits_multi=multiprocessing.Value('i',0)

 
def frequence_de_hits_pour_n_essais_multi(nb_iteration):
# Calcul Multi−Processus
# Calculer le nbr de hits dans un cercle unitaire 
    count=0
    for i in range(nb_iteration):
        x = random.random()
        y = random.random()
        # si le point est dans l’unit circle
        if x * x + y * y <= 1:
            count+=1 
    mutex.acquire()
    nb_hits_multi.value+=count
    mutex.release()


def frequence_de_hits_pour_n_essais(nb_iteration):    
# Calcul Mono−Processus 
# Calculer le nbr de hits dans un cercle unitaire
    count = 0
    for i in range(nb_iteration):
        x = random.random()
        y = random.random()
        # si le point est dans l’unit circle
        if x * x + y * y <= 1: count += 1
    return count



def run(n,nb_process):
# Programme principal, permetant de calculer PI avec la méthode Monte-Carlo
# En entré : n, le nombre de points à générer
#          : nb_process, le nombre de process sur lequels diviser le calcul
  
    N=n
    nb_proce=nb_process
    print("\nOn fait "+str(N)+" itérations")
    
    
#Multi-Processus
    t0_multi=time.time()
    with multiprocessing.Pool(nb_proce) as p:       #Création et lancemant des N Ptocessus
        p.map(frequence_de_hits_pour_n_essais_multi,[int(N/nb_proce)]*nb_proce)
    t1_multi=time.time()

    mutex.acquire()
    # Affichage des résultats Multi-Processus
    print("\nPour "+str(nb_proce)+" processus")
    print("Valeur estimée Pi par la méthode Multi−Processus : ",  4*nb_hits_multi.value / N)
    print("Le temps du multi-processus est",t1_multi-t0_multi)
    mutex.release()


#Mono-Processus
    t0_mono=time.time()
    nb_hits_mono=frequence_de_hits_pour_n_essais(N)
    t1_mono=time.time()

    # Affichage des résultats Mono-Processus
    print("\nPour le mono-processus")
    print("Valeur estimée Pi par la méthode Mono−Processus : ", 4 * nb_hits_mono / N)
    print("Le temps du mono-processus est",t1_mono-t0_mono)

# Main qui permet de lancer directement le programme 
if __name__=='__main__':
    #variables Monte Carlo calcul de Pi
    NOMBRE_POINTS=1000000
    NBR_PROCESS=4
    run(NOMBRE_POINTS,NBR_PROCESS)

