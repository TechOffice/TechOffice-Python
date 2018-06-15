import tkinter as tk

root = tk.Tk()
text = tk.Text(root)
text.insert(tk.INSERT, "testing")
text.pack()
root.mainloop()