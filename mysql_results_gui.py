import tkinter as tk

# Create the main window
root = tk.Tk()
root.title('Results Display')

# Text box to display the returned results
text_frame = tk.Frame(root)
text_frame.pack(side='top', fill='both', expand=True)
scrollbar = tk.Scrollbar(text_frame)
scrollbar.pack(side='right', fill='y')
result_text = tk.Text(text_frame, wrap='none', yscrollcommand=scrollbar.set)
result_text.pack(side='left', fill='both', expand=True)
scrollbar.config(command=result_text.yview)

# function to add a given message to the text box
# make sure to clear the text box first

def display_results(data):
    result_text.delete('1.0', tk.END)
    for row in data:
        result_text.insert('end', row)

# Start the GUI window
root.mainloop()