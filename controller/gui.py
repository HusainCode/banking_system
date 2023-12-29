import tkinter as tk


class GUI:
    """
    GUI class for creating and managing a Tkinter window.
    It sets up a window with specified dimensions, makes it resizable,
    and positions it at the center of the screen.
    """
    def __init__(self, window_width=800, window_height=800):
        self.main_window = None
        self.window_height = window_height
        self.window_width = window_width
        self.create_window()
        self.window_size()
        self.locate_window()

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

    def locate_window(self):
        # Get screen width and height
        screen_width = self.main_window.winfo_screenwidth()
        screen_height = self.main_window.winfo_screenheight()

        # Calculate the x and y coordinates for the window to be centered
        center_x = int((screen_width - self.window_width) / 2)
        center_y = int((screen_height - self.window_height) / 2)

        # Set window position, the middle
        self.main_window.geometry(f"{self.window_width}x{self.window_height}+{center_x}+{center_y}")

    def creat_button(self):
        pass

    def creat_label(self):
        pass

    # Run the window
    def run(self):
        self.main_window.mainloop()



#app = GUI()
#app.run()