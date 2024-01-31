import sys

import numpy as np
from PyQt5.QtGui import QFont, QColor, QPainter, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QCompleter, QProgressBar, \
    QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt


class PredictionWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.progressbar = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Prediction Window')
        self.setGeometry(100, 100, 520, 300)

        # 创建垂直布局
        layout = QVBoxLayout()

        # 添加 'Prediction' 标签
        prediction_label = QLabel('Prediction', self)
        prediction_label.setAlignment(Qt.AlignCenter)  # 居中对齐
        prediction_label.setStyleSheet("background-color: black; color: white;")  # 设置样式
        font = QFont()
        font.setPointSize(50)  # 设置字体大小
        font.setBold(True)  # 设置字体为粗体
        prediction_label.setFont(font)
        # prediction_label.setStyleSheet("color: black;")  # 设置字体颜色
        layout.addWidget(prediction_label, 2)

        matrix_a = np.load('club_names.npy', allow_pickle=True)  # 从矩阵a获取选项
        # 添加两个输入框和下拉框
        self.team1 = QLineEdit(self)
        self.team2 = QLineEdit(self)
        self.button = QPushButton('Start Prediction', self)


        self.team1.setPlaceholderText("Enter team name and choose from the box")
        self.team2.setPlaceholderText("Enter team name from the same league and choose from the box")

        # 创建一个QCompleter对象，并设置其自动完成的模式
        completer1 = QCompleter(matrix_a, self)
        completer1.setCaseSensitivity(0)  # 设置大小写不敏感
        self.team1.setCompleter(completer1)
        completer2 = QCompleter(matrix_a, self)
        completer2.setCaseSensitivity(0)  # 设置大小写不敏感
        self.team2.setCompleter(completer2)
        self.button.clicked.connect(self.prediction)

        # 将下拉框添加选项

        # 将组件添加到布局中
        layout.addWidget(self.team1, 1)
        layout.addWidget(self.team2, 1)
        layout.addWidget(self.button, 1)

        # 创建子窗口
        self.sub_window = QLabel(self)

        self.match_info_layout = QHBoxLayout(self.sub_window)

        layout.addWidget(self.sub_window, 6)

        # 设置窗口布局
        self.setLayout(layout)

        self.show()

    def prediction(self):
        for i in reversed(range(self.match_info_layout.count())):
            for j in reversed(range(self.match_info_layout.itemAt(i).layout().count())):
                self.match_info_layout.itemAt(i).layout().itemAt(j).widget().setParent(None)
            self.match_info_layout.itemAt(i).layout().setParent(None)

        team_a = self.team1.text()
        team_b = self.team2.text()

        self.progressbar = QProgressBar()
        self.progressbar.setMinimum(0)
        self.progressbar.setMaximum(100)
        self.progressbar.setValue(70)  # 设置进度为70%

        score = '70% —— 30%'

        # team1标签
        self.team_a_label = QLabel(f"{team_a}")
        font = QFont("Arial", 15, QFont.Bold)  # 使用 Arial 字体，字号 12，粗体
        self.team_a_label.setFont(font)

        self.team_a_label.setAlignment(Qt.AlignCenter)

        team_logo_ht_layout = QVBoxLayout()

        team_logo_ht_layout.addWidget(self.team_a_label)

        logo_path = 'team logo/' + self.team_a_label.text() + '.png'  # 替换为你的图片路径
        pixmap = QPixmap(logo_path)
        self.logo_ht_label = QLabel()
        self.logo_ht_label.setPixmap(pixmap)
        self.logo_ht_label.setAlignment(Qt.AlignCenter)
        team_logo_ht_layout.addWidget(self.logo_ht_label)

        self.match_info_layout.addLayout(team_logo_ht_layout, 1)

        score_button_layout = QVBoxLayout()

        # 比分标签
        score_label = QLabel(f"{score}")
        score_button_layout.addWidget(score_label)
        font_score = QFont("Arial", 20, QFont.Bold)  # 使用 Arial 字体，字号 12，粗体
        score_label.setFont(font_score)
        score_label.setAlignment(Qt.AlignCenter)

        score_button_layout.addWidget(self.progressbar)

        self.match_info_layout.addLayout(score_button_layout)

        # team2
        self.team_b_label = QLabel(f"{team_b}")
        self.team_b_label.setFont(font)
        self.team_b_label.setAlignment(Qt.AlignCenter)

        team_logo_at_layout = QVBoxLayout()

        team_logo_at_layout.addWidget(self.team_b_label)

        logo_path = 'team logo/' + self.team_b_label.text() + '.png'  # 替换为你的图片路径
        pixmap = QPixmap(logo_path)
        self.logo_at_label = QLabel()
        self.logo_at_label.setPixmap(pixmap)
        self.logo_at_label.setAlignment(Qt.AlignCenter)
        team_logo_at_layout.addWidget(self.logo_at_label)

        self.match_info_layout.addLayout(team_logo_at_layout, 1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PredictionWindow()
    sys.exit(app.exec_())
