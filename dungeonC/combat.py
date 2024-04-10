import pygame
from pygame import mixer
from entities import Player, Monster, Weapon, Item
from combat_utils import Enchants, UndoEnchants, do_health
import random

# Initialiser Pygame
pygame.init()

# Charger la musique d'introduction
mixer.music.load('intro.mp3')

# Charger la musique de combat
mixer.music.load('combat.mp3')

# Fonction pour jouer la musique de combat
def play_combat_music():
    mixer.music.load('combat.mp3')
    mixer.music.play(-1)  # -1 pour jouer en boucle

# Fonction pour arrêter la musique de combat
def stop_combat_music():
    mixer.music.stop()

# Fonction pour jouer la musique d'introduction
def play_intro_music():
    mixer.music.load('intro.mp3')
    mixer.music.play(-1)  # -1 pour jouer en boucle

def fight(player, monster):
    # Arrêter la musique d'introduction
    mixer.music.stop()

    # Logique de combat
    print("\n"*30)
    monster.health = monster.getMaxHealth()
    print("Vous avez rencontré un " + monster.name)
    print(monster.name + ":")
    print(do_health(monster.getMaxHealth(), monster.health, int(monster.getMaxHealth()/5)))
    print("Joueur:")
    print(do_health(player.getMaxHealth(), player.getHealth(), 20))
    
    # Démarrer la musique de combat
    play_combat_music()
    
    while player.getHealth() > 0 and monster.health > 0:
        print("1. Attaquer")
        print("2. Fuir")
        choice = input("Entrer votre choix : ")
        if choice == "1":
            print("\n")
            Enchants(player.getWeapon(),monster,player)
            monster.health -= player.getAttack()
            print("Vous attaquez le " + monster.name + " et infligez " + str(player.getAttack()) + " de dégâts")
            print("Monstre:")
            print(do_health(monster.getMaxHealth(), monster.health, int(monster.getMaxHealth()/5)))
            if monster.health > 0:
                player.health -= monster.attack - round(player.defense / 5)
                print("Le " + monster.name + " vous attaque et vous inflige " + str(monster.attack - round(player.defense / 5)) + " points de dégâts")
                print("Joueur:")
                print(do_health(player.getMaxHealth(), player.getHealth(), 20))
            UndoEnchants(player.getWeapon(),player)
        elif choice == "2":
            print("\n")
            if random.randint(0, 100) < 50:
                print("Vous avez réussi à fuir.")
                # Arrêter la musique de combat
                stop_combat_music()
                return
            else:
                print("Vous n'avez pas réussi à fuir.")
                player.health -= monster.attack - round(player.defense / 5)
                print(monster.name + " vous attaque et vous inflige " + str(monster.attack - round(player.defense / 5)) + " points de dégâts")
                print("Joueur:")
                print(do_health(player.getMaxHealth(), player.getHealth(), 20))
        else:
            print("Choix invalide")
    
    # Arrêter la musique de combat
    stop_combat_music()
    
    if player.getHealth() <= 0:
        print("Vous êtes mort.")
    elif monster.health <= 0:
        print("Vous avez vaincu " + monster.name + " et trouvé une clé !")
        player.has_key = True  # Attribue la clé au joueur
        print("Il vous reste " + str(player.getHealth()) + " points de santé.")
        print("\n"*30)
        
    # Rejouer la musique d'introduction
    play_intro_music()

def UseItem(player, item):
    # Utilisation d'un objet
    if item.name == "Health Potion":
        player.health += item.health
        print("Vous avez récupéré 20 points de santé !")
        if player.health > player.maxhealth:
            player.health = player.maxhealth
    elif item.name == "Attack Potion":
        player.attack += item.attack
        print("Votre attaque a augmenté de 2 points !")
    elif item.name == "Defense Potion":
        print("Votre défense a augmenté de 2 points !")
        player.defense += item.defense
    elif item.name == "Scroll of Power":
        player.attack += item.attack
        player.defense += item.defense
        print("Vous avez gagné 5 points d'attaque et 5 points de défense !")
    elif item.name == "Scroll of MaxHealth":
        player.health += item.health
        if player.health > player.maxhealth:
            player.health = player.maxhealth
        print("Vous avez gagné 100 points de santé !")
    elif item.name == "Scroll of Ultimate Power":
        player.attack += item.attack
        player.defense += item.defense
        player.health += item.health
        if player.health > player.maxhealth:
            player.health = player.maxhealth
        print("Vous avez gagné 30 points d'attaque, 20 points de défense et 100 points de santé !")
