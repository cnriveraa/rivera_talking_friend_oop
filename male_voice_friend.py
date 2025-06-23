from voice_friend import VoiceFriend
import random

class MaleVoiceFriend(VoiceFriend):
    '''Male voice friend implementation.'''

    def _setup_voice(self):
        '''Setup male voice properties.'''
        voices = self.engine.getProperty('voices')
        for voice in voices:
            if "male" in voice.name.lower() or "david" in voice.name.lower():
                self.engine.setProperty('voice', voice.id)
                break
        else:
            self.engine.setProperty('voice', voices[0].id)  # Fallback to first available voice

        # Set speaking rate and volume
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 1.0)