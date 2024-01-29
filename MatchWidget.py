import class_match_event
from PyQt5.QtWidgets import (QWidget,
                             QPushButton, QVBoxLayout, QLabel, QHBoxLayout)
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt
from Detail_information_window import NewWindow
from data import extract_all_location
from team_chosen_from_league import NewWindow_for_team_chosen


def show_team_chosen(team):
    new_window = NewWindow_for_team_chosen(team)
    new_window.exec_()


def show_detail(result, i):
    id_odsp = result[i].id_odsp
    event = extract_all_location(id_odsp)
    new_window = NewWindow(result, i, event)
    new_window.exec_()


class MatchWidget(QWidget):
    def __init__(self, result, i):
        super().__init__()

        layout = QVBoxLayout()
        time = result[i].date
        team_a = result[i].ht
        score = f'{result[i].htscore} - {result[i].atscore}'
        team_b = result[i].at
        # 时间标签
        time_label = QLabel(f"{time}")
        layout.addWidget(time_label)
        time_label.setAlignment(Qt.AlignCenter)

        # 主队、比分和客队水平布局
        self.match_info_layout = QHBoxLayout()

        # 主队标签
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

        self.match_info_layout.addLayout(team_logo_ht_layout)



        # 比分和按钮垂直布局
        score_button_layout = QVBoxLayout()

        # 比分标签
        score_label = QLabel(f"{score}")
        score_button_layout.addWidget(score_label)
        font_score = QFont("Arial", 10, QFont.Bold)  # 使用 Arial 字体，字号 12，粗体
        score_label.setFont(font_score)
        score_label.setAlignment(Qt.AlignCenter)

        # 详细信息按钮
        detail_button = QPushButton("Detail")
        detail_button.clicked.connect(lambda: show_detail(result, i))
        score_button_layout.addWidget(detail_button)

        # 将比分和按钮的垂直布局添加到水平布局中
        self.match_info_layout.addLayout(score_button_layout)

        # 客队标签
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

        self.match_info_layout.addLayout(team_logo_at_layout)

        layout.addLayout(self.match_info_layout)

        self.setLayout(layout)

    def mousePressEvent(self, event):
        # 检查是否点击了 self.team_a_label
        if self.team_a_label.geometry().contains(event.pos()) or self.logo_ht_label.geometry().contains(event.pos()):
            team_chosen = self.team_a_label.text()
        elif self.team_b_label.geometry().contains(event.pos()) or self.logo_at_label.geometry().contains(event.pos()):
            team_chosen = self.team_b_label.text()
        show_team_chosen(team_chosen)

