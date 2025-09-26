import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import pyperclip
import hashlib
import json
import os
from datetime import datetime

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Password Generator")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        self.root.configure(bg='#f0f0f0')
        
        # Password history file
        self.history_file = "password_history.json"
        self.password_history = self.load_password_history()
        
        self.setup_ui()
        
    def setup_ui(self):
        # Header
        header_frame = tk.Frame(self.root, bg='#2c3e50', height=80)
        header_frame.pack(fill=tk.X, padx=10, pady=10)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(header_frame, text="Advanced Password Generator", 
                              font=('Arial', 18, 'bold'), fg='white', bg='#2c3e50')
        title_label.pack(expand=True)
        
        # Main content frame
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Password length selection
        length_frame = tk.Frame(main_frame, bg='#f0f0f0')
        length_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(length_frame, text="Password Length:", font=('Arial', 12), 
                bg='#f0f0f0').pack(side=tk.LEFT)
        
        self.length_var = tk.IntVar(value=12)
        length_scale = tk.Scale(length_frame, from_=6, to=32, orient=tk.HORIZONTAL, 
                               variable=self.length_var, bg='#f0f0f0', 
                               length=200, showvalue=True)
        length_scale.pack(side=tk.RIGHT, padx=10)
        
        # Character options
        options_frame = tk.LabelFrame(main_frame, text="Character Options", 
                                     font=('Arial', 12, 'bold'), bg='#f0f0f0')
        options_frame.pack(fill=tk.X, pady=10)
        
        self.uppercase_var = tk.BooleanVar(value=True)
        tk.Checkbutton(options_frame, text="Uppercase Letters (A-Z)", 
                      variable=self.uppercase_var, bg='#f0f0f0').pack(anchor=tk.W)
        
        self.lowercase_var = tk.BooleanVar(value=True)
        tk.Checkbutton(options_frame, text="Lowercase Letters (a-z)", 
                      variable=self.lowercase_var, bg='#f0f0f0').pack(anchor=tk.W)
        
        self.digits_var = tk.BooleanVar(value=True)
        tk.Checkbutton(options_frame, text="Digits (0-9)", 
                      variable=self.digits_var, bg='#f0f0f0').pack(anchor=tk.W)
        
        self.symbols_var = tk.BooleanVar(value=True)
        tk.Checkbutton(options_frame, text="Symbols (!@#$%^&*)", 
                      variable=self.symbols_var, bg='#f0f0f0').pack(anchor=tk.W)
        
        # Password strength indicator
        strength_frame = tk.Frame(main_frame, bg='#f0f0f0')
        strength_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(strength_frame, text="Password Strength:", font=('Arial', 12), 
                bg='#f0f0f0').pack(side=tk.LEFT)
        
        self.strength_label = tk.Label(strength_frame, text="", font=('Arial', 12, 'bold'), 
                                      bg='#f0f0f0')
        self.strength_label.pack(side=tk.RIGHT)
        
        # Generated password display
        password_frame = tk.Frame(main_frame, bg='#f0f0f0')
        password_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(password_frame, text="Generated Password:", font=('Arial', 12), 
                bg='#f0f0f0').pack(anchor=tk.W)
        
        self.password_var = tk.StringVar()
        password_entry = tk.Entry(password_frame, textvariable=self.password_var, 
                                 font=('Arial', 14), state='readonly', width=30)
        password_entry.pack(fill=tk.X, pady=5)
        
        # Buttons
        button_frame = tk.Frame(main_frame, bg='#f0f0f0')
        button_frame.pack(fill=tk.X, pady=10)
        
        generate_btn = tk.Button(button_frame, text="Generate Password", 
                                command=self.generate_password, bg='#3498db', 
                                fg='white', font=('Arial', 12), width=15)
        generate_btn.pack(side=tk.LEFT, padx=5)
        
        copy_btn = tk.Button(button_frame, text="Copy to Clipboard", 
                            command=self.copy_to_clipboard, bg='#2ecc71', 
                            fg='white', font=('Arial', 12), width=15)
        copy_btn.pack(side=tk.LEFT, padx=5)
        
        save_btn = tk.Button(button_frame, text="Save Password", 
                            command=self.save_password, bg='#e74c3c', 
                            fg='white', font=('Arial', 12), width=15)
        save_btn.pack(side=tk.LEFT, padx=5)
        
        # Password history
        history_frame = tk.LabelFrame(main_frame, text="Password History", 
                                     font=('Arial', 12, 'bold'), bg='#f0f0f0')
        history_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Create a scrollable text widget for history
        scrollbar = tk.Scrollbar(history_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.history_text = tk.Text(history_frame, height=8, yscrollcommand=scrollbar.set,
                                   state=tk.DISABLED, font=('Arial', 10))
        self.history_text.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.history_text.yview)
        
        # Update history display
        self.update_history_display()
        
    def generate_password(self):
        # Check if at least one character type is selected
        if not any([self.uppercase_var.get(), self.lowercase_var.get(), 
                   self.digits_var.get(), self.symbols_var.get()]):
            messagebox.showerror("Error", "Please select at least one character type.")
            return
        
        # Build character set based on selections
        characters = ""
        if self.uppercase_var.get():
            characters += string.ascii_uppercase
        if self.lowercase_var.get():
            characters += string.ascii_lowercase
        if self.digits_var.get():
            characters += string.digits
        if self.symbols_var.get():
            characters += "!@#$%^&*()_+-=[]{}|;:,.<>?"
        
        # Generate password
        length = self.length_var.get()
        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_var.set(password)
        
        # Update strength indicator
        self.update_strength_indicator(password)
    
    def update_strength_indicator(self, password):
        score = 0
        if len(password) >= 12:
            score += 2
        elif len(password) >= 8:
            score += 1
            
        # Check for character variety
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_symbol = any(not c.isalnum() for c in password)
        
        variety_score = sum([has_upper, has_lower, has_digit, has_symbol])
        score += variety_score
        
        # Set strength label
        if score >= 5:
            self.strength_label.config(text="Strong", fg="green")
        elif score >= 3:
            self.strength_label.config(text="Medium", fg="orange")
        else:
            self.strength_label.config(text="Weak", fg="red")
    
    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Success", "Password copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "No password generated yet.")
    
    def save_password(self):
        password = self.password_var.get()
        if not password:
            messagebox.showwarning("Warning", "No password to save.")
            return
            
        # Create a simple hash for identification (not for security)
        password_hash = hashlib.md5(password.encode()).hexdigest()[:8]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Add to history
        self.password_history.append({
            'password': password,
            'hash': password_hash,
            'timestamp': timestamp,
            'length': len(password)
        })
        
        # Save to file
        self.save_password_history()
        
        # Update display
        self.update_history_display()
        messagebox.showinfo("Success", "Password saved to history!")
    
    def load_password_history(self):
        if os.path.exists(self.history_file):
            try:
                with open(self.history_file, 'r') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def save_password_history(self):
        try:
            with open(self.history_file, 'w') as f:
                json.dump(self.password_history, f)
        except:
            pass  # Silently fail if we can't save history
    
    def update_history_display(self):
        self.history_text.config(state=tk.NORMAL)
        self.history_text.delete(1.0, tk.END)
        
        if not self.password_history:
            self.history_text.insert(tk.END, "No passwords saved yet.")
        else:
            for i, entry in enumerate(reversed(self.password_history[-10:])):  # Show last 10
                self.history_text.insert(tk.END, 
                    f"{i+1}. Length: {entry['length']} | Hash: {entry['hash']} | {entry['timestamp']}\n")
        
        self.history_text.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()