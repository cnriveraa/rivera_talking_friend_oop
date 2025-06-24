from logging import root
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from male_voice_friend import MaleVoiceFriend
from female_voice_friend import FemaleVoiceFriend

class TalkingFriendApp:
    '''Main Aplication GUI'''

    def __init__(self):
        self.root = root
        self.root.title = "Talking Friend"
        self.root.geometry('600x500')
        self.root.protocol('WM_DELETE_WINDOW', self.on_close)

        self.friend = None

        # Main frames
        self.control_frame = ttk.Frame(root, padding='10')
        self.control_frame.pack(fill=tk.x)

        self.chat_frame = ttk.Frame(root)
        self.chat_frame.pack(fill=tk.BOTH, expand=True)

        # Controls
        self.setup_controls()

        # Chat display
        self.setup_chat()

    def setup_control(self):
        '''Setup control widgets'''

        # Name entry
        ttk.Label(self.control_frame, text="Friend's Name:").grid(row=0, column=0, sticky=tk.w)
        self.name_entry = ttk.Entry(self.control_frame, width=20)
        self.name_entry.grid(row=0, column=1, sticky=tk.w)
        self.name_entry.insert(0, " ")

        # Voice type selection
        ttk.Label(self.control_frame, text="Voice Type:").grid(row=1, column=0, sticky=tk.w)
        self.voice_type = tk.StringVar(value="male")
        ttk.Radiobutton(self.control_frame, text="Male", variable=self.voice_type, value="male").grid(row=1, column=1, sticky=tk.w)
        ttk.Radiobutton(self.control_frame, text="Female", variable=self.voice_type, value="female").grid(row=1, column=1, sticky=tk.w)

        # Mood Selection
        ttk.Label(self.control_frame, text="Initial Mood:").grid(row=2, column=0, sticky=tk.w)
        self.mood_var = tk.StringVar(value='neutral')
        moods = ["happy", "sad", "excited", "angry", "neutral"]
        self.mood_menu = ttk.Combobox(self.control_frame, textvariable=self.mood_var, values=moods, state="readonly", width=10)
        self.mood_menu.grid(row=2, column=1, sticky=tk.w)

        # Create button
        self.create_button = ttk.Button(self.control_frame, text="Create Friend", command=self.create_friend)
        self.create_button.grid(row=2, column=2, padx=5)

        # Action Buttons (disabled initially)
        self.action_frame = ttk.Frame(self.control_frame)
        self.action_frame.grid(row=3, column=0, columnspan=3, pady=(10, 0), sticky=tk.w)

        self.greet_button = ttk.Button(self.action_frame, text="Greet", command=self.do_greet, state=tk.DISABLED)
        self.greet_button.grid(side=tk.LEFT, padx=2)

        self.joke_button = ttk.Button(self.action_frame, text="Tell a Joke", command=self.do_tell_joke, state=tk.DISABLED)
        self.joke_button.grid(side=tk.LEFT, padx=2)

        self.mood_button = ttk.Button(self.action_frame, text="Express Mood", command=self.do_express_mood, state=tk.DISABLED)
        self.mood_button.grid(side=tk.LEFT, padx=2)

        self.special_ability_button = ttk.Button(self.action_frame, text="Special Ability", command=self.do_special_ability, state=tk.DISABLED)
        self.special_ability_button.grid(side=tk.LEFT, padx=2)

        # Change mood controls
        self.change_mood_frame = ttk.Frame(self.control_frame)
        self.change_mood_frame.grid(row=4, column=0, columnspan=3, pady=(5, 0), sticky=tk.w)

        ttk.Label(self.change_mood_frame, text="Change Mood").pack(side=tk.LEFT)
        self.new_mood_var = tk.StringVar()
        self.new_mood_menu = ttk.Combobox(self.change_mood_frame, textvariable=self.new_mood_var, values=moods, state="readonly", width=10)
        self.new_mood_menu.pack(side=tk.LEFT)

    def setup_chat(self):
        '''Setup chat display'''
        self.chat_text = scrolledtext.ScrolledText(self.chat_frame, wrap=tk.WORD, width=60, height=20)
        self.chat_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.chat_text.configure(state='disabled')

    def create_friend(self):
        '''Create new friend instance'''
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showerror("Error.", "Please enter a name for your friend.")
            return
        
        voice_type = self.voice_type.get()
        initial_mood = self.new_mood_var.get()

        # Clear previous friend if exists
        if self.friend:
            self.friend.stop()

        # Create an appropriate friend type
        if voice_type == "male":
            self.friend = MaleVoiceFriend(name, self.chat_text)
        else:
            self.friend = FemaleVoiceFriend(name, self.chat_text)

        self.friend.mood = initial_mood

        # Enable action buttons
        self.greet_button.config(state=tk.NORMAL)
        self.joke_button.config(state=tk.NORMAL)
        self.mood_button.config(state=tk.NORMAL)
        self.special_ability_button.config(state=tk.NORMAL)
        self.change_button.config(state=tk.NORMAL)

        # Clear chat
        self.chat_text.configure(state='normal')
        self.chat_text.delete(1.0, tk.END)
        self.chat_text.configure(state='disabled')

        # Initial greeting
        self.friend.greet()

    def do_greet(self):
        '''Handle greet action'''
        if self.friend:
            self.friend.greet()

    def do_tell_joke(self):
        '''Handle tell joke action'''
        if self.friend:
            self.do_tell_joke()

    def do_express_mood(self):
        '''Handle express mood action'''
        if self.friend:
            self.do_express_mood()

    def do_special_ability(self):
        if self.friend:
            self.do_special_ability()

    def do_change_mood(self):
        if self.friend and self.new_mood_var.get():
            self.friend.change_mood(self.new_mood_var.get())

    def on_close(self):
        '''Handle window close'''
        if self.friend:
            self.friend.stop()
        self.root.destrot()