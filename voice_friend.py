from abc import ABC, abstractmethod
import pyttsx3
import random
import threading

class VoiceFriend(ABC):
    '''Abstract base class representing a voice friend.'''

    def __init__(self, name):
        self.name = name
        self.text_widget = text_widget
        self.engine = pyttsx3.init()
        self.setup_voice()
        self._mood - "neutral"
        self._running = True
        self._message_queue = []
        self._speech_thread = None

    def log(self, message):
        '''Add message to the text widget.'''
        self.text_widget.insert(tk.END, f"{message}\n")
        self.text_widget.see(tk.END)

    @abstractmethod
    def _setup_voice(self):
        '''Set the voice properties (to be implemented by subclasses)'''
        pass

    @property
    def moood(self, value):
        '''Set the mood with validation.'''
        valid_moods = ["happy", "sad", "excited", "angry", "neutral"]
        if value.lower() in valid_moods:
            self._mood = value.lower()
        else:
            self.log(f"Invalid mood. Keep current mood: {self._mood}")

    def say(self, text):
        '''Add speech to queue.'''
        self.message_queue.append(text)
        self.log(f"{self.name}: {text}")
        if not self._speech_thread or not self._speech_thread.is_alive():
            self._speech_thread = threading.Thread(target=self._process_speech_queue)
            self._speech_thread.start()

    def _process_speech_queue(self):
        '''Process the speech queue.'''
        while self._message_queue and self._running:
            text = self._message_queue.pop(0)
            self.engine.say(text)
            self.engine.runAndWait()

    def greet(self):
        '''Greet the user based on mood.'''
        greetings = {
            "happy": f"Hello there! I'm {self.name} and I'm feeling great today!",
            "sad": f"Hi... I'm {self.name}. Not feeling my best...",
            "excited": f"OH MY GOSH HI!!! I'm {self.name} and I'M SO EXCITED TO TALK TO YOUUU!!!",
            "angry": f"I'm {self.name}. What do you want?",
            "neutral": f"Hello, I'm {self.name}."
        }
        self.say(greetings.get(self._mood, greetings["neutral"]))

    def tell_joke(self):
        '''Tell random joke.'''
        jokes = [
            "Why don't the skeleton fight each other? It's because they don't have the guts!",
            "I'm reading a book about anti-gravity. It's impossible to put down!",
            "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Why don't scientists trust atoms? Because they make up everything!"
            "I used to be a baker, but I couldn't make enough dough.",
            "Why did the bicycle fall over? Because it was two-tired!",
            "What do you call fake spaghetti? An impasta!",
            "Why did the computer go to the doctor? Because it had a virus!",
            "My wallet is like an onion. I cry every time I open it because it's empty!"
            "I told my mom I'm sick. She gave me medicine, water, Vicks, and said 'Kakaselpon mo yan.'"
        ]
        joke = random.choice(jokes)
        self.say(joke)
        self.say("HAHAHAHA! That was funny, right? I know, I know, I'm hilarious!")

    def express_feeling(self):
        '''Express current feeling.'''
        feelings = {
            "happy": "I'm feeling on top of the world! Everything is just perfect!",
            "sad": "I'm feeling a bit at the moment. I could use a hug.",
            "excited": "I CAN'T CONTAIN MY EXCITEMENT! EVERYTHING IS THRILLING!",
            "angry": "I'm really annoyed right now. Leave me alone.",
            "neutral": "I'm feeling pretty normal. Just another day."
        }
        self.say(feelings.get(self._mood, "I'm not sure how I feel right now."))