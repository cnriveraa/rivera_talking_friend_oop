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

    def special_ability(self):
        '''Male's friend special ability.'''
        self.say("Check this out! My deep voice can shake the room!")

        # Deep voice effect temporarily
        original_rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', 50)  # Slower rate for deep voice effect
        self.say("BOOM! Did you feel that? I can make the ground tremble with my voice!")
        self.engine.setProperty('rate', original_rate)