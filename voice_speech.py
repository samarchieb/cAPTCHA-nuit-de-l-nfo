#word list
words = ["Bonjour", 'bonsoir', 'salut', 'comment ça va', "au revoir"] #peut etre un liste générer a partir d'un api 


#converting word to voice
import random 
import gtts
from playsound import playsound
def convert_word_to_voice(word):
    tts = gtts.gTTS(word)
    tts.save("{}.mp3".format(word))
    playsound("{}.mp3".format(word))
convert_word_to_voice("words[random.randrange(len(words))]")


#recording voice of the user 
import sounddevice as sd
import wavio as wv

def record_voice():
    freq = 44100
    duration = 5
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
    sd.wait()
    wv.write("recording1.wav", recording, freq, sampwidth=2)
    

#converting voice to word
import speech_recognition as sr
def convert_voice_to_word(file,):
    filename = file
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
        return text


#testing the input of the user with the given word 

def verifier(user_text, given_word):
    if user_text == given_word:
        print("successful")