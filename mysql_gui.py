from tkinter import *
import mysql_class

class MysqlGui:
    def __init__(self):
        self.master = Tk()
        self.master.title("MySQL GUI")
        self.mysql = mysql_class.Mysql()
        self.question_label = Label(self.master, text="What's your question?")
        self.question_label.pack()
        self.question_entry = Entry(self.master)
        self.question_entry.pack()
        self.submit_button = Button(self.master, text="Submit", command=self.get_result)
        self.submit_button.pack()
        self.result_label = Label(self.master, text="")
        self.result_label.pack()
        self.master.mainloop()

    def get_result(self):
        question = self.question_entry.get()
        result = self.mysql.query(question)
        self.result_label.configure(text=result)

if __name__ == '__main__':
    MysqlGui()

# Path: scripts/auto_gpt_workspace/mysql_interactions.py