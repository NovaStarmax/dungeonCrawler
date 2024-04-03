from entities import Player, Monster, Weapon, Item
from combat_utils import Enchants, UndoEnchants, do_health
import random

def fight(player, monster):
    # Logique de combat
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

def UseItem(player, item):
    # Utilisation d'un objet
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