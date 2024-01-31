import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout
from PyQt5.QtGui import QPixmap, QPainter, QPalette, QColor

from GUI import Windows
from Prediction import PredictionWindow


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Homepage')
        self.setGeometry(100, 100, 1100, 600)

        # 创建按钮
        btn_view_matches = QPushButton('Match Check', self)
        btn_estimate_results = QPushButton('Prediction of the match', self)

        # 设置按钮的宽度为页面宽度的五分之一
        button_width = self.width() // 5
        btn_view_matches.setFixedWidth(button_width)
        btn_estimate_results.setFixedWidth(button_width)

        # 创建垂直布局并将按钮添加到其中
        vbox = QVBoxLayout()

        # 添加伸缩空间，将按钮推到窗口的下四分之一位置
        vbox.addStretch(3)

        # 创建水平布局并将按钮添加到其中
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(btn_view_matches)
        hbox.addWidget(btn_estimate_results)
        hbox.addStretch(1)

        # 将水平布局添加到垂直布局中
        vbox.addLayout(hbox)

        # 添加伸缩空间，将按钮推到窗口的下四分之一位置
        vbox.addStretch(1)

        # 将布局应用到窗口
        self.setLayout(vbox)

        # 将按钮点击事件与处理函数相关联
        btn_view_matches.clicked.connect(self.view_matches)
        btn_estimate_results.clicked.connect(self.estimate_results)

        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("homepage.png").scaled(self.size())
        painter.drawPixmap(self.rect(), pixmap)

    def view_matches(self):
        windows = Windows()
        windows.exec_()

    def estimate_results(self):
        windows = PredictionWindow()
        windows.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())
