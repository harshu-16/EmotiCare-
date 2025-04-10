# face_emotion.py
import cv2
from fer import FER

def analyze_face_emotion():
    detector = FER()
    cap = cv2.VideoCapture(0)  # Start webcam

    detected_emotion = None

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        result = detector.detect_emotions(frame)
        if result:
            emotion, score = detector.top_emotion(frame)
            if emotion:
                detected_emotion = emotion
                print(f"Detected Emotion: {emotion} ({score*100:.2f}%)")
                break

        cv2.imshow('Emotion Detection - Press Q to Exit', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return detected_emotion
