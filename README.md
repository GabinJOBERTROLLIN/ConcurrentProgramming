# ConcurrentProgramming
exercices to learn concurrent programming



# Concurrent Programming Project

JOBERT--ROLLIN Gabin
CHRONOWSKI Amaury



2022

# Sommaire

[Structure générale 1](#_Toc105857658)

[Composition 1](#_Toc105857659)

[Programme main.py 1](#_Toc105857660)

[Programme Course Hippique 1](#_Toc105857661)

[Programme Calcul de pi par Monte-Carlo 1](#_Toc105857662)

[Programme Gestionnaire de billes 1](#_Toc105857663)

[Programme Contrôleur de température et pression 1](#_Toc105857664)

[Programme Game of Life 1](#_Toc105857665)

[Cahier des charges 1](#_Toc105857666)

[Explication du Programme 2](#_Toc105857667)

# Structure générale

## Composition

Notre fichier est composé de 7 programmes , les 5 programmes pour résoudre les exercices :

- Course Hippique
- Calcul de pi selon la méthode Monte-Carlo
- Gestionnaire de billes
- Programme contrôleur de température et pression
- Game of life

Ainsi que deux autres programmes :

- main.py pour appeler les autres programmes ( on nous a demandé de faire un main.py )
- affichage.py, un sous-programme contenant des fonctions et variables utiles pour de l'affichage dans le terminal

## Programme main.py

Le programme main.py permet de lancer les programmes un par un, ou tous en même temps selon la valeur de la variable Launcher :

| **Valeur de Launcher** | **Programme lancé** |
| --- | --- |
| ALL | Tous |
| 1 | Course Hippique |
| 2 | Calcul de Pi par Monte-Carlo |
| 3 | Gestionnaire de Billes |
| 4 | Jeu de la vie |
| 5 | Contrôle de température |

Certains paramètres des sous-programmes sont définis directement dans main.py.

# Programme Course Hippique

## Cahier des charges du programme de la course hippique

On souhaite modifier un programme fourni pour y ajouter des fonctionnalités :

- Afficher qui et le premier et le dernier tout au long de la course
- Afficher le gagnant de la course
- Pouvoir parier sur l'un des concurrents avant le début de la course
- Modifier l'élément visuel qui représente les participant

## Explication du programme de la course hippique

On crée un processus Arbitre qui va servir à afficher qui est le premier et dernier en récupérant l'information de celui qui se trouve le plus loin et celui qui se trouve le plus proche dans la liste des participant et va garder en mémoire le premier arriver pour l'afficher.

 En lançant le programme, le joueur peut choisir sur quel participant parier, la saisi est protégée et ne permet de rentrer que seulement la lettre des participants : ![](RackMultipart20230223-1-xxenf7_html_790cb876d8985b5d.png)

Pour modifier l'apparence la ligne qui était avant atribué à chaque participant est mainenant ca place et va prendre les lignes de son numéro fois 4 jsuqu'à son numéro fois 4 plus 3 car notre motife fait 4 ligne.

Et on obtien quand le programme est fini le gagnant et on nous indique si on a gagner ou pas :



# Programme Calcul de pi par Monte-Carlo

## Cahier des charges du programme de calcule de pi par Monte-Carlo

On souhaite calculer pi via la méthode de Monte-Carlo via un monoprocessus et un multiprocessus et de comparer les temps entre chaque méthode.

## Explication du programme calcul de pi par Monte-Carlo

On calcule pi via la méthode de Monte-Carlo qui consiste à prendre des points appartenant au cercle unitaire parmi un nombre de point placer aléatoirement dans un carrée de 2 x 2. Dans notre programme, nous avons juste rapporter le cercle unitaire à 4 portions de disque entre 0 et pi/2 pour simplifier la programmation.

Le programme Mono-Processus charge de calculer toutes les itérations tandis que le programme en multiprocessus lui va diviser la tache en 4 et chaque processus va s'occuper d'une des quatre portions.

Et enfin chaque méthode affiche la valeur de pi trouver ainsi que le temps que le programme a demandé.

On obtient ça en sortie du programme :



# Programme Gestionnaire de billes

## Cahier des charges du programme gestionnaire de billes

On souhaite modéliser des travailleurs, par des processus, qui utilise une ressource partager qui sera sous la forme de billes. Cependant chaque travailleur demander une quantité de billes différente pour travailler et ne mette pas tout le même temps pour finir la tâche. Il faut donc gérer l'attente des travailleurs et leur utilisation de la ressource

## Explication du programme gestionnaire de billes

On crée les processus travailleurs qui exécute la fonction travaille avec en entrée le nombre de billes qu'il consomme pour travailler. Chaque travailleur se met en attentes ou en pause selon la disponibilité. Ils vont faire un certain nombre de fois le travail puis s'arrête. On a un dernier processus qui est ici comme contrôleur qui indique le nombre de bille à un instant T. Et il regarde s'il y a bien le bon nombre de billes à la fin de programme.

On obtient ça en lançant le programme (une partie de ce qu'on obtient) :


On obtient ça à la fin :



# Programme Contrôleur de température et pression

## Cahier des charges du programme contrôleur de température et pression

On souhaite réguler la pression et la température d'un endroit en fonction des données entrées et afficher l'évolution de celles-ci sur un écran. Il faut récolter les données des capteurs de pressions et de température pour suivre l'évolution du système et s'adapter en conséquence. Il faut lancer la pompe quand la pression est trop élevée et la couper quand elle est à la bonne valeur ou en-dessous. Et il faut lancer le chauffage quand la température est trop basse et le couper quand elle est à la bonne valeur ou au-dessus.

## Explication du programme contrôleur de température et pression

D'abord, on entre les valeurs de pression et température voulue la température entrée doit être supérieur ou égale à 25 car on ne fait que chauffer et la pression entrée doit être inferieur ou égale à 1013 car on ne fait que pomper (la saisie est protégée).

On crée un processus qui va contrôler la pression et la température, en fonction des donner obtenue par le capteur va enclenche la pompe/chauffage ou l'arrêter. Il va faire un certain nombre de boucle puis va arrêter tous les programmes pour simuler un temps de fonctionnement.

On crée un processus de pompe et de chauffage qui marche de la mem façon quand ils sont autorisés il fonction et modifie la valeur d'un montant fix pour se rapprocher de la valeur voulu (augmentation de la température pour le chauffage et baisse de la pression pour la pompe).

On crée des processus qui vont simuler la captation de la pression et de la température. Etant donner qu'on ne mesure pas de vraie variation on les simule en perturbant aléatoirement les valeur( On baisse la température aléatoirement et on augmente la pression aléatoirement).

Et enfin un processus qui simule un écran et affiche les valeurs de pression et de température a un instant T.



On obtient ça en lançant le programme :

Au début : Quand on atteint les valeur voulue :


# Programme Game of Life

## Cahier des charges du programme jeu de la vie

Le jeu de la vie est un automate cellulaire les règles classiques ont été appliquées. C'est-à-dire que le jeu se déroule par étape et toutes les cases sont changées en même temps en fonction de l'état des cellules voisines à l'étape précédente :





## Explication du programme jeu de la vie

**Etape 1 :** Initialisation de la grille

**Etape 2 :** Attribution à des process différentes parti de la grille grâce à decoupe(tab)

**Etape 3 :** Chaque process utilise la fonction actualise(tabT, tabTPLUS1, numprocess) sur des parties différentes de la grille. Où « tabT » est la grille à l'instant « t » et « tabTPLUS1 » la copie de tabT. Grâce à cela chaque process regarde pour chaque cellule qui lui est attribué son voisinage à l'instant « T » dans « TabT » et détermine donc son résultat à l'instant T+1 dans « tabTPLUS1 ». Vu que les process ne changent pas « tabT » , et qu'ils ne s'occupent pas des mêmes cases de la grille dans « tabTPLUS1 » il n'est pas nécessaire d'utiliser de sémaphore, ou de demander des autorisations pour écrire dans « tabTPLUS1 ».

**Etape 4 :** Quand tous les Process ont fini de calculer, on peut faire tabT=tabTPLUS1 et afficher ce tableau. On recommence ensuite à l'étape 3 autant de cycle que l'on a choisi en entré.

**Conclusion :** faire une copie du tableau permet de suivre le cahier des charges du jeu de la vie classique et simplifie significativement l'implémentation d'une version multiprocessus de ce jeu



Grille à l'instant t

Grille à l'instant t+1
