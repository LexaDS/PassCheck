"""
This python script is meant to help create a custom text editor using
 tkinter library. The editor has the basic functionality of a normal text editor,
 such as creating new files, opening  files, saving and saving as files and closing files
"""

import tkinter as tk
from tkinter import filedialog,messagebox,Frame

class Menu:
    def __init__(self, parent):
        font_type_size = ('Franklin Gothic', 10)

        menubar=tk.Menu(parent.editor,{'bg':'indian red'})
        parent.editor.config(menu=menubar)

        dropdown=tk.Menu(menubar, font=font_type_size,tearoff=0)
        dropdown.add_command(label='New File',accelerator='Ctrl+N',command=parent.new_file)
        dropdown.add_command(label='Open File',accelerator='Ctrl+O',command=parent.open_file)
        dropdown.add_command(label='Save',accelerator='Ctrl+S',command=parent.save_file)
        dropdown.add_command(label='Save as',accelerator='Ctrl+Shift+S',command=parent.save_as)
        dropdown.add_separator()
        dropdown.add_command(label='Exit', command=parent.editor.destroy)

        about=tk.Menu(menubar, font=font_type_size,tearoff=0)
        view=tk.Menu(menubar,font=font_type_size,tearoff=0)
        help_bar=tk.Menu(menubar,font=font_type_size,tearoff=0)

        view.add_command(label='View version',command=self.msg)
        about.add_command(label="About the editor",command=self.about_msg)
        help_bar.add_command(label='Help',command=self.help_msg)

        menubar.add_cascade(label='Options', menu=dropdown)
        menubar.add_cascade(label='View', menu=view)
        menubar.add_cascade(label='About', menu=about)
        menubar.add_cascade(label='Help', menu=help_bar)


    def about_msg(self):
        title="About the Editor"
        msg="My tiny text editor"
        messagebox.showinfo(title,msg)

    def msg(self):
        title="Release notes"
        msg="Version 1.0"
        messagebox.showinfo(title,msg)

    def help_msg(self):
        title="Ask for assistance"
        msg="Kindly send an email to: [Insert your email address]"
        messagebox.showinfo(title, msg)

class Status:
    def __init__(self,parent):
        font_type_size=('Franklin Gothic', 8)
        self.status=tk.StringVar()
        self.status.set("TextEditor-V.1.0")

        label1=tk.Label(parent.textarea, textvariable=self.status, fg='VioletRed', bg='pink',
                       anchor='sw',font=font_type_size)
        label1.pack(side=tk.BOTTOM,fill=tk.BOTH)

        self.status1 = tk.StringVar()

        label2=tk.Label(parent.textarea, textvariable=self.status1, fg='VioletRed', bg='pink',
                       anchor='se',font=font_type_size)
        label2.pack(side=tk.BOTTOM, fill=tk.BOTH)

    def update_save(self,*args):
        if isinstance(args[0],bool):
            self.status.set("Your file has been saved!")




class TxtEditor:
    def __init__(self,editor):

        editor.title('My Text Editor')
        title_bar=Frame(editor,bg='pink')
        title_bar.bind()
        editor.geometry('1000x500')
        font_type_size=('Franklin Gothic', 8)

        self.editor=editor
        self.filename=None
        self.textarea=tk.Text(editor,{'bg':'RosyBrown1','font':font_type_size})
        self.scroll=tk.Scrollbar(editor,{'bg':'salmon'},command=self.textarea.yview)
        self.textarea.configure(yscrollcommand=self.scroll.set)
        self.textarea.pack(side=tk.LEFT,fill=tk.BOTH, expand=True)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.userinput=tk.StringVar()
        self.menubar=Menu(self)
        self.statusbar=Status(self)
        self.output = tk.Text(editor, {'bg': 'RosyBrown1', 'font': font_type_size}, wrap='word')
        self.shortcut_keys()

    def user_input(self):
        c=0
        u=self.userinput
        text=u.get()
        for w in text:
            if w is str:
                c+=1


    def set_title(self,name=None):
        if name:
            self.editor.title(name+"-TextEditor")
        else:
            self.editor.title("Untitle-TextEditor")

    def new_file(self,*args):
        self.textarea.delete(1.0,tk.END)
        self.filename=None
        self.set_title()

    def open_file(self,*args):
        self.filename=filedialog.askopenfilename(
            defaultextension='.txt',
            filetypes=[('All Files','*.*'),
                       ('Text Files','*.txt'),
                       ('Python Scripts','*.py')]
        )
        if self.filename:
            self.textarea.delete(1.0,tk.END)
            with open(self.filename,'r') as f:
                self.textarea.insert(1.0,f.read())
            self.set_title(self.filename)

    def save_file(self,*args):
        if self.filename:
            try:
                textarea_content=self.textarea.get(1.0,tk.END)
                with open(self.filename,'w') as f:
                    f.write(textarea_content)
                self.statusbar.update_save(True)
            except Exception as e:
                print(e)
        else:
            self.save_as()

    def save_as(self,*args):
        try:
            new_file=filedialog.asksaveasfilename(
                initialfile="Untitled.txt",
                defaultextension='.txt',
                filetypes=[('All Files', '*.*'),
                           ('Text Files', '*.txt'),
                           ('Python Scripts', '*.py')]
            )
            textarea_content=self.textarea.get(1.0,tk.END)
            with open(new_file,'w') as n:
                n.write(textarea_content)
            self.filename=new_file
            self.set_title(self.filename)
            self.statusbar.update_save(True)

        except Exception as e:
            print(e)


    def shortcut_keys(self):
        self.textarea.bind("<Control-n>",self.new_file)
        self.textarea.bind("<Control-o>", self.open_file)
        self.textarea.bind("<Control-s>", self.save_file)
        self.textarea.bind("<Control-S>", self.save_as)
        self.textarea.bind("<Key>", self.statusbar.update_save)



if __name__=="__main__":
    editor=tk.Tk()
    te=TxtEditor(editor)
    editor.mainloop()
