# from tkinter import *
# from tkinter.ttk import *
# import subprocess
# import os

# def get_input(prompt):
#     def on_submit():
#         response.set(input_field.get())
#         root.destroy()

#     root = Tk()
#     root.geometry('800x500')
#     root.title(prompt)

#     response = StringVar()

#     label = Label(root, text=prompt)
#     label.pack()

#     input_field = Entry(root, width=100, textvariable=response)
#     input_field.pack(pady=20)
#     input_field.focus_set()

#     submit = Button(root, text='Submit', command=on_submit)
#     submit.pack()

#     root.mainloop()

#     return response.get()

# # Replace this line with the output of `which python` in your terminal
# python_path = '/opt/homebrew/bin/python3'

# while True:
#     prompt = "What's your question about MYSQL?"
#     question = get_input(prompt)

#     if question:
#         command = f'{python_path} mysql_flow.py "{question}"'  # Updated this line
#         response = subprocess.check_output(command, shell=True).strip().decode()
#         print(response)

#     prompt = f'Do you have another question about MYSQL?'
#     if get_input(prompt).lower() in ['no', 'n']:
#         break

from tkinter import *
from tkinter.ttk import *
import subprocess
import os
from pathlib import Path
import pinecone

# init pinecone client
pinecone.init(api_key=os.getenv("PINECONE_API_KEY"))

# init pinecone index
index = pinecone.Index(name="mysql_index")
env = pinecone.Environment(name="mysql_env")

# function to store the query and its result in pinecone
def store_query(query, result):
    # store the query and its result in pinecone
    index.upsert([pinecone.IndexItem(id=query, vector=result)])

# function to get the query and its result from pinecone
def get_query(query):
    # get the query and its result from pinecone
    return index.search(query, 1)

def on_submit():
    question = input_field.get()
    input_field.delete(0, END)
    
    if question:
        chat_history.insert(END, f'User: {question}')
        chat_history.see(END)
        
        # Get AI response
        command = f'{python_path} {mysql_flow_path} "{question}"'
        response = subprocess.check_output(command, shell=True).strip().decode()
        
        chat_history.insert(END, f'AI: {response}')
        chat_history.see(END)

        # Add approval/denial buttons for the query
        approve_button = Button(root, text='Approve', command=approve_query)
        deny_button = Button(root, text='Deny', command=deny_query)
        approve_button.pack()
        deny_button.pack()

def approve_query():
    # Log the success and update the MySQL vector
    # Then remove the approval/denial buttons
    pass

def deny_query():
    # Log the failure and update the MySQL vector
    # Then remove the approval/denial buttons
    pass

root = Tk()
root.geometry('800x500')
root.title("MYSQL Chat")

chat_history = Text(root, wrap=WORD, height=20)
chat_history.pack(pady=20)

input_field = Entry(root, width=100)
input_field.pack(pady=20)
input_field.focus_set()

submit = Button(root, text='Submit', command=on_submit)
submit.pack()

python_path = '/opt/homebrew/bin/python3'

current_file_path = Path(__file__).resolve()
current_directory = current_file_path.parent
mysql_flow_path = current_directory / "mysql_flow.py"

root.mainloop()
