import streamlit as st
from face_emotion import analyze_face_emotion
from voice_emotion import analyze_voice_emotion
from interaction import interact_based_on_emotion
from alert_system import send_alert_email

st.title("🧠 EmotiCare - Emotion Detection and Support App")

if st.button("Analyze My Emotion"):
    st.write("📸 Detecting face emotion...")
    face_emotion = analyze_face_emotion()

    st.write("🎙️ Detecting voice emotion...")
    voice_emotion = analyze_voice_emotion()

    # Decide final emotion
    if face_emotion in ['sad', 'angry', 'disgust'] or voice_emotion in ['sad', 'angry', 'disgust']:
        final_emotion = face_emotion if face_emotion in ['sad', 'angry', 'disgust'] else voice_emotion
        st.warning(f"⚠️ You seem {final_emotion}. Sending alert...")
        send_alert_email(final_emotion)
    else:
        final_emotion = face_emotion or voice_emotion
        st.success("😊 You're doing good!")

    # Interact based on emotion
    interact_based_on_emotion(final_emotion)
