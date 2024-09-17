import re
import tkinter as tk
from tkinter import messagebox

class PasswordCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Strength Checker")
        self.set_initial_size()

        # Set up the GUI
        self.label = tk.Label(root, text="Enter your password:")
        self.label.pack(pady=20)

        # Frame for password entry and show password checkbox
        self.entry_frame = tk.Frame(root)
        self.entry_frame.pack(pady=10, padx=20, fill=tk.X)

        self.password_entry = tk.Entry(self.entry_frame, show="*", width=40)
        self.password_entry.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)

        self.show_password_var = tk.BooleanVar()
        self.show_password_checkbox = tk.Checkbutton(self.entry_frame, text="Show Password", variable=self.show_password_var, command=self.toggle_password_visibility)
        self.show_password_checkbox.pack(side=tk.LEFT, padx=10)

        self.check_button = tk.Button(root, text="Check Password", command=self.check_password)
        self.check_button.pack(pady=20)

    def set_initial_size(self):
        # Dynamically adjust size based on screen size
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        # Set the window size to a percentage of the screen size
        window_width = int(screen_width * 0.5)  # 50% of the screen width
        window_height = int(screen_height * 0.4)  # 40% of the screen height
        self.root.geometry(f"{window_width}x{window_height}")

    def toggle_password_visibility(self):
        if self.show_password_var.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    def check_password(self):
        password = self.password_entry.get()

        # Check the password and generate feedback
        feedback = []
        if len(password) < 8 or len(password) > 16:
            feedback.append("Password should contain more than 8 characters and less than 16 characters.")
        if not re.search("[A-Z]", password):
            feedback.append("Password must contain at least one uppercase letter.")
        if not re.search("[a-z]", password):
            feedback.append("Password must contain at least one lowercase letter.")
        if not re.search("[0-9]", password):
            feedback.append("Password must contain at least one number.")
        if not re.search("[~`!@#$%^&*()_\-+={}[\]|\\;:'\",.<>/?]", password):
            feedback.append("Password should contain at least one special character.")
        
        if feedback:
            # Display feedback in a message box
            messagebox.showerror("Password Strength", "\n".join(feedback))
        else:
            messagebox.showinfo("Password Strength", "Password is strong.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordCheckerApp(root)
    root.mainloop()
