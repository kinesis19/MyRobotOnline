import random
import threading
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

        greetings_with_name = [f"Hello, {self.user.name}!", f"Welcome, {self.user.name}!"]
        greetings_without_name = ["How are you?", "Welcome Back! I missed you"]
        
        # 대사 랜덤 선택
        if random.choice([True, False]):  
            selected_greeting = random.choice(greetings_with_name)
            window.statusBar().showMessage(selected_greeting)
            # 음성 생성 및 재생을 비동기적으로 처리
            threading.Thread(target=self.SpeakingHello, args=(selected_greeting,)).start()
        else:
            selected_greeting = random.choice(greetings_without_name)
            window.statusBar().showMessage(selected_greeting)
            # 음성 생성 및 재생을 비동기적으로 처리
            threading.Thread(target=self.SpeakingHello, args=(selected_greeting,)).start()

    def SpeakingHello(self, text):
        tts = gTTS(text=text, lang='en')
        fileName = 'VoiceHello.mp3'
        tts.save(fileName)
        playsound.playsound(fileName)
        os.remove(fileName)