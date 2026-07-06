import tkinter as tk
from PIL import Image, ImageTk
from utils import background, save_score, show_leaderboard

# Class for game over screen
class End:
    def __init__(self, root, score, time_taken, GameClass):
        self.root = root

        # Sets the window size
        root.geometry("500x500")

        # Prevents resizing bigger than 500x500
        root.maxsize(width=500, height=500)

        # Gives the window a title
        root.title("Give the Duck a Qwacker")

        # Gives the window an icon
        icon = tk.PhotoImage(file="../img/duck.png")
        root.iconphoto(True, icon)

        # Creates the main canvas and resizes the image to fit
        self.canvas = tk.Canvas(root, width=500, height=500)
        self.canvas.pack(fill="both", expand=True)
        self.bg_icon = ImageTk.PhotoImage(Image.open("../img/bg.png").resize((500, 500)))

        # Adds the background image
        background(self.canvas, self.bg_icon)

        # Stores game data as variables for later use
        self.score = score
        self.GameClass = GameClass
        self.time = time_taken

        # Creates the game over text and displays it on the canvas
        self.canvas.create_text(
            250, 52,
            text="GAME OVER!!!",
            font=("Arial", 36, "bold"),
            justify="center"
        )

        # Draws a background box
        self.canvas.create_rectangle(40, 100, 460, 460, fill="lightblue", stipple="gray75", outline="")

        # Placeholder for greeting after player enters their name (empty at first)
        self.name_text = self.canvas.create_text(
            250, 133,
            text="",
            font=("Arial", 16, "bold"),
            justify="center"
        )

        # Creates the play again text and displays it on the canvas
        self.canvas.create_text(
            250, 180,
            text=f"Would you like to Play Again?",
            font=("Arial", 16, "bold"),
            justify="center"
        )

        # Creates the button for play again
        self.play_again = tk.Button(
            root,
            text="Play Again?",
            font=("Arial", 13),
            width=18,
            bg="light blue",
            command=self.restart_game
        )

        # Places the play again button on the canvas
        self.canvas.create_window(250, 225, anchor="center", window=self.play_again)

        # Creates the leaderboard text and displays it on the canvas
        self.canvas.create_text(
            250, 275,
            text=f"Leaderboard",
            font=("Arial", 15, "bold"),
            justify="center"
        )

        # Creates the button for the leaderboard
        self.leaderboard_btn = tk.Button(
            root,
            text="Leaderboard",
            font=("Arial", 13),
            width=18,
            bg="light blue",
            command=lambda: show_leaderboard(self.root) # only run when button is clicked
                                                                      # with these parameters
        )

        # Places the leaderboard button on the canvas
        self.canvas.create_window(250, 320, window=self.leaderboard_btn)

        # Creates the quit text and displays it on the canvas
        self.canvas.create_text(
            250, 370,
            text=f"Press 'Q' or click to Quit",
            font=("Arial", 15, "bold"),
            justify="center"
        )

        # Press Q to quit function
        self.root.bind("q", self.quit_game)
        self.root.bind("Q", self.quit_game)

        # Creates the button for quit
        self.quit = tk.Button(
            root,
            text="Quit",
            font=("Arial", 13),
            width=18,
            bg="light blue",
            command=self.quit_game
        )

        # Places the quit button on the canvas
        self.canvas.create_window(250, 415, anchor="center", window=self.quit)

        # Opens the score input popup immediately when the screen loads
        self.save_score()

        # Closes the window on press of (X) button ands quits the game
        self.root.protocol("WM_DELETE_WINDOW", self.quit_game)

    # Function to show the score popup and save the players name
    def save_score(self):
        # Creates the pop out window for name input
        score_window = tk.Toplevel(self.root)

        # Gives the pop out a title
        score_window.title("Enter Name")

        # Sets the size of the window
        score_window.geometry("400x300")

        # Prevents resizing bigger than 400x300
        score_window.maxsize(width=400, height=300)

        # Makes the pop out stay on top of the game over window
        score_window.transient(self.root)
        score_window.grab_set()
        score_window.focus_force()

        # Creates the canvas for the pop out
        canvas_score = tk.Canvas(score_window, width=400, height=300)
        canvas_score.pack(fill="both", expand=True)

        # Draws the background
        background(canvas_score, self.bg_icon)

        # Creates a background box and places it on the canvas
        self.box = canvas_score.create_rectangle(
            35, 35, 365, 240,
            fill="lightblue",
            outline="",
            stipple="gray75"
        )

        # Creates the score text and displays the score
        canvas_score.create_text(
            200, 70,
            text=f"You Scored: {self.score}",
            font=("Arial", 20, "bold")
        )

        # Creates the text and asks for the players name
        canvas_score.create_text(
            200, 125,
            text="Enter your name:",
            font=("Arial", 20, "bold")
        )

        # Creates the entry box for input and displays on the canvas
        name_entry = tk.Entry(score_window)
        canvas_score.create_window(200, 180, anchor="center", window=name_entry)

        # Function to submit the score
        def submit_score():
            name = name_entry.get()

            # Gives the default name of Player if input box is left empty
            if name == "":
                name = "Player"

            # Saves the name, time and score to the CSV file
            save_score(name, self.time, self.score)
            print("Score saved!")

            # Updates the name after saving and displays it on the game over screen
            self.canvas.itemconfig(self.name_text, text=f"Hi {name}!")

            # Closes the pop out window after saving
            score_window.destroy()

        # Creates the submit button
        submit_btn = tk.Button(
            score_window,
            text="Submit",
            font=("Arial", 13),
            width=14,
            bg="light blue",
            command=submit_score
        )

        # Places the submit button on the canvas
        canvas_score.create_window(200, 265, anchor="center", window=submit_btn)

        # Prevents closing the window without submitting the name and score
        score_window.protocol("WM_DELETE_WINDOW", lambda: None)


    # Function to restart the game
    def restart_game(self):
        self.root.destroy()  # fully closes the game over window

        # Opens a new window for the new game
        game_window = tk.Toplevel()

        # Runs the game class
        self.GameClass(game_window)

    # Function to quit the application
    def quit_game(self, event=None):
        # Stops the Tkinter event loop
        self.root.quit()

        # Closes the main window
        self.root.destroy()

        # Exits the program
        exit()