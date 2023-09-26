import tkinter as tk
from tkinter import ttk, filedialog

def PrintFileContents(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
        print(data)

def OnlyNumbers(char):
    return char.isdigit() or char == " "

file_name = ""  # Define file_name as a global variable

class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)

        # Make the app responsive
        for index in [0, 1, 2]:
            self.columnconfigure(index=index, weight=1)
            self.rowconfigure(index=index, weight=1)

        # Create widgets :)
        self.setup_widgets()

    def OpenFileAndGetName(self):
        global file_name
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                PrintFileContents(file_path)
            file_name = file_path.split("/")[-1]
            self.label.config(text=file_name)

    def setup_widgets(self):
        # Create a Frame for the Checkbuttons
        self.check_frame = ttk.LabelFrame(self, text="Input", padding=(20, 20))
        self.check_frame.grid(
            row=0, column=0, padx=(25, 10), pady=(20, 10), sticky="nsew"
        )

        # Create a button to trigger file dialog
        self.button = ttk.Button(self.check_frame, text="Select File", command=self.OpenFileAndGetName)
        self.button.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="nsew")

        #set it right to the button what file was imported
        self.label = ttk.Label(self.check_frame, text=file_name)
        self.label.grid(row=0, column=1,padx=5, pady=(0, 10), sticky="nsew")

        # Create a label and entry for mileage input
        self.mileage_label = ttk.Label(self.check_frame, text= "Enter Mileage:")
        self.mileage_label.grid(row=1, column=0, padx=0, pady=(0, 10), sticky="nsew")

        # Entry
        CurrentMileage = tk.StringVar()
        self.CurrentMileage = ttk.Entry(self.check_frame, validate="key", validatecommand=(root.register(OnlyNumbers), "%P"))
        self.CurrentMileage.grid(row=2, column=0, padx=5, pady=(0, 10), sticky="ew")
        self.CurrentMileage.bind("<Return>", self.PrintMileage) # Bind Enter Key
        #create a check for switching between kilometers and freedom units
        self.units_var = tk.StringVar()
        self.units_checkbutton = ttk.Checkbutton(self.check_frame, text="Kilometers", variable=self.units_var, onvalue="km", offvalue="mi", command=self.update_units)
        self.units_checkbutton.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")
        # Set default units to kilometers
        self.units_var.set("km")
        # Initialize boolean variable to False
        self.checkbox_ticked = True
        
        # set the mileage next to the mileage input
        self.mileage = 0
        self.CurrentMileageLabel = ttk.Label(self.check_frame, text=f"Current Mileage: {self.mileage} {self.units_var.get()}")
        self.CurrentMileageLabel.grid(row=2, column=1, padx=5, pady=(0,10), sticky="ew")

        # Sizegrip
        self.sizegrip = ttk.Sizegrip(self)
        self.sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))

    def ToggleCheckbox(self):
        self.checkbox_ticked = not self.checkbox_ticked

        # Print the current state of the checkbox
        print(f"Checkbox Ticked: {self.checkbox_ticked}")

    def PrintMileage(self, event):
        mileage = self.CurrentMileage.get()
        units = self.units_var.get()
        if mileage and mileage.isdigit():
            self.mileage = int(mileage)
            self.CurrentMileageLabel.config(text=f"Current Mileage: {self.mileage} {self.units_var.get()}")
            self.CurrentMileage.delete(0, tk.END)
            print(f"Mileage: {mileage} {units}")
        
    def update_units(self):
        self.CurrentMileageLabel.config(text=f"Current Mileage: {self.mileage} {self.units_var.get()}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tracker")
    root.iconbitmap("transparent.ico")

    # Simply set the theme
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "dark")

    app = App(root)
    app.pack(fill="both", expand=True)

    # Set a minsize for the window, and place it in the middle
    root.update()
    #root.minsize(root.winfo_width(), root.winfo_height())
    root.geometry("600x600")
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate-20))

    root.mainloop()