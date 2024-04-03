from entities import Player, Monster, Weapon, Item
from combat_utils import Enchants, UndoEnchants, do_health
import random

def fight(player, monster):
    # Logique de combat
    print("\n"*30)
    monster.health = monster.getMaxHealth()
    print("Vous avez rencontré un(e) " + monster.name)
    print(monster.name + " :")
    print(do_health(monster.getMaxHealth(), monster.health, int(monster.getMaxHealth()/5)))
    print("Joueur :")
    print(do_health(player.getMaxHealth(), player.getHealth(), 20))
    while player.getHealth() > 0 and monster.health > 0:
        print("1. Attaquer")
        print("2. Fuir")
        choice = input("Entrez votre choix : ")
        if choice == "1":
            print("\n")
            Enchants(player.getWeapon(),monster,player)
            monster.health -= player.getAttack()
            print("Vous avez attaqué " + monster.name + " et infligé " + str(player.getAttack()) + " dégâts.")
            print("Monstre :")
            print(do_health(monster.getMaxHealth(), monster.health, int(monster.getMaxHealth()/5)))
            if monster.health > 0:
                damageDealt = max(0, monster.attack - round(player.defense / 5.0))
                player.health -= damageDealt
                print(monster.name + " vous a attaqué et infligé " + str(damageDealt) + " dégâts.")
                print("Joueur :")
                print(do_health(player.getMaxHealth(), player.getHealth(), 20))
            UndoEnchants(player.getWeapon(),player)
        elif choice == "2":
            print("\n")
            if random.randint(0, 100) < 50:
                print("Vous avez réussi à fuir.")
                return
            else:
                Enchants(player.getWeapon(),monster,player)
                print("Vous n'avez pas réussi à fuir.")
                damageDealt = max(0, monster.attack - round(player.defense / 5.0))
                player.health -= damageDealt
                print(monster.name + " vous a attaqué et infligé " + str(damageDealt) + " dégâts.")
                print("Joueur :")
                print(do_health(player.getMaxHealth(), player.getHealth(), 20))
                UndoEnchants(player.getWeapon(),player)
        else:
            print("Choix invalide.")
    if player.getHealth() <= 0:
        print("Vous êtes mort(e).")
    else:
        print("Vous avez vaincu " + monster.name + ".")
        print("Il vous reste " + str(player.getHealth()) + " points de vie.")
        print("\n"*30)

def UseItem(player, item):
    # Utilisation d'un objet
    if item.name == "Health Potion":
        player.health += item.health
        print("Vous avez récupéré 20 points de vie !")
        if player.health > player.maxhealth:
            player.health = player.maxhealth
    elif item.name == "Attack Potion":
        player.attack += item.attack
        print("Vous avez gagné 2 points d'attaque !")
    elif item.name == "Defense Potion":
        player.defense += item.defense
        print("Vous avez gagné 2 points de défense !")
    elif item.name == "Scroll of Power":
        player.attack += item.attack
        player.defense += item.defense
        print("Vous avez gagné 5 points d'attaque et de défense !")
    elif item.name == "Scroll of MaxHealth":
        player.health += item.health
        if player.health > player.maxhealth:
            player.health = player.maxhealth
        print("Votre santé maximale a augmenté de 100 points !")
    elif item.name == "Scroll of Ultimate Power":
        player.attack += item.attack
        player.defense += item.defense
        player.health += item.health
        if player.health > player.maxhealth:
            player.health = player.maxhealth
        print("Vous avez gagné 30 points d'attaque, 20 points de défense et votre santé maximale a augmenté.")
