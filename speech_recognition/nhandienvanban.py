import speech_recognition as SR

r=SR.Recognizer()

audio=SR.AudioFile('ghiam.mp3')

with audio as source:
	audioData=r.record(source)
type(audioData)
text=r.recognize_google(audioData)
print (text)
