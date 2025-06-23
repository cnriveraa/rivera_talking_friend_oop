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