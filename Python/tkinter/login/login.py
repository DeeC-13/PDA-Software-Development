# import tkinter library
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

# class that creates the GUI for our application
class LoginApp:

    # init function is the constructor of this class
    def __init__(self):

        # create the main window and set its appearance
        self.root_window = tk.Tk()
        self.root_window.title("Login")
        self.root_window.geometry("540x400")

        # add a frame with two columns to hold our components
        self.input_frame = tk.Frame(self.root_window)
        self.input_frame.columnconfigure(0, weight=1)
        self.input_frame.columnconfigure(1, weight=1)

        # create two labels to be positioned in the frame
        self.label = tk.Label(self.input_frame, text="Enter your Username", font=('Arial', 12))
        self.label1 = tk.Label(self.input_frame, text="Enter your Password", font=('Arial', 12))

        # display the frame on the window
        self.input_frame.pack(pady = 30)

        # display the label on the window
        self.label.grid(row = 0, column = 0, padx=10, pady=10)
        self.label1.grid(row = 1, column = 0, padx=10, pady=10)

        # create and position a text box for input entry
        self.username = tk.Entry(self.input_frame)
        self.password = tk.Entry(self.input_frame)

        # display the label on the window
        self.username.grid(row=0, column=1, padx=10, pady=10)
        self.password.grid(row=1, column=1, padx=10, pady=10)

        # add a button for the user to press when they've entered their data
        self.login = tk.Button(self.root_window, text="Login", fg = "darkblue", bg = "lightblue", command = self.handle_loginpress)
        self.login.place(x=220, y=155, height=30, width=100)

        # creates label image
        self.login_img = ImageTk.PhotoImage(Image.open("confetti.jpg"))
        self.img_label = tk.Label(image=self.login_img)

        # run the window
        self.root_window.mainloop()

    # Function to hide the input box and button
    def hide_widgets(self):
       # self.login.place_forget()
        self.username.delete(0, tk.END)
        self.password.delete(0, tk.END)

    # event handler for go button
    def handle_loginpress(self):
        user_input = self.username.get() and self.password.get()
        if not user_input.strip():  # Check if the input is empty or only whitespace
            messagebox.showerror("Input Error", "Please enter your Username and Password.")
        else:
            # hides the text box and submit button
            self.hide_widgets()

            # displays the image on screen
            self.img_label.place(x=0, y=0, relwidth=1, relheight=1)

            # pops up a message box with goodbye message
            messagebox.showinfo('Hello', message = "You are now Logged In!")


# create an instance of the class that will kick off our GUI application
LoginApp()