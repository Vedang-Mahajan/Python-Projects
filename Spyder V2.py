import speech_recognition as Spyder
import pyttsx3
import wikipedia
import calendar

response=("Spyder: ")

listening=0

Wake_Word="hey spider", "hello spider", "hola spider", "bonjour spider", "spider", "excuse me spider", "wassup spider", "okay spider"

engine = pyttsx3.init()

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
#print (rate)                        #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate


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

    if "hello" or "hi" or "excuse me" or "spider" or "hey" in command:
         print(response+ "Yes?")
         engine.say("Yes?")
         engine.runAndWait()
         print(response+ "I am listening.")
         engine.say("I am listening")
         engine.runAndWait()
         listening=listening+1
         break

while listening==1:
        AudioIn=Spyder.Recognizer()
        with Spyder.Microphone() as source:
            print(" ")
            print(response+ "Go ahead.")
            engine.say("go ahead")
            engine.runAndWait()
            audio=AudioIn.listen(source)
        command=AudioIn.recognize_google(audio)
        
        if "name" in command:
            print(response+ "My name is Spyder from team Spyder Navigator, or SpyNav for short.")
            engine.say("My name is Spider from team Spyder Navigator, or Spynav for short.")
            engine.runAndWait()
            
        if "thank you" in command:
            print("You are Welcome!")
            engine.say("you are welcome")
            engine.runAndWait()

        if "hands" in command or "Clean Hands" in command:
            print(response+ "You have to clean hands thoroughly by soap regularly. Rub them under running water for atleast 20 seconds.")
            engine.say("You have to clean hands thoroughly by soap regularly. Rub them under running water for at least 20 seconds")
            engine.runAndWait()
        
        if "garbage" in command or "Garbage" in command:
            print(response+ "Garbage, trash, rubbish, or refuse is waste material that is discarded by humans, usually due to lack of utility. You have to keep seperate garbage bins for wet, and dry waste.")
            engine.say("Garbage, trash, rubbish, or refuse is waste material that is discarded by humans, usually due to lack of utility. You have to keep seperate garbage bins for wet, and dry waste.")
            engine.runAndWait()
        
        if "sanitizer" in command or "Sanitizer" in command:
            print(response+ "Apply sanitizer to clean your hands , if soap and water is not available. Make sure that it contains Alcohol content to kill the micro-organism. It also acts quickly to kill microorganisms on hands.")
            engine.say("Apply sanitizer to clean your hands , if soap and water is not available. Make sure that it contains Alcohol content to kill the micro-organism. It also acts quickly to kill microorganisms on hands.")
            engine.runAndWait()
        
        if "you" and "live" in command:
            print(response+ "I live in the device from which you are accessing me.")
            engine.say("I live in the device from which you are accessing me")
            engine.runAndWait()
            engine.runAndWait()
            
        if "who is" in command:
            print(response+ wikipedia.summary(command, sentences=3))
            engine.say(wikipedia.summary(command, sentences=3))
            engine.runAndWait()
        
        if "bye" in command:
            break
    
print(response+ "Goodbye!")
engine.say("Good Bye!")
engine.runAndWait()
