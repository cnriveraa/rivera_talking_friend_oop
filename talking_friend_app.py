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