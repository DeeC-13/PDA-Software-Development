# import tkinter library
import tkinter as tk
from tkinter import messagebox

counter = 1


# class that creates the GUI for our application
class Counter:

    # init function is the constructor of this class
    def __init__(self):

        # create the main window and set its appearance
        self.root_window = tk.Tk()
        self.root_window.title("Counter")
        self.root_window.geometry("420x320")
        self.root_window.maxsize(420,320)

        # add a frame with two columns to hold our components
        self.input_frame = tk.Frame(self.root_window)
        self.input_frame.columnconfigure(0, weight=1)
        self.input_frame.columnconfigure(1, weight=1)

        # creates a label to be positioned in the frame
        self.label = tk.Label(self.input_frame, text="Enter a Number", font=('Arial', 12))

        # display the frame on the window
        self.input_frame.pack(pady=30)

        # display the label on the window
        self.label.grid(row=0, column=0, padx=10, pady=10)

        # create and position a text box for input entry
        self.input = tk.Entry(self.input_frame)

        # display the label on the window
        self.input.grid(row=0, column=1, padx=10, pady=10)

        # add a button for the user to press when they've entered their data
        self.increment = tk.Button(self.root_window, text="Increment", fg="darkblue", bg="lightblue",
                                   command=self.handle_increment)
        self.decrement = tk.Button(self.root_window, text="Decrement", fg="darkblue", bg="lightblue",
                                   command=self.handle_decrement)
        self.reset = tk.Button(self.root_window, text="Reset", fg="darkblue", bg="lightblue", command=self.handle_reset)

        self.increment.place(x=70, y=85, height=30, width=80)
        self.decrement.place(x=170, y=85, height=30, width=80)
        self.reset.place(x=270, y=85, height=30, width=80)

        # run the window
        self.root_window.mainloop()

    # handles increment button press
    def handle_increment(self):
        global counter

        # creates variable for the input
        num = self.input.get()
        num1 = int(num) + counter

        if num.isdigit():  #checks input is a number
            counter += 1
            print(num1)

            # creates a label
            num_label = tk.Label(self.root_window, text=num1, font=('Arial', 18))

            # display the label on the window
            num_label.pack(padx=(10, 10), side="left")

            #-----figure out why it's printing both numbers -----
            if num1:
               self.handle_decrement()

        else:
            # creates an error message box
            messagebox.showerror("Input Error", "Enter a number")

    # handles decrement button press
    def handle_decrement(self):
        global counter

        num = self.input.get()
        num1 = int(num) - counter

        # creates variable for the input
        if num.isdigit():  #checks input is a number
            counter += 1
            print(num1)

            # creates a label
            num_label = tk.Label(self.root_window, text=num1, font=('Arial', 18))

            # display the label on the window
            num_label.pack(padx=(10, 10), side="left")

            #--------recursion error------
            # if num1:
            #     self.handle_increment()

        else:
            # creates an error message box
            messagebox.showerror("Input Error", "Enter a number")


    # handles reset button press
    def handle_reset(self):
        self.input.delete(0, tk.END)  # deletes the input in the entry box
        #num_label.config(text = '')        #couldn't get it to clear the output too


# calls class to launch GUI application
Counter()
