# voice_emotion.py
import speech_recognition as sr
from transformers import pipeline

def analyze_voice_emotion():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("Listening... Please speak something:")

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)

        # Force PyTorch, skip TF to avoid keras.__internal__ issue
        classifier = pipeline("sentiment-analysis", framework="pt")
        result = classifier(text)[0]

        label = result['label'].lower()
        score = result['score']

        if label == 'positive':
            emotion = 'happy'
        elif label == 'negative':
            emotion = 'sad'
        else:
            emotion = 'neutral'

        print(f"Detected Voice Emotion: {emotion} ({score*100:.2f}%)")
        return emotion

    except Exception as e:
        print("Sorry, could not understand the audio:", e)
        return None
