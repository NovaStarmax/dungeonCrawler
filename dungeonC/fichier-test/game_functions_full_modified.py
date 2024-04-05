
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

# Nouvelle structure pour gérer la génération de la carte et la boucle de salles
class Dungeon:
    def __init__(self):
        self.rooms = [] # Liste des salles générées
        self.current_room = 0 # Index de la salle actuelle
        self.key_obtained = False # Si le joueur a obtenu la clé

    def generate_rooms(self):
        # Génération de 3 salles avec des dimensions aléatoires entre 10x10 et 30x30
        for _ in range(3):
            size = random.randint(10, 30)
            self.rooms.append(self.generate_map(size))

    def generate_map(self, size):
        # Création de la carte d'une salle
        map = [["  " for _ in range(size)] for _ in range(size)]
        map[1][1] = "🏳️" # Point de départ
        map[size - 2][size - 2] = "🚪" # Sortie
        return map

    def display_room(self):
        # Affichage de la salle actuelle
        for row in self.rooms[self.current_room]:
            print(' '.join(row))

    def next_room(self):
        # Passage à la salle suivante, avec retour à la 1ère après la 3ème
        self.current_room = (self.current_room + 1) % 3
        if self.current_room == 0 and not self.key_obtained:
            print("Vous avez obtenu une clé spéciale !")
            self.key_obtained = True

# Remplacement de la fonction start_game par une version adaptée à la nouvelle structure de Dungeon
def start_game():
    dungeon = Dungeon()
    dungeon.generate_rooms()
    # Exemple de logique pour avancer à travers les salles et intégrer la salle du boss
    # Cette partie sera développée plus en détail lors de l'implémentation complète


# Import de la bibliothèque nécessaire pour détecter les pressions de touches
import keyboard

class Dungeon:
    # Ajout d'une méthode pour afficher les stats et objets du joueur
    def display_player_stats(self, player):
        print("\nStats du Joueur:")
        print(f"Vie: {player.health} / {player.max_health}")
        print(f"Attaque: {player.attack}")
        print(f"Défense: {player.defense}")
        print("Objets:", ", ".join([item.name for item in player.inventory]))
        print("")  # Ligne vide pour séparer les stats des autres outputs

    # Modification de la méthode next_room pour intégrer le déplacement des ennemis
    def next_room(self, player):
        # Passage à la salle suivante avec logique de déplacement des ennemis
        super().next_room()  # Appel de la méthode de base pour changer de salle
        
        # Déplacement aléatoire des ennemis
        for enemy in self.rooms[self.current_room].enemies:
            enemy.move_randomly(self.rooms[self.current_room])

# Ajout d'une fonction pour gérer les pressions de touches et afficher les stats du joueur
def handle_key_presses(player):
    if keyboard.is_pressed('s'):  # Si la touche 's' est pressée, afficher les stats du joueur
        dungeon.display_player_stats(player)

# Exemple simplifié de la méthode pour déplacer un ennemi aléatoirement
# À intégrer dans la classe des ennemis
def move_randomly(self, room):
    # Logique de déplacement aléatoire, en veillant à ne pas traverser les murs
    directions = ['up', 'down', 'left', 'right']
    direction = random.choice(directions)
    # Implémenter la logique de déplacement ici, en prenant en compte les limites de la carte et les murs
