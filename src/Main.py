import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from MainModeGUI import Ui_MainModeWindow
from LightModeGUI import Ui_LightModeWindow

# Main Window Class
class MainModeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainModeWindow()
        self.ui.setupUi(self)
        self.setupMenuBar()

        # Light Mode Window를 멤버 변수로 유지함.
        self.light_mode_window = None

    def setupMenuBar(self):
        action_light_mode = self.ui.actionLight_Mode
        action_light_mode.triggered.connect(self.openLightModeWindow)

    def openLightModeWindow(self):
        # 이미 LightModeWindow가 열려있는지 확인함.
        if self.light_mode_window is None:
            self.hide()  # MainModeWindow를 숨김.
            self.light_mode_window = LightModeWindow()
            self.light_mode_window.show()

# Light Mode Window Class
class LightModeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LightModeWindow()
        self.ui.setupUi(self)

# First Start, Main Window Show
if __name__ == "__main__":
    app = QApplication([])

    window = MainModeWindow()
    window.show()

    sys.exit(app.exec())
