from PIL import Image, ImageTk
from utils import crunch_sound

# Creates the duck class for movement, image and collision
class Duck:
    def __init__(self, canvas, x, y, image_path):
        self.canvas = canvas
        self.ground_y = y # Stores the ground position y

        # Variables for movement physics (jumping and falling)
        self.velocity_y = 0
        self.gravity = 1
        self.jump_strength = 12

        # Checks if the duck is moving
        self.is_moving = False

        # Creates and loads the duck sprite
        self.load_sprite(x, y, image_path)

    # Function to load the duck images
    def load_sprite(self, x, y, image_path):
        # Loads and resizes the normal duck image
        self.img = Image.open(image_path).resize((50, 50))
        self.icon = ImageTk.PhotoImage(self.img)

        # Creates a flipped image of the duck (facing right)
        self.flipped_img = self.img.transpose(Image.FLIP_LEFT_RIGHT)
        self.flipped_icon = ImageTk.PhotoImage(self.flipped_img)

        # Creates the duck sprite on canvas
        self.sprite = self.canvas.create_image(x, y, image=self.flipped_icon)

        # Loads and resizes the floating duck image on win condition
        self.float_img = Image.open("../img/duck3.png").resize((50, 50))
        self.float_icon = ImageTk.PhotoImage(self.float_img)

        # Creates a flipped image of the floating duck (facing right)
        self.flipped_float_img = self.float_img.transpose(Image.FLIP_LEFT_RIGHT)
        self.flipped_float_icon = ImageTk.PhotoImage(self.flipped_float_img)

    # Function to change the duck image to the floating image on win condition
    def float_mode(self):
        self.canvas.itemconfig(self.sprite, image=self.flipped_float_icon)

    # Function to check collision with the cracker
    def check_collision(self, cracker):
        # Checks if the cracker is displayed
        if cracker.sprite is None:
            return False

        # Gets the current position of the duck
        duck_x, duck_y = self.canvas.coords(self.sprite)

        # Gets the current position of the cracker
        cracker_x, cracker_y = self.canvas.coords(cracker.sprite)

        # Checks for collision by comparing distance between objects
        if abs(duck_x - cracker_x) < 19 and abs(duck_y - cracker_y) < 19:
            print("Crunch! Duck ate the cracker!") # Debug print
            # Prints positions for testing
            print(f"Duck: ({duck_x}, {duck_y}), Cracker: ({cracker_x}, {cracker_y})")

            # Play the crunch sound effect on collision
            crunch_sound()

            return True # Collision detected
        return False # Else not collision

    # Function to move the duck forward with a bouncing effect
    def move(self, distance, cracker, on_collision):
        # Stops the duck moving again if it is already moving
        if self.is_moving:
            return

        # Sets moving flag to true
        self.is_moving = True

        # Resets velocity for jumping
        self.velocity_y = self.jump_strength

        # Gets the current X position of the duck
        x, _ = self.canvas.coords(self.sprite)
        target_x = x + distance # The target position based on distance to move

        # Function for the animation loop (runs repeatedly to move the duck)
        def step():
            # Gets the duck's current position
            x, y = self.canvas.coords(self.sprite)

            # Stops the duck's movement when the target is reached
            if x >= target_x:
                self.canvas.coords(self.sprite, target_x, self.ground_y)
                self.is_moving = False # Sets the moving flag to false
                return # Ends the movement

            # Moves the duck to the right each frame and updates the position
            new_x = x + 0.8

            # Applies gravity to create the bounce effect (jump and fall)
            self.velocity_y -= self.gravity
            new_y = y - self.velocity_y # Updates the duck's position while bouncing

            # Checks the duck's position and stops duck going below the ground level
            if new_y > self.ground_y:
                new_y = self.ground_y
                self.velocity_y = self.jump_strength  # Makes the duck bounce again when on ground
            else:
                self.velocity_y = 0 # Sets the duck's y valocity to 0 (not jumping)

            # Updates the duck's position with the new coordinates
            self.canvas.coords(self.sprite, new_x, new_y)

            # Checks collides with the cracker and handles it
            if cracker and cracker.sprite:
                if self.check_collision(cracker):
                    cracker.hide() # Hides the cracker when the duck eats it
                    self.is_moving = False # Sets the moving flag to false
                    on_collision() # Triggers the collision callback function
                    return

                if new_x == target_x and new_y == self.ground_y:
                    self.is_moving = False  # Stops the duck's movement once target position is reached
                    return  # Exits the step function as the duck has reached the destination

            # Continues the movement in the next frame
            self.canvas.after(20, step)

        # Starts the movement animation
        step()

    # Function for final jump into pond on win condition
    def pond_jump(self, distance, target_y, on_finish=None):
        # Stops function if duck is already moving
        if self.is_moving:
            return

        # Sets is moving flag to true
        self.is_moving = True

        # Get starting position of duck
        start_x, start_y = self.canvas.coords(self.sprite)

        # Sets the duck's final x position
        target_x = start_x + distance

        # Sets initial upward force for jump
        self.velocity_y = -14

        # Gravity pulls duck back down
        self.gravity = 1

        # Controls the duck's horizontal speed across animation
        dx = distance / 40

        # Function for the animation loop
        def step():
            # Stops any leftover loops running
            if not self.is_moving:
                return

            # Gets the duck's current position each frame
            x, y = self.canvas.coords(self.sprite)

            # Stops the duck's movement when it reaches the pond
            if x >= target_x:
                self.canvas.coords(self.sprite, target_x, target_y)

                # Sets is moving flag to false
                self.is_moving = False

                print("POND JUMP FINISHED")  # Debug code

                # Runs the end game function
                if on_finish:
                    on_finish()
                return  # Stops the animation loop

            # Moves the duck horizontally towards the pond
            new_x = x + dx

            # Applies gravity for a smooth jump arc
            self.velocity_y += self.gravity
            new_y = y + self.velocity_y

            # Stops the duck falling below pond level
            if new_y >= target_y:
                new_y = target_y
                self.velocity_y = 0 # Sets the duck's y valocity to 0 (not jumping)

            # Updates the duck's position on the screen
            self.canvas.coords(self.sprite, new_x, new_y)

            # Repeats the animation
            self.canvas.after(20, step)

        # Starts the pond jump animation
        step()