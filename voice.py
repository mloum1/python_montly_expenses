import speech_recognition as sr
import os

# Fonction pour activer le narrateur
def activer_narrateur():
    os.system("Narrator.exe")

# Fonction de détection de la voix
def detecter_voix():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Parlez maintenant...")
        audio = r.listen(source)

    try:
        texte = r.recognize_google(audio, language="fr-FR")
        print("Vous avez dit : " + texte)
        activer_narrateur()
    except sr.UnknownValueError:
        print("Impossible de reconnaître la voix.")
    except sr.RequestError as e:
        print("Erreur lors de la requête au service de reconnaissance vocale : " + str(e))

# Appel de la fonction de détection de voix
detecter_voix()