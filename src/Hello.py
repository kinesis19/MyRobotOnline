import random
from PySide6.QtWidgets import QMainWindow
from UserData import Users

class SayHello(QMainWindow):
    def __init__(self):
        super().__init__()
        self.user = Users()

    def SayingHello(self, window): # QMainWindow 인스턴스를 window로 받음
        greetings_with_name = [f"안녕하세요, {self.user.name}!", f"Hello, {self.user.name}!"]
        greetings_without_name = ["반가워요!", "Hello World!"]
        
        if random.choice([True, False]):  # 사용자 이름을 포함하는 경우와 포함하지 않는 경우를 랜덤으로 선택
            window.statusBar().showMessage(random.choice(greetings_with_name))
        else:
            window.statusBar().showMessage(random.choice(greetings_without_name))
