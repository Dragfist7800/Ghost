from gtts import gTTS
import speech_recognition as sr
import os 
import webbrowser 
import smtplib
import datetime
import re
import bs4
from pygame import mixer
import random
import requests
import urllib.request
import urllib.parse
import pyaudio
num=1

def talk(audio):
    print(audio)
    for line in audio.splitlines():
        text_to_speech = gTTS(text=audio, lang='en-uk')
        text_to_speech.save('audio.mp3')
        mixer.init()
        mixer.music.load("audio.mp3")
        mixer.music.play()
def myCommand():

    r = sr.Recognizer()
    with sr.microphone() as source:
        print('Listening...')
        #wait for a second to let the recognizer adjust the  
        #energy threshold based on the surrounding noise level
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        #listen for user's input
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print('You said: ' + command + '/n')
    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Command Not Understood')
        command=myCommand()

    return command
def Ghost(command):
    errors=[
        "I don\'t know what you mean!",
        "Excuse me?",
        "Can you repeat it please?",
    ]

    if 'Hello' in command:
        talk('Hello! I am Ghost. How can I help you?')
    # Search on Google
    if 'open google and search' in command:
        reg_ex = re.search('open google and search (.*)', command)
        search_for = command.split("search",1)[1] 
        print(search_for)
        url = 'https://www.google.com/'
        if reg_ex:
            subgoogle = reg_ex.group(1)
            url = url + 'r/' + subgoogle
        talk('Okay!')
        driver = webdriver.Firefox(executable_path='/home/coderasha/Desktop/geckodriver')
        driver.get('http://www.google.com')
        search = driver.find_element_by_name('q')
        search.send_keys(str(search_for))
        search.send_keys(Keys.RETURN) # hit return after you enter search text
    #For just opening google
    elif 'open google' in command:
        #matching command to check it is available
        reg_ex = re.search('open google (.*)', command)
        url = 'https://www.google.com/'
        if reg_ex:
            subgoogle = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')
    # for just opening youtube
    elif 'open Youtube' in command:
        #matching command to check it is available
        reg_ex = re.search('open Youtube (.*)', command)
        url = 'https://www.youtube.com/'
        if reg_ex:
            subgoogle = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')
    #To send email
    if 'email' or 'gmail' in command:
        talk('What is the subject?')
        time.sleep(3)
        subject = myCommand()
        talk('What should I say?')
        time.sleep(3)
        message = myCommand()
        content = 'Subject: {}\n\n{}'.format(subject, message)

        #init gmail SMTP
        mail = smtplib.SMTP('smtp.gmail.com', 587)

        #identify to server
        mail.ehlo()

        #encrypt session
        mail.starttls()

        #login
        mail.login('danishboss022@gmail.com', 'rdaya7800')

        #send message
        mail.sendmail('FROM', 'TO', content)

        #end mail connection
        mail.close()

        talk('Email sent.')
    
    # search in wikipedia (e.g. Can you search in wikipedia apples)
    elif 'wikipedia' in command:
        reg_ex = re.search('wikipedia (.+)', command)
        if reg_ex: 
            query = command.split("wikipedia",1)[1] 
            response = requests.get("https://en.wikipedia.org/wiki/" + query)
            if response is not None:
                html = bs4.BeautifulSoup(response.text, 'html.parser')
                title = html.select("#firstHeading")[0].text
                paragraphs = html.select("p")
                for para in paragraphs:
                    print (para.text)
                intro = '\n'.join([ para.text for para in paragraphs[0:3]])
                print (intro)
                mp3name = 'speech.mp3'
                language = 'en'
                myobj = gTTS(text=intro, lang=language, slow=False)   
                myobj.save(mp3name)
                mixer.init()
                mixer.music.load("speech.mp3")
                
    elif 'stop' in command:
        mixer.music.stop()
    # Search videos on Youtube and play (e.g. Search in youtube believer)
    elif 'youtube' in command:
        talk('Ok!')
        reg_ex = re.search('youtube (.+)', command)
        if reg_ex:
            domain = command.split("youtube",1)[1] 
            query_string = urllib.parse.urlencode({"search_query" : domain})
            html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
            search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
            #print("http://www.youtube.com/watch?v=" + search_results[0])
            webbrowser.open("http://www.youtube.com/watch?v={}".format(search_results[0]))
            pass
    elif 'time' in task:
            srtTime = datetime.datetime.now().srttime("%H:%M:%S")
            speak(f"the time is {srtTime}")
    if 'stop' in command:
        talk('Good bye')
        exit()
    elif 'hello' in command:
        talk('Hello! I am Ghost. How can I help you?')
        time.sleep(3)
    elif 'who are you' in command:
        talk('I am Ghost')
        time.sleep(3)
    else:
        error = random.choice(errors)
        talk(error)
        time.sleep(3)


talk('Ghost is ready!')

#loop to executr ultiple commands
while True:
    time.sleep(4)
    Ghost(myCommand())