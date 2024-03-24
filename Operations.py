import pyttsx3
import openai
import pyaudio
import wave
import time
import pyttsx3  #python text to speech
import speech_recognition as sr
import speech_recognition as sr
from datetime import date
#----------Raspberry Libraries---------------#
import gpiozero
from gpiozero import LED
from gpiozero import Motor
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
#----------end Raspberry Libraries---------------#

from time import sleep
r = sr.Recognizer()
mic = sr.Microphone()

# This stack is to keep the track of the functions of the car
class StringStack:
    def _init_(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty")
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty")
            return None

    def size(self):
        return len(self.stack)
#----------------------------------------------------------------------------

def speak(text):
    speaker = pyttsx3.init()
    speaker.setProperty('rate', 150)
    speaker.say(text)
    speaker.runAndWait()


def del_stack(stack, element):
    """Deletes the first occurrence of the specified element from the stack."""
    temp_stack = []
    while stack:
        popped = stack.pop()
        if popped != element:
            temp_stack.append(popped)
    while temp_stack:
        stack.append(temp_stack.pop())

# to search on pins
def search(self, element):
        for item in reversed(self.items):
            if item == element:
                return True
        return False

# Car Movement
def Movement(string,stack):
    print(stack)
    words1 = ["back","backward"]
    words2 = ["front","forward","up","upward"]
    left_side = Motor(3, 4)
    right_side = Motor(17, 27)
    if "right" in string: 

        print("turning right")
        speak("turning right")
        left_side.forward()
        right_side.stop()
        time.sleep(0.3)
        left_side.stop()
        stack.push("turning right")
        #processors.insert(0,"turning right")
    elif "left" in string:
        print("turning left")
        speak("turning left")
        right_side.forward()
        left_side.stop()
        time.sleep(0.3)
        right_side.stop()
        stack.push("turning left")
    elif any(word in string for word in words1):
        print("moving backward")
        speak("moving backward")
        left_side.backward() 
        right_side.backward() 
        time.sleep(0.3)
        left_side.stop()
        right_side.stop()
        stack.push("going back")
    elif any(word in string for word in words2):
        print("moving forward")
        speak("moving forward")
        left_side.forward()
        right_side.forward()
        time.sleep(0.3)
        left_side.stop()
        right_side.stop()
        stack.push("going forward")
        
# Car headligh
def light(string,stack):
    print(stack)
    headligh_PIN = 18
    headligh = LED(headligh_PIN)
    if "on" in string:
        headligh.on()
        print("headlight is turned On")
        speak("headlight is turned On")
        stack.push("headlight is on")
    elif  "off" in string:
        headligh.off()
        print("headlight is turned Off")

# Car indicator
def indicator(string,stack):
    
    word1 = ["off","close"]
    word2 = ["right","left"]
    
    if not any(word in string for word in word2 ):

        if "on" in string:
            speak("which indicator do you want to turned on")
            with mic as source:
                audio = r.listen(source)
            words = r.recognize_google(audio)
            
            string = string+words

    if any(word in string for word in word1 ):
        Left_Indicator_PIN = 16
        Right_Indicator_PIN = 20
        Left_Indicator = LED(Left_Indicator_PIN)
        Right_Indicator = LED(Right_Indicator_PIN)
        if "left" in string:
            #print("left indicator Off")
            Left_Indicator.off()
            speak("left indicator Off")
            #stack.push("left indicator")
        elif "right" in string:
            #print("right indicator Off")
            Right_Indicator.off()
            speak("right indicator Off")
            #stack.push("right indicator")
        print("Indicator is turned Off")
    elif  "on" in string:
        if "left" in string:
            print("turned on left indicator") #dont forgot to turn off right indicator
            Left_Indicator.on()
            speak("turned on left indicator")  
            stack.push("left indicator")
        elif "right" in string:
            print("turned on right indicator")#dont forgot to turn off left indicator
            Right_Indicator.on()
            speak("turned on right indicator")
            stack.push("right indicator")
                
# Car door
def door(string,stack):
    word1 = ["off","close"]
    word2 = ["right","left"]
    if not any(word in string for word in word2 ):
        if "open" in string:
            speak("which door do you want to turned on")
            with mic as source:
                audio = r.listen(source)
            words = r.recognize_google(audio)
            
            #str = input("which door do you want to turned on : ")
            string = string+words
    GPIO.setup(23,GPIO.OUT) 
    left_door = GPIO.PWM(23, 50)
    left_door.start(0)
    GPIO.setup(24,GPIO.OUT)  # Sets up pin 12 to an output (instead of an input)
    right_door = GPIO.PWM(24, 50)     # Sets up pin 12 as a PWM pin
    right_door.start(0)    
    if any(word in string for word in word1 ):  
        if "left" in string:
            left_door.ChangeDutyCycle(12)
            print("left door Off")
            speak("left door Off")
            #stack.push("left door")
        elif "right" in string:
            right_door.ChangeDutyCycle(6)
            #stack.push("right door")
            print("right door is turned Off")
            speak("door is turned Off")
    elif  "open" in string:
        if "left" in string:
            left_door.ChangeDutyCycle(8)
            print("turned on left door")
            speak("turned on left door")
            stack.push("left door")
        elif "right" in string:
            right_door.ChangeDutyCycle(12)
            print("turned on right door")
            speak("turned on right door")
            stack.push("right door")
    #else
        #here write a code to turn off indicator pin

# # Car wiper
# def wiper(string,stack):
#     print(stack)
#     if "on" in string:
#         print("wiper is turned On")
#         speak("wiper is turned on")
#         stack.push("wiper is on")
#         # print("stack is : ")
#         # stack.peek()
#     elif  "off" in string:
#         print("wiper is turned Off")
#         speak("wiper is turned Off")
#         del_stack(stack,"wiper is on")


def check_word_in_string(string,stack):
    words = ["turn off", "turned off", "turn of", "turned of" , "of", "off"]
    words1 = ["move", "go", "come"]
    words2 = ["light","headlight"]
    matching_words = [word for word in words1 if word == string]
    if matching_words:
        #print(stack.pop()) #here we get the pin number then write a code to turn of this pin
        print("temp")
    else:
        if any(word in string for word in words1): #for car movement
            Movement(string,stack)
        elif any(word in string for word in words2):#for headlight
            light(string,stack)
        elif "indicator" in string:
            indicator(string,stack)
        elif "door" in string:
            door(string,stack)
        # elif "wiper" in string:
        #     wiper(string,stack)
        


# Main
# speak("Hello I'm your assistant here to help u. Please give me command to proceed")
stack = StringStack()
while True:
    try:
        print("Call me....")
        with mic as source:
            audio = r.listen(source)
        words = r.recognize_google(audio)
        if "Jarvis" in words:
            speak("Hello sir, How can i help you")
            CHUNK = 1024  # Number of frames per audio chunk
            FORMAT = pyaudio.paInt16  # Audio format (16-bit integer)
            CHANNELS = 1  # Number of channels (mono)
            RATE = 44100  # Sampling rate (samples per second)
            RECORD_SECONDS = 5  # Duration of recording

            # Create an instance of PyAudio
            p = pyaudio.PyAudio()

            # Open a stream to record audio from the microphone
            stream = p.open(format=FORMAT,
                            channels=CHANNELS,
                            rate=RATE,
                            input=True,
                            frames_per_buffer=CHUNK)

            print("* Recording audio...")

            frames = []

            # Record audio for the specified duration
            for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                data = stream.read(CHUNK)
                frames.append(data)

            print("* Finished recording")

            # Stop the stream and close it
            stream.stop_stream()
            stream.close()

            # Terminate the PyAudio instance
            p.terminate()

            # Save the recorded audio to a WAV file
            wf = wave.open("recorded.wav", "wb")
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
            wf.close()

            print("* Audio saved to recorded_audio.wav")

        #------------------------------------------------------------------
            openai.organization = "org-iVuvSLiObMLmVJOihyNu2vqq"

            openai.api_key= "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"

            audio_file = open(r"C:\\Users\\Pushpak\\Desktop\\Car\\recorded.wav","rb")
            transcript = openai.Audio.translate("whisper-1",audio_file)
            string = transcript['text']
            print(string)
            
            string = string.lower()
            #stack = StringStack()
            check_word_in_string(string,stack)
            print("----------------------------------------")
            print("stack elements")
            print("----------------------------------------")
            print(stack)
            print("----------------------------------------")
            print("----------------------------------------")
            time.sleep(1)
        else:
            print("could not recognize")
    except:
        print("continue.....")
        continue