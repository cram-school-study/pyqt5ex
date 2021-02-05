import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QTimer

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
# 창 위치 변수로 저장
        self.x = 300
        self.y = 300
        self.w = 300
        self.h = 300
# 점 오른쪽 이동 - False, 왼쪽 이동 - True
# 점의 현재 위치값 변수
        self.flag = False
        self.point_width = 150
        self.point_height = 150
        self.initUI()

    def initUI(self):
# 창 크기대로 만들고, 타이틀 'ball'로 생성
        self.setGeometry(self.x, self.y, self.w, self.h)
        self.setWindowTitle('ball')
        self.show()

# 0.1초 단위로 타이머 실행
        self.timer = QTimer(self)
        self.timer.start(10)
        self.timer.timeout.connect(self.timeout)

    def timeout(self):
# 점의 이동 변수값 변동 지정
        if self.flag is True:
            if self.point_width == 1:
                self.flag = False
            self.point_width = self.point_width - 1
        elif self.flag is not True:
            if self.point_width == self.w-1:
                self.flag = True
            self.point_width = self.point_width + 1
# 점 이동값 화면 표출하기위한 update
        self.update()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_point(qp, self.point_width, self.point_height)

    def draw_point(self, qp, width, height):
        qp.setPen(QPen(Qt.blue, 8))
        qp.drawPoint(width, height)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
