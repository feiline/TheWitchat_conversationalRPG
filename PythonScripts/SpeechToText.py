import speech_recognition as sr


def RecordVoice():
    recording = True
    r = sr.Recognizer()
    transcript = ""
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.energy_threshold = 700
        print("Please say something to Geralt")
        audio = r.listen(source, timeout= 4, phrase_time_limit= 5)
        try:
            print("You have said the following: \n" +r.recognize_google(audio))
            transcript = str(r.recognize_google(audio))
            recording = False
        except Exception as e:
            recording = False
            transcript = "no valid sound"
            print("Error : " + str(e))
    return transcript
