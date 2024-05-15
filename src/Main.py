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

    # def setupUI(self, ):


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



# if __name__ == "__light__":
#     app = QApplication([])

#     window = LightModeWindow()
#     window.show()

#     sys.exit(app.exec())
