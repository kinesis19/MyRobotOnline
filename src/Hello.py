import random
from PySide6.QtWidgets import QMainWindow
from gtts import gTTS
import os
import playsound
from UserData import Users

class SayHello(QMainWindow):
    def __init__(self):
        super().__init__()
        self.user = Users()


    def SayingHello(self, window): # QMainWindow 인스턴스를 window로 받음

        greetings_with_name = [f"안녕하세요, {self.user.name}!", f"Hello, {self.user.name}!"]
        greetings_without_name = ["반가워요!", "Hello World!"]
        
        if random.choice([True, False]):  # 사용자 이름을 포함하는 경우와 포함하지 않는 경우를 랜덤으로 선택
            selected_greeting = random.choice(greetings_with_name)
            window.statusBar().showMessage(selected_greeting)
            SpeakingHello(selected_greeting)
        else:
            selected_greeting = random.choice(greetings_without_name)
            window.statusBar().showMessage(selected_greeting)
            SpeakingHello(selected_greeting)

def SpeakingHello(text):
    tts = gTTS(text=text, lang='ko')
    fileName = 'VoiceHello.mp3'
    tts.save(fileName)
    playsound.playsound(fileName)
    os.remove(fileName)
