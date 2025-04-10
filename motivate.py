import pyttsx3

def motivate_user():
    message = "You are doing great! Never give up. I'm cheering for you!"
    print("Motivation:", message)
    
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()
