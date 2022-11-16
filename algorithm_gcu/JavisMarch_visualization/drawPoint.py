import sys

from PyQt5.QtCore import *

from PyQt5.QtGui import *

from PyQt5.QtWidgets import *

#from PyQt5 import uic



#form_class = uic.loadUiType("pointCanvas1.ui")[0]



#class WindowClass(QMainWindow, form_class):

class WindowClass(QMainWindow):

    def __init__(self):

        #QImage(가로,세로) 캔버스 생성 및 brush 인자 세팅

        super().__init__()

        self.image = QImage(QSize(1000, 600), QImage.Format_RGB32)

        self.image.fill(Qt.white)

        self.drawing = False

        self.brush_size = 5

        self.brush_color = Qt.black

        self.last_point = QPoint()

        self.initUi()



    def initUi(self):

        # 화면 클리어하는 메뉴 만들기

        menubar = self.menuBar()

        menubar.setNativeMenuBar(False)

        menu = menubar.addMenu('Menu')



        clear_action = QAction('Clear', self)

        clear_action.setShortcut('Ctrl+C')

        clear_action.triggered.connect(self.clear)

        menu.addAction(clear_action)



        # 창 이름 및 (생성위치x, 생성위치y, 창크기 x, 창크기y) 설정, 보여주기

        self.setWindowTitle("pointCanvas")

        self.setGeometry(300,300,1000,600)

        self.show()



    def paintEvent(self, e): #그림그리는곳 정보 설정

        canvas = QPainter(self)

        canvas.drawImage(self.rect(), self.image, self.image.rect())



    def mousePressEvent(self, e): # 마우스 클릭시 이벤트

        if e.button() == Qt.LeftButton:

            self.drawing = True

            self.last_point = e.pos()



            painter = QPainter(self.image)

            painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap))

            painter.drawPoint(e.pos())

            self.getPos(e.pos())

            self.update()





    # def mouseMoveEvent(self, e): # 마우스 클릭 후 이동 시, 선 그리기

    #     if (e.buttons() & Qt.LeftButton) & self.drawing:

    #         painter = QPainter(self.image)

    #         painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap))

    #         painter.drawLine(self.last_point, e.pos())

    #         self.getPos(e.pos())

    #         self.last_point = e.pos()

    #         self.update()



    def mouseReleaseEvent(self, e):

        if e.button() == Qt.LeftButton:

            self.drawing = False



    def clear(self):

        self.image.fill(Qt.white)

        self.update()    



    def getPos(self, pos):#x, y좌표 받아서 출력

        contentsRect = self.image.rect()

        if pos not in contentsRect:

            # 캔버스 마진을 벗어나면 무시

            return

        print('X={}, Y={}'.format(pos.x(), pos.y()))





if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = WindowClass()

    sys.exit(app.exec_())


