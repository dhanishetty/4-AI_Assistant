#pip install pyaudio
#pip install pipwin
#pip install pyttsx3
#pip install speechrecognition
#pip list





#Function definitions for the following two functions
#for the "record_text" function we need following libraries so the python can access our microphone.
import speech_recognition as sr
import pyttsx3

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

# Will allow the python program to take the string produced from the previous funtion and output it to a text file.
def output_text(text):
    # Open a text file using open function and appending "a" or adding text to it
    f = open("output.txt", "a") #Acess to the file is stored in f variable
    f.write(text) #using write function to append text to the file
    f.write("\n") #Text is seperated using new line character
    f.close() #Close access to the file
    return

while(1):
    text = record_text()
    output_text(text)

    print("Wrote text")