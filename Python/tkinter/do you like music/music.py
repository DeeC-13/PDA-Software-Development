# import tkinter library
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

# class that creates the GUI for our application
class Music:

    # init function is the constructor of this class
    def __init__(self):

        # creates the main window and set its appearance
        self.root_window = tk.Tk()
        self.root_window.title("Music")
        self.root_window.geometry("420x320")
        self.music_img = ImageTk.PhotoImage(Image.open("music.jpg"))
        self.img_label = tk.Label(self.root_window, image= self.music_img)
        self.img_label.place(x=0, y=0, relwidth=1, relheight=1)

        # creates a label to be positioned in the window
        self.label = tk.Label(self.root_window, text="Do you like Music?", font=('Arial', 13))

        # displays the label on the window
        self.label.place(relx = 0.5, rely = 0.1, anchor = 'center')

        # adds two buttons for the user to press a choice
        self.yes = tk.Button(self.root_window, text="Yes", fg="darkblue", bg="lightblue",
                             command=self.handle_choice_yes)
        self.no = tk.Button(self.root_window, text="No", fg="darkblue", bg="lightblue",
                             command=self.handle_choice_no)

        # displays the buttons on the window
        self.yes.place(relx = 0.4, rely = 0.25, width = 70, anchor = 'center')
        self.no.place(relx = 0.6, rely = 0.25, width = 70, anchor = 'center')

        # creates a label to be positioned in the window after yes is clicked
        self.band_fave = tk.Label(self.root_window, text="What's your Fave Band?", font=('Arial', 13))

        # create a text box for input entry after yes is clicked
        self.band = tk.Entry(self.root_window)

        # creates a button on the window after yes is clicked
        self.fband = tk.Button(self.root_window, text="Submit", fg="darkblue", bg="lightblue",
                               command=self.handle_submit)

        # creates a label to be positioned in the window after no is clicked
        self.no_band = tk.Label(self.root_window, text="You're Boring. Byeeeeeeeeeeeee",
                                font=('Arial', 13))

        # run the window
        self.root_window.mainloop()

    # Function to hide the buttons
    def hide_button(self):
        self.yes.place_forget()
        self.no.place_forget()

    # Function to hide the input box and button
    def hide_widgets(self):
        self.band.place_forget()
        self.fband.place_forget()

    # function to handle choice yes
    def handle_choice_yes(self):
        # creates a variable for the yes button
        yes = self.yes

        if yes:
            # hides the yes/no buttons
            self.hide_button()

            # displays the label on the window
            self.band_fave.place(relx = 0.5, rely = 0.25, anchor = 'center')

            # displays the label on the window
            self.band.place(relx=0.5, rely=0.37, anchor='center')

            # displays the button on the window
            self.fband.place(relx=0.5, rely=0.5, width=70, anchor='center')

    # function to handle choice no
    def handle_choice_no(self):
        # creates a variable for the no button
        no = self.no

        if no:
            # hides the yes/no buttons
            self.hide_button()

            # displays the label on the window
            self.no_band.place(relx=0.5, rely=0.25, anchor='center')

    # displays message for no button press
    def message(self):
        # hides the text box and submit button
        self.hide_widgets()

        # creates a label to be positioned in the window after submit is clicked
        self.mess = tk.Label(self.root_window, text="You're a Die Hard Fan of " + self.band.get() + " !!!!", font=('Arial', 13))

        # displays the label on the window
        self.mess.place(relx=0.5, rely=0.25, anchor='center')

    # event handler for submit button press
    def handle_submit(self):
        # creates a variable for the submit button
        submit = self.band.get()

        if not submit.strip():  # Check if the input is empty or only whitespace
            messagebox.showerror("Input Error", "Please enter your Fave Band")
        else:
            self.message()

# calls class to launch GUI application
Music()
