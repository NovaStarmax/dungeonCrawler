import random
import time

from entities import Player, Monster, Weapon, generateItem, generateWeapon
from combat import fight, UseItem

def main_menu():
    print("Bienvenue dans le Dungeon Crawler !")
    print("1. Commencer la partie")
    print("2. Quitter")
    choix = input("Entrez votre choix : ")
    if choix == "1":
        start_game()
    elif choix == "2":
        exit()
    else:
        print("Choix invalide")
        main_menu()

MapS = 10

def generateMap(size=None, generate=False):
    # Code pour générer la carte
    global MapS
    if generate:
        MapS = random.randint(10, 30)
    
    carte = []
    for i in range(MapS):
        carte.append(["  "] * MapS)
    carte[1][1] = "🏳️"
    carte[MapS - 2][MapS - 2] = "🏴"
    
    for i in range(MapS):
        for j in range(MapS):
            probabilité = random.randint(0, 100)
            if probabilité < 10 and carte[i][j] == "  ":
                carte[i][j] = "👹"
            elif probabilité > 99:
                carte[i][j] = "📦"
    
    for i in range(MapS):
        if i == 0 or i == MapS - 1:
            carte[i] = ["🧱"] * MapS
        else:
            carte[i][0] = "🧱"
            carte[i][MapS - 1] = "🧱"

    if carte[MapS - 2][MapS - 3] != "  " or carte[MapS - 3][MapS - 2] != "  ":
        carte[MapS - 2][MapS - 3] = "  "
        carte[MapS - 3][MapS - 2] = "  "
    
    if size == "size":
        return MapS
    else:
        return carte

def printMap(carte, mapS):
    # Code pour afficher la carte
    for ligne in carte:
        print("".join(ligne))

roomsCleared = 0
starttime = time.time()

def start_game():
    # Code pour démarrer le jeu
    global starttime, roomsCleared
    starttime = time.time()
    carte = generateMap()
    roomsCleared = 0
    # Instanciation du joueur et des monstres ici
    
    # Logique du jeu ici
    
    while True:
        if Player.health <= 0:
            break
        print(f"Vous avez nettoyé {roomsCleared} salles")
        printMap(carte, MapS)
        # Autre logique du jeu ici

# Continuez avec les autres fonctions et logique du jeu ici...
