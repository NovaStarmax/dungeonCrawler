import random
import time
import os
import sys
import keyboard

def main_menu():
    print("Welcome to the Dungeon Crawler!")
    print("1. Start Game")
    print("2. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        start_game()
    elif choice == "2":
        exit()
    else:
        print("Invalid choice")
        main_menu()

MapS = 10

def generateMap(size=None,generate=False):
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


class Weapon:
    def __init__(self, name, attack, enchant = None):
        self.name = name
        self.attack = attack
        self.enchant = enchant

    def getAttack(self):
        return self.attack

    def getName(self):
        return self.name
    
    def getEnchant(self):
        return self.enchant

    
def Enchants(weapon,monster,player):
    if weapon.enchant == "Sharpness":
        weapon.attack += 2
    elif weapon.enchant == "Fire":
        print("Your fire enchanted weapon burns the {}! It dealt 2 damage".format(monster.name))
        monster.health -= 2
    elif weapon.enchant == "Defensive Light":
        player.defense += 2
    elif weapon.enchant == "Lightning":
        print("The {} was struck by lightning! It dealt 10 damage".format(monster.name))
        monster.health -= 10
        
def UndoEnchants(weapon,player):
    if weapon.enchant == "Sharpness":
        weapon.attack -= 2
    elif weapon.enchant == "Defensive Light":
        player.defense -= 2

def generateWeapon():
    weapon = random.randint(0, 1000)
    enchant = random.randint(0, 1000)
    if enchant > 990:
        weaponEnchant = True
    else:
        weaponEnchant = False
    
    if weaponEnchant == True:
        enchant = random.randint(0, 1000)
        if enchant <= 500:
            wEnchant = "Sharpness"
        elif enchant <= 750:
            wEnchant = "Fire"
        elif enchant <= 900:
            wEnchant = "Defensive Light"
        elif enchant <= 1000:
            wEnchant = "Lightning"

    if weapon < 100:
        if weaponEnchant == True:
            return Weapon("Sword of " + wEnchant, 5, wEnchant)
        else:
            return Weapon("Sword", 5)
    elif weapon < 200:
        if weaponEnchant == True:
            return Weapon("Axe of " + wEnchant, 7, wEnchant)
        else:
            return Weapon("Axe", 7)
    elif weapon < 300:
        if weaponEnchant == True:
            return Weapon("Mace of " + wEnchant, 6, wEnchant)
        else:
            return Weapon("Mace", 6)
    elif weapon < 400:
        if weaponEnchant == True:
            return Weapon("Dagger of " + wEnchant, 5, wEnchant)
        else:
            return Weapon("Dagger", 5)
    elif weapon < 500:
        if weaponEnchant == True:
            return Weapon("Bow of " + wEnchant, 13, wEnchant)
        else:
            return Weapon("Bow", 13)
    elif weapon < 550:
        if weaponEnchant == True:
            return Weapon("Staff of " + wEnchant, 10, wEnchant)
        else:
            return Weapon("Staff", 10)
    elif weapon < 600:
        if weaponEnchant == True:
            return Weapon("Club of " + wEnchant, 3, wEnchant)
        else:
            return Weapon("Club", 3)   
    elif weapon < 700:
        if weaponEnchant == True:
            return Weapon("Spear of " + wEnchant, 11, wEnchant)
        else:
            return Weapon("Spear", 11)
    elif weapon < 800:
        if weaponEnchant == True:
            return Weapon("Longsword of " + wEnchant, 10, wEnchant)
        else:
            return Weapon("Longsword", attack=10)
    elif weapon < 850:
        if weaponEnchant == True:
            return Weapon("Warhammer of " + wEnchant, 15, wEnchant)
        else:
            return Weapon("Warhammer", attack=15)
    elif weapon < 900:
        if weaponEnchant == True:
            return Weapon("Shortsword of " + wEnchant, 7, wEnchant)
        else:
            return Weapon("Shortsword", attack=7)
    elif weapon < 950:
        if weaponEnchant == True:
            return Weapon("Rapier of " + wEnchant, 8, wEnchant)
        else:
            return Weapon("Rapier", attack=8) 
    elif weapon < 975:
        if weaponEnchant == True:
            return Weapon("Scimitar of " + wEnchant, 9, wEnchant)
        else:
            return Weapon("Scimitar", attack=9)
    elif weapon < 980:
        if weaponEnchant == True:
            return Weapon("Flail of " + wEnchant, 12, wEnchant)
        else:
            return Weapon("Flail", attack=12)
    elif weapon < 990:
        if weaponEnchant == True:
            return Weapon("Halberd of " + wEnchant, 14, wEnchant)
        else:
            return Weapon("Halberd", attack=14)
    elif weapon < 995:
        if weaponEnchant == True:
            return Weapon("Pike of " + wEnchant, 16, wEnchant)
        else:
            return Weapon("Pike", attack=16)
    elif weapon < 998:
        if weaponEnchant == True:
            return Weapon("Claymore of " + wEnchant, 20, wEnchant)
        else:
            return Weapon("Claymore", attack=20)
    elif weapon < 999:
        if weaponEnchant == True:
            return Weapon("Maul of " + wEnchant, 25, wEnchant)
        else:
            return Weapon("Maul", attack=25)
    elif weapon == 1000:
        if weaponEnchant == True:
            return Weapon("Excalibur of " + wEnchant, 100, wEnchant)
        else:
            return Weapon("Excalibur", attack=100)



class Item:
    def __init__(self, name, health=None, attack=None, defense=None, weapon=None):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.weapon = weapon

    def getName(self):
        return self.name

    def getHealth(self):
        return self.health

    def getAttack(self):
        return self.attack

    def getDefense(self):
        return self.defense

    def getWeapon(self):
        return self.weapon



def printMap(map, mapS):
    for i in range(0, mapS):
        for j in range(0, mapS):
            print(map[i][j], end="")
        print()


class Player:
    def __init__(self,maxhealth ,health, attack,defense,weapon):
        self.health = health
        self.attack = attack
        self.maxhealth = maxhealth
        self.defense = defense
        self.weapon = weapon
    
    def getHealth(self):
        return self.health
    
    def getAttack(self):
        return self.attack
    def getMaxHealth(self):
        return self.maxhealth
    def getDefense(self):
        return self.defense
    def getWeapon(self):
        return self.weapon

class Monster:
    def __init__(self, name, health, attack, maxhealth):
        self.name = name
        self.health = health
        self.attack = attack
        self.maxhealth = maxhealth
    
    def getHealth(self):
        return self.health
    
    def getAttack(self):
        return self.attack
    
    def getName(self):
        return self.name
    
    def getMaxHealth(self):
        return self.maxhealth


def do_health(maxHealth, health, healthDashes):
  dashConvert = int(maxHealth/healthDashes)            
  try:
    currentDashes = int(health/dashConvert)              
  except ZeroDivisionError:
    currentDashes = 0   
  remainingHealth = healthDashes - currentDashes       

  healthDisplay = '❤️' * currentDashes                  
  remainingDisplay = ' ' * remainingHealth             
  percent = str(int((health/maxHealth)*100)) + "%"     

  print("" + healthDisplay + remainingDisplay + "")  
  print("         " + percent + "    {}/{}".format(health, maxHealth)) 


def generateItem():
    item = random.randint(0, 1000)
    if item < 500:
        return Item("Health Potion", health=20)
    elif item < 750:
        return Item("Attack Potion", attack=2)
    elif item < 900:
        return Item("Defense Potion", defense=2)
    elif item < 950:
        return Item("Scroll of Power", attack=5, defense=5)
    elif item < 990:
        return Item("Scroll of MaxHealth", health=100)
    elif item == 1000:
        return Item("Scroll of Ultimate Power", attack=30, defense=20, health=100)

def UseItem(player, item):
    if item.name == "Health Potion":
        player.health += item.health
        print("You healed 20 health!")
        if player.health > player.maxhealth:
            player.health = player.maxhealth
    elif item.name == "Attack Potion":
        player.attack += item.attack
        print("You gained 2 attack!")
    elif item.name == "Defense Potion":
        print("You gained 2 defense!")
        player.defense += item.defense
    elif item.name == "Scroll of Power":
        player.attack += item.attack
        player.defense += item.defense
        print("You gained 5 attack and 5 defense!")
    elif item.name == "Scroll of MaxHealth":
        player.health += item.health
        if player.health > player.maxhealth:
            player.health = player.maxhealth
        print("You gained 100 health!")
    elif item.name == "Scroll of Ultimate Power":
        player.attack += item.attack
        player.defense += item.defense
        player.health += item.health
        if player.health > player.maxhealth:
            player.health = player.maxhealth
        print("You gained 30 attack, 20 defense, and 100 health!")

def fight(player, monster):
    print("\n"*30)
    monster.health = monster.getMaxHealth()
    print("You have encountered a " + monster.name)
    print(monster.name + ":")
    print(do_health(monster.getMaxHealth(), monster.health, int(monster.getMaxHealth()/5)))
    print("Player:")
    print(do_health(player.getMaxHealth(), player.getHealth(), 20))
    while player.getHealth() > 0 and monster.health > 0:
        print("1. Attack")
        print("2. Run")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("\n")
            Enchants(player.getWeapon(),monster,player)
            monster.health -= player.getAttack()
            print("You attacked the " + monster.name + " for " + str(player.getAttack()) + " damage")
            print("Monster:")
            print(do_health(monster.getMaxHealth(), monster.health, int(monster.getMaxHealth()/5)))
            if monster.health > 0:
                if monster.attack - round(player.defense / 5.0) < 0.0:
                    player.health -= 0
                    damageDone = 0
                else:
                    player.health -= monster.attack-round(player.defense/5)
                    damageDone = monster.attack-round(player.defense/5)
                print("The " + monster.name + " attacked you for " + str(damageDone) + " damage")
                print("Player:")
                print(do_health(player.getMaxHealth(), player.getHealth(), 20))
            UndoEnchants(player.getWeapon(),player)
        elif choice == "2":
            print("\n")
            if random.randint(0, 100) < 50:
                print("You ran away")
                return
            else:
                Enchants(player.getWeapon(),monster,player)
                print("You failed to run away")
                if monster.attack-round(player.defense/5.0) < 0.0:
                    player.health -= 0
                    damageDone = 0
                else:
                    player.health -= monster.attack-round(player.defense/5)
                    damageDone = monster.attack-round(player.defense/5)
                print("The " + monster.name + " attacked you for " + str(damageDone) + " damage")
                print("Player:")
                print(do_health(player.getMaxHealth(), player.getHealth(), 20))
                UndoEnchants(player.getWeapon(),player)
        else:
            print("Invalid choice")
    if player.getHealth() <= 0:
        print("You died")
    else:
        print("You killed the " + monster.name)
        print("You have " + str(player.getHealth()) + " health")
        print("\n"*30)


roomsCleared = 0
starttime = time.time()
def start_game():
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
                pressed = input("Enter w/a/s/d to move")
                if pressed == "a":
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




                elif pressed == "w":
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