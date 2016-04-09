#!/usr/bin/env python3
# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import pyaudio
import subprocess
import os

# audio message from user using speech recognition
r = sr.Recognizer()
with sr.Microphone() as source:
	print ("Hey this is Jarvis what i can do for you")
	#voice message is store in audio
	audio = r.listen(source)


# here we use google's api which convert audio into text

try:
	# text is stored in command
	command = r.recognize_google(audio)
	#print (command)
	# convert string in lower case letter 
	command=command.lower()
	#print (command)
	try:
		test = subprocess.Popen([command], stdout=subprocess.PIPE)
		output = test.communicate()[0]
		subprocess.call(["espeak",output])
	except:
		os.system(command)
	#except print ("can't execute command")
		




except sr.UnknownValueError:
	print ("Google speech recognizer can not understand audio")
except sr.RequestError as e:
	print ("Could not request results from Google Speech Recognition service; {0}".format(e))
