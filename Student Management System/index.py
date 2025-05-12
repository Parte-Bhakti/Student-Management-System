import tkinter as tk
from tkinter import messagebox, ttk
import json
import os
from tkinter.font import Font

class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1000x700")
        self.root.configure(bg="#e6e6fa")  # Light purple background
        
        # Custom fonts
        self.title_font = Font(family="Helvetica", size=18, weight="bold")
        self.button_font = Font(family="Arial", size=14, weight="bold")
        self.label_font = Font(family="Arial", size=12)
        
        # Color scheme
        self.bg_color = "#e6e6fa"  # Light purple background
        self.primary_color = "#6a5acd"  # Slate blue
        self.secondary_color = "#9370db"  # Medium purple
        self.accent_color = "#ba55d3"  # Medium orchid
        self.danger_color = "#ff6b6b"  # Soft red
        self.warning_color = "#ffd166"  # Soft yellow
        self.dark_color = "#4b4b4b"  # Dark gray
        self.light_color = "#ffffff"  # White
        self.card_color = "#f8f9fa"  # Light card background
        
        # User data files
        self.users_file = "users.json"
        self.students_file = "students.json"
        
        # Initialize data files
        self.init_files()
        
        # Center the main window
        self.center_window()
        
        # Show login page first
        self.show_login_page()
    
    def init_files(self):
        """Initialize data files if they don't exist"""
        if not os.path.exists(self.users_file):
            with open(self.users_file, 'w') as f:
                json.dump([], f)
        
        if not os.path.exists(self.students_file):
            with open(self.students_file, 'w') as f:
                json.dump([], f)
    
    def clear_window(self):
        """Clear all widgets from the window"""
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def center_window(self):
        """Center the main window on the screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def show_login_page(self):
        """Display the login page with attractive design"""
        self.clear_window()
        self.root.configure(bg=self.bg_color)
        
        # Main container
        container = tk.Frame(self.root, bg=self.bg_color)
        container.place(relx=0.5, rely=0.5, anchor="center")
        
        # Login card with white background
        card = tk.Frame(container, bg=self.card_color, padx=40, pady=40, 
                        relief="ridge", borderwidth=2, highlightbackground=self.primary_color)
        card.pack()
        
        # Login form
        tk.Label(card, text="Login to Your Account", font=("Helvetica", 20, "bold"), 
                bg=self.card_color, fg=self.primary_color).grid(row=0, column=0, columnspan=2, pady=(0, 30))
        
        # Username
        tk.Label(card, text="Username:", font=self.label_font, 
                bg=self.card_color, fg=self.dark_color).grid(row=1, column=0, sticky="e", padx=10, pady=15)
        self.login_username = tk.Entry(card, font=self.label_font, 
                                     width=25, borderwidth=2, relief="groove")
        self.login_username.grid(row=1, column=1, padx=10, pady=15)
        
        # Password
        tk.Label(card, text="Password:", font=self.label_font, 
                bg=self.card_color, fg=self.dark_color).grid(row=2, column=0, sticky="e", padx=10, pady=15)
        self.login_password = tk.Entry(card, font=self.label_font, show="*", 
                                     width=25, borderwidth=2, relief="groove")
        self.login_password.grid(row=2, column=1, padx=10, pady=15)
        
        # Buttons frame
        button_frame = tk.Frame(card, bg=self.card_color)
        button_frame.grid(row=3, column=0, columnspan=2, pady=30)
        
        # Login button with primary color
        login_btn = tk.Button(button_frame, text="LOGIN", font=self.button_font, 
                            bg=self.primary_color, fg=self.light_color, width=15, height=1,
                            command=self.login, relief="raised", borderwidth=2)
        login_btn.pack(side=tk.LEFT, padx=15)
        
        # Register button with secondary color
        register_btn = tk.Button(button_frame, text="REGISTER", font=self.button_font, 
                               bg=self.secondary_color, fg=self.light_color, width=15, height=1,
                               command=self.show_register_page, relief="raised", borderwidth=2)
        register_btn.pack(side=tk.LEFT, padx=15)
    
    def show_register_page(self):
        """Display the registration page with attractive design"""
        self.clear_window()
        self.root.configure(bg=self.bg_color)
        
        # Main container
        container = tk.Frame(self.root, bg=self.bg_color)
        container.place(relx=0.5, rely=0.5, anchor="center")
        
        # Registration card with white background
        card = tk.Frame(container, bg=self.card_color, padx=40, pady=40, 
                        relief="ridge", borderwidth=2, highlightbackground=self.primary_color)
        card.pack()
        
        # Registration form
        tk.Label(card, text="Create New Account", font=("Helvetica", 20, "bold"), 
                bg=self.card_color, fg=self.primary_color).grid(row=0, column=0, columnspan=2, pady=(0, 30))
        
        # Registration fields
        fields = [
            ("Username:", "reg_username"),
            ("Password:", "reg_password"),
            ("Confirm Password:", "reg_confirm")
        ]
        
        for i, (label_text, var_name) in enumerate(fields, start=1):
            tk.Label(card, text=label_text, font=self.label_font, 
                    bg=self.card_color, fg=self.dark_color).grid(row=i, column=0, sticky="e", padx=10, pady=15)
            entry = tk.Entry(card, font=self.label_font, width=25, 
                            borderwidth=2, relief="groove")
            if "Password" in label_text:
                entry.config(show="*")
            entry.grid(row=i, column=1, padx=10, pady=15)
            setattr(self, var_name, entry)
        
        # Buttons frame
        button_frame = tk.Frame(card, bg=self.card_color)
        button_frame.grid(row=4, column=0, columnspan=2, pady=30)
        
        # Register button with secondary color
        register_btn = tk.Button(button_frame, text="REGISTER", font=self.button_font, 
                               bg=self.secondary_color, fg=self.light_color, width=15, height=1,
                               command=self.register, relief="raised", borderwidth=2)
        register_btn.pack(side=tk.LEFT, padx=15)
        
        # Back button with danger color
        back_btn = tk.Button(button_frame, text="BACK", font=self.button_font, 
                           bg=self.danger_color, fg=self.light_color, width=15, height=1,
                           command=self.show_login_page, relief="raised", borderwidth=2)
        back_btn.pack(side=tk.LEFT, padx=15)
    
    def show_dashboard(self):
        """Display the main dashboard with attractive design"""
        self.clear_window()
        self.root.configure(bg=self.bg_color)
        
        # Configure root grid
        self.root.grid_rowconfigure(0, weight=0)  # Header
        self.root.grid_rowconfigure(1, weight=1)  # Content
        self.root.grid_rowconfigure(2, weight=0)  # Footer
        self.root.grid_columnconfigure(0, weight=1)
        
        # Header with primary color
        header = tk.Frame(self.root, bg=self.primary_color, height=100)
        header.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
        
        tk.Label(header, text="STUDENT MANAGEMENT SYSTEM", font=("Helvetica", 20, "bold"), 
                bg=self.primary_color, fg="white").pack(side=tk.LEFT, padx=20)
        
        # Logout button with danger color
        logout_btn = tk.Button(header, text="LOGOUT", font=self.button_font, 
                             bg=self.danger_color, fg="white", width=10, height=1,
                             command=self.show_login_page, relief="raised", borderwidth=2)
        logout_btn.pack(side=tk.RIGHT, padx=20)
        
        # Dashboard content
        content = tk.Frame(self.root, bg=self.bg_color)
        content.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
        
        # Welcome message
        welcome_frame = tk.Frame(content, bg=self.bg_color)
        welcome_frame.pack(fill="x", pady=(0, 30))
        tk.Label(welcome_frame, text="Welcome to Dashboard", font=("Helvetica", 18, "bold"), 
                bg=self.bg_color, fg=self.primary_color).pack()
        
        # Big buttons container
        buttons_frame = tk.Frame(content, bg=self.bg_color)
        buttons_frame.pack(expand=True, fill="both")
        
        # Configure grid for buttons
        buttons_frame.grid_rowconfigure(0, weight=1)
        buttons_frame.grid_rowconfigure(1, weight=1)
        buttons_frame.grid_columnconfigure(0, weight=1)
        buttons_frame.grid_columnconfigure(1, weight=1)
        
        # Big buttons (2x2 grid) with different colors
        buttons = [
            ("Add Student", self.secondary_color, self.show_add_student),
            ("View Students", self.accent_color, self.show_view_students),
            ("Search Student", self.warning_color, self.show_search_student),
            ("Manage Database", self.danger_color, self.show_database_tools)
        ]
        
        # Button styling parameters
        btn_width = 20  # Increased width
        btn_height = 3   # Increased height
        btn_font = ("Arial", 14, "bold")  # Bigger font
        
        for i, (text, color, command) in enumerate(buttons):
            btn = tk.Button(buttons_frame, text=text, font=btn_font, 
                           bg=color, fg="white", height=btn_height, width=btn_width,
                           command=command, relief="raised", borderwidth=3,
                           activebackground=color, activeforeground="white")
            btn.grid(row=i//2, column=i%2, padx=30, pady=30, sticky="nsew")
        
        # Footer with dark color
        footer = tk.Frame(self.root, bg=self.dark_color, height=50)
        footer.grid(row=2, column=0, sticky="nsew")
        tk.Label(footer, text="© 2023 Student Management System", font=("Arial", 10), 
                bg=self.dark_color, fg=self.light_color).pack(pady=15)
    
    def show_add_student(self):
        """Show the add student form with attractive design"""
        self.clear_window()
        self.root.configure(bg=self.bg_color)
        
        # Header with primary color
        header = tk.Frame(self.root, bg=self.primary_color, height=100)
        header.pack(fill="x")
        
        tk.Label(header, text="ADD NEW STUDENT", font=("Helvetica", 20, "bold"), 
                bg=self.primary_color, fg="white").pack(side=tk.LEFT, padx=20)
        
        # Back button with danger color
        back_btn = tk.Button(header, text="BACK", font=self.button_font, 
                           bg=self.danger_color, fg="white", width=10, height=1,
                           command=self.show_dashboard, relief="raised", borderwidth=2)
        back_btn.pack(side=tk.RIGHT, padx=20)
        
        # Main container
        container = tk.Frame(self.root, bg=self.bg_color)
        container.place(relx=0.5, rely=0.5, anchor="center")
        
        # Form card with white background
        card = tk.Frame(container, bg=self.card_color, padx=40, pady=40, 
                        relief="ridge", borderwidth=2, highlightbackground=self.primary_color)
        card.pack()
        
        # Form fields
        fields = ["Student ID", "Full Name", "Age", "Grade", "Email", "Phone", "Address"]
        self.entries = {}
        
        for i, field in enumerate(fields):
            tk.Label(card, text=f"{field}:", font=self.label_font, 
                    bg=self.card_color, fg=self.dark_color).grid(row=i, column=0, sticky="e", padx=10, pady=15)
            entry = tk.Entry(card, font=self.label_font, width=30, 
                            borderwidth=2, relief="groove")
            entry.grid(row=i, column=1, padx=10, pady=15)
            self.entries[field.lower().replace(" ", "_")] = entry
        
        # Submit button with secondary color
        submit_btn = tk.Button(card, text="SAVE STUDENT", font=self.button_font, 
                             bg=self.secondary_color, fg="white", height=2, width=20,
                             command=self.save_student, relief="raised", borderwidth=2)
        submit_btn.grid(row=len(fields), column=0, columnspan=2, pady=30)
        
        # Footer with dark color
        footer = tk.Frame(self.root, bg=self.dark_color, height=50)
        footer.pack(side="bottom", fill="x")
        tk.Label(footer, text="© 2023 Student Management System", font=("Arial", 10), 
                bg=self.dark_color, fg=self.light_color).pack(pady=15)
    
    def show_view_students(self):
        """Show all students in an attractive table with delete functionality"""
        self.clear_window()
        self.root.configure(bg=self.bg_color)
        
        # Header with primary color
        header = tk.Frame(self.root, bg=self.primary_color, height=100)
        header.pack(fill="x")
        
        tk.Label(header, text="VIEW STUDENTS", font=("Helvetica", 20, "bold"), 
                bg=self.primary_color, fg="white").pack(side=tk.LEFT, padx=20)
        
        # Back button with danger color
        back_btn = tk.Button(header, text="BACK", font=self.button_font, 
                           bg=self.danger_color, fg="white", width=10, height=1,
                           command=self.show_dashboard, relief="raised", borderwidth=2)
        back_btn.pack(side=tk.RIGHT, padx=20)
        
        # Refresh button with accent color
        refresh_btn = tk.Button(header, text="REFRESH", font=self.button_font, 
                              bg=self.accent_color, fg="white", width=10, height=1,
                              command=self.load_students_to_tree, relief="raised", borderwidth=2)
        refresh_btn.pack(side=tk.RIGHT, padx=10)
        
        # Content
        content = tk.Frame(self.root, bg=self.bg_color)
        content.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Treeview with scrollbars
        tree_frame = tk.Frame(content, bg=self.bg_color)
        tree_frame.pack(fill="both", expand=True)
        
        # Vertical scrollbar
        vsb = ttk.Scrollbar(tree_frame, orient="vertical")
        vsb.pack(side="right", fill="y")
        
        # Horizontal scrollbar
        hsb = ttk.Scrollbar(tree_frame, orient="horizontal")
        hsb.pack(side="bottom", fill="x")
        
        # Treeview with style
        style = ttk.Style()
        style.configure("Treeview.Heading", font=self.label_font, background=self.primary_color, foreground="white")
        style.configure("Treeview", font=self.label_font, rowheight=25, background=self.card_color)
        
        self.tree = ttk.Treeview(tree_frame, columns=("ID", "Name", "Age", "Grade", "Email", "Phone", "Address"), 
                                show="headings", yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.tree.pack(fill="both", expand=True)
        
        # Configure scrollbars
        vsb.config(command=self.tree.yview)
        hsb.config(command=self.tree.xview)
        
        # Define columns
        columns = [
            ("ID", 100),
            ("Name", 200),
            ("Age", 80),
            ("Grade", 100),
            ("Email", 200),
            ("Phone", 150),
            ("Address", 300)
        ]
        
        for col, width in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=width, anchor="center")
        
        # Add delete and update buttons
        button_frame = tk.Frame(content, bg=self.bg_color)
        button_frame.pack(pady=20)
        
        delete_btn = tk.Button(button_frame, text="DELETE SELECTED", font=self.button_font, 
                             bg=self.danger_color, fg="white", width=20, height=1,
                             command=self.delete_selected_student, relief="raised", borderwidth=2)
        delete_btn.pack(side=tk.LEFT, padx=15)
        
        update_btn = tk.Button(button_frame, text="UPDATE SELECTED", font=self.button_font, 
                             bg=self.warning_color, fg="white", width=20, height=1,
                             command=self.show_update_student, relief="raised", borderwidth=2)
        update_btn.pack(side=tk.LEFT, padx=15)
        
        # Load data
        self.load_students_to_tree()
        
        # Footer with dark color
        footer = tk.Frame(self.root, bg=self.dark_color, height=50)
        footer.pack(side="bottom", fill="x")
        tk.Label(footer, text="© 2025 Student Management System", font=("Arial", 10), 
                bg=self.dark_color, fg=self.light_color).pack(pady=15)
    
    def show_update_student(self):
        """Show the update student form with current data"""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a student to update")
            return
        
        # Get selected student data
        student_data = self.tree.item(selected_item)['values']
        
        self.clear_window()
        self.root.configure(bg=self.bg_color)
        
        # Header with primary color
        header = tk.Frame(self.root, bg=self.primary_color, height=100)
        header.pack(fill="x")
        
        tk.Label(header, text="UPDATE STUDENT", font=("Helvetica", 20, "bold"), 
                bg=self.primary_color, fg="white").pack(side=tk.LEFT, padx=20)
        
        # Back button with danger color
        back_btn = tk.Button(header, text="BACK", font=self.button_font, 
                           bg=self.danger_color, fg="white", width=10, height=1,
                           command=self.show_view_students, relief="raised", borderwidth=2)
        back_btn.pack(side=tk.RIGHT, padx=20)
        
        # Main container
        container = tk.Frame(self.root, bg=self.bg_color)
        container.place(relx=0.5, rely=0.5, anchor="center")
        
        # Form card with white background
        card = tk.Frame(container, bg=self.card_color, padx=40, pady=40, 
                        relief="ridge", borderwidth=2, highlightbackground=self.primary_color)
        card.pack()
        
        # Form fields
        fields = ["Student ID", "Full Name", "Age", "Grade", "Email", "Phone", "Address"]
        self.update_entries = {}
        
        for i, field in enumerate(fields):
            tk.Label(card, text=f"{field}:", font=self.label_font, 
                    bg=self.card_color, fg=self.dark_color).grid(row=i, column=0, sticky="e", padx=10, pady=15)
            entry = tk.Entry(card, font=self.label_font, width=30, 
                            borderwidth=2, relief="groove")
            entry.grid(row=i, column=1, padx=10, pady=15)
            self.update_entries[field.lower().replace(" ", "_")] = entry
        
        # Fill the form with current data
        self.update_entries['student_id'].insert(0, student_data[0])
        self.update_entries['student_id'].config(state='readonly')  # Don't allow ID change
        self.update_entries['full_name'].insert(0, student_data[1])
        self.update_entries['age'].insert(0, student_data[2])
        self.update_entries['grade'].insert(0, student_data[3])
        self.update_entries['email'].insert(0, student_data[4])
        self.update_entries['phone'].insert(0, student_data[5])
        self.update_entries['address'].insert(0, student_data[6])
        
        # Store the original ID for reference
        self.original_id = student_data[0]
        
        # Submit button with warning color (for update)
        submit_btn = tk.Button(card, text="UPDATE STUDENT", font=self.button_font, 
                             bg=self.warning_color, fg="white", height=2, width=20,
                             command=self.update_student, relief="raised", borderwidth=2)
        submit_btn.grid(row=len(fields), column=0, columnspan=2, pady=30)
        
        # Footer with dark color
        footer = tk.Frame(self.root, bg=self.dark_color, height=50)
        footer.pack(side="bottom", fill="x")
        tk.Label(footer, text="© 2023 Student Management System", font=("Arial", 10), 
                bg=self.dark_color, fg=self.light_color).pack(pady=15)
    
    def update_student(self):
        """Update the student record in the database"""
        updated_data = {
            "id": self.update_entries['student_id'].get(),
            "name": self.update_entries['full_name'].get(),
            "age": self.update_entries['age'].get(),
            "grade": self.update_entries['grade'].get(),
            "email": self.update_entries['email'].get(),
            "phone": self.update_entries['phone'].get(),
            "address": self.update_entries['address'].get()
        }
        
        # Validate all fields are filled
        if not all(updated_data.values()):
            messagebox.showerror("Error", "All fields are required")
            return
        
        try:
            with open(self.students_file, 'r') as f:
                students = json.load(f)
            
            # Find and update the student
            for i, student in enumerate(students):
                if student['id'] == self.original_id:
                    students[i] = updated_data
                    break
            
            with open(self.students_file, 'w') as f:
                json.dump(students, f)
            
            messagebox.showinfo("Success", "Student updated successfully!")
            self.show_view_students()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update student: {str(e)}")
    
    def show_search_student(self):
        """Show the search student form with attractive design"""
        self.clear_window()
        self.root.configure(bg=self.bg_color)
        
        # Header with primary color
        header = tk.Frame(self.root, bg=self.primary_color, height=100)
        header.pack(fill="x")
        
        tk.Label(header, text="SEARCH STUDENT", font=("Helvetica", 20, "bold"), 
                bg=self.primary_color, fg="white").pack(side=tk.LEFT, padx=20)
        
        # Back button with danger color
        back_btn = tk.Button(header, text="BACK", font=self.button_font, 
                           bg=self.danger_color, fg="white", width=10, height=1,
                           command=self.show_dashboard, relief="raised", borderwidth=2)
        back_btn.pack(side=tk.RIGHT, padx=20)
        
        # Main container
        container = tk.Frame(self.root, bg=self.bg_color)
        container.place(relx=0.5, rely=0.5, anchor="center")
        
        # Search card with white background
        card = tk.Frame(container, bg=self.card_color, padx=40, pady=40, 
                        relief="ridge", borderwidth=2, highlightbackground=self.primary_color)
        card.pack()
        
        # Search options
        tk.Label(card, text="Search Criteria:", font=self.label_font, 
                bg=self.card_color, fg=self.dark_color).grid(row=0, column=0, sticky="e", padx=10, pady=15)
        
        self.search_by = tk.StringVar(value="id")
        options = ["ID", "Name", "Grade", "Email"]
        
        option_menu = tk.OptionMenu(card, self.search_by, *options)
        option_menu.config(font=self.label_font, width=15, bg=self.card_color, fg=self.dark_color)
        option_menu.grid(row=0, column=1, sticky="w", padx=10, pady=15)
        
        # Search entry
        tk.Label(card, text="Search Term:", font=self.label_font, 
                bg=self.card_color, fg=self.dark_color).grid(row=1, column=0, sticky="e", padx=10, pady=15)
        
        self.search_entry = tk.Entry(card, font=self.label_font, width=30, 
                                   borderwidth=2, relief="groove")
        self.search_entry.grid(row=1, column=1, sticky="w", padx=10, pady=15)
        
        # Search button with accent color
        search_btn = tk.Button(card, text="SEARCH", font=self.button_font, 
                             bg=self.accent_color, fg="white", height=2, width=20,
                             command=self.search_student, relief="raised", borderwidth=2)
        search_btn.grid(row=2, column=0, columnspan=2, pady=30)
        
        # Results frame
        results_frame = tk.Frame(card, bg=self.card_color)
        results_frame.grid(row=3, column=0, columnspan=2, sticky="nsew")
        
        # Treeview for results
        style = ttk.Style()
        style.configure("Treeview.Heading", font=self.label_font, background=self.primary_color, foreground="white")
        style.configure("Treeview", font=self.label_font, background=self.card_color)
        
        self.search_tree = ttk.Treeview(results_frame, columns=("ID", "Name", "Age", "Grade", "Email"), 
                                       show="headings", height=5)
        self.search_tree.pack(fill="both", expand=True)
        
        # Define columns
        columns = [("ID", 100), ("Name", 200), ("Age", 80), ("Grade", 100), ("Email", 200)]
        
        for col, width in columns:
            self.search_tree.heading(col, text=col)
            self.search_tree.column(col, width=width, anchor="center")
        
        # Footer with dark color
        footer = tk.Frame(self.root, bg=self.dark_color, height=50)
        footer.pack(side="bottom", fill="x")
        tk.Label(footer, text="© 2023 Student Management System", font=("Arial", 10), 
                bg=self.dark_color, fg=self.light_color).pack(pady=15)
    
    def show_database_tools(self):
        """Show database management tools"""
        messagebox.showinfo("Info", "Database tools will be implemented in the next version")
        self.show_dashboard()
    
    # ========== Business Logic Methods ==========
    
    def login(self):
        """Handle login logic"""
        username = self.login_username.get()
        password = self.login_password.get()
        
        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password")
            return
        
        with open(self.users_file, 'r') as f:
            users = json.load(f)
        
        for user in users:
            if user['username'] == username and user['password'] == password:
                messagebox.showinfo("Success", f"Welcome, {username}!")
                self.show_dashboard()
                return
        
        messagebox.showerror("Error", "Invalid username or password")
    
    def register(self):
        """Handle registration logic"""
        username = self.reg_username.get()
        password = self.reg_password.get()
        confirm = self.reg_confirm.get()
        
        if not username or not password or not confirm:
            messagebox.showerror("Error", "All fields are required")
            return
        
        if password != confirm:
            messagebox.showerror("Error", "Passwords do not match")
            return
        
        with open(self.users_file, 'r') as f:
            users = json.load(f)
        
        # Check if username exists
        if any(user['username'] == username for user in users):
            messagebox.showerror("Error", "Username already exists")
            return
        
        # Add new user
        users.append({
            "username": username,
            "password": password
        })
        
        with open(self.users_file, 'w') as f:
            json.dump(users, f)
        
        messagebox.showinfo("Success", "Registration successful! Please login.")
        self.show_login_page()
    
    def save_student(self):
        """Save a new student record"""
        student_data = {
            "id": self.entries['student_id'].get(),
            "name": self.entries['full_name'].get(),
            "age": self.entries['age'].get(),
            "grade": self.entries['grade'].get(),
            "email": self.entries['email'].get(),
            "phone": self.entries['phone'].get(),
            "address": self.entries['address'].get()
        }
        
        # Validate all fields are filled
        if not all(student_data.values()):
            messagebox.showerror("Error", "All fields are required")
            return
        
        with open(self.students_file, 'r') as f:
            students = json.load(f)
        
        # Check if student ID exists
        if any(student['id'] == student_data['id'] for student in students):
            messagebox.showerror("Error", "Student ID already exists")
            return
        
        # Add new student
        students.append(student_data)
        
        with open(self.students_file, 'w') as f:
            json.dump(students, f)
        
        messagebox.showinfo("Success", "Student added successfully!")
        self.show_dashboard()
    
    def load_students_to_tree(self):
        """Load students into the treeview"""
        # Clear existing data
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        try:
            with open(self.students_file, 'r') as f:
                students = json.load(f)
            
            for student in students:
                self.tree.insert("", tk.END, values=(
                    student['id'],
                    student['name'],
                    student['age'],
                    student['grade'],
                    student['email'],
                    student.get('phone', ''),
                    student.get('address', '')
                ))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load students: {str(e)}")
    
    def delete_selected_student(self):
        """Delete the selected student from the database"""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a student to delete")
            return
        
        student_id = self.tree.item(selected_item)['values'][0]
        
        try:
            with open(self.students_file, 'r') as f:
                students = json.load(f)
            
            # Find and remove the student
            students = [s for s in students if s['id'] != student_id]
            
            with open(self.students_file, 'w') as f:
                json.dump(students, f)
            
            messagebox.showinfo("Success", "Student deleted successfully!")
            self.load_students_to_tree()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete student: {str(e)}")
    
    def search_student(self):
        """Search for a student"""
        search_term = self.search_entry.get().lower()
        search_by = self.search_by.get().lower()
        
        if not search_term:
            messagebox.showerror("Error", "Please enter a search term")
            return
        
        # Clear previous results
        for item in self.search_tree.get_children():
            self.search_tree.delete(item)
        
        try:
            with open(self.students_file, 'r') as f:
                students = json.load(f)
            
            found = False
            for student in students:
                # Handle different search criteria
                if search_by == "id" and search_term == student['id'].lower():
                    self.search_tree.insert("", tk.END, values=(
                        student['id'],
                        student['name'],
                        student['age'],
                        student['grade'],
                        student['email']
                    ))
                    found = True
                elif search_by == "name" and search_term in student['name'].lower():
                    self.search_tree.insert("", tk.END, values=(
                        student['id'],
                        student['name'],
                        student['age'],
                        student['grade'],
                        student['email']
                    ))
                    found = True
                elif search_by == "grade" and search_term == student['grade'].lower():
                    self.search_tree.insert("", tk.END, values=(
                        student['id'],
                        student['name'],
                        student['age'],
                        student['grade'],
                        student['email']
                    ))
                    found = True
                elif search_by == "email" and search_term in student['email'].lower():
                    self.search_tree.insert("", tk.END, values=(
                        student['id'],
                        student['name'],
                        student['age'],
                        student['grade'],
                        student['email']
                    ))
                    found = True
            
            if not found:
                messagebox.showinfo("Info", "No students found matching your search")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to search students: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementSystem(root)
    root.mainloop()