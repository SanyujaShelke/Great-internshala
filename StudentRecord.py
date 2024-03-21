import tkinter as tk
from tkinter import messagebox

class StudentRecordSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Record System")
        
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=20, pady=20)
        
        self.name_label = tk.Label(self.frame, text="Name:")
        self.name_label.grid(row=0, column=0, sticky="w")
        self.name_entry = tk.Entry(self.frame)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)
        
        self.age_label = tk.Label(self.frame, text="Age:")
        self.age_label.grid(row=1, column=0, sticky="w")
        self.age_entry = tk.Entry(self.frame)
        self.age_entry.grid(row=1, column=1, padx=10, pady=5)
        
        self.grade_label = tk.Label(self.frame, text="Grade:")
        self.grade_label.grid(row=2, column=0, sticky="w")
        self.grade_entry = tk.Entry(self.frame)
        self.grade_entry.grid(row=2, column=1, padx=10, pady=5)
        
        self.add_button = tk.Button(self.frame, text="Add Record", command=self.add_record)
        self.add_button.grid(row=3, columnspan=2, pady=10)
        
        self.display_button = tk.Button(self.frame, text="Display Records", command=self.display_records)
        self.display_button.grid(row=4, columnspan=2, pady=10)
        
        self.records = []

    def add_record(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        grade = self.grade_entry.get()
        
        if name and age and grade:
            record = {"Name": name, "Age": age, "Grade": grade}
            self.records.append(record)
            messagebox.showinfo("Success", "Record added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def display_records(self):
        if self.records:
            display_window = tk.Toplevel(self.root)
            display_window.title("Student Records")
            
            for i, record in enumerate(self.records):
                for j, (key, value) in enumerate(record.items()):
                    label = tk.Label(display_window, text=f"{key}: {value}")
                    label.grid(row=i, column=j, padx=5, pady=5, sticky="w")
        else:
            messagebox.showwarning("No Records", "No records to display.")

    def clear_entries(self):
        self.name_entry.delete(0, "end")
        self.age_entry.delete(0, "end")
        self.grade_entry.delete(0, "end")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentRecordSystem(root)
    root.mainloop()
