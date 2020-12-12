import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
print(sr.Microphone.list_microphone_names())
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(command)
            command = command.lower()
            if 'niyati' in command:
                command = command.replace('niyati', '')
                print(command)
    except:
        pass
    return command


def run_virtual_assistant():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        speak('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        speak(info)
    elif 'sick' in command:
        speak('yes, I have a headache')
    elif 'how are you' in command:
        speak('I am doing well , how about you?')
    elif 'are you single' in command:
        speak('I am in a relationship with wifi')
    elif 'joke' in command:
        speak(pyjokes.get_joke())
    else:
        speak('Please say the command again.')

while True:
    run_virtual_assistant()
