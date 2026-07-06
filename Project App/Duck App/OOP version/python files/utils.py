import tkinter as tk
import csv
import os
from PIL import Image, ImageTk
import pyglet

# Function to add a background image to a canvas
def background(canvas, image):
    canvas.image = image  # Keep the reference

    # Draws the image at the top-left corner
    canvas.create_image(0, 0, image=image, anchor="nw")

# Function to play the background music
def play_background_music():
    # Loads the background music
    bg_music = pyglet.media.load('../sounds/bg music.mp3', streaming=False)

    # Sets the music to loop
    bg_music.loop = True

    # Plays the music
    bg_music.play()

# Function to play the crunch sound effect on collision
def crunch_sound():
    # Loads the crunch sound effect
    crunch_sound = pyglet.media.load('../sounds/crunch.mp3', streaming=False)

    # Plays the sound effect
    crunch_sound.play()

# Function to play the correct answer sound effect
def play_correct():
    # Loads the correct answer sound effect
    correct_sound = pyglet.media.load('../sounds/correct.mp3', streaming=False)

    # Plays the sound effect
    correct_sound.play()

# Function to play the wrong answer sound effect
def play_wrong():
    # Loads the wrong answer sound effect
    wrong_sound = pyglet.media.load('../sounds/wrong.mp3', streaming=False)

    # Plays the sound effect
    wrong_sound.play()

# Function to play the you win sound effect
def you_win_sound():
    # Loads the you win sound effect
    win_sound = pyglet.media.load('../sounds/you win.mp3', streaming=False)

    # Plays the sound effect
    win_sound.play()

# Function to play the you lose sound effect
def you_lose_sound():
    # Loads the you lose sound effect
    lose_sound = pyglet.media.load('../sounds/you lose.mp3', streaming=False)

    # Plays the sound effect
    lose_sound.play()

# Sets the file name for the leaderboard
FILE_NAME = "leaderboard.csv"


# Function to read the leaderboard from the CSV file
def read_leaderboard():
    # Creates an empty list to store the scores
    score_list = []

    # Checks if the file exists
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, newline="") as f:
            reader = csv.reader(f)

            # Loops through each row in the file
            for row in reader:
                # Checks the row has 3 values
                if len(row) == 3:
                    try:
                        name = row[0]
                        time = int(row[1])  # Converts the time to an integer
                        score = int(row[2])  # Converts the score to an integer
                        score_list.append((name, time, score))  # Adds to the list as a tuple

                    except ValueError:
                        pass  # Skips invalid rows

    return score_list


# Function to write the leaderboard to the CSV file
def write_leaderboard(score_list):
    # Opens the file in write mode (overwrites existing data)
    with open(FILE_NAME, "w", newline="") as f:
        # Creates a CSV writer to write data to the file
        writer = csv.writer(f)

        # Writes each score to the file after the game over
        for name, time, score in score_list:
            # Writes the name, time and score as a new row in the CSV file
            writer.writerow([name, time, score])


# Function to save a new score
def save_score(name, time, score, file_name="leaderboard.csv"):
    # Opens the file in append mode (adds new data without deleting existing data)
    with open(file_name, "a", newline="") as f:
        # Creates a CSV writer to write data to the file
        writer = csv.writer(f)

        # Writes the name, time and score as a new row in the CSV file
        writer.writerow([name, time, score])


# Function to manually sort the scores by fastest time
def manual_sort_by_time(scores):
    # Manually sorts the leaderboard by the fastest time (lowest first)

    # Gets the number of scores in the list
    n = len(scores)

    # i = the current index where the fastest score will be placed (placing)
    # j = loops through the remaining items to compare times and find a faster score (checking)

    # Loops through each position in the list
    for i in range(n):

        # Assumes the current position (i) is the fastest
        fastest_index = i

        # Looks through the rest of the list (after i)
        for j in range(i + 1, n):

            # Compares the times (index 1 in the tuple)
            # If a smaller time is found, it's faster
            if scores[j][1] < scores[fastest_index][1]:
                fastest_index = j  # Updates the fastest position

        # After checking all the list items, swaps the fastest with position i

        # Stores the current score temporarily
        temp = scores[i]

        # Moves the fastest score into the correct position (position i)
        scores[i] = scores[fastest_index]

        # Puts the original score (stored in temp) into the position where the fastest score was
        scores[fastest_index] = temp

    # Returns the sorted score list
    return scores


# Function to show the leaderboard in the pop out window
def show_leaderboard(parent):
    # Creates the new pop out window
    leaderboard_window = tk.Toplevel(parent)
    leaderboard_window.title("Leaderboard")

    # Sets the window size
    leaderboard_window.geometry("500x550")

    # Stops the window being rezised to larger than 500x550
    leaderboard_window.maxsize(width=500, height=550)

    # Create the canvas
    canvas_leaderboard = tk.Canvas(leaderboard_window, width=500, height=550)
    canvas_leaderboard.pack(fill="both", expand=True)

    # Loads and resizes the background image
    bg_icon = ImageTk.PhotoImage(Image.open("../img/bg.png").resize((500, 550)))
    canvas_leaderboard.bg_icon = bg_icon

    # Displays the background image on the canvas
    background(canvas_leaderboard, bg_icon)

    # Creates a grey background box
    canvas_leaderboard.create_rectangle(28, 80, 473, 470, fill="gray", stipple="gray25", outline="")

    # Creates the title text
    canvas_leaderboard.create_text(
        250, 45,
        text="Leaderboard",
        font=("Arial", 24, "bold"),
        fill="dark blue",
        justify="center"
    )

    # Loads the scores from the CSV file
    scores = read_leaderboard()

    # Sorts the scores by the fastest time
    scores = manual_sort_by_time(scores)

    # Keeps the top 10 scores
    scores = scores[:10]

    # Creates the header row titles
    canvas_leaderboard.create_text(105, 110, text="Name", font=("Arial", 15, "bold"), fill="dark blue")
    canvas_leaderboard.create_text(250, 110, text="Time", font=("Arial", 15, "bold"), fill="dark blue")
    canvas_leaderboard.create_text(395, 110, text="Score", font=("Arial", 15, "bold"), fill="dark blue")

    # Sets the y position to start the scores display
    y = 152

    # Loops through the scores and displays each one
    for name, time_taken, score in scores:
        canvas_leaderboard.create_text(105, y, text=name, font=("Arial", 14), fill="dark blue")
        canvas_leaderboard.create_text(250, y, text=f"{time_taken}s", font=("Arial", 14), fill="dark blue")
        canvas_leaderboard.create_text(395, y, text=str(score), font=("Arial", 14), fill="dark blue")

        # Sets y distance between scores to display the next row
        y += 31

    # Creates the close button
    close_btn = tk.Button(
        leaderboard_window,
        text="Close",
        font=("Arial", 14),
        anchor="center",
        bg="light blue",
        command=leaderboard_window.destroy
    )

    # Places the close button on the canvas
    canvas_leaderboard.create_window(250, 510, anchor="center", window=close_btn)
