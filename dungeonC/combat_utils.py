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

def do_health(maxHealth, health, healthDashes):
    # Affichage de la barre de santé
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