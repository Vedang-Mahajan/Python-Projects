"""
ADMINISTRATOR: Vedang Mahajan
"""

from PyDictionary import PyDictionary
import speech_recognition as Spyder
import pyttsx3
import wikipedia
from playsound import playsound
import random
from googletrans import Translator

spyder_active_sound = "Spyder_Active_sound.mp3"
spyder_processing_sound = "Spyder_Processing_sound.mp3"
spyder_end_sound = "Spyder_end_sound.mp3"

response_s=("Spyder: ")
response_u=("You: ")

listening=0
ending_word = ["Goodbye", "Adios", "Cyan"]
greeting_word = ["Hi", "Hello", "Salut", "Hey", "Bonjour", "Hola", "Hey, wassup?"]
music = {"Alan Walker Alone":"Alan Walker - Alone.mp3",
         "Walker Alone":"Alan Walker - Alone.mp3",
         "Alan Alone":"Alan Walker - Alone.mp3",
         "End of time":"K-391, Alan Walker & Ahrix - End Of Time (Tribute Remix).mp3",
         "End of time tribute remix":"K-391, Alan Walker & Ahrix - End Of Time (Tribute Remix).mp3",
         "end of time remix":"K-391, Alan Walker & Ahrix - End Of Time (Tribute Remix).mp3",
         "Marshmello Alone":"Marshmello - Alone (Official Music Video).mp3"}

trans_dict={
             "english" : "en",
             "french" : "fr",
             "afrikaans" : "af",
             "irish" : "ga" ,
             "albanian" : "sq",
             "italian" : "it",
             "arabic" : "ar",
             "japanese" : "ja",
             "azerbaijani": "az",
             "kannada":"kn",
             "basque":"eu",
             "korean":"ko",
             "bengali":"bn",
             "latin":"la",
             "belarusian":"be",
             "latvian":"lv",
             "bulgarian":"bg",
             "lithuanian":"lt",
             "catalan" : "ca",
             "macedonian":"mk",
             "chinese simplefied": "zh-CN",
             "malay" : "ms",
             "chinese traditional" : "zh-TW",
             "maltese":"mt",
             "german":"de",
             "croatian":"hr",
             "norwegian":"no",
             "czech":"cs",
             "persian":"fa",
             "danish":"da",
             "polish":"pl",
             "dutch":"nl",
             "portuguese":"pt",
             "romanian":"ro",
             "esparanto":"eo",
             "russian":"ru",
             "estonian":"et",
             "serbian":"sr",
             "filipino":"tl",
             "slovak":"sk",
             "finnish":"fi",
             "slovenian":"sl",
             "spanish":"es",
             "galician":"gl",
             "swahili":"sw",
             "georgian":"ka",
             "swedish":"sv",
             "tamil":"ta",
             "greek":"el",
             "telugu":"te",
             "gujarati":"gu",
             "thai":"th",
             "haitian creole":"ht",
             "turkish":"tr",
             "hebrew":"iw",
             "ukarainian":"uk",
             "hindi":"hi",
             "urdu":"ur",
             "hungarian":"hu",
             "vietnamese":"vi",
             "icelandic":"is",
             "welsh":"cy",
             "indonesian":"id",
             "yiddish":"yi"
             }

Wake_Word="hey spider", "hello spider", "hola spider", "bonjour spider", "spider", "excuse me spider", "wassup spider", "okay spider"

engine = pyttsx3.init()

translator = Translator()

dictionary = PyDictionary()

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
#print (rate)                        #printing current voice rate
engine.setProperty('rate', 150)     # setting up new voice rate

"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
#print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female

while listening == 0:
    AudioIn=Spyder.Recognizer()
    with Spyder.Microphone() as source:
        print("I am Active.")
        audio=AudioIn.listen(source)
    command=AudioIn.recognize_google(audio)

    if "hello" or "hi" or "excuse me" or "spider" or "hey" or "bonjour" or "salut" in command:
         listening=1
         break
    else:
        listening = 0

while listening==1:
        AudioIn=Spyder.Recognizer()
        with Spyder.Microphone() as source:
            playsound(spyder_active_sound)
            audio=AudioIn.listen(source)
            playsound(spyder_processing_sound)
        command=AudioIn.recognize_google(audio)
        
        if "translate" and "to" in command:
            split_string = command.split("translate ", 1)
            
            substring = split_string[1]
            
            super_split_string = substring.split(" to", 1)
            
            super_substring = super_split_string[1]
            
            super_duper_split_string = super_substring.split(" ", 1)
            
            translate_word = super_split_string[0]
            translate_lang = super_duper_split_string[1]
            
            translated_sentence = translator.translate(translate_word, (trans_dict[translate_lang.lower()]), "en")
            
            print("")
            print(response_u+ command)
            print("")
            print(response_s+ translated_sentence.text)
            engine.say(translated_sentence.text)
            engine.runAndWait()
            
        elif "meaning" and "of" in command:
            split_string1 = command.split("meaning of ", 1)
            word_of_meaning = split_string1[1]
            
            meaning = dictionary.meaning(word_of_meaning)
            
            print(meaning)
            engine.say(meaning)
            engine.runAndWait()
            
        elif "hello" in command or "hi" in command or "excuse me" in command or "spider" in command or "hey" in command or "bonjour" in command or "salut" in command:
            greeting_num = random.randint(0, len(greeting_word))
            greeting = (greeting_word[greeting_num-1])
            print("")
            print(response_u+command)
            print("")
            print(response_s+ greeting)
            engine.say(greeting)
            engine.runAndWait()
        elif "your" and "name" in command:
            print("")
            print(response_u+command)
            print("")
            print(response_s+ "My name is Spyder, pleased to meet you!")
            engine.say("My name is Spider, pleased to meet you!")
            engine.runAndWait()
        elif "thank you" in command or "thanks" in command:
            print("")
            print(response_u+command)
            print("")
            print(response_s+ "You are Welcome!")
            engine.say("you are welcome")
            engine.runAndWait()
        elif "hands" in command or "Clean Hands" in command:
            print("")
            print(response_u+command)
            print("")
            print(response_s+ "You have to clean hands thoroughly by soap regularly. Rub them under running water for atleast 20 seconds.")
            engine.say("You have to clean hands thoroughly by soap regularly. Rub them under running water for at least 20 seconds")
            engine.runAndWait()
        elif "garbage" in command or "Garbage" in command:
            print("")
            print(response_u+command)
            print("")
            print(response_s+ "Garbage, trash, rubbish, or refuse is waste material that is discarded by humans, usually due to lack of utility. You have to keep seperate garbage bins for wet, and dry waste.")
            engine.say("Garbage, trash, rubbish, or refuse is waste material that is discarded by humans, usually due to lack of utility. You have to keep seperate garbage bins for wet, and dry waste.")
            engine.runAndWait()
        elif "sanitizer" in command or "Sanitizer" in command:
            print("")
            print(response_u+command)
            print("")
            print(response_s+ "Apply sanitizer to clean your hands , if soap and water is not available. Make sure that it contains Alcohol content to kill the micro-organism. It also acts quickly to kill microorganisms on hands.")
            engine.say("Apply sanitizer to clean your hands , if soap and water is not available. Make sure that it contains Alcohol content to kill the micro-organism. It also acts quickly to kill microorganisms on hands.")
            engine.runAndWait()
        elif "you" and "live" in command:
            print("")
            print(response_u+command)
            print("")
            print(response_s+ "I live in the device from which you are accessing me.")
            engine.say("I live in the device from which you are accessing me")
            engine.runAndWait()
        elif "how" and "are" and "you" in command:
            print("")
            print(response_u+command)
            print("")
            print(response_s+"I am great, just like always!")
            engine.say("I am great, just like always!")
            engine.runAndWait()
        elif "who is" in command:
            print("")
            print(response_u+command)
            print("")
            print(response_s+ wikipedia.summary(command, sentences=3))
            engine.say(wikipedia.summary(command, sentences=3))
            engine.runAndWait()
        #elif "play" in command:
            #song_name_split = command.split("play ", 1)
            #song_name = song_name_split[1]
            #playsound(music[song_name])
        elif "bye" in command:
            #engine.setProperty('language', 'hi')
            #engine.say("हैलो")
            print("")
            print(response_u+command)
            print("")
            break
        else:
            pass
        
word_num = random.randint(0, len(ending_word))
word = (ending_word[word_num-1])
print(response_s+ word)
engine.say(word)
engine.runAndWait()
playsound(spyder_end_sound)
