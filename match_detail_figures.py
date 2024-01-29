import pdb

from PIL import Image

import numpy as np
from PyQt5.QtWidgets import QDialog, QWidget, QVBoxLayout, QPushButton, QLabel, QScrollArea
from matplotlib import pyplot as plt
from librosa.display import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.pyplot import colorbar

from data import calculate_heat_map, calculate_attack_distribution

matplotlib.use("Qt5Agg")


class match_detail_figures():
    def __init__(self, result, event, i):
        super().__init__()
        self.event = event
        self.result = result
        self.i = i
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setMinimumSize(600, 600)
        self.ax = self.figure.add_subplot(111)
        self.heat_map = calculate_heat_map(self.event)
        self.matrix = calculate_attack_distribution(self.event) * 100
        self.add_plot()
        # pdb.set_trace()


class passes_for_passes(match_detail_figures):
    def add_plot(self):
        matrix = self.matrix
        # Récupérer le nombre de tentatives depuis la base de données
    # Remplacer cette ligne par la méthode pour obtenir le nombre de tentatives depuis la base de données
         # Remplacez ceci par votre logique pour récupérer le nombre de tentatives

            # Afficher l'image du terrain de football

        image = Image.open("terrainfoot.jpg")  # Remplacez ceci par le chemin de votre image
        self.ax.imshow(image)
        logo_equipe1 = Image.open(
            'team logo/' + self.result[self.i].ht + '.png')  # Remplacez par le chemin du logo de l'équipe 1
        logo_equipe2 = Image.open('team logo/' + self.result[self.i].at + '.png')

        # Redimensionner les logos (ajustez la taille selon vos besoins)
        logo_equipe1 = logo_equipe1.resize((50, 50))
        logo_equipe2 = logo_equipe2.resize((50, 50))

        position1 = (216, 1)
        position2 = (346, 1)
        self.ax.imshow(logo_equipe1, extent=[position1[0], position1[0] + 50, position1[1], position1[1] + 50])
        self.ax.imshow(logo_equipe2, extent=[position2[0], position2[0] + 50, position2[1], position2[1] + 50])
        nombre_tentatives = matrix[0,0]
        nombre_tentatives = "{:.2f}".format(nombre_tentatives)

        # Calculer les coordonnées de la flèche en fonction du nombre de tentatives
        x1 = 180  # Remplacez ceci par la coordonnée x de la flèche
        y1 = 100  # Remplacez ceci par la coordonnée y de la flèche
        dx1 = -60 # Remplacez ceci par le décalage x de la flèche
        dy1 = 50  # Remplacez ceci par le décalage y de la flèche

            # Dessiner la flèche avec le nombre de tentatives
        arrow = self.ax.arrow(x1, y1, dx1, dy1, width=5, color='red')
        self.ax.text(x1  - 80, y1 + 80, f"{nombre_tentatives}%", fontsize=20, color='red')
        nombre_tentatives = matrix[1,0]
        nombre_tentatives = "{:.2f}".format(nombre_tentatives)
        x2 = 180  # Remplacez ceci par la coordonnée x de la flèche
        y2 = 269  # Remplacez ceci par la coordonnée y de la flèche
        dx2 = -60 # Remplacez ceci par le décalage x de la flèche
        dy2 = -50  # Remplacez ceci par le décalage y de la flèche

        arrow = self.ax.arrow(x2, y2, dx2, dy2, width=5, color='red')

        t = np.linspace(0.9, 1.15*np.pi, 100)  # Créer une série de valeurs de 0 à 2*pi
        x_curve = 100 + 50 * np.cos(t)  # Exemple de coordonnées x pour une courbe
        y_curve = 250 + 80 * np.sin(t)  # Exemple de coordonnées y pour une courbe

        # Dessiner une ligne courbe
        self.ax.plot(x_curve, y_curve,linewidth=5,color='red')
        self.ax.arrow(x_curve[-2], y_curve[-2], x_curve[-1] - x_curve[-2], y_curve[-1] - y_curve[-2],
                  head_width=10, head_length=20, fc='red', ec='red')
        self.ax.text(100, 285, f"{nombre_tentatives}%", fontsize=20, color='red')
        nombre_tentatives = matrix[2,0]
        nombre_tentatives = "{:.2f}".format(nombre_tentatives)
        t2 = np.linspace(0.9, 1.15*np.pi, 100)  # Créer une série de valeurs de 0 à 2*pi
        x_curve2 = 100 + 50 * np.cos(t)  # Exemple de coordonnées x pour une courbe
        y_curve2 = 120 - 80 * np.sin(t)  # Exemple de coordonnées y pour une courbe

        # Dessiner une ligne courbe
        self.ax.plot(x_curve2, y_curve2,linewidth=5,color='red')
        self.ax.arrow(x_curve2[-2], y_curve2[-2], x_curve2[-1] - x_curve2[-2], y_curve2[-1] - y_curve2[-2],
                  head_width=10, head_length=20, fc='red', ec='red')
        self.ax.text(100, 74, f"{nombre_tentatives}%", fontsize=20, color='red')
            # Afficher l'image avec la flèche
        x1 = 432  # Remplacez ceci par la coordonnée x de la flèche
        y1 = 100  # Remplacez ceci par la coordonnée y de la flèche
        dx1 = 60 # Remplacez ceci par le décalage x de la flèche
        dy1 = 50  # Remplacez ceci par le décalage y de la flèche
        nombre_tentatives = matrix[0,1]
        nombre_tentatives = "{:.2f}".format(nombre_tentatives)

            # Dessiner la flèche avec le nombre de tentatives
        arrow = self.ax.arrow(x1, y1, dx1, dy1, width=5, color='blue')
        self.ax.text(450, 180, f"{nombre_tentatives}%", fontsize=20, color='blue')
        x2 = 432  # Remplacez ceci par la coordonnée x de la flèche
        y2 = 269  # Remplacez ceci par la coordonnée y de la flèche
        dx2 = 60 # Remplacez ceci par le décalage x de la flèche
        dy2 = -50  # Remplacez ceci par le décalage y de la flèche

            # Dessiner la flèche avec le nombre de tentatives
        arrow = self.ax.arrow(x2, y2, dx2, dy2, width=5, color='blue')
        nombre_tentatives = matrix[1,1]
        nombre_tentatives = "{:.2f}".format(nombre_tentatives)
        t = np.linspace(0.9, 1.15*np.pi, 100)  # Créer une série de valeurs de 0 à 2*pi
        x_curve = 512 - 50 * np.cos(t)  # Exemple de coordonnées x pour une courbe
        y_curve = 250 + 80 * np.sin(t)  # Exemple de coordonnées y pour une courbe

        # Dessiner une ligne courbe
        self.ax.plot(x_curve, y_curve,linewidth=5,color='blue')
        self.ax.arrow(x_curve[-2], y_curve[-2], x_curve[-1] - x_curve[-2], y_curve[-1] - y_curve[-2],
                  head_width=10, head_length=20, fc='blue', ec='blue')
        self.ax.text(450, 285, f"{nombre_tentatives}%", fontsize=20, color='blue')
        nombre_tentatives = matrix[2,1]
        nombre_tentatives = "{:.2f}".format(nombre_tentatives)
        t = np.linspace(0.9, 1.15*np.pi, 100)  # Créer une série de valeurs de 0 à 2*pi
        x_curve = 512 - 50 * np.cos(t)  # Exemple de coordonnées x pour une courbe
        y_curve = 120 - 80 * np.sin(t)  # Exemple de coordonnées y pour une courbe

        # Dessiner une ligne courbe
        self.ax.plot(x_curve, y_curve,linewidth=5,color='blue')
        self.ax.arrow(x_curve[-2], y_curve[-2], x_curve[-1] - x_curve[-2], y_curve[-1] - y_curve[-2],
                  head_width=10, head_length=20, fc='blue', ec='blue')
        self.ax.text(450, 75, f"{nombre_tentatives}%", fontsize=20, color='blue')
        self.ax.axis('off')  # Masquer les axes


class heat_map(match_detail_figures):
    def add_plot(self):
        # Charger l'image du terrain de football
        terrain_image = Image.open("terrainfoot.jpg")  # Remplacez par le chemin de votre image de terrain
        terrain_width, terrain_height = terrain_image.size
        self.ax.imshow(terrain_image, extent=[0, terrain_width, 0, terrain_height])
        logo_equipe1 = Image.open(
            'team logo/' + self.result[self.i].ht + '.png')  # Remplacez par le chemin du logo de l'équipe 1
        logo_equipe2 = Image.open('team logo/' + self.result[self.i].at + '.png')

        # Redimensionner les logos (ajustez la taille selon vos besoins)
        logo_equipe1 = logo_equipe1.resize((50, 50))
        logo_equipe2 = logo_equipe2.resize((50, 50))

        position1 = (216, 1)
        position2 = (346, 1)
        self.ax.imshow(logo_equipe1, extent=[position1[0], position1[0] + 50, position1[1], position1[1] + 50])
        self.ax.imshow(logo_equipe2, extent=[position2[0], position2[0] + 50, position2[1], position2[1] + 50])

        # Données de pourcentage des actions (exemple arbitraire)
        # Ici, j'utilise des valeurs arbitraires pour les pourcentages de chaque zone
        pourcentage_actions = self.heat_map
        # Normalisation des pourcentages pour les adapter aux dimensions de l'image du terrain
        pourcentage_actions = pourcentage_actions / np.max(pourcentage_actions) * 100

        # Affichage de l'image du terrain


        # Affichage de la heatmap superposée à l'image du terrain
        heatmap = self.ax.imshow(pourcentage_actions, origin='lower', alpha=0.5, cmap='hot',
                       extent=[0, terrain_width, 0, terrain_height])

        # Configuration du titre, des étiquettes, etc.
        self.ax.axis('off')
        self.figure.colorbar(heatmap, ax=self.ax)
        self.ax.set_title('Heat map')
        self.ax.set_xlabel('Position en x sur le terrain')
        self.ax.set_ylabel('Position en y sur le terrain')
        self.ax.grid(False)


class shot_position(match_detail_figures):
    def add_plot(self):
        # Charger l'image du but
        but_image = Image.open("but.jpg")  # Remplacez par le chemin de votre image du but
        but_width, but_height = but_image.size

        x_shots = [150, 150, 250, 400, 550, 250, 400, 550, 650, 650]  # Coordonnées x des tirs
        y_shots = [250, 190, 250, 250, 250, 190, 190, 190, 250, 190]  # Coordonnées y des tirs

        # Affichage de l'image du but
        self.ax.imshow(but_image, extent=[0, but_width, 0, but_height])

        # Affichage des tirs sur l'image du but
        self.ax.scatter(x_shots, y_shots, color='red', marker='x', label='Tirs', s=100)

        # Affichage du nombre de tirs dans la zone spécifique du but

        # Configuration du titre, des étiquettes, etc.
        self.ax.axis('off')
        self.ax.set_title('Visualisation des tirs dans une zone spécifique du but')
        self.ax.set_xlabel('Position en x sur le but')
        self.ax.set_ylabel('Position en y sur le but')
        self.ax.grid(False)

class attacs(match_detail_figures):
    def add_plot(self):
        matrix = self.matrix
        # Fonction pour afficher le nombre de tentatives

        # Supprimer la précédente flèche si elle existe

        # Récupérer le nombre de tentatives depuis la base de données
        # Remplacer cette ligne par la méthode pour obtenir le nombre de tentatives depuis la base de données
        nombre_tentatives = matrix[0, 0]  # Remplacez ceci par votre logique pour récupérer le nombre de tentatives
        nombre_tentatives = "{:.2f}".format(nombre_tentatives)
        # Afficher l'image du terrain de football
        image = Image.open("terrainfoot.jpg")  # Remplacez ceci par le chemin de votre image

        self.ax.imshow(image)

        logo_equipe1 = Image.open(
            'team logo/' + self.result[self.i].ht + '.png')  # Remplacez par le chemin du logo de l'équipe 1
        logo_equipe2 = Image.open('team logo/' + self.result[self.i].at + '.png')

        # Redimensionner les logos (ajustez la taille selon vos besoins)
        logo_equipe1 = logo_equipe1.resize((50, 50))
        logo_equipe2 = logo_equipe2.resize((50, 50))

        position1 = (216, 1)
        position2 = (346, 1)
        self.ax.imshow(logo_equipe1, extent=[position1[0], position1[0] + 50, position1[1], position1[1] + 50])
        self.ax.imshow(logo_equipe2, extent=[position2[0], position2[0] + 50, position2[1], position2[1] + 50])
        # Superposer les logos sur l'image du terrain

        # logo_equipe1 = Image.open("Logo_home")  # Remplacez par le chemin du logo de l'équipe 1
        # logo_equipe2 = Image.open("Logo_away")  # Remplacez par le chemin du logo de l'équipe 2

        # Redimensionner les logos (ajustez la taille selon vos besoins)
        # logo_equipe1 = logo_equipe1.resize((50, 50))
        # logo_equipe2 = logo_equipe2.resize((50, 50))

        # Superposer les logos sur l'image du terrain
        # image.paste(logo_equipe1, (246-30, 50))  # Position du logo de l'équipe 1
        # image.paste(logo_equipe2, (366-20, 50))  # Position du logo de l'équipe 2
        # self.ax.imshow(image)
        # Calculer les coordonnées de la flèche en fonction du nombre de tentatives
        x1 = 180  # Remplacez ceci par la coordonnée x de la flèche
        y1 = 50  # Remplacez ceci par la coordonnée y de la flèche
        dx1 = -100  # Remplacez ceci par le décalage x de la flèche
        dy1 = 0  # Remplacez ceci par le décalage y de la flèche

        # Dessiner la flèche avec le nombre de tentatives
        arrow = self.ax.arrow(x1, y1, dx1, dy1, width=5, color='red')
        self.ax.text(x1 + dx1 / 2, y1 + 10, f"{nombre_tentatives}%", fontsize=20, color='red')
        nombre_tentatives = matrix[1, 0]
        nombre_tentatives = "{:.2f}".format(nombre_tentatives)
        x2 = 180  # Remplacez ceci par la coordonnée x de la flèche
        y2 = 319  # Remplacez ceci par la coordonnée y de la flèche
        dx2 = -100  # Remplacez ceci par le décalage x de la flèche
        dy2 = 0  # Remplacez ceci par le décalage y de la flèche

        # Dessiner la flèche avec le nombre de tentatives
        arrow = self.ax.arrow(x2, y2, dx2, dy2, width=5, color='red')
        self.ax.text(x2 + dx2 / 2, y2 + 10, f"{nombre_tentatives}%", fontsize=20, color='red')
        nombre_tentatives = matrix[2, 0]
        nombre_tentatives = "{:.2f}".format(nombre_tentatives)
        x3 = 180  # Remplacez ceci par la coordonnée x de la flèche
        y3 = 185  # Remplacez ceci par la coordonnée y de la flèche
        dx3 = -100  # Remplacez ceci par le décalage x de la flèche
        dy3 = 0  # Remplacez ceci par le décalage y de la flèche

        # Dessiner la flèche avec le nombre de tentatives
        arrow = self.ax.arrow(x3, y3, dx3, dy3, width=5, color='red')
        self.ax.text(x3 + dx3 / 2, y3 + 10, f"{nombre_tentatives}%", fontsize=20, color='red')

        # Afficher l'image avec la flèche
        nombre_tentatives = matrix[0, 1]
        nombre_tentatives = "{:.2f}".format(nombre_tentatives)
        x4 = 432  # Remplacez ceci par la coordonnée x de la flèche
        y4 = 50  # Remplacez ceci par la coordonnée y de la flèche
        dx4 = 100  # Remplacez ceci par le décalage x de la flèche
        dy4 = 0  # Remplacez ceci par le décalage y de la flèche

        # Dessiner la flèche avec le nombre de tentatives
        arrow = self.ax.arrow(x4, y4, dx4, dy4, width=5, color='blue')
        self.ax.text(x4 - dx4 / 9, y4 + 10, f"{nombre_tentatives}%", fontsize=20, color='blue')
        nombre_tentatives = matrix[1, 1]
        nombre_tentatives = "{:.2f}".format(nombre_tentatives)
        x5 = 432  # Remplacez ceci par la coordonnée x de la flèche
        y5 = 319  # Remplacez ceci par la coordonnée y de la flèche
        dx5 = 100  # Remplacez ceci par le décalage x de la flèche
        dy5 = 0  # Remplacez ceci par le décalage y de la flèche

        # Dessiner la flèche avec le nombre de tentatives
        arrow = self.ax.arrow(x5, y5, dx5, dy5, width=5, color='blue')
        self.ax.text(x5 - dx5 / 9, y5 + 10, f"{nombre_tentatives}%", fontsize=20, color='blue')
        nombre_tentatives = matrix[2, 1]
        nombre_tentatives = "{:.2f}".format(nombre_tentatives)
        x6 = 432  # Remplacez ceci par la coordonnée x de la flèche
        y6 = 185  # Remplacez ceci par la coordonnée y de la flèche
        dx6 = 100  # Remplacez ceci par le décalage x de la flèche
        dy6 = 0  # Remplacez ceci par le décalage y de la flèche

        # Dessiner la flèche avec le nombre de tentatives
        arrow = self.ax.arrow(x6, y6, dx6, dy6, width=5, color='blue')
        self.ax.text(x6 - dx6 / 9, y6 + 10, f"{nombre_tentatives}%", fontsize=20, color='blue')
        self.ax.set_title('Attack distribution')

        # Afficher l'image avec la flèche
        self.ax.axis('off')  # Masquer les axes

