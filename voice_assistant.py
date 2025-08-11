import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser


# Function to speak text
def speak(text):
    print("Assistant:", text)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Function to take commands from the microphone
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
        return query.lower()
    except Exception:
        print("Could not understand, please repeat...")
        return None

# Function to search Google
def google_search(query):
    search_url = f"https://www.google.com/search?q={query}"
    speak(f"Searching Google for {query}")
    webbrowser.open(search_url)

# Main loop
if __name__ == "__main__":
    speak("Hello! I am your assistant. How can I help you today?")
    
    while True:
        command = take_command()

        if command:
            if "time" in command:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is {strTime}")

            

            elif "hello" in command:
                speak("Hello! How are you doing today?")

            elif "search" in command:
                query = command.replace("search", "").strip()
                if query:
                    google_search(query)
                else:
                    speak("What do you want me to search for?")
                    search_query = take_command()
                    if search_query:
                        google_search(search_query)

            elif "open youtube" in command:
                speak("Opening YouTube")
                webbrowser.open("https://youtube.com")

            elif "quit" in command or "exit" in command:
                speak("Goodbye!")
                break

            else:
                speak("I am not sure how to do that yet.")
