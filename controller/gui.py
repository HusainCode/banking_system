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

    # Window dimensions
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 150

    def __init__(self, WINDOW_WIDTH=None):
        self.window_height = GUI.WINDOW_HEIGHT  # Store the height of the window
        self.window_width = GUI.WINDOW_WIDTH  # Store the width of the window

    # self._setup_window()  # Call to set up the window properties and position
    # self.create_ui_elements()  # Call to create the user interface components
    def setup_window(self):
        self.create_window()
        self.window_size()
        self.window_position()
        self.main_window.title("")

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

    # Run the window
    def run(self):
        self.main_window.mainloop()
