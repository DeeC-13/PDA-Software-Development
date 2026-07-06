import tkinter as tk
import time  # Used for the countdown timer
from PIL import Image, ImageTk
from duck import Duck
from crackers import Cracker
from qbox import Questions
from g_over import End
from utils import background, play_correct, play_wrong, you_win_sound, you_lose_sound


# Class for main game screen
# Controls the gameplay, UI, scoring system, timer, and game state
class Game:
    def __init__(self, root):  # Initialises the main game window, canvas, and all game objects
        self.root = root

        # Sets the window size
        root.geometry("700x600")

        # Create the canvas
        self.canvas = tk.Canvas(root, width=700, height=600)
        self.canvas.pack()

        # Prevents resizing the window bigger than 700x600
        root.maxsize(width=700, height=600)

        # Gives the window a title
        root.title("Give the Duck a Qwacker")

        # Gives the window an icon
        icon = tk.PhotoImage(file="../img/duck.png")
        root.iconphoto(True, icon)

        # Loads the background image and resizes to the window
        self.bg_img = Image.open("../img/background.png").resize((700, 600))
        self.bg_icon = ImageTk.PhotoImage(self.bg_img)

        # Draws the background image to the canvas
        background(self.canvas, self.bg_icon)

        # Game state control variable (prevents actions after game ends)
        self.game_over = False

        # Specifies the Duck and crackers initial positions
        self.duck = Duck(self.canvas, 32, 455, "../img/duck2.png")
        self.cracker_x = 91
        self.cracker_y = 447

        # Creates the cracker object
        self.cracker = Cracker(self.canvas, self.cracker_x, self.cracker_y)

        # Sets the score variable to 0
        self.score = 0

        # Creates the score text and displays it on the canvas
        self.score_text = self.canvas.create_text(
            55, 580,  # Position of the score
            text=f"Score = {self.score}",
            font=("Arial", 15),
            fill="#000000"  # White with 50% transparency
        )

        # Creates the countdown text and displays it on the canvas
        self.timer_text = self.canvas.create_text(
            620, 580,
            text="Countdown: 50",
            font=("Arial", 15),
            fill="#000000"  # White with 50% transparency
        )

        # Sets the length of the game to countdown in seconds
        self.game_time = 50

        # Records the start time for the timer calculations
        self.start_time = time.time()

        # Starts the countdown loop
        self.update_timer()

        # Creates the questions object (handles the question display and answers)
        self.questions = Questions(self.root, self.canvas)

        # Sets the function to call when the answer is correct/wrong
        self.questions.on_correct = self.correct_answer
        self.questions.on_wrong = self.wrong_answer

        # Gets the first question from the list in the CSV file
        q = self.questions.get_next_question()
        if q:  # If a question exists
            self.current_question = q  # Stores the current question in 'self.current_question'
            self.questions.set_question(q)  # Displays the question on the screen

        # Result label shows feedback for correct/wrong answers
        self.result_label = tk.Label(self.root, text="", font=("Arial", 14))

        # Prevents multiple answers being processed at same time
        self.question_locked = False

    # Function to update the countdown timer every second and ends the game when time reaches zero
    def update_timer(self):
        # Stops the timer if the game has ended
        if self.game_over:
            return

        # Calculates how much time has passed
        elapsed = int(time.time() - self.start_time)
        print(f"{elapsed}")

        # Calculates the remaining time
        remaining = max(self.game_time - elapsed, 0)

        # Updates the timer text on the screen as it counts down
        self.canvas.itemconfig(self.timer_text, text=f"Countdown: {remaining}")
        print(f"{remaining}")

        if remaining > 0:
            # Updates the timer every 1 second
            self.root.after(1000, self.update_timer)
            return

       # Sets the game over flag to true so other game logic stops running
        self.game_over = True

        # Hides the questions and results
        self.questions.hide()
        self.result_label.place_forget()

        # Clears the timer and the score
        self.canvas.itemconfig(self.timer_text, text="")
        self.canvas.itemconfig(self.score_text, text="")

       # Plays the you lose sound effect
        you_lose_sound()

        # Creates the times up and displays it on the canvas
        self.canvas.create_text(
            350, 220,
            text="Times Up!",
            font=("Arial", 50, "bold"),
            fill="dark blue"
        )

        # Stores the final time taken for the game
        time_taken = int(time.time() - self.start_time)

        # Function to show the game over screen after a short delay
        def show_game_over():
            # Creates a new window for the game over screen
            end_window = tk.Toplevel(self.root)

            # Opens the game over screen and passes score + time data
            End(end_window, self.score, time_taken, Game)

            # Hides the main game window instead of destroying it immediately
            self.root.withdraw()

        # Waits 2 seconds before showing the game over screen
        self.root.after(2000, show_game_over)

    # Function for correct answer logic
    def correct_answer(self):
        # Prevents multiple clicks being processed
        if self.question_locked or self.game_over:
            return

        # Shows the correct answer feedback on the canvas
        self.result_label.config(text="Correct! Feed your Duck", font=("Arial", 14), bg="light blue")
        self.result_label.place(x=350, y=320, anchor="center")
        self.question_locked = True  # locks the question

        # Increases the score by 1
        self.score += 1

        # Updates the score display on the canvas
        self.canvas.itemconfig(self.score_text, text=f"Score = {self.score}")
        print(f"score {self.score}")

        # Checks the win condition for 10 correct answers and then calls the win_game function
        if self.score == 10:
            self.win_game()
            return

        # Plays the correct answer sound effect
        play_correct()

        # Shows the cracker if it's not already visible and displays at the coordinates
        if self.cracker.sprite is None:
            self.cracker.show(self.cracker_x, self.cracker_y)

        # Function that runs after the duck collides with the cracker
        def on_eaten():
            # Move next cracker position forward for after the next correct answer
            self.cracker_x += 41

            # Clears the feedback text
            self.result_label.config(text="")

            # Loads the next question
            self.next_question()

        # Moves the duck toward the cracker by the set distance
        self.duck.move(45, self.cracker, on_collision=on_eaten)


    # Function for the wrong answer
    def wrong_answer(self):
        # Checks game state and stops the game from continuing if it is over
        if self.game_over:
            return

        # Plays the wrong answer sound effect
        play_wrong()

        # Shows the wrong answer feedback on the canvas
        self.result_label.config(text="Wrong! Try again", font=("Arial", 14), bg="light blue")
        self.result_label.place(x=350, y=320, anchor="center")

    # Function to load the next question
    def next_question(self):
        # Checks game state and stops the game from continuing if it is over
        if self.game_over:
            return

        # Unlocks the question so the player can answer
        self.question_locked = False

        # Hides the result label
        self.result_label.place_forget()

        # Loads and displays the next question if available
        q = self.questions.get_next_question()
        if q:  # If a next question exists
            self.current_question = q  # Save as the current question
            self.questions.set_question(q)  # Displays the next question on the Canvas

    # Function to check win game conditions
    def win_game(self):
        # Checks game state and stops the game from continuing if it is over
        if self.game_over:
            return

        # Checks the game state and sets it to True
        self.game_over = True
        print("WIN GAME TRIGGERED")

        # Hides the questions and results
        self.questions.hide()
        self.result_label.place_forget()

        # Clears the timer and the score
        self.canvas.itemconfig(self.timer_text, text="")
        self.canvas.itemconfig(self.score_text, text="")

        # Plays the you win sound effect
        you_win_sound()

        # Creates and displays the you win text on the canvas
        self.canvas.create_text(
            350, 220,
            text="You Win!",
            font=("Arial", 50, "bold"),
            fill="dark blue"
        )

        # Calls the function to change the duck image to the floating duck image
        self.duck.float_mode()

        # Finishes the animation and then ends the game
        self.duck.pond_jump(90, 476, on_finish=self.end_game)

    # Function to end the game and call the game over screen
    def end_game(self):
        def show_game_over():
            print("ABOUT TO OPEN END WINDOW")

            # Opens the end screen window
            end_window = tk.Toplevel(self.root)

            # Stores the final time taken for the game
            time_taken = int(time.time() - self.start_time)

            # Loads the end screen and passes the score and time data
            End(end_window, self.score, time_taken, Game)

            # Hides the main game window
            self.root.withdraw()

        # Waits 2 seconds before showing the game over screen
        self.root.after(2000, show_game_over)
