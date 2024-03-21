import tkinter as tk
from tkinter import messagebox

class LibraryManagementSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Library Management System")
        self.master.geometry("400x300")

        self.books = []

        self.title_label = tk.Label(self.master, text="Library Management System", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        self.book_label = tk.Label(self.master, text="Book Title:")
        self.book_label.pack()

        self.book_entry = tk.Entry(self.master)
        self.book_entry.pack()

        self.add_button = tk.Button(self.master, text="Add Book", command=self.add_book)
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(self.master, text="Delete Book", command=self.delete_book)
        self.delete_button.pack()

        self.search_button = tk.Button(self.master, text="Search Book", command=self.search_book)
        self.search_button.pack()

        self.books_listbox = tk.Listbox(self.master, width=40)
        self.books_listbox.pack(pady=10)

    def add_book(self):
        book_title = self.book_entry.get()
        if book_title:
            self.books.append(book_title)
            self.books_listbox.insert(tk.END, book_title)
            self.book_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a book title.")

    def delete_book(self):
        selected_index = self.books_listbox.curselection()
        if selected_index:
            self.books_listbox.delete(selected_index)
            del self.books[selected_index[0]]
        else:
            messagebox.showwarning("Warning", "Please select a book to delete.")

    def search_book(self):
        book_title = self.book_entry.get()
        if book_title:
            found = False
            for i, title in enumerate(self.books):
                if book_title.lower() in title.lower():
                    messagebox.showinfo("Book Found", f"Book '{title}' found at index {i}.")
                    found = True
                    break
            if not found:
                messagebox.showinfo("Book Not Found", f"No book matching '{book_title}' found.")
        else:
            messagebox.showwarning("Warning", "Please enter a book title to search.")

def main():
    root = tk.Tk()
    app = LibraryManagementSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()
