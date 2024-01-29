from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor, QPixmap
from PyQt5.QtWidgets import QDialog, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel, QScrollArea, QSizePolicy, \
    QComboBox

import class_match_event
from Detail_information_window import NewWindow
from data import extract_all_location

season_dict = {}
for i in range(6):
    season_dict[f'201{7 - i} ~ 201{6 - i}'] = 2017 - i


def get_season_result(res, season):
    return [match for match in res if match.season == season]


class NewWindow_for_team_chosen(QDialog):
    def __init__(self, team):
        super().__init__()
        self.setGeometry(50, 50, 600, 900)
        self.team = team

        self.init_ui()

    def init_ui(self):
        # The title of the detail information window
        self.setWindowTitle(f'Matches of {self.team}')

        # 创建主布局
        main_layout = QVBoxLayout(self)

        # 创建两个子窗口
        self.sub_window1 = QLabel(self)
        self.sub_window2 = QLabel(self)
        self.sub_window1_layout = QVBoxLayout(self.sub_window1)
        self.sub_window2_layout = QVBoxLayout(self.sub_window2)

        # self.sub_window2.setStyleSheet("background-color: lightgreen;")

        main_layout.addWidget(self.sub_window1, 1)

        # 创建筛选框并添加选项
        self.season_combobox = QComboBox(self)
        self.season_combobox.addItem('All Seasons')  # 默认选项
        for i in range(6):
            season = f'201{7 - i} ~ 201{6 - i}'
            self.season_combobox.addItem(season)


        # 将筛选框添加到布局中
        main_layout.addWidget(self.season_combobox)

        main_layout.addWidget(self.sub_window2, 9)

        self.season_combobox.currentIndexChanged.connect(self.choose_season)  # 连接选择变化的信号

        self.text_of_League(self.team, 'black')
        self.window_of_match()


        self.show()

    def choose_season(self):
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
            for i in range(l - 1, -1, -1):
                match_widget = sub_MatchWidget(self.results, i)
                self.match_info_layout.addWidget(match_widget)
        else:
            season = season_dict[selected_season]
            season_results = get_season_result(self.results, season)
            l = len(season_results)
            for i in range(l - 1, -1, -1):
                match_widget = sub_MatchWidget(season_results, i)
                self.match_info_layout.addWidget(match_widget)

    def window_of_match(self):
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)  # 允许窗口小部件大小调整
        scroll_content = QWidget(self.scroll_area)
        self.scroll_area.setWidget(scroll_content)
        self.sub_window2_layout.addWidget(self.scroll_area)
        self.match_info_layout = QVBoxLayout(scroll_content)
        team_result = class_match_event.choosed_team_result(self.team)
        self.results = team_result
        num_team = len(team_result)
        for i in range(num_team - 1, -1, -1):
            match_widget = sub_MatchWidget(team_result, i)
            self.match_info_layout.addWidget(match_widget)

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


def show_detail(result, i):
    id_odsp = result[i].id_odsp
    event = extract_all_location(id_odsp)
    new_window = NewWindow(result, i, event)
    new_window.exec_()


class sub_MatchWidget(QWidget):
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
        detail_button.setFocusPolicy(Qt.NoFocus)

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
