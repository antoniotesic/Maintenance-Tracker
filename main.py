import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import datetime
import os

def PrintFileContents(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
        print(data)

def OnlyNumbers(char):
    return char.isdigit() or char == " "

file_name = ""  # Define file_name as a global variable

current_date = datetime.date.today()
print(current_date)

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

    file_name = ""

    def setup_widgets(self):
        # Create a Frame for the Checkbuttons
        self.check_frame = ttk.LabelFrame(self, text="Input", padding=(20, 10))
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
        vcmd = (self.register(OnlyNumbers, "%S"))
        self.CurrentMileage = ttk.Entry(self.check_frame, validate="key", validatecommand=vcmd)
        self.CurrentMileage.grid(row=2, column=0, padx=5, pady=(0, 10), sticky="ew")
        self.CurrentMileage.bind("<Return>", self.PrintMileage) # Bind Enter Key
        # Bind Enter key to PrintMileage function
        self.CurrentMileage.bind('<Return>', self.PrintMileage)

        #create a check for switching between kilometers and freedom units
        self.units_var = tk.StringVar()
        self.units_checkbutton = ttk.Checkbutton(self.check_frame, text="Kilometers", variable=self.units_var, onvalue="km", offvalue="mi")
        self.units_checkbutton.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")

        # Set default units to kilometers
        self.units_var.set("km")

        # Initialize boolean variable to False
        self.checkbox_ticked = True

        # Attach a command to the Checkbutton to toggle the boolean variable
        self.units_checkbutton.config(command=self.ToggleCheckbox)
        
        #TODO: set the mileage next to the mileage input
        mileage = 20
        units = "km"
        self.CurrentMileageLabel = ttk.Label(self.check_frame, text=f"Current Mileage: {mileage} {units}")
        self.CurrentMileageLabel.grid(row=2, column=1, padx=5, pady=(0,10), sticky="ew")
        
        # Panedwindow
        self.paned = ttk.PanedWindow(self)
        self.paned.grid(row=1, column=0, padx=25, pady=(25, 5), sticky="nsew", rowspan=3)

        # Pane #1
        self.pane_1 = ttk.Frame(self.paned, padding=5)
        self.paned.add(self.pane_1, weight=1)

        # Scrollbar
        self.scrollbar = ttk.Scrollbar(self.pane_1)
        self.scrollbar.pack(side="right", fill="y")

        # Treeview
        self.treeview = ttk.Treeview(
            self.pane_1,
            selectmode="browse",
            yscrollcommand=self.scrollbar.set,
            columns=(1, 2),
            height=10,
        )
        self.treeview.pack(expand=True, fill="both")
        self.scrollbar.config(command=self.treeview.yview)

        # Treeview columns
        self.treeview.column("#0", anchor="w", width=120)
        self.treeview.column(1, anchor="w", width=120)
        self.treeview.column(2, anchor="w", width=120)

        # Treeview headings
        self.treeview.heading("#0", text="Column 1", anchor="center")
        self.treeview.heading(1, text="Column 2", anchor="center")
        self.treeview.heading(2, text="Column 3", anchor="center")

        # Define treeview data
        treeview_data = [
            ("", 1, "Parent", ("Item 1", "Value 1")),
            (1, 2, "Child", ("Subitem 1.1", "Value 1.1")),
            (1, 3, "Child", ("Subitem 1.2", "Value 1.2")),
            (1, 4, "Child", ("Subitem 1.3", "Value 1.3")),
            (1, 5, "Child", ("Subitem 1.4", "Value 1.4")),
            ("", 6, "Parent", ("Item 2", "Value 2")),
            (6, 7, "Child", ("Subitem 2.1", "Value 2.1")),
            (6, 8, "Sub-parent", ("Subitem 2.2", "Value 2.2")),
            (8, 9, "Child", ("Subitem 2.2.1", "Value 2.2.1")),
            (8, 10, "Child", ("Subitem 2.2.2", "Value 2.2.2")),
            (8, 11, "Child", ("Subitem 2.2.3", "Value 2.2.3")),
            (6, 12, "Child", ("Subitem 2.3", "Value 2.3")),
            (6, 13, "Child", ("Subitem 2.4", "Value 2.4")),
            ("", 14, "Parent", ("Item 3", "Value 3")),
            (14, 15, "Child", ("Subitem 3.1", "Value 3.1")),
            (14, 16, "Child", ("Subitem 3.2", "Value 3.2")),
            (14, 17, "Child", ("Subitem 3.3", "Value 3.3")),
            (14, 18, "Child", ("Subitem 3.4", "Value 3.4")),
            ("", 19, "Parent", ("Item 4", "Value 4")),
            (19, 20, "Child", ("Subitem 4.1", "Value 4.1")),
            (19, 21, "Sub-parent", ("Subitem 4.2", "Value 4.2")),
            (21, 22, "Child", ("Subitem 4.2.1", "Value 4.2.1")),
            (21, 23, "Child", ("Subitem 4.2.2", "Value 4.2.2")),
            (21, 24, "Child", ("Subitem 4.2.3", "Value 4.2.3")),
            (19, 25, "Child", ("Subitem 4.3", "Value 4.3")),
        ]

        # Insert treeview data
        for item in treeview_data:
            self.treeview.insert(
                parent=item[0], index="end", iid=item[1], text=item[2], values=item[3]
            )
            if item[0] == "" or item[1] in {8, 21}:
                self.treeview.item(item[1], open=True)  # Open parents

        # Select and scroll
        self.treeview.selection_set(10)
        self.treeview.see(7)

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
        if mileage:
            print(f"Mileage: {mileage} {units}")

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
