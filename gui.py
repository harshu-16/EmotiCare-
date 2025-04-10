from face_emotion import analyze_face_emotion
from voice_emotion import analyze_voice_emotion
from motivate import motivate_user
from alert_system import send_alert_email
from interaction import interact_based_on_emotion  # speaks to user
from music_player import play_music_based_on_emotion  # 🆕 plays Tamil songs

def run_gui():
    print("🎬 Running EmotiCare... detecting emotion...")

    # Step 1: Detect face emotion
    face_emotion = analyze_face_emotion()
    
    # Step 2: Detect voice emotion
    print("🎤 Now analyzing voice emotion...")
    voice_emotion = analyze_voice_emotion()

    # Step 3: Decide final emotion
    if face_emotion in ['sad', 'angry', 'disgust'] or voice_emotion in ['sad', 'angry', 'disgust']:
        final_emotion = face_emotion if face_emotion in ['sad', 'angry', 'disgust'] else voice_emotion
        print("😟 User looks upset. Sending alert to caretaker...")
        send_alert_email(final_emotion)
    else:
        final_emotion = face_emotion or voice_emotion
        print("😊 User looks fine.")

    print(f"🧠 Final Detected Emotion: {final_emotion}")

    # Step 4: Talk to the user
    interact_based_on_emotion(final_emotion)

    # Step 5: Play music based on emotion
    play_music_based_on_emotion(final_emotion)

    # Step 6: Motivate user if emotion is not negative
    if final_emotion not in ['sad', 'angry', 'disgust']:
        motivate_user()
