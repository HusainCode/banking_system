import tkinter as tk

from banking_system.models.account.Checking import Checking

"""
THIS CLASS WILL BE BROKEN DOWN LATER TO A PARENT AND A FEW CHILDRENS 
"""

"""

TODO
1- REFACTOR BEFORE FINALIZING

 TODO add logo

Find a logo
# icon = photoImage(file='')
# window.iconphoto(True, icon)

"""


class GUI:
    """
    GUI class for creating and managing a Tkinter window.
    It sets up a window with specified dimensions, makes it resizable,
    and positions it at the center of the screen.
    """

    # canvas dimensions
    CANVAS_WIDTH = 300
    CANVAS_HEIGHT = 300

    def __init__(self, window_width=500, window_height=500):
        self.main_window = None  # Placeholder for the main Tkinter window object
        self.window_height = window_height  # Store the height of the window
        self.window_width = window_width  # Store the width of the window

    # self._setup_window()  # Call to set up the window properties and position
    # self.create_ui_elements()  # Call to create the user interface components

    def create_window(self):
        # Create the main window
        self.main_window = tk.Tk()

        # Set window title
        self.main_window.title("ATM")

    def window_size(self):
        # Make the window resizable (width=True, height=True)
        self.main_window.resizable(True, True)

        # Set initial size of the window (width x height)
        self.main_window.geometry(f"{self.window_width}x{self.window_height}")

    def window_position(self):
        # Get screen width and height
        screen_width = self.main_window.winfo_screenwidth()
        screen_height = self.main_window.winfo_screenheight()

        # Calculate the x and y coordinates for the window to be centered
        center_x = int((screen_width - self.window_width) / 2)
        center_y = int((screen_height - self.window_height) / 2)

        # Set window position, the middle
        self.main_window.geometry(f"{self.window_width}x{self.window_height}+{center_x}+{center_y}")

    # def create_canvas(self):
    #     """
    #     Create the UI elements of the application.
    #     initializing all the user interface components
    #
    #     """
    #     # Creat a canvas widget
    #     canvas = tk.Canvas(self.main_window,
    #                        width=self.CANVAS_WIDTH,
    #                        height=self.CANVAS_HEIGHT,
    #                        bg='gray',
    #                        relief=tk.RAISED,
    #                        bd=10)
    #
    #     # Centering the canvas in the window
    #     canvas.place(relx=0.5,
    #                  rely=0.5,
    #                  anchor="center")

    # Run the window
    def run(self):
        self.main_window.mainloop()
