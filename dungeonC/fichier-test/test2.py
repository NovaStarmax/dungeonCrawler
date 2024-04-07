import random
import time
import keyboard

class Player:
    def __init__(self, health, max_health, attack, defense):
        self.health = health
        self.max_health = max_health
        self.attack = attack
        self.defense = defense

class Monster:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

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

        # Placement aléatoire des monstres dans la salle
        monsters = ["👹", "👺", "🐉", "🧟"]
        for _ in range(random.randint(3, 5)):
            x, y = random.randint(1, size - 2), random.randint(1, size - 2)
            if map[x][y] == "  ":
                map[x][y] = random.choice(monsters)

        return map

    def display_room(self):
        # Affichage de la salle actuelle
        for row in self.rooms[self.current_room]:
            print(' '.join(row))

    def next_room(self, player):
        # Passage à la salle suivante, avec retour à la 1ère après la 3ème
        self.current_room = (self.current_room + 1) % 3
        if self.current_room == 0 and not self.key_obtained:
            print("Vous avez obtenu une clé spéciale !")
            self.key_obtained = True

    def display_player_stats(self, player):
        print("\nStats du Joueur:")
        print(f"Vie: {player.health} / {player.max_health}")
        print(f"Attaque: {player.attack}")
        print(f"Défense: {player.defense}")
        print("")  # Ligne vide pour séparer les stats des autres outputs

    def handle_key_presses(self, player):
        if keyboard.is_pressed('i'):  # Si la touche 'i' est pressée, afficher les stats du joueur
            self.display_player_stats(player)

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

def start_game():
    dungeon = Dungeon()
    dungeon.generate_rooms()
    player = Player(100, 100, 10, 5)
    while True:
        print("1. Afficher la salle")
        print("2. Passer à la salle suivante")
        print("3. Afficher les statistiques du joueur")
        print("4. Quitter")
        choice = input("Entrez votre choix : ")
        if choice == "1":
            dungeon.display_room()
        elif choice == "2":
            dungeon.next_room(player)
        elif choice == "3":
            dungeon.display_player_stats(player)
        elif choice == "4":
            exit()
        else:
            print("Choix invalide")

if __name__ == "__main__":
    main_menu()
