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

    def tell_joke(self):
        '''Override with more masculine humor.'''
        jokes = [
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "How do you organize a space party? You planet!",
            "I'm on a seafood diet. Every time I see food, I eat it!",
            "They said real men don't cry — try steppin on a LEGO.",
            "I don't chase girls. I chase unli-rice.",
            "Real men cook, especially when mom isn't home.",
            "I don't need six-pack abs... I just have a six-pack jokes.",
            "I go to the gym... to take mirror selfies.",
            "I can lift heavy things... espcially my food to my mouth.",
            "Gym is life — until cheat day turns into cheat week!",
            "I walk like a boss... especially when I see my crush passing by."
        ]
        joke = random.choice(jokes)
        self.say(joke)
        self.say("HAHAHA! That was a good one, right? I know! I'm really funny!")