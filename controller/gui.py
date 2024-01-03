import tkinter as tk


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

        self.setup_window()  # Call to set up the window properties and position
        self.create_ui_elements()  # Call to create the user interface components

    def setup_window(self):
        self.create_window()  # Create the main window
        self.window_size()  # Set the size of the window
        self.window_position()  # Position the window on the screen

    def create_ui_elements(self):
        self.create_checkbox()  # Create checkboxes
        self.create_button()  # Create a button
        self.creat_canvas()  # Create a canvas
        self.creat_label()  # Create labels for text display

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

    def creat_canvas(self):
        """
        Create the UI elements of the application.
        initializing all the user interface components

        """
        # Creat a canvas widget
        canvas = tk.Canvas(self.main_window, width=self.CANVAS_WIDTH, height=self.CANVAS_HEIGHT, bg='gray')

        # Centering the canvas in the window
        canvas.place(relx=0.5, rely=0.5, anchor="center")

    def create_checkbox(self):
        # Variables for checkboxes
        var_savings = tk.IntVar()
        var_checking = tk.IntVar()

        # Variables for checkboxes - used to track the state (checked/unchecked)
        self.var_savings = tk.IntVar()  # Variable for the savings account checkbox
        self.var_checking = tk.IntVar()  # Variable for the checking account checkbox

        # Checkboxes for account type
        cb_savings = tk.Checkbutton(self.main_window, text="Savings", variable=var_savings)
        cb_savings.pack()

        cb_checking = tk.Checkbutton(self.main_window, text="Checking", variable=var_checking)
        cb_checking.pack()

    def create_button(self):
        # Button to create account
        btn_create = tk.Button(self.main_window, text="Submit")
        btn_create.pack()

    def creat_label(self):
        label = tk.Label(self.main_window, text="Enter your full name")
        label.pack()

        entry = tk.Entry(self.main_window)
        entry.pack()

    def creat_frame(self):
        # Create a frame to hold the UI elements
        frame = tk.Frame(self.main_window)
        return frame

    # Run the window
    def run(self):
        self.main_window.mainloop()


app = GUI()
app.run()
