import os
try:
    import speech_recognition as sr
except:
    print('Please Install all package in "requirements.txt"')

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Now!")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print('')
        print("You said : {}".format(text))
        print('')
        if(text == 'hello'):
            print('Computer said : Hi!')
            os.system('pause')
        else:
            os.system('pause')
    except:
        print("Sorry could not recognize what you said")
        os.system('pause')
