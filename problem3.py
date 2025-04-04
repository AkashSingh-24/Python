import pyttsx3
engine = pyttsx3.init()
"""VOICE"""
"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1
engine.stop()
engine.say("chintu")
engine.runAndWait() 