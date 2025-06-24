import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from male_voice_friend import MaleVoiceFriend
from female_voice_friend import FemaleVoiceFriend

class TalkingFriendApp:
    '''Main Aplication GUI'''

    def __init__(self):
        self.root = root
        self.root.title = "Talking Friend"
        self.root geometry('600x500')
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
        '''Setup control displays'''

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