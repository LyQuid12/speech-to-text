import os
try:
    import speech_recognition as sr
    from googlesearch import search
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
        print('Searching In Google...')
        print('')
        # to search
        query = (f"{text}")
  
        for j in search(query, tld="co.in", num=10, stop=10, pause=2):
             print(j)

        print('')
        os.system('pause')

    except:
        print("Sorry could not recognize what you said")
        os.system('pause')
