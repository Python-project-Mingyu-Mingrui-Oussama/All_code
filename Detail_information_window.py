import pdb

from PIL import Image
from match_detail_figures import passes_for_passes, heat_map, shot_position, attacs
import numpy as np
from PyQt5.QtWidgets import QDialog, QWidget, QVBoxLayout, QPushButton, QLabel, QScrollArea
from matplotlib import pyplot as plt
from librosa.display import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
matplotlib.use("Qt5Agg")

class NewWindow(QDialog):
    def __init__(self, result, i, event):
        super().__init__()
        self.setGeometry(50, 50, 900, 600)
        self.result = result
        self.i = i
        self.event = event
        # pdb.set_trace()

        self.init_ui()

    def init_ui(self):
        # The title of the detail information window
        self.setWindowTitle(f'{self.result[self.i].date}  {self.result[self.i].ht}  vs  {self.result[self.i].at}')
        main_layout = QVBoxLayout(self)
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)  # 允许窗口小部件大小调整
        scroll_content = QWidget(self.scroll_area)
        main_layout.addWidget(self.scroll_area)
        self.match_detail_layout = QVBoxLayout(scroll_content)

        self.scroll_area.setWidget(scroll_content)

        '''
        canvas = passes_for_passes(self.result, self.event, self.i).canvas
        self.match_detail_layout.addWidget(canvas)

        canvas = heat_map(self.result, self.event, self.i).canvas
        self.match_detail_layout.addWidget(canvas)

        canvas = shot_position(self.result, self.event, self.i).canvas
        self.match_detail_layout.addWidget(canvas)

        canvas = attacs(self.result, self.event, self.i).canvas
        self.match_detail_layout.addWidget(canvas)
        '''

        canvas = heat_map(self.result, self.event, self.i).canvas
        self.match_detail_layout.addWidget(canvas)

        canvas = attacs(self.result, self.event, self.i).canvas
        self.match_detail_layout.addWidget(canvas)

        canvas = passes_for_passes(self.result, self.event, self.i).canvas
        self.match_detail_layout.addWidget(canvas)

        self.scroll_area.setWidget(scroll_content)