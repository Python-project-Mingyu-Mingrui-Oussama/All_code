# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 10:58:08 2024

@author: 秋山暦
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas 
from PIL import Image, ImageTk
from class_file import Match
from class_file import Event
from data import extract_all_location
from data import calculate_heat_map
from data import calculate_attack_distribution
from data import extract_two_team


def heat_funct(heat_map) :
# Charger l'image du terrain de football
    terrain_image = Image.open("terrainfoot.jpg")  # Remplacez par le chemin de votre image de terrain
    terrain_width, terrain_height = terrain_image.size
    
    # Données de pourcentage des actions (exemple arbitraire)
    # Ici, j'utilise des valeurs arbitraires pour les pourcentages de chaque zone
    pourcentage_actions = heat_map
    # Normalisation des pourcentages pour les adapter aux dimensions de l'image du terrain
    pourcentage_actions = pourcentage_actions / np.max(pourcentage_actions) * 100
    
    # Affichage de l'image du terrain
    plt.imshow(terrain_image, extent=[0, terrain_width, 0, terrain_height])
    
    # Affichage de la heatmap superposée à l'image du terrain
    plt.imshow(pourcentage_actions, origin='lower', alpha=0.5, cmap='hot', extent=[0, terrain_width, 0, terrain_height])
    
    # Configuration du titre, des étiquettes, etc.
    plt.axis('off')
    plt.colorbar(label='Pourcentage d\'actions')
    plt.title('Heat map RMA vs FCB')
    plt.xlabel('Position en x sur le terrain')
    plt.ylabel('Position en y sur le terrain')
    plt.grid(False)
    plt.show()
    
    
def attaques(matrix) :

        # Fonction pour afficher le nombre de tentatives
        # Initialisation de la variable arrow
        arrow = None
        
        # Fonction pour afficher le nombre de tentatives
        
            # Supprimer la précédente flèche si elle existe
           
            
            # Récupérer le nombre de tentatives depuis la base de données
            # Remplacer cette ligne par la méthode pour obtenir le nombre de tentatives depuis la base de données
        nombre_tentatives = matrix[0,0]  # Remplacez ceci par votre logique pour récupérer le nombre de tentatives
            
            # Afficher l'image du terrain de football
        image = Image.open("terrainfoot.jpg")  # Remplacez ceci par le chemin de votre image
        plt.imshow(image)
        
        #logo_equipe1 = Image.open("Logo_home")  # Remplacez par le chemin du logo de l'équipe 1
        #logo_equipe2 = Image.open("Logo_away")  # Remplacez par le chemin du logo de l'équipe 2
        
        # Redimensionner les logos (ajustez la taille selon vos besoins)
        #logo_equipe1 = logo_equipe1.resize((50, 50))
        #logo_equipe2 = logo_equipe2.resize((50, 50))
        
        # Superposer les logos sur l'image du terrain
        #image.paste(logo_equipe1, (246-30, 50))  # Position du logo de l'équipe 1
        #image.paste(logo_equipe2, (366-20, 50))  # Position du logo de l'équipe 2
        #plt.imshow(image)
            # Calculer les coordonnées de la flèche en fonction du nombre de tentatives
        x1 = 180  # Remplacez ceci par la coordonnée x de la flèche
        y1 = 50  # Remplacez ceci par la coordonnée y de la flèche
        dx1 = -100 # Remplacez ceci par le décalage x de la flèche
        dy1 = 0  # Remplacez ceci par le décalage y de la flèche
            
            # Dessiner la flèche avec le nombre de tentatives
        arrow = plt.arrow(x1, y1, dx1, dy1, width=5, color='red')
        plt.text(x1  + dx1/2, y1 + 30, str(nombre_tentatives)+"%", fontsize=20, color='red')
        nombre_tentatives = matrix[1,0]
        x2 = 180  # Remplacez ceci par la coordonnée x de la flèche
        y2 = 319  # Remplacez ceci par la coordonnée y de la flèche
        dx2 = -100 # Remplacez ceci par le décalage x de la flèche
        dy2 = 0  # Remplacez ceci par le décalage y de la flèche
            
            # Dessiner la flèche avec le nombre de tentatives
        arrow = plt.arrow(x2, y2, dx2, dy2, width=5, color='red')
        plt.text(x2  + dx2/2, y2 + 30, str(nombre_tentatives)+"%", fontsize=20, color='red')
        nombre_tentatives = matrix[2,0] 
        x3 = 180  # Remplacez ceci par la coordonnée x de la flèche
        y3 = 185  # Remplacez ceci par la coordonnée y de la flèche
        dx3 = -100 # Remplacez ceci par le décalage x de la flèche
        dy3 = 0  # Remplacez ceci par le décalage y de la flèche
            
            # Dessiner la flèche avec le nombre de tentatives
        arrow = plt.arrow(x3, y3, dx3, dy3, width=5, color='red')
        plt.text(x3  + dx3/2, y3 + 30, str(nombre_tentatives)+"%", fontsize=20, color='red')
        
            # Afficher l'image avec la flèche
        nombre_tentatives = matrix[0,1] 
        x4 = 432  # Remplacez ceci par la coordonnée x de la flèche
        y4 = 50  # Remplacez ceci par la coordonnée y de la flèche
        dx4 = 100 # Remplacez ceci par le décalage x de la flèche
        dy4 = 0  # Remplacez ceci par le décalage y de la flèche
            
            # Dessiner la flèche avec le nombre de tentatives
        arrow = plt.arrow(x4, y4, dx4, dy4, width=5, color='blue')
        plt.text(x4  - dx4/9, y4 + 30, str(nombre_tentatives)+"%", fontsize=20, color='blue')
        nombre_tentatives = matrix[1,1]   
        x5 = 432  # Remplacez ceci par la coordonnée x de la flèche
        y5 = 319  # Remplacez ceci par la coordonnée y de la flèche
        dx5 = 100 # Remplacez ceci par le décalage x de la flèche
        dy5 = 0  # Remplacez ceci par le décalage y de la flèche
            
            # Dessiner la flèche avec le nombre de tentatives
        arrow = plt.arrow(x5, y5, dx5, dy5, width=5, color='blue')
        plt.text(x5  -dx5/9, y5 + 30, str(nombre_tentatives)+"%", fontsize=20, color='blue')
        nombre_tentatives = matrix[2,1]   
        x6 = 432  # Remplacez ceci par la coordonnée x de la flèche
        y6 = 185  # Remplacez ceci par la coordonnée y de la flèche
        dx6 = 100 # Remplacez ceci par le décalage x de la flèche
        dy6 = 0  # Remplacez ceci par le décalage y de la flèche
            
            # Dessiner la flèche avec le nombre de tentatives
        arrow = plt.arrow(x6, y6, dx6, dy6, width=5, color='blue')
        plt.text(x6  - dx6/9, y6 + 30, str(nombre_tentatives)+"%", fontsize=20, color='blue')
            
        
            # Afficher l'image avec la flèche
        plt.axis('off')  # Masquer les axes
        plt.tight_layout()
        plt.show()

    # Mettre à jour l'affichage de la figure dans la fenêtre Tkinter
    
def passes_function(matrix)   : 
    # Récupérer le nombre de tentatives depuis la base de données
    # Remplacer cette ligne par la méthode pour obtenir le nombre de tentatives depuis la base de données
         # Remplacez ceci par votre logique pour récupérer le nombre de tentatives
            
            # Afficher l'image du terrain de football
        image = Image.open("terrainfoot.jpg")  # Remplacez ceci par le chemin de votre image
        plt.imshow(image)
        
        
        '''
        logo_equipe1 = Image.open(Logo_home)  # Remplacez par le chemin du logo de l'équipe 1
        logo_equipe2 = Image.open(Logo_away)  # Remplacez par le chemin du logo de l'équipe 2
        
        # Redimensionner les logos (ajustez la taille selon vos besoins)
        logo_equipe1 = logo_equipe1.resize((50, 50))
        logo_equipe2 = logo_equipe2.resize((50, 50))
        
        # Superposer les logos sur l'image du terrain
        image.paste(logo_equipe1, (246-30, 50))  # Position du logo de l'équipe 1
        image.paste(logo_equipe2, (366-20, 50))  # Position du logo de l'équipe 2
        plt.imshow(image)
        '''
        nombre_tentatives = matrix[0,0]
            # Calculer les coordonnées de la flèche en fonction du nombre de tentatives
        x1 = 180  # Remplacez ceci par la coordonnée x de la flèche
        y1 = 100  # Remplacez ceci par la coordonnée y de la flèche
        dx1 = -60 # Remplacez ceci par le décalage x de la flèche
        dy1 = 50  # Remplacez ceci par le décalage y de la flèche
            
            # Dessiner la flèche avec le nombre de tentatives
        arrow = plt.arrow(x1, y1, dx1, dy1, width=5, color='red')
        plt.text(x1  - 80, y1 + 95, str(nombre_tentatives)+"%", fontsize=20, color='red')
        nombre_tentatives = matrix[1,0]
        x2 = 180  # Remplacez ceci par la coordonnée x de la flèche
        y2 = 269  # Remplacez ceci par la coordonnée y de la flèche
        dx2 = -60 # Remplacez ceci par le décalage x de la flèche
        dy2 = -50  # Remplacez ceci par le décalage y de la flèche
        
        arrow = plt.arrow(x2, y2, dx2, dy2, width=5, color='red')
        
        t = np.linspace(0.9, 1.15*np.pi, 100)  # Créer une série de valeurs de 0 à 2*pi
        x_curve = 100 + 50 * np.cos(t)  # Exemple de coordonnées x pour une courbe
        y_curve = 250 + 80 * np.sin(t)  # Exemple de coordonnées y pour une courbe
        
        # Dessiner une ligne courbe
        plt.plot(x_curve, y_curve,linewidth=5,color='red')
        plt.arrow(x_curve[-2], y_curve[-2], x_curve[-1] - x_curve[-2], y_curve[-1] - y_curve[-2],
                  head_width=10, head_length=20, fc='red', ec='red')
        plt.text(100, 300, str(nombre_tentatives)+"%", fontsize=20, color='red')
        nombre_tentatives = matrix[2,0]
        t2 = np.linspace(0.9, 1.15*np.pi, 100)  # Créer une série de valeurs de 0 à 2*pi
        x_curve2 = 100 + 50 * np.cos(t)  # Exemple de coordonnées x pour une courbe
        y_curve2 = 120 - 80 * np.sin(t)  # Exemple de coordonnées y pour une courbe
        
        # Dessiner une ligne courbe
        plt.plot(x_curve2, y_curve2,linewidth=5,color='red')
        plt.arrow(x_curve2[-2], y_curve2[-2], x_curve2[-1] - x_curve2[-2], y_curve2[-1] - y_curve2[-2],
                  head_width=10, head_length=20, fc='red', ec='red')
        plt.text(100, 89, str(nombre_tentatives)+"%", fontsize=20, color='red')
            # Afficher l'image avec la flèche
        x1 = 432  # Remplacez ceci par la coordonnée x de la flèche
        y1 = 100  # Remplacez ceci par la coordonnée y de la flèche
        dx1 = 60 # Remplacez ceci par le décalage x de la flèche
        dy1 = 50  # Remplacez ceci par le décalage y de la flèche
        nombre_tentatives = matrix[0,1]
            
            # Dessiner la flèche avec le nombre de tentatives
        arrow = plt.arrow(x1, y1, dx1, dy1, width=5, color='blue')
        plt.text(450, 195, str(nombre_tentatives)+"%", fontsize=20, color='blue')
        x2 = 432  # Remplacez ceci par la coordonnée x de la flèche
        y2 = 269  # Remplacez ceci par la coordonnée y de la flèche
        dx2 = 60 # Remplacez ceci par le décalage x de la flèche
        dy2 = -50  # Remplacez ceci par le décalage y de la flèche
            
            # Dessiner la flèche avec le nombre de tentatives
        arrow = plt.arrow(x2, y2, dx2, dy2, width=5, color='blue')
        nombre_tentatives = matrix[1,1]
        t = np.linspace(0.9, 1.15*np.pi, 100)  # Créer une série de valeurs de 0 à 2*pi
        x_curve = 512 - 50 * np.cos(t)  # Exemple de coordonnées x pour une courbe
        y_curve = 250 + 80 * np.sin(t)  # Exemple de coordonnées y pour une courbe
        
        # Dessiner une ligne courbe
        plt.plot(x_curve, y_curve,linewidth=5,color='blue')
        plt.arrow(x_curve[-2], y_curve[-2], x_curve[-1] - x_curve[-2], y_curve[-1] - y_curve[-2],
                  head_width=10, head_length=20, fc='blue', ec='blue')
        plt.text(450, 300, str(nombre_tentatives)+"%", fontsize=20, color='blue')
        nombre_tentatives = matrix[2,1]
        t = np.linspace(0.9, 1.15*np.pi, 100)  # Créer une série de valeurs de 0 à 2*pi
        x_curve = 512 - 50 * np.cos(t)  # Exemple de coordonnées x pour une courbe
        y_curve = 120 - 80 * np.sin(t)  # Exemple de coordonnées y pour une courbe
        
        # Dessiner une ligne courbe
        plt.plot(x_curve, y_curve,linewidth=5,color='blue')
        plt.arrow(x_curve[-2], y_curve[-2], x_curve[-1] - x_curve[-2], y_curve[-1] - y_curve[-2],
                  head_width=10, head_length=20, fc='blue', ec='blue')
        plt.text(450, 300, str(nombre_tentatives)+"%", fontsize=20, color='blue')
        plt.axis('off')  # Masquer les axes
        plt.tight_layout()
        plt.show()

    # Mettre à jour l'affichage de la figure dans la fenêtre Tkinter
    
def pourcentage_victoire(home_team, away_team, historique_rencontres):
    # Calcul du pourcentage en se basant sur l'historique, les matchs gagnés et les buts marqués
    pourcentage_home = 0.6  # Valeur initiale pour l'équipe à domicile (peut être ajustée)

    # Influence de l'historique des rencontres
    for match in historique_rencontres:
        if match.ht == home_team:
            if match.htscore > match.atscore:
                pourcentage_home += 0.1  # Ajouter 0.1 si l'équipe à domicile a gagné ce match dans l'historique
            if match.htscore < match.atscore:
                pourcentage_home -= 0.1  # Soustraire 0.1 si l'équipe à domicile a perdu ce match dans l'historique
        if match.at == home_team:
            if match.htscore < match.atscore:
                pourcentage_home += 0.1  # Ajouter 0.1 si l'équipe à domicile a gagné ce match dans l'historique
            if match.htscore > match.atscore:
                pourcentage_home -= 0.1  # Soustraire 0.1 si l'équipe à domicile a perdu ce match dans l'historique
    
    
    # Influence du nombre de matchs gagnés
    #pourcentage_home += 0.01 * (matchs_gagnes_home - matchs_gagnes_away)

    # Influence du nombre de buts marqués
    #pourcentage_home += 0.005 * (buts_marques_home - buts_marques_away)
    
    

    # Assurer que le pourcentage est dans la plage [0, 1]
    #pourcentage_home = max(0, min(1, pourcentage_home))

    # Calculer le pourcentage pour l'équipe à l'extérieur
    pourcentage_away = 1 - pourcentage_home

    return pourcentage_home, pourcentage_away
    
# Example usage:
if __name__ == "__main__":
    results = pandas.read_csv("archive/ginf.csv")   #read the database
    events = pandas.read_csv("archive/events.csv")   #read the database
    id_odsp='newuFc20/'
    #id_odsp='UFot0hit/'
    
    location_objects = extract_all_location(id_odsp)
    heat_map = calculate_heat_map(location_objects)
    heat_funct(heat_map)
    matrix = calculate_attack_distribution(location_objects)
    attaques(matrix)
    passes_function(matrix)
    
    name1 = 'Bordeaux'
    name2 = 'Lyon'
    match_history = extract_two_team(name1,name2)
    
    [pourcentage_home, pourcentage_away] = pourcentage_victoire(name1, name2, match_history)
