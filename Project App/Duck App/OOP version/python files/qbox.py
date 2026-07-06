
import tkinter as tk
import csv
import random

# Class for the questions, labels and answer buttons
class Questions:
    def __init__(self, root, canvas, filename="duckq.csv"):
        self.root = root

        # Create the canvas
        self.canvas = canvas

        # Starts the question count at 0 to keep track
        self.question_count = 0

        # Stores the current question data
        self.current_question = None

        # Stores the correct answer button index
        self.correct_button_index = None

        # Draws a background box on the canvas
        self.box = self.canvas.create_rectangle(
            175, 50, 540, 345,
            fill="lightblue",
            outline="",
            stipple="gray75"
        )

        # Creates the question label on the canvas
        self.question_label = self.canvas.create_text(
            350, 100,
            text="",
            font=("Arial", 17),
            fill="black",
            width=320,
            anchor="center"
        )

        # Loads the questions from the CSV file
        self.questions = self.load_questions(filename)

        # Creates an empty list to store the answer buttons
        self.answer_buttons = []

        # Creates and places the answer buttons on the canvas
        for i in range(3):
            btn = tk.Button(
                root,
                text="",
                font=("Arial", 14),
                background="light blue",
                command=lambda i=i: self.check_answer(i)
            )
            btn.place(x=350, y=170 + i*55, width=288, height=38, anchor="center")

            # Adds the buttons to the list
            self.answer_buttons.append(btn)

        # Sets the functions for the correct and wrong answers
        self.on_correct = None
        self.on_wrong = None

    # Function to load the questions from the csv file (with error handling)
    def load_questions(self, filename):
        # Creates an empty list for the questions
        questions = []
        try:
            with open(filename, newline="", encoding="utf-8") as f:
                # Reads the file using tabs to separate values
                reader = csv.reader(f, delimiter="\t")  # denotes it as tab-separated

                # Loops through each row in the file
                for row in reader:
                    # Checks if the row has the correct number of values
                    if len(row) != 5:
                        continue

                    # Stores the question and answers
                    question_text = row[0]
                    choices = row[1:4]

                    # Stores the correct answer button index
                    correct_index = int(row[4])

                    # Adds the questions to the list
                    questions.append({
                        "text": question_text,
                        "choices": choices,
                        "correct": correct_index
                    })

            # Shuffles the questions in a random order
            random.shuffle(questions)
            print(f"Loaded {len(questions)} questions")

        except Exception as e:
            # Prints an error if the file fails to load
            print("Error loading CSV:", e)
        return questions

    # Function to display the question on the screen
    def set_question(self, question_data):
        # Stores the current question
        self.current_question = question_data

        # Updates the question text throughout the game
        self.canvas.itemconfig(self.question_label, text=question_data["text"])

        # Shuffle the answer choices
        choices = list(enumerate(question_data["choices"]))
        random.shuffle(choices)

        # Places the 3 answers into the buttons
        for i, (orig_index, choice_text) in enumerate(choices):
            self.answer_buttons[i].config(text=choice_text)

            # Checks which button has the correct answer
            if orig_index == question_data["correct"]:
                self.correct_button_index = i

        # Debug print
        print("Correct answer:", question_data["choices"][question_data["correct"]])
        print("Correct button index:", self.correct_button_index)

    # Function to get next question
    def get_next_question(self):
        # Checks if there are questions left
        if self.question_count < len(self.questions):
            q = self.questions[self.question_count]
            self.question_count += 1
            return q

        # Returns nothing if there are no questions left
        return None

    # Function to handle answer button clicks
    def check_answer(self, index):
        # Checks if there is a current question
        if self.current_question is None:
            return

        # Checks if the selected answer is correct
        if index == self.correct_button_index:
            print("Correct!") # debug print

            # If it is correct, runs the correct answer function
            if self.on_correct:
                self.on_correct()
        else:
            print("Wrong!") # debug print
            # If it is wrong, runs the wrong answer function
            if self.on_wrong:
                self.on_wrong()

    # Function to hide the question UI
    def hide(self):
        # Hides the question text
        self.canvas.itemconfig(self.question_label, text="")

        # Hides the question box
        self.canvas.itemconfig(self.box, state="hidden")

        # Hides the answer buttons
        for btn in self.answer_buttons:
            btn.place_forget()