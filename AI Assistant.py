#pip install pyaudio
#pip install pipwin
#pip install pyttsx3
#pip install speechrecognition
#pip list




#Function definitions for the following two functions
#for the "record_text" function we need following libraries so the python can access our microphone.
import speech_recognition as sr
import pyttsx3




import os
import openai

from openai import OpenAI

client = OpenAI( api_key)

# Function to convert text to speech
def SpeakText(command):

    #Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


#Initialize the recognizer (It is the Python object used to interact with microphone)
r = sr.Recognizer()

# Will allow the python to record audio input from PC microphone. It will convert audio input into the string.
def record_text():
    # Loop in case of errors or it cannot convert audio to text so we need to try again
    while(1):
        try:
            # use the microphone as source for input.
            with sr.Microphone() as source2:
                
                # Prepare recognizer to recieve input
                r.adjust_for_ambient_noise(source2, duration=0.9)

                #listen for the user's input
                audio2 = r.listen(source2)

                # Using google to recognize audio from users input
                MyText = r.recognize_google(audio2)

                return MyText


        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print  ("unknown error occured") 

    return

def send_to_chatGPT(messages, model="gpt-3.5-turbo"): #This function sending messages to ChatGPT


    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].message.content
    messages.append(response.choices[0].message)#we use messages array to append (put together) the text we recieved
    return message



messages = [] #Initialize messages Array where its purpose is to keep track of converstaion with ChatGPT
while(1):
    text = record_text() # It returns our audio commands into text format
    messages.append({"role":"user","content":text}) #we use messages array to append (put together) the text we recieved
    response = send_to_chatGPT(messages) #Once the messages array is updated we send it to ChatGPT and we recieve back and recorded in "response"
    SpeakText(response) # This Audibly say the response.
    

    print(response)
