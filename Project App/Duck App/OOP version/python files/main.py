import tkinter as tk
from PIL import Image, ImageTk
from g_logic import Game
from utils import background, show_leaderboard, play_background_music


# Class for the main window
class Welcome:
    def __init__(self, root):
        self.root = root

        # Sets the window size
        self.root.geometry("500x500")

        # Prevent resizing bigger than 500x500
        root.maxsize(width=500, height=500)

        # Gives the window a title
        root.title("Give the Duck a Qwacker")

        # Displays the window icon
        icon = tk.PhotoImage(file="../img/duck.png")
        root.iconphoto(True, icon)

        # Creates the main canvas
        self.canvas = tk.Canvas(root, width=500, height=500)
        self.canvas.pack(fill="both", expand=True)
        self.bg_icon = ImageTk.PhotoImage(Image.open("../img/bg.png"))

        # Adds the background image
        background(self.canvas, self.bg_icon)

        # Creates the title text and displays it on the canvas
        self.canvas.create_text(
            250, 90,  # x, y position (centered)
            text="Welcome to the Game!",
            font=("Arial", 24, "bold"),
            fill="black"
        )

        # Creates the start button
        self.start = tk.Button(
            root,
            text="Start Game",
            font=("Arial", 15),
            width=20,
            anchor="center",
            bg="light blue",
            command=self.start_game
        )

        # Place the start button on the canvas
        self.canvas.create_window(250, 170, window=self.start)

        # Creates the instructions button and displays it on the canvas
        self.instructions = tk.Button(
            root,
            text="Instructions",
            font=("Arial", 15),
            width=20,
            anchor="center",
            bg="light blue",
            command=self.show_instructions
        )

        # Place the instructions button on the canvas
        self.canvas.create_window(250, 235, window=self.instructions)

        # Creates the leaderboard button
        self.leaderboard_btn = tk.Button(
            root,
            text="Leaderboard",
            font=("Arial", 15),
            width=20,
            anchor="center",
            bg="light blue",
            command=lambda: show_leaderboard(self.root) # only runs when the button is clicked
                                                                      # with these parameters
        )

        # Place the leaderboard button on the canvas
        self.canvas.create_window(250, 300, window=self.leaderboard_btn)

        # Creates the quit button
        self.quit = tk.Button(
            root,
            text="Quit",
            font=("Arial", 15),
            width=20,
            anchor="center",
            bg="light blue",
            command=self.quit_game
        )

        # Places the quit button on the canvas
        self.canvas.create_window(250, 365, window=self.quit)

        # Plays the background music
        play_background_music()

    # Function to start the game and open the game window
    def start_game(self):
        print("Starting game...")

        # Hides the main window
        self.root.withdraw()

        # Opens a new window for the game
        game_window = tk.Toplevel()

        # Runs the game class
        Game(game_window)

        # Uses (X) to close the game window and reopen the welcome window
        game_window.protocol("WM_DELETE_WINDOW", lambda: self.close_game(game_window))

    # Function to close the game window and open the welcome screen
    def close_game(self, game_window):
        game_window.destroy()  # Closes the game window
        self.root.deiconify()  # Shows the welcome window again after the game screen is closed

    # Function to quit the game and close the application
    def quit_game(self):
        self.root.quit()
        self.root.destroy()

    # Function to pop out the instructions in a separate window
    def show_instructions(self):
        # Creates the instructions window
        instructions_window = tk.Toplevel(self.root)
        instructions_window.title("Instructions")

        # Set the size of the pop out window
        instructions_window.geometry("500x500")

        # Sets the maximum size for the window to prevent resizing
        instructions_window.maxsize(width=500, height=500)

        # Creates a canvas
        canvas_instructions = tk.Canvas(instructions_window, width=500, height=500)
        canvas_instructions.pack(fill="both", expand=True)

        # Adds the background image
        background(canvas_instructions, self.bg_icon)

        # Creates a grey background box
        canvas_instructions.create_rectangle(28, 40, 475, 420, fill="gray", stipple="gray25", outline="")

        # Displays the instructions text
        canvas_instructions.create_text(
            250, 180,  # center position on x axis
            text="Game Instructions:\n\n"
                 "Get your duck home to his pond!\n"
                 "Answer 10 questions in time.\n"
                 "Time runs out = game over.\n"
                 "Answer correctly to feed your duck.\n"
                 "Wrong answers don't move your duck.\n\n"
                 "Have fun feeding your duck!",
            width=460,  # wraps text
            font=("Arial", 17, "bold"),
            fill="dark blue",
            justify="center"
        )

        # Creates the close button
        close_btn = tk.Button(
            instructions_window,
            text="Close",
            font=("Arial", 14),
            anchor="center",
            bg="light blue",
            command=instructions_window.destroy
        )

        # Place the close button on the canvas
        canvas_instructions.create_window(250, 460, anchor="center", window=close_btn)

# Main program
if __name__ == "__main__":
    root = tk.Tk()

    # Starts the welcome screen as the initial application window
    Welcome(root)

    # Runs the program loop
    root.mainloop()

