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
    # Code de génération de la carte
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

    for i in range(0, MapS):
        for j in range(0, MapS):
            if random.randint(0, 100) < 10 and map[i][j] == "  ":
                map[i][j] = "👹"
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
def start_game():
    # Code pour démarrer le jeu
    global starttime
    global roomsCleared
    starttime = time.time()
    map = generateMap()
    roomsCleared = 0
    player = Player(100.0,100.0, Weapon("Sword", 5).getAttack(), 1.0,Weapon("Sword",5))
    
    monster1 = Monster("Goblin 👺", 20.0, 5.0, 20.0)
    monster2 = Monster("Orc 👿", 30.0, 10.0, 30.0)
    monster3 = Monster("Troll 🐸", 50.0, 15.0, 50.0)
    monster4 = Monster("Dragon 🐉", 100.0, 20.0,   100.0)
    monster5 = Monster("Giant 🧍", 150.0, 25.0, 150.0)
    monster6 = Monster("Giant Spider 🕷️", 10.0, 2.0, 10.0)
    monster7 = Monster("Giant Rat 🐀", 5.0, 1.0, 5.0)
    monster8 = Monster("Giant Snake 🐍", 15.0, 3.0, 15.0)
    monster9 = Monster("Giant Scorpion 🦂", 25.0, 4.0, 25.0)
    monster10 = Monster("Giant Ant 🐜", 10.0, 2.0, 10.0)
    monster11 = Monster("Giant Bee 🐝", 10.0, 2.0, 10.0)
    monster12 = Monster("Giant Bat 🦇", 10.0, 2.0, 10.0)
    monster13 = Monster("Giant Wolf 🐺", 20.0, 5.0, 20.0)
    monster14 = Monster("Giant Bear 🐻", 30.0, 10.0, 30.0)
    monster15 = Monster("Giant Lion 🦁", 50.0, 15.0, 50.0)
    monster16 = Monster("Giant Tiger 🐅", 50.0, 15.0, 50.0)
    monster17 = Monster("Giant Elephant 🐘", 100.0, 20.0, 100.0)
    monster18 = Monster("Gryphon 🦅", 120.0, 20.0, 120.0)
    monster19 = Monster("Hydra 🐉", 150.0, 25.0, 150.0)
    monster20 = Monster("Minotaur 🐂", 80.0, 30.0, 80.0)
    monster21 = Monster("Cyclops 👁️", 100.0, 30.0, 100.0)
    monster22 = Monster("Golem 🗿", 150.0, 30.0, 150.0)
    monster23 = Monster("Skeleton 💀", 20.0, 5.0, 20.0)
    monster24 = Monster("Zombie 🧟", 30.0, 10.0, 30.0)
    monster25 = Monster("Vampire 🧛", 30.0, 15.0, 30.0)
    monster26 = Monster("Werewolf 🐺", 50.0, 20.0, 50.0)
    monster27 = Monster("Wraith 👻", 10.0, 15.0, 10.0)
    monster28 = Monster("Ghost 👻", 20.0, 10.0, 20.0)


    playerX, playerY = [1, 1]
    monsters = [monster1, monster2, monster3, monster4, monster5, monster6, monster7, monster8, monster9, monster10, monster11, monster12, monster13, monster14, monster15, monster16, monster17, monster18, monster19, monster20, monster21, monster22, monster23, monster24, monster25, monster26, monster27, monster28]
    while True:
        if player.health <= 0:
            break
        print("Rooms cleared: " + str(roomsCleared))
        size = generateMap("size")
        printMap(map, size)
        print("1. Move")
        print("2. Quit")
        print("3. Player Stats")
        print("4. Tutorial")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            while True:
                print("\n"*50)
                if player.health <= 0:
                    break
                print("Rooms cleared: " + str(roomsCleared))
                size = generateMap("size")
                printMap(map, size)
                print("Move with wasd")
                pressed = input("Enter z/q/s/d to move")
                if pressed == "q":
                    if map[playerX][playerY - 1] == "🧱":
                        print("You can't go that way")


                    elif map[playerX][playerY - 1] == "👹":
                        monster = random.choice(monsters)
                        fight(player, monster)
                        map[playerX][playerY] = "  "
                        playerY -= 1
                        map[playerX][playerY] = "🧑"


                    elif map[playerX][playerY - 1] == "📦":
                        itemOrWeapon = random.randint(1,100)
                        if itemOrWeapon <=75:
                            item = generateItem()
                            print("You found a " + item.getName())
                            print("1. Use")
                            print("2. Leave")
                            choice = input("Enter your choice: ")
                            if choice == "1":
                                UseItem(player, item)
                            elif choice == "2":
                                pass
                            else:
                                print("Invalid choice")
                        else:
                            print("You found a weapon")
                            currentAtc = player.getAttack()
                            weapon = generateWeapon()
                            print("You found a " + weapon.getName())
                            print("This weapon does " + str(weapon.getAttack()) + " damage")
                            if weapon.getAttack() > player.weapon.getAttack():
                                print("You equiped the " + weapon.getName())
                                player.attack -= currentAtc
                                player.attack += weapon.getAttack()
                                player.weapon = weapon
                                time.sleep(1)
                            else:
                                print("You didn't equip the " + weapon.getName())
                        map[playerX][playerY] = "  "
                        playerY -= 1
                        map[playerX][playerY] = "🧑"
                    
                    elif map[playerX][playerY - 1] == "🏴":
                        print("\n"*30)
                        print("NEW ROOM")
                        roomsCleared += 1
                        map = generateMap(None,True)
                        playerX, playerY = [1,1]
                        map[playerX][playerY] = "🧑"


                    else:
                        map[playerX][playerY] = "  "
                        playerY -= 1
                        map[playerX][playerY] = "🧑"





                elif pressed == "d":
                    if map[playerX][playerY + 1] == "🧱":
                        print("You can't go that way")
                    
                    elif map[playerX][playerY + 1] == "👹":
                        monster = random.choice(monsters)
                        fight(player, monster)
                        map[playerX][playerY] = "  "
                        playerY += 1
                        map[playerX][playerY] = "🧑"


                    elif map[playerX][playerY + 1] == "🏴":
                        print("\n"*30)
                        print("NEW ROOM")
                        roomsCleared += 1
                        map = generateMap(None,True)
                        playerX, playerY = [1,1]
                        map[playerX][playerY] = "🧑"


                    elif map[playerX][playerY + 1] == "📦":
                        itemOrWeapon = random.randint(1,100)
                        if itemOrWeapon <=75:
                            item = generateItem()
                            print("You found a " + item.getName())
                            print("1. Use")
                            print("2. Leave")
                            choice = input("Enter your choice: ")
                            if choice == "1":
                                UseItem(player, item)
                            elif choice == "2":
                                pass
                            else:
                                print("Invalid choice")
                        else:
                            print("You found a weapon")
                            currentAtc = player.getAttack()
                            weapon = generateWeapon()
                            print("You found a " + weapon.getName())
                            print("This weapon does " + str(weapon.getAttack()) + " damage")
                            if weapon.getAttack() > player.weapon.getAttack():
                                print("You equiped the " + weapon.getName())
                                player.attack -= currentAtc
                                player.attack += weapon.getAttack()
                                player.weapon = weapon
                                time.sleep(1)
                            else:
                                print("You didn't equip the " + weapon.getName())
                        map[playerX][playerY] = "  "
                        playerY += 1
                        map[playerX][playerY] = "🧑"


                    else:
                        map[playerX][playerY] = "  "
                        playerY += 1
                        map[playerX][playerY] = "🧑"




                elif pressed == "z":
                    if map[playerX - 1][playerY] == "🧱":
                        print("You can't go that way")
                    
                    elif map[playerX - 1][playerY] == "👹":
                        monster = random.choice(monsters)
                        fight(player, monster)
                        map[playerX][playerY] = "  "
                        playerX -= 1
                        map[playerX][playerY] = "🧑"


                    elif map[playerX-1][playerY] == "🏴":
                        print("\n"*30)
                        print("NEW ROOM")
                        roomsCleared += 1
                        map = generateMap(None,True)
                        playerX, playerY = [1,1]
                        map[playerX][playerY] = "🧑"


                    elif map[playerX-1][playerY] == "📦":
                        itemOrWeapon = random.randint(1,100)
                        if itemOrWeapon <=75:
                            item = generateItem()
                            print("You found a " + item.getName())
                            print("1. Use")
                            print("2. Leave")
                            choice = input("Enter your choice: ")
                            if choice == "1":
                                UseItem(player, item)
                            elif choice == "2":
                                pass
                            else:
                                print("Invalid choice")
                        else:
                            print("You found a weapon")
                            currentAtc = player.getAttack()
                            weapon = generateWeapon()
                            print("You found a " + weapon.getName())
                            print("This weapon does " + str(weapon.getAttack()) + " damage")
                            if weapon.getAttack() > player.weapon.getAttack():
                                print("You equiped the " + weapon.getName())
                                player.attack -= currentAtc
                                player.attack += weapon.getAttack()
                                player.weapon = weapon
                                time.sleep(1)
                            else:
                                print("You didn't equip the " + weapon.getName())
                        map[playerX][playerY] = "  "
                        playerX -= 1
                        map[playerX][playerY] = "🧑"


                    else:
                        map[playerX][playerY] = "  "
                        playerX -= 1
                        map[playerX][playerY] = "🧑"




                elif pressed == "s":
                    if map[playerX + 1][playerY] == "🧱":
                        print("You can't go that way")


                    elif map[playerX + 1][playerY] == "👹":
                        monster = monsters[random.randint(0, len(monsters) - 1)]
                        fight(player, monster)
                        map[playerX][playerY] = "  "
                        playerX += 1
                        map[playerX][playerY] = "🧑"


                    elif map[playerX+1][playerY] == "🏴":
                        print("\n"*30)
                        print("NEW ROOM")
                        roomsCleared += 1
                        map = generateMap(None,True)
                        playerX, playerY = [1,1]
                        map[playerX][playerY] = "🧑"


                    elif map[playerX+1][playerY] == "📦":
                        itemOrWeapon = random.randint(1,100)
                        if itemOrWeapon <=75:
                            item = generateItem()
                            print("You found a " + item.getName())
                            print("1. Use")
                            print("2. Leave")
                            choice = input("Enter your choice: ")
                            if choice == "1":
                                UseItem(player, item)
                            elif choice == "2":
                                pass
                            else:
                                print("Invalid choice")
                        else:
                            print("You found a weapon")
                            currentAtc = player.getAttack()
                            weapon = generateWeapon()
                            print("You found a " + weapon.getName())
                            print("This weapon does " + str(weapon.getAttack()) + " damage")
                            if weapon.getAttack() > player.weapon.getAttack():
                                print("You equiped the " + weapon.getName())
                                player.attack -= currentAtc
                                player.attack += weapon.getAttack()
                                player.weapon = weapon
                                time.sleep(1)
                            else:
                                print("You didn't equip the " + weapon.getName())
                        map[playerX][playerY] = "  "
                        playerX += 1
                        map[playerX][playerY] = "🧑"

                    else:
                        map[playerX][playerY] = "  "
                        playerX += 1
                        map[playerX][playerY] = "🧑"
                elif pressed == "esc":
                    break


                else:
                    print("Invalid choice")
            
        elif choice == "2":
            exit()
        elif choice == "3":
            print("Attack: " + str(player.getAttack()))
            print("Health: {}/{}".format(player.getHealth(), player.getMaxHealth()))
        elif choice == "4":
            print("'🧱' are walls that you can't go through.")
            print("'👹' are monsters that you can fight.")
            print("'🏴' are exits that lead to the next room.")
            print("'📦' are items that you can use, Be aware you cant use items during fights only when found.")
            print("'🧑' is you.")
        else:
            print("Invalid choice")
while True:
    print("You cleared " + str(roomsCleared) + " rooms")
    totaltime = round((time.time() - starttime), 2)
    print("You survived for " + str(totaltime) + " seconds")
    main_menu()
    pygame.mixer.music.stop()
