import random
import time
from entities import Player, Monster, Weapon, generateItem, generateWeapon
from combat import fight, UseItem
import keyboard
import pygame


# Initialise pygame
pygame.init()

# Chargez la musique de fond
pygame.mixer.music.load("intro.mp3")

# Démarrez la musique en boucle
pygame.mixer.music.play(-1)


def main_menu():
    print("Bienvenue dans le jeu Dungeon Crawler !")
    print("1. Démarrer le jeu")
    print("2. Quitter")
    choice = input("Entrez votre choix : ")
    if choice == "1":
        start_game()
    elif choice == "2":
        exit()
    else:
        print("Choix invalide")
        main_menu()

MapS = 10

def generateMap(size=None, generate=False):
    global MapS
    if generate == True:
        MapS = random.randint(10, 30)
    
    map = []
    for i in range(0, MapS):
        map.append([])
        for j in range(0, MapS):
            map[i].append("  ")
    map[1][1] = "🏳️"
    map[MapS - 2][MapS - 2] = "🏴"

    enemies_count = 0  # Initialize the count of enemies

    while enemies_count < 5:  # Limit the number of enemies to 5
        i = random.randint(0, MapS - 1)
        j = random.randint(0, MapS - 1)
        if map[i][j] == "  ":  # Check if the position is empty
            map[i][j] = "👹"
            enemies_count += 1

    for i in range(0, MapS):
        for j in range(0, MapS):
            if random.randint(0,100) > 99 and map[i][j] == "  ":
                map[i][j] = "📦"
    
    for i in range(0, MapS):
        for j in range(0, MapS):
            if map[i][j] == "  ":
                if random.randint(0, 100) < 10:
                    map[i][j] = "🧱"
                if i == 0 or j == 0 or i == MapS - 1 or j == MapS - 1:
                    map[i][j] = "🧱"
                elif map[i - 1][j] == "🧱" or map[i + 1][j] == "🧱" or map[i][j - 1] == "🧱" or map[i][j + 1] == "🧱":
                    pass

    if map[MapS - 2][MapS - 3] or map[MapS - 3][MapS - 2] != "  ":
        map[MapS - 2][MapS - 3] = "  "
        map[MapS - 3][MapS - 2] = "  "
    if map[1][2] or map[2][1] != "  ":
        map[1][2] = "  "
        map[2][1] = "  "
    for i in range(0, MapS):
        map[0][i] = "🧱"
        map[MapS - 1][i] = "🧱"
        map[i][0] = "🧱"
        map[i][MapS - 1] = "🧱"
    if size == "size":
        return MapS
    else:
        return map


def printMap(map, mapS):
    # Code pour afficher la carte
    for i in range(0, mapS):
        for j in range(0, mapS):
            print(map[i][j], end="")
        print()

roomsCleared = 0
starttime = time.time()
has_key = False


def start_game():
    # Code pour démarrer le jeu
    global starttime
    global roomsCleared
    starttime = time.time()
    map = generateMap()
    roomsCleared = 0
    player = Player(100.0,100.0, Weapon("Sword", 5).getAttack(), 1.0,Weapon("Sword",5))
    player.attack = player.generateRandomAttack()
    
    monster1 = Monster("Goblin 👺", 20.0, 5.0, 20.0)
    monster1.attack = monster1.generateRandomAttack()

    monster2 = Monster("Orc 👿", 30.0, 10.0, 30.0)
    monster2.attack = monster1.generateRandomAttack()

    monster3 = Monster("Troll 🐸", 50.0, 15.0, 50.0)
    monster3.attack = monster1.generateRandomAttack()

    monster4 = Monster("Dragon 🐉", 100.0, 20.0, 100.0)
    monster4.attack = monster1.generateRandomAttack()

    monster5 = Monster("Giant 🧍", 150.0, 25.0, 150.0)
    monster5.attack = monster1.generateRandomAttack()

    monster6 = Monster("Giant Spider 🕷️", 10.0, 2.0, 10.0)
    monster6.attack = monster1.generateRandomAttack()

    monster7 = Monster("Giant Rat 🐀", 5.0, 1.0, 5.0)
    monster7.attack = monster1.generateRandomAttack()

    monster8 = Monster("Giant Snake 🐍", 15.0, 3.0, 15.0)
    monster8.attack = monster1.generateRandomAttack()

    monster9 = Monster("Giant Scorpion 🦂", 25.0, 4.0, 25.0)
    monster9.attack = monster1.generateRandomAttack()

    monster10 = Monster("Giant Ant 🐜", 10.0, 2.0, 10.0)
    monster10.attack = monster1.generateRandomAttack()

    monster11 = Monster("Giant Bee 🐝", 10.0, 2.0, 10.0)
    monster11.attack = monster1.generateRandomAttack()

    monster12 = Monster("Giant Bat 🦇", 10.0, 2.0, 10.0)
    monster12.attack = monster1.generateRandomAttack()

    monster13 = Monster("Giant Wolf 🐺", 20.0, 5.0, 20.0)
    monster13.attack = monster1.generateRandomAttack()

    monster14 = Monster("Giant Bear 🐻", 30.0, 10.0, 30.0)
    monster14.attack = monster1.generateRandomAttack()

    monster15 = Monster("Giant Lion 🦁", 50.0, 15.0, 50.0)
    monster15.attack = monster1.generateRandomAttack()

    monster16 = Monster("Giant Tiger 🐅", 50.0, 15.0, 50.0)
    monster16.attack = monster1.generateRandomAttack()

    monster17 = Monster("Giant Elephant 🐘", 100.0, 20.0, 100.0)
    monster17.attack = monster1.generateRandomAttack()

    monster18 = Monster("Gryphon 🦅", 120.0, 20.0, 120.0)
    monster18.attack = monster1.generateRandomAttack()

    monster19 = Monster("Hydra 🐉", 150.0, 25.0, 150.0)
    monster19.attack = monster1.generateRandomAttack()

    monster20 = Monster("Minotaur 🐂", 80.0, 30.0, 80.0)
    monster20.attack = monster1.generateRandomAttack()

    monster21 = Monster("Cyclops 👁️", 100.0, 30.0, 100.0)
    monster21.attack = monster1.generateRandomAttack()

    monster22 = Monster("Golem 🗿", 150.0, 30.0, 150.0)
    monster22.attack = monster1.generateRandomAttack()

    monster23 = Monster("Skeleton 💀", 20.0, 5.0, 20.0)
    monster23.attack = monster1.generateRandomAttack()

    monster24 = Monster("Zombie 🧟", 30.0, 10.0, 30.0)
    monster24.attack = monster1.generateRandomAttack()

    monster25 = Monster("Vampire 🧛", 30.0, 15.0, 30.0)
    monster25.attack = monster1.generateRandomAttack()

    monster26 = Monster("Werewolf 🐺", 50.0, 20.0, 50.0)
    monster26.attack = monster1.generateRandomAttack()

    monster27 = Monster("Wraith 👻", 10.0, 15.0, 10.0)
    monster27.attack = monster1.generateRandomAttack()

    monster28 = Monster("Ghost 👻", 20.0, 10.0, 20.0)
    monster28.attack = monster1.generateRandomAttack()


    playerX, playerY = [1, 1]
    monsters = [monster1, monster2, monster3, monster4, monster5, monster6, monster7, monster8, monster9, monster10, monster11, monster12, monster13, monster14, monster15, monster16, monster17, monster18, monster19, monster20, monster21, monster22, monster23, monster24, monster25, monster26, monster27, monster28]
    while True:
        if player.health <= 0:
            break
        print("Salles nettoyées : " + str(roomsCleared))
        size = generateMap("size")
        printMap(map, size)
        print("1. Se déplacer")
        print("2. Quitter")
        print("3. Statistiques du joueur")
        print("4. Tutoriel")
        
        choice = input("Entrez votre choix : ")
        if choice == "1":
            while True:
                print("\n"*50)
                if player.health <= 0:
                    break
                print("Salles nettoyées : " + str(roomsCleared))
                size = generateMap("size")
                printMap(map, size)
                print("Déplacez-vous avec les touches zqsd")
                pressed = ("Appuyez sur z/q/s/d pour vous déplacer")
                pressed = keyboard.read_key()
                time.sleep(0.2)

                if pressed == "z":
                    if map[playerX - 1][playerY] == "🧱":
                        print("Vous ne pouvez pas aller par là")
                    elif map[playerX - 1][playerY] == "👹":
                        monster = monsters[random.randint(0, len(monsters) - 1)]
                        fight(player, monster)
                        map[playerX][playerY] = "  "
                        playerX -= 1
                        map[playerX][playerY] = "🧑"
                        has_key = True
                    elif map[playerX - 1][playerY] == "🏴":
                        if has_key:
                            print("\n"*30)
                            print("NOUVELLE SALLE")
                            roomsCleared += 1
                            map = generateMap(None,True)
                            playerX, playerY = [1,1]
                            map[playerX][playerY] = "🧑"
                        else:
                            print("Vous avez besoin d'une clé pour ouvrir cette porte.")
                    elif map[playerX - 1][playerY] == "📦":
                        itemOrWeapon = random.randint(1,100)
                        if itemOrWeapon <=75:
                            item = generateItem()
                            print("Vous avez trouvé un " + item.getName())
                            print("1. Utiliser")
                            print("2. Laisser")
                            choice = input("Entrez votre choix : ")
                            if choice == "1":
                                UseItem(player, item)
                            elif choice == "2":
                                pass
                            else:
                                print("Choix invalide")
                        else:
                            print("Vous avez trouvé une arme")
                            currentAtc = player.getAttack()
                            weapon = generateWeapon()
                            print("Vous avez trouvé une " + weapon.getName())
                            print("Cette arme inflige " + str(weapon.getAttack()) + " de dégâts")
                            if weapon.getAttack() > player.weapon.getAttack():
                                print("Vous avez équipé la " + weapon.getName())
                                player.attack -= currentAtc
                                player.attack += weapon.getAttack()
                                player.weapon = weapon
                                time.sleep(1)
                            else:
                                print("Vous n'avez pas équipé la " + weapon.getName())
                        map[playerX][playerY] = "  "
                        playerX -= 1
                        map[playerX][playerY] = "🧑"
                    else:
                        map[playerX][playerY] = "  "
                        playerX -= 1
                        map[playerX][playerY] = "🧑"




                elif pressed == "d":
                    if map[playerX][playerY + 1] == "🧱":
                        print("Vous ne pouvez pas aller par là")
                    elif map[playerX][playerY + 1] == "👹":
                        monster = monsters[random.randint(0, len(monsters) - 1)]
                        fight(player, monster)
                        map[playerX][playerY] = "  "
                        playerY += 1
                        map[playerX][playerY] = "🧑"
                        has_key = True
                    elif map[playerX][playerY + 1] == "🏴":
                        if has_key:
                            print("\n"*30)
                            print("NOUVELLE SALLE")
                            roomsCleared += 1
                            map = generateMap(None,True)
                            playerX, playerY = [1,1]
                            map[playerX][playerY] = "🧑"
                        else:
                            print("Vous avez besoin d'une clé pour ouvrir cette porte.")
                    elif map[playerX][playerY + 1] == "📦":
                        itemOrWeapon = random.randint(1,100)
                        if itemOrWeapon <=75:
                            item = generateItem()
                            print("Vous avez trouvé un " + item.getName())
                            print("1. Utiliser")
                            print("2. Laisser")
                            choice = input("Entrez votre choix : ")
                            if choice == "1":
                                UseItem(player, item)
                            elif choice == "2":
                                pass
                            else:
                                print("Choix invalide")
                        else:
                            print("Vous avez trouvé une arme")
                            currentAtc = player.getAttack()
                            weapon = generateWeapon()
                            print("Vous avez trouvé une " + weapon.getName())
                            print("Cette arme inflige " + str(weapon.getAttack()) + " de dégâts")
                            if weapon.getAttack() > player.weapon.getAttack():
                                print("Vous avez équipé la " + weapon.getName())
                                player.attack -= currentAtc
                                player.attack += weapon.getAttack()
                                player.weapon = weapon
                                time.sleep(1)
                            else:
                                print("Vous n'avez pas équipé la " + weapon.getName())
                        map[playerX][playerY] = "  "
                        playerY += 1
                        map[playerX][playerY] = "🧑"
                    else:
                        map[playerX][playerY] = "  "
                        playerY += 1
                        map[playerX][playerY] = "🧑"

                elif pressed == "q":
                    if map[playerX][playerY - 1] == "🧱":
                        print("Vous ne pouvez pas aller par là")
                    elif map[playerX][playerY - 1] == "👹":
                        monster = monsters[random.randint(0, len(monsters) - 1)]
                        fight(player, monster)
                        map[playerX][playerY] = "  "
                        playerY -= 1
                        map[playerX][playerY] = "🧑"
                        has_key = True
                    elif map[playerX][playerY - 1] == "🏴":
                        if has_key:
                            print("\n"*30)
                            print("NOUVELLE SALLE")
                            roomsCleared += 1
                            map = generateMap(None,True)
                            playerX, playerY = [1,1]
                            map[playerX][playerY] = "🧑"
                        else:
                            print("Vous avez besoin d'une clé pour ouvrir cette porte.")
                    elif map[playerX][playerY - 1] == "📦":
                        itemOrWeapon = random.randint(1,100)
                        if itemOrWeapon <=75:
                            item = generateItem()
                            print("Vous avez trouvé un " + item.getName())
                            print("1. Utiliser")
                            print("2. Laisser")
                            choice = input("Entrez votre choix : ")
                            if choice == "1":
                                UseItem(player, item)
                            elif choice == "2":
                                pass
                            else:
                                print("Choix invalide")
                        else:
                            print("Vous avez trouvé une arme")
                            currentAtc = player.getAttack()
                            weapon = generateWeapon()
                            print("Vous avez trouvé une " + weapon.getName())
                            print("Cette arme inflige " + str(weapon.getAttack()) + " de dégâts")
                            if weapon.getAttack() > player.weapon.getAttack():
                                print("Vous avez équipé la " + weapon.getName())
                                player.attack -= currentAtc
                                player.attack += weapon.getAttack()
                                player.weapon = weapon
                                time.sleep(1)
                            else:
                                print("Vous n'avez pas équipé la " + weapon.getName())
                        map[playerX][playerY] = "  "
                        playerY -= 1
                        map[playerX][playerY] = "🧑"
                    else:
                        map[playerX][playerY] = "  "
                        playerY -= 1
                        map[playerX][playerY] = "🧑"


                elif pressed == "s":
                    if map[playerX + 1][playerY] == "🧱":
                        print("Vous ne pouvez pas aller par là")
                    elif map[playerX + 1][playerY] == "👹":
                        monster = monsters[random.randint(0, len(monsters) - 1)]
                        fight(player, monster)
                        map[playerX][playerY] = "  "
                        playerX += 1
                        map[playerX][playerY] = "🧑"
                        has_key = True
                    elif map[playerX + 1][playerY] == "🏴":
                        if has_key:
                            print("\n"*30)
                            print("NOUVELLE SALLE")
                            roomsCleared += 1
                            map = generateMap(None,True)
                            playerX, playerY = [1,1]
                            map[playerX][playerY] = "🧑"
                        else:
                            print("Vous avez besoin d'une clé pour ouvrir cette porte.")
                    elif map[playerX + 1][playerY] == "📦":
                        itemOrWeapon = random.randint(1,100)
                        if itemOrWeapon <=75:
                            item = generateItem()
                            print("Vous avez trouvé un " + item.getName())
                            print("1. Utiliser")
                            print("2. Laisser")
                            choice = input("Entrez votre choix : ")
                            if choice == "1":
                                UseItem(player, item)
                            elif choice == "2":
                                pass
                            else:
                                print("Choix invalide")
                        else:
                            print("Vous avez trouvé une arme")
                            currentAtc = player.getAttack()
                            weapon = generateWeapon()
                            print("Vous avez trouvé une " + weapon.getName())
                            print("Cette arme inflige " + str(weapon.getAttack()) + " de dégâts")
                            if weapon.getAttack() > player.weapon.getAttack():
                                print("Vous avez équipé la " + weapon.getName())
                                player.attack -= currentAtc
                                player.attack += weapon.getAttack()
                                player.weapon = weapon
                                time.sleep(1)
                            else:
                                print("Vous n'avez pas équipé la " + weapon.getName())
                        map[playerX][playerY] = "  "
                        playerX += 1
                        map[playerX][playerY] = "🧑"
                    else:
                        map[playerX][playerY] = "  "
                        playerX += 1
                        map[playerX][playerY] = "🧑"

            
        elif choice == "2":
            exit()
        elif choice == "3":
            print("Attaque : " + str(player.getAttack()))
            print("Santé : {}/{}".format(player.getHealth(), player.getMaxHealth()))
        elif choice == "4":
            print("'🧱' sont des murs que vous ne pouvez pas traverser.")
            print("'👹' sont des monstres contre lesquels vous pouvez vous battre.")
            print("'🏴' sont les sorties menant à la pièce suivante.")
            print("'📦' sont des objets que vous pouvez utiliser. Notez que vous ne pouvez pas utiliser d'objets pendant les combats, seulement lorsque vous les trouvez.")
            print("'🧑' représente votre personnage.")
        else:
            print("Choix invalide")
        

while True:
    print("Vous avez nettoyé " + str(roomsCleared) + " pièces")
    totaltime = round((time.time() - starttime), 2)
    print("Vous avez survécu pendant " + str(totaltime) + " secondes")
    main_menu()
    pygame.mixer.music.stop()

    
