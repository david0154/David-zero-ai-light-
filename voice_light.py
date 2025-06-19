import pyttsx3

class VoiceLight:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 175)

    def speak(self, text):
        print(f"🗣️ Speaking: {text}")
        self.engine.say(text)
        self.engine.runAndWait()