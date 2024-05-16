import sys
import threading
from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtGui import QMovie, QPixmap, QAction
from PySide6.QtCore import QDir
from MainModeGUI import Ui_MainModeWindow
from LightModeGUI import Ui_LightModeWindow
from Hello import SayHello

# Main Window Class
class MainModeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainModeWindow()
        self.ui.setupUi(self)
        self.setupMenuBar()

        # Light Mode Window를 멤버 변수로 유지함.
        self.light_mode_window = None

        # 클릭 이벤트 감지
        self.ui.pushButton_1.clicked.connect(self.button1Clicked)

        # 캐릭터 이미지 세팅
        # resources 폴더 내의 GIF 이미지 경로 설정
        gif_path = QDir.current().filePath("resources/ImgCharacter.gif")

        # QLabel에 GIF 이미지 표시
        movie = QMovie(gif_path)
        self.ui.label_CharImg.setMovie(movie)
        movie.start()

    def setupMenuBar(self):
        action_light_mode = self.ui.actionLight_Mode
        action_light_mode.triggered.connect(self.openLightModeWindow)

    def openLightModeWindow(self):
        # 이미 LightModeWindow가 열려있는지 확인함.
        self.hide()  # MainModeWindow를 숨김.
        if self.light_mode_window is None:
            self.light_mode_window = LightModeWindow(parent=self)
        # 이미 생성된 LightModeWindow가 있는 경우 show만 호출함.
        self.light_mode_window.show()

    def button1Clicked(self):
        hello_instance = SayHello()  # SayHello 클래스의 인스턴스 생성
        hello_instance.SayingHello(self)  # 메서드 호출,  QMainWindow를 SayingHello 메서드에 넘김
        
# Light Mode Window Class
class LightModeWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_LightModeWindow()
        self.ui.setupUi(self)

        self.setWindowOpacity(0.5)

        # 캐릭터 이미지 세팅2
        # resources 폴더 내의 PNG 이미지 경로 설정
        png_path = QDir.current().filePath("resources/ImgCharacterHead2.png")
        pixmap = QPixmap(png_path)
        pixmap_resized = pixmap.scaled(100, 100)
        self.ui.label_CharHeadImg.setPixmap(pixmap_resized)

        
        self.setWindowFlags(
            QtCore.Qt.FramelessWindowHint # 윈도우 타이틀바 제거
            | QtCore.Qt.WindowStaysOnTopHint # 항상 최상위 윈도우로 유지
            | QtCore.Qt.SplashScreen # 작업 표시줄에 안 나타남
        )
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

        quitAction = QAction("E&xit", self, shortcut="Ctrl+Q",
                triggered=QApplication.instance().quit)
        self.addAction(quitAction)
        self.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        
        backAction = QAction("MainMode", self, shortcut="Ctrl+1",
            triggered=self.goToMainMode)
        self.addAction(backAction)
        self.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)

        self.draggable = True  # 창을 드래그하여 이동 가능하도록 플래그 설정
        self.old_pos = self.pos()  # 이전 위치 저장

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.draggable:
            self.old_pos = event.globalPos() - self.pos()  # 창을 클릭한 위치 저장

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton and self.draggable:
            self.move(event.globalPos() - self.old_pos)  # 창을 새로운 위치로 이동

    def mouseReleaseEvent(self, event):
        pass
    
    def goToMainMode(self, event):
        if self.parent():
            self.parent().show()
        self.close()


# First Start, Main Window Show
if __name__ == "__main__":
    app = QApplication([])

    window = MainModeWindow()
    window.show()

    sys.exit(app.exec())
