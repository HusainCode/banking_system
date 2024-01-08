import tkinter as tk
import json


from banking_system.models.account.Checking import Checking

"""
THIS CLASS WILL BE BROKEN DOWN LATER TO A PARENT AND A FEW CHILDRENS 
"""

"""
grid

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

        self.setup_window()  # Call to set up the window properties and position
        self.create_ui_elements()  # Call to create the user interface components

    def setup_window(self):
        self.create_window()  # Create the main window
        self.window_size()  # Set the size of the window
        self.window_position()  # Position the window on the screen

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

    def create_canvas(self):
        """
        Create the UI elements of the application.
        initializing all the user interface components

        """
        # Creat a canvas widget
        canvas = tk.Canvas(self.main_window,
                           width=self.CANVAS_WIDTH,
                           height=self.CANVAS_HEIGHT,
                           bg='gray',
                           relief=tk.RAISED,
                           bd=10)

        # Centering the canvas in the window
        canvas.place(relx=0.5,
                     rely=0.5,
                     anchor="center")

    def create_checkbox(self):
        # Variables for checkboxes
        self.var_savings = tk.IntVar()
        self.var_checking = tk.IntVar()

        cb_savings = tk.Checkbutton(self.main_window,
                                    text="Savings",
                                    variable=self.var_savings)
        cb_savings.pack()

        cb_checking = tk.Checkbutton(self.main_window,
                                     text="Checking",
                                     variable=self.var_checking)
        cb_checking.pack()

    def handle_submit(self):
        if self.var_checking.get():
            pass

        if self.var_savings.get():
            pass

     def submit_form(self):
         pass


    def add_user_to_jason(self, fullname, password, account_type, deposit):
        user_date ={
            "fullname": fullname,
            "password": password,
            "account_type": account_type,
            "deposit": deposit
        }

        filename = "fake_users.json"

        try:
            with open(filename, "r") as file:
                data = json.load(file)
         except FileNotFoundError:
                data = {"users": []}

        # Add the new user
        data["users"].append(user_data)

         # Write the data back to the file
         with open(filename, "w") as file:
            json.dump(data, file, indent=4)




    def create_button(self):
        # Button to create account
        btn_create = tk.Button(self.main_window,
                               text="Submit")
        btn_create.pack()

    def create_label(self):
        label = tk.Label(self.main_window,
                         text="Enter your full name")
        label.pack()

        entry = tk.Entry(self.main_window)
        entry.pack()

    def create_ui_elements(self):
        # Directly call UI element creation methods
        self.create_checkbox()
        self.create_button()
        self.create_canvas()
        self.create_label()

    # Run the window
    def run(self):
        self.main_window.mainloop()


app = GUI()
app.run()
