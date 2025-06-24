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

    def special_ability(self):
        '''Female friend's special ability'''
        self.say("Let me sing you a little song!")
        # Song: Soda Pop by Saja Boys (from the Netflix K-Animation film "KPop Demon Hunters".)
        song = "You're all I can think of, Every drop I drink up, You're my soda pop, my little soda pop. Cool me down, you're so hot, Pour me up, I won't stop. You're my soda pop, my little soda pop."
        self.say(song + "! ♫")