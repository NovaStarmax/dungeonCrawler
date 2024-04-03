def Enchantements(arme, monstre, joueur):
    if arme.enchantement == "Aiguisement":
        arme.attaque += 2
    elif arme.enchantement == "Feu":
        print(f"Votre arme enchantée de feu brûle le {monstre.nom} ! Elle inflige 2 points de dégâts.")
        monstre.santé -= 2
    elif arme.enchantement == "Lumière défensive":
        joueur.defense += 2
    elif arme.enchantement == "Foudre":
        print(f"Le {monstre.nom} a été frappé par la foudre ! Cela a causé 10 points de dégâts.")
        monstre.santé -= 10
        
def AnnulerEnchantements(arme, joueur):
    if arme.enchantement == "Aiguisement":
        arme.attaque -= 2
    elif arme.enchantement == "Lumière défensive":
        joueur.defense -= 2

def faire_sante(santeMax, sante, tiretsSante):
    # Affichage de la barre de santé
    conversionTiret = int(santeMax/tiretsSante)            
    try:
        tiretsActuels = int(sante/conversionTiret)              
    except ZeroDivisionError:
        tiretsActuels = 0   
    santeRestante = tiretsSante - tiretsActuels       

    affichageSante = '❤️' * tiretsActuels                  
    affichageRestant = ' ' * santeRestante             
    pourcentage = str(int((sante/santeMax)*100)) + "%"     

    print(affichageSante + affichageRestant)  
    print(f"         {pourcentage}    {sante}/{santeMax}")
