import random

class Weapon:
    # Classe Arme avec ses méthodes
    def __init__(self, name, attack, enchant=None):
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
    # Classe Objet avec ses méthodes
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
    # Classe Joueur avec ses méthodes
    def __init__(self, maxhealth, health, attack, defense, weapon):
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
    # Classe Monstre avec ses méthodes
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
    weaponEnchant = enchant > 990
    
    if weaponEnchant:
        enchant = random.randint(0, 1000)
        if enchant <= 500:
            wEnchant = "Tranchant"
        elif enchant <= 750:
            wEnchant = "Feu"
        elif enchant <= 900:
            wEnchant = "Lumière défensive"
        elif enchant <= 1000:
            wEnchant = "Foudre"

    if weapon < 100:
        return Weapon("Épée " + ("de " + wEnchant if weaponEnchant else ""), 5, wEnchant if weaponEnchant else None)
    # ... Répétez pour les autres types d'armes

def generateItem():
    item = random.randint(0, 1000)
    if item < 500:
        return Item("Potion de santé", health=20)
    elif item < 750:
        return Item("Potion d'attaque", attack=2)
    # ... Répétez pour les autres types d'objets
