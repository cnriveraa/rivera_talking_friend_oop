from talking_friend_app import TalkingFriendApp
import tkinter as tk

def main():
    root = tk.Tk()
    app = TalkingFriendApp(root, root)  # Pass root as master to the app
    root.mainloop()

if __name__ == "__main__":
    main()