from PySide6.QtWidgets import QMainWindow

class SayHello(QMainWindow):
    def __init__(self):
        super().__init__()

    def SayingHello(self, window): # QMainWindow 인스턴스를 window로 받음
        window.statusBar().showMessage("안녕!")