import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
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

        self.ui.label_CharImg.mousePressEvent = self.goToMainMode

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
