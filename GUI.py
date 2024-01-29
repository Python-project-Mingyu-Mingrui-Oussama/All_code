import pdb
import sys

import numpy as np
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QMessageBox, QApplication, QVBoxLayout, QLabel, QHBoxLayout, QSizePolicy,
                             QSplitter, QLineEdit, QCompleter, QScrollArea, QDialog, QListWidget, QListWidgetItem,
                             QComboBox)
from PyQt5.QtGui import QFont, QPixmap, QColor
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from MatchWidget import MatchWidget

import class_match_event
from class_match_event import E0_results, SP1_results, D1_results, I1_results, F1_results

num_E = len(E0_results)
num_SP = len(SP1_results)
num_D = len(D1_results)
num_I = len(I1_results)
num_F = len(F1_results)
season_dict = {}
for i in range(6):
    season_dict[f'201{7 - i} ~ 201{6 - i}'] = 2017 - i


def get_season_result(res, season):
    return [match for match in res if match.season == season]


class Windows(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 1200, 900)
        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        # Creat the buttons for the different leagues
        self.E0btn = self.LeagueButton('LeagueLogo/E0.png')
        self.E0btn.setObjectName('E0')
        self.SP1btn = self.LeagueButton('LeagueLogo/SP1.png')
        self.SP1btn.setObjectName('SP1')
        self.D1btn = self.LeagueButton('LeagueLogo/D1.jpeg')
        self.D1btn.setObjectName('D1')
        self.I1btn = self.LeagueButton('LeagueLogo/I1.png')
        self.I1btn.setObjectName('I1')
        self.F1btn = self.LeagueButton('LeagueLogo/F1.png')
        self.F1btn.setObjectName('F1')
        self.E0btn.clicked.connect(self.chooseLeague)
        self.SP1btn.clicked.connect(self.chooseLeague)
        self.D1btn.clicked.connect(self.chooseLeague)
        self.I1btn.clicked.connect(self.chooseLeague)
        self.F1btn.clicked.connect(self.chooseLeague)
        self.E0btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.SP1btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.D1btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.I1btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.F1btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # 创建主布局
        main_layout = QHBoxLayout(self)

        # 创建左侧布局
        left_layout = QVBoxLayout()

        self.search_line_edit = QLineEdit(self)
        self.search_line_edit.setPlaceholderText("Enter team name and choose from the box")

        # 创建一个QCompleter对象，并设置其自动完成的模式
        completer = QCompleter(self.get_team_names(), self)
        completer.setCaseSensitivity(0)  # 设置大小写不敏感
        self.search_line_edit.setCompleter(completer)
        completer.activated.connect(self.chooseTeam)


        # 将左侧布局添加到主布局中，宽度比例为1
        main_layout.addLayout(left_layout, 1)
        left_layout.addWidget(self.search_line_edit, 1)
        left_layout.addWidget(self.E0btn, 2)
        left_layout.addWidget(self.SP1btn, 2)
        left_layout.addWidget(self.D1btn, 2)
        left_layout.addWidget(self.I1btn, 2)
        left_layout.addWidget(self.F1btn, 2)

        self.setLayout(left_layout)

        # 创建右侧布局
        right_layout = QVBoxLayout()

        # 将右侧布局添加到主布局中，宽度比例为2
        main_layout.addLayout(right_layout, 2)

        # 创建两个子窗口
        self.sub_window1 = QLabel(self)
        self.sub_window2 = QLabel(self)
        self.sub_window1_layout = QVBoxLayout(self.sub_window1)
        self.sub_window2_layout = QVBoxLayout(self.sub_window2)

        # self.sub_window2.setStyleSheet("background-color: lightgreen;")

        right_layout.addWidget(self.sub_window1, 1)

        # 创建筛选框并添加选项
        self.season_combobox = QComboBox(self)
        self.season_combobox.addItem('All Seasons')  # 默认选项
        for i in range(6):
            season = f'201{7 - i} ~ 201{6 - i}'
            self.season_combobox.addItem(season)

        self.season_combobox.setVisible(False)  # 初始时隐藏
        self.season_combobox.currentIndexChanged.connect(self.choose_season)  # 连接选择变化的信号

        # 将筛选框添加到布局中
        right_layout.addWidget(self.season_combobox)

        right_layout.addWidget(self.sub_window2, 9)

        self.show()

    def choose_season(self):
        if self.run_choose_season:
            for i in reversed(range(self.sub_window2_layout.count())):
                self.sub_window2_layout.itemAt(i).widget().setParent(None)
            self.scroll_area = QScrollArea()
            self.scroll_area.setWidgetResizable(True)  # 允许窗口小部件大小调整
            scroll_content = QWidget(self.scroll_area)
            self.scroll_area.setWidget(scroll_content)
            self.sub_window2_layout.addWidget(self.scroll_area)
            self.match_info_layout = QVBoxLayout(scroll_content)
            selected_season = self.season_combobox.currentText()
            if selected_season == 'All Seasons':
                l = len(self.results)
                print(l)
                for i in range(l - 1, -1, -1):
                    match_widget = MatchWidget(self.results, i)
                    self.match_info_layout.addWidget(match_widget)
            else:
                season = season_dict[selected_season]
                season_results = get_season_result(self.results, season)
                l = len(season_results)
                for i in range(l - 1, -1, -1):
                    match_widget = MatchWidget(season_results, i)
                    self.match_info_layout.addWidget(match_widget)


    def window_of_match(self, league):
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)  # 允许窗口小部件大小调整
        scroll_content = QWidget(self.scroll_area)
        self.scroll_area.setWidget(scroll_content)
        self.sub_window2_layout.addWidget(self.scroll_area)
        self.match_info_layout = QVBoxLayout(scroll_content)
        self.run_choose_season = False
        self.season_combobox.setCurrentText('All Seasons')
        if league == 'E0':
            self.results = E0_results
            for i in range(num_E - 1, -1, -1):
                match_widget = MatchWidget(E0_results, i)
                self.match_info_layout.addWidget(match_widget)
        elif league == 'SP1':
            self.results = SP1_results
            for i in range(num_SP - 1, -1, -1):
                match_widget = MatchWidget(SP1_results, i)
                self.match_info_layout.addWidget(match_widget)
        elif league == 'D1':
            self.results = D1_results
            for i in range(num_D - 1, -1, -1):
                match_widget = MatchWidget(D1_results, i)
                self.match_info_layout.addWidget(match_widget)
        elif league == 'I1':
            self.results = I1_results
            for i in range(num_I - 1, -1, -1):
                match_widget = MatchWidget(I1_results, i)
                self.match_info_layout.addWidget(match_widget)
        elif league == 'F1':
            self.results = F1_results
            for i in range(num_F - 1, -1, -1):
                match_widget = MatchWidget(F1_results, i)
                self.match_info_layout.addWidget(match_widget)
        else:
            team_result = class_match_event.choosed_team_result(league)
            self.results = team_result
            num_team = len(team_result)
            for i in range(num_team - 1, -1, -1):
                match_widget = MatchWidget(team_result, i)
                self.match_info_layout.addWidget(match_widget)
        self.run_choose_season = True

    def get_team_names(self):
        # 返回一些球队的英文名字作为自动完成的数据源
        team_names = np.load('club_names.npy', allow_pickle=True)
        return team_names

    def chooseTeam(self):
        selected_text = self.search_line_edit.text()
        self.season_combobox.setVisible(True)  # 按键时显示
        # 或者使用 self.team_input.text() 获取当前输入框的文本
        print('You choose:', selected_text)
        for i in reversed(range(self.sub_window1_layout.count())):
            self.sub_window1_layout.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.sub_window2_layout.count())):
            self.sub_window2_layout.itemAt(i).widget().setParent(None)
        self.text_of_League(selected_text, 'black')
        self.window_of_match(selected_text)

    def LeagueButton(self, path):
        button = QPushButton(self)
        button.setIcon(QIcon(path))
        button.setIconSize(QtCore.QSize(100, 100))
        button.setToolTip('Choose one league you want')
        return button

    def chooseLeague(self):
        click_btn = self.sender()
        league = click_btn.objectName()
        self.season_combobox.setVisible(True)  # 按键时显示
        # print(league)
        '''
                for item in self.sub_window1.children():
            item.deleteLater()
        '''
        for i in reversed(range(self.sub_window1_layout.count())):
            self.sub_window1_layout.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.sub_window2_layout.count())):
            self.sub_window2_layout.itemAt(i).widget().setParent(None)
        if league == 'E0':
            self.text_of_League('Premier League', 'purple')
            self.window_of_match('E0')
        elif league == 'SP1':
            self.text_of_League('LALIGA', 'orange')
            self.window_of_match('SP1')
        elif league == 'D1':
            self.text_of_League('BUNDESLIGA', 'red')
            self.window_of_match('D1')
        elif league == 'I1':
            self.text_of_League('Serie A', 'blue')
            self.window_of_match('I1')
        elif league == 'F1':
            self.text_of_League('LIGUE 1', 'navy')
            self.window_of_match('F1')

    def text_of_League(self, text_input, color_input):
        text_label_sub_window1 = QLabel()
        text_label_sub_window1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        text = text_input
        font = QFont("Arial", 40, QFont.Bold)  # 使用 Arial 字体，字号 12，粗体
        color = QColor(color_input)  # 设置文本颜色
        text_label_sub_window1.setText(text)
        text_label_sub_window1.setFont(font)
        text_label_sub_window1.setAlignment(Qt.AlignCenter)  # 文本居中显示
        text_label_sub_window1.setStyleSheet(f"color: {color.name()};")  # 设置文本颜色
        self.sub_window1_layout.addWidget(text_label_sub_window1)
        # text_label_sub_window1.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message', f"Are you sure to quit?", QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = Windows()
    sys.exit(app.exec_())
