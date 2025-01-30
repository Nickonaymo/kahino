import tkinter as tk
from tkinter import ttk

class BeautySalonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Beauty Salon Management System")

        # Create the notebook (tabbed view)
        notebook = ttk.Notebook(root)

        # Admin tab
        self.admin_tab = ttk.Frame(notebook)
        ttk.Label(self.admin_tab, text="Admin Functions: Manage Staff, Reports").pack(padx=10, pady=10)
        notebook.add(self.admin_tab, text="Admin")

        # Staff tab
        self.staff_tab = ttk.Frame(notebook)
        ttk.Label(self.staff_tab, text="Staff Functions: Manage Appointments").pack(padx=10, pady=10)
        notebook.add(self.staff_tab, text="Staff")

        # Appointments tab
        self.appointments_tab = ttk.Frame(notebook)
        ttk.Label(self.appointments_tab, text="Appointments Functions: View Calendar").pack(padx=10, pady=10)
        notebook.add(self.appointments_tab, text="Appointments")

        # Pack the notebook (tabs)
        notebook.pack(expand=True, fill="both")

if __name__ == "__main__":
    root = tk.Tk()
    app = BeautySalonApp(root)
    root.mainloop()
