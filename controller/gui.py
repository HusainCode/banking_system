import tkinter as tk


class GUI:
    """
    GUI class for creating and managing a Tkinter window.
    It sets up a window with specified dimensions, makes it resizable,
    and positions it at the center of the screen.
    """

    # canvas dimensions
    CANVAS_WIDTH = 400
    CANVAS_HEIGHT = 400

    def __init__(self, window_width=800, window_height=800):
        self.main_window = None
        self.window_height = window_height
        self.window_width = window_width
        self.var_savings = tk.IntVar()
        self.var_checking = tk.IntVar()
        self.setup_window()
        self.create_ui_elements()

    def setup_window(self):
        self.create_window()
        self.window_size()
        self.window_position()

    def create_ui_elements(self):
        self.create_checkbox()
        self.create_button()
        self.creat_canvas()
        self.creat_label()

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
        # Creat a canvas widget
        canvas = tk.Canvas(self.main_window, width=self.CANVAS_WIDTH, height=self.CANVAS_HEIGHT, bg='white')

        # Centering the canvas in the window
        canvas.place(relx=0.5, rely=0.5, anchor="center")

    def create_checkbox(self):
        # Variables for checkboxes
        var_savings = tk.IntVar()
        var_checking = tk.IntVar()

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

    # Run the window
    def run(self):
        self.main_window.mainloop()

# app = GUI()
# app.run()
