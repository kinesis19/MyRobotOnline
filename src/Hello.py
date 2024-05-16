from PySide6.QtWidgets import QMainWindow
from UserData import Users

class SayHello(QMainWindow):
    def __init__(self):
        super().__init__()
        self.user = Users()

    def SayingHello(self, window): # QMainWindow 인스턴스를 window로 받음
        window.statusBar().showMessage(f"안녕하세요, {self.user.name}!")