import game_functions
import entities
import combat
import sys

# Rediriger stdout vers la console
sys.stdout = sys.__stdout__



# Importations des modules spécifiques du jeu
from game_functions import start_game, main_menu

# Ici, on lance le menu principal du jeu.
if __name__ == "__main__":
    game_functions.main_menu()
