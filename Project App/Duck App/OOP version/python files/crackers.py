from PIL import Image, ImageTk

# Creates cracker class
class Cracker:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x  # Cracker x position
        self.y = y  # Cracker y position
        self.sprite = None  # No sprite shown when the game starts

    # Function to load the cracker
    def load_sprite(self):

        cracker_img = Image.open("../img/crackers.png")  # Sets the cracker image
        cracker_img = cracker_img.resize((30, 30))  # Resizes the image to the specified size
        self.cracker_icon = ImageTk.PhotoImage(cracker_img) # Converts the image for tkinter to use

        # Creates the image for the sprite on the canvas
        self.sprite = self.canvas.create_image(self.x, self.y, image=self.cracker_icon)

    # Function to show the cracker sprite at coordinates
    def show(self, x, y):

        if self.sprite is None:  # Checks the cracker is not displayed on the canvas
            self.load_sprite()  # Loads the cracker

        # Displays the cracker at (x, y)
        self.canvas.coords(self.sprite, x, y)

    # Function to hide the cracker after duck eats it
    def hide(self):

        if self.sprite is not None: # checks the cracker is displayed
            self.canvas.delete(self.sprite) # Deletes the cracker on collision
            self.sprite = None # Resets the cracker back to not displayed

    # Function to get the current position of the cracker
    def get_position(self):

        if self.sprite is not None: # Checks the cracker is displayed
            position = self.canvas.coords(self.sprite) # Gets current position
            print(f"Cracker position: {position}")  # Debug print
            return position # Returns position of displayed cracker
        return None # Else returns none if not displayed