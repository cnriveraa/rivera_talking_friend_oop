from voice_friend import VoiceFriend
import random

class FemaleVoiceFriend(VoiceFriend):
    '''Female voice friend implementation.'''

    def _setup_voice(self):
        '''Setup female voice properties.'''
        voices = self.engine.getProperty('voices')
        for voice in voices:
            if 'female' in voice.name.lower() or 'zira' in voice.name.lower():
                self.engine.setProperty('voice', voice.id)
                break
        else:
            if len(voices) > 1:
                self.engine.setProperty('voices', voices[1].id)
            else:
                self.engine.setProperty('voices', voices[0].id)
                
        # Set female-typical voice properties
        self.engine.setProperty('rate', 170)
        self.engine.setProperty('volume', 0.8)