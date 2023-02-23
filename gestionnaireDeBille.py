#---------------------------------------------------------
# Créateur : CHRONOWSKI Amaury / JOBERT--ROLLIN Gabin
# Crée le : 10/06/2022
# Programme : Control de la température et de la pression via un système multiprocessing
#---------------------------------------------------------

# Bibliothèques classiques
import time,multiprocessing

def travail(bille):
    m=5
    while m>0:
        demandebille(bille)
        time.sleep(1*bille)
        retournebille(bille)
        m-=1
    mutex.acquire()
    Control.value+=1
    mutex.release()
    print("j'avais besoin de "+str(bille)+" billes j'ai finit")



def demandebille(bille):
    mutex.acquire()
    while nb_bille.value<bille:
        print('je suis en attente, je demande '+str(bille)+' billes')
        mutex.release()
        Sem.acquire()
        mutex.acquire()

    print("c'est bon j'ai "+str(bille)+" billes" )
    nb_bille.value-=bille
    mutex.release()
    Sem.release()
    


def retournebille(bille):
        mutex.acquire()
        nb_bille.value+=bille
        print("c'est bon je restitue "+str(bille)+" billes" )
        mutex.release()



def controleur():
#controle et arrète tout si le nombre de bille est inférieur au nommbre maximum de bille
    Test=0
    while Test < 4:
        time.sleep(0.5)
        mutex.acquire()
        print("il y a " + str(nb_bille.value) + " billes")
        mutex.release()
        mutex.acquire()
        Test=Control.value
        mutex.release()
    print("\nTout le monde a finit")
    mutex.acquire()
    if nb_bille.value != 9:
        print("Erreur")
    else:
        print("\nToutes les billes son bien été réstituées")
    mutex.release()


def run():
#Programme principal

    C=multiprocessing.Process(target=controleur,args=())
    P1=multiprocessing.Process(target=travail,args=(5,))
    P2=multiprocessing.Process(target=travail,args=(3,))
    P3=multiprocessing.Process(target=travail,args=(4,))
    P4=multiprocessing.Process(target=travail,args=(2,))
    C.start()
    P1.start()
    P2.start()
    P3.start()
    P4.start()
    C.join()
    P1.join()
    P2.join()
    P3.join()
    P4.join()


# Main qui permet de lancer directement le programme 
if __name__=='__main__':
    # Variables partégées, verrou etc...
    Sem=multiprocessing.Semaphore(0)
    mutex=multiprocessing.Lock()
    nb_bille=multiprocessing.Value('i',9)
    Control=multiprocessing.Value('i',0)

    #variables Gestionnaire de bille
    run()
