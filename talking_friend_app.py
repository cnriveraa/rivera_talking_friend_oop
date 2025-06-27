import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from male_voice_friend import MaleVoiceFriend
from female_voice_friend import FemaleVoiceFriend

class TalkingFriendApp:
    '''Main application GUI'''

    def __init__(self, root):
        self.root = root
        self.root.title("Talking Friend")
        self.root.geometry("600x400")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.friend = None

        # Create main frames
        self.control_frame = ttk.Frame(root, padding="10")
        self.control_frame.pack(fill=tk.X)

        self.chat_frame = ttk.Frame(root, padding="10")
        self.chat_frame.pack(fill=tk.BOTH, expand=True)

        # Setup contols
        self.setup_controls()

        # Setup chat display
        self.setup_chat()

    def setup_controls(self):
        '''Setup control widgets'''

        # Name entry
        ttk.Label(self.control_frame, text="Friend's Name:").grid(row=0, column=0, sticky=tk.W)
        self.name_entry = ttk.Entry(self.control_frame, width=20)
        self.name_entry.grid(row=0, column=1, sticky=tk.W)
        self.name_entry.insert(0, "")

        # Voice type selection
        ttk.Label(self.control_frame, text="Voice Type:").grid(row=1, column=0, sticky=tk.W)
        self.voice_type = tk.StringVar(value="male")
        ttk.Radiobutton(self.control_frame, text="Male", variable=self.voice_type, value="male").grid(row=1, column=1, sticky=tk.W)
        ttk.Radiobutton(self.control_frame, text="Female", variable=self.voice_type, value="female").grid(row=1, column=2, sticky=tk.W)

        # Mood selection
        ttk.Label(self.control_frame, text="Initial Mood:").grid(row=2, column=0, sticky=tk.W)
        self.mood_var = tk.StringVar(value="neutral")
        self.moods = ["happy", "sad", "excited", "angry", "neutral"]
        self.mood_menu = ttk.Combobox(self.control_frame, textvariable=self.mood_var, values=self.moods, state="readonly", width=10)
        self.mood_menu.grid(row=2, column=1, sticky=tk.W)

        # Create button
        self.create_button = ttk.Button(self.control_frame, text="Create Friend", command=self.create_friend)
        self.create_button.grid(row=2, column=2, sticky=tk.W)

        # Action buttons (initially disabled)
        self.action_frame = ttk.Frame(self.control_frame)
        self.action_frame.grid(row=3, column=0, columnspan=3, pady=(10,0), sticky=tk.W)

        self.greet_button = ttk.Button(self.action_frame, text="Greet", command=self.do_greet, state=tk.DISABLED)
        self.greet_button.pack(side=tk.LEFT, padx=2)

        self.joke_button = ttk.Button(self.action_frame, text="Tell Joke", command=self.do_joke, state=tk.DISABLED)
        self.joke_button.pack(side=tk.LEFT, padx=2)

        self.mood_button = ttk.Button(self.action_frame, text="Change Mood", command=self.do_express_feeling, state=tk.DISABLED)
        self.mood_button.pack(side=tk.LEFT, padx=2)

        self.special_button = ttk.Button(self.action_frame, text="Special Ability", command=self.do_special_ability, state=tk.DISABLED)
        self.special_button.pack(side=tk.LEFT, padx=2)

        # Change mood controls
        self.change_mood_frame = ttk.Frame(self.control_frame)
        self.change_mood_frame.grid(row=4, column=0, columnspan=3, pady=(5, 0), sticky=tk.W)

        ttk.Label(self.change_mood_frame, text="Change Mood:").pack(side=tk.LEFT)
        self.new_mood_var = tk.StringVar()
        self.new_mood_menu = ttk.Combobox(self.change_mood_frame, textvariable=self.new_mood_var, values=self.moods, state="readonly", width=10)
        self.new_mood_menu.pack(side=tk.LEFT, padx=5)

        self.change_button = ttk.Button(self.change_mood_frame, text="Change", command=self.do_change_mood, state=tk.DISABLED)
        self.change_button.pack(side=tk.LEFT)

    def setup_chat(self):
        '''Setup chat display area'''
        self.chat_text = scrolledtext.ScrolledText(self.chat_frame, wrap=tk.WORD, width=60, height=20)
        self.chat_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.chat_text.configure(state=tk.DISABLED)

    def create_friend(self):
        '''Create a new friend instance'''

        name =  self.name_entry.get().strip()

        if not name:
            messagebox.showerror("Error", "Please enter your name for you your")
            return
        
        voice_type = self.voice_type.get()
        initial_mood = self.mood_var.get()

        # Clear pevious friend if exists
        if self.friend:
            self.friend.stop()

        # Create appropriate friend instance
        if voice_type == "male":
            self.friend = MaleVoiceFriend(name, self.chat_text)
        else:
            self.friend = FemaleVoiceFriend(name, self.chat_text)

        self.friend.mood = initial_mood

        # Enable action buttons
        self.greet_button.config(state=tk.NORMAL)
        self.joke_button.config(state=tk.NORMAL)
        self.mood_button.config(state=tk.NORMAL)
        self.special_button.config(state=tk.NORMAL)
        self.change_button.config(state=tk.NORMAL)

        # Set change mood menu to current mood
        self.new_mood_var.set(initial_mood)

        # Clear chat
        self.chat_text.configure(state="normal")
        self.chat_text.delete(1.0, tk.END)
        self.chat_text.configure(state="disabled")

        # Initial greeting
        self.friend.greet()

    def do_greet(self):
        '''Handle greet action'''
        if self.friend:
            self.friend.greet()

    def do_joke(self):
        '''Handle tell joke action'''
        if self.friend:
            self.friend.tell_joke()

    def do_express_feeling(self):
        '''Handle express feeling action'''
        if self.friend:
            self.friend.express_feeling()

    def do_special_ability(self):
        '''Handle special ability action'''
        if self.friend:
            self.friend.special_ability()

    def do_change_mood(self):
        '''Handle change mood action'''
        if self.friend and self.new_mood_var.get():
            new_mood = self.new_mood_var.get()
            if new_mood == self.friend.mood:
                messagebox.showinfo("Info", f"Mood has changed to {new_mood}.")
            else:
                self.friend.change_mood(new_mood)

    def on_closing(self):
        '''Handle window close'''
        if self.friend:
            self.friend.stop()
        self.root.destroy()