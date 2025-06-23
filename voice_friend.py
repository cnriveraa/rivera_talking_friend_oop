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