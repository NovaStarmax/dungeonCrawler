import random

class Weapon:
    # Classe Weapon avec ses méthodes
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

class Item:
    # Classe Item avec ses méthodes
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

class Player:
    # Classe Player avec ses méthodes
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
    # Classe Monster avec ses méthodes
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

# Fonctions de génération aléatoire pour les armes et les objets
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