from tkinter import * 
from tkinter import filedialog
from tkinter import font
from tkinter import ttk

class Editor:
    def __init__(self):
        self.w = Tk()
        self.w.iconbitmap('./assets/pythonIcon.ico')

        # Menu Bar
        self.menu = Menu(self.w)
        self.file = Menu(self.menu, tearoff = 0)
        self.edit = Menu(self.menu, tearoff = 0)

        self.w.config(menu = self.menu)

        self.menu.add_cascade(label  = "Arquivo", menu       = self.file)
        self.file.add_command(label  = "Novo",    command    = self.new,  accelerator = "Ctrl+N")
        self.file.add_command(label  = "Salvar",  command    = self.save, accelerator = "Ctrl+S")
        self.file.add_command(label  = "Abrir",   command    = self.open, accelerator = "Ctrl+O")
        self.file.add_command(label  = "Sair",    command    = self.exit, accelerator = "Alt+F4")

        self.menu.add_cascade(label  = "Editar",   menu      = self.edit)
        self.edit.add_command(label  = "Desfazer", command   = self.undo, accelerator = "Ctrl+Z")
        self.edit.add_command(label  = "Refazer",  command   = self.redo, accelerator = "Ctrl+Y")

        # Comandos do accelerator
        self.w.bind_all("<Control-n>", self.new)
        self.w.bind_all("<Control-s>", self.save)
        self.w.bind_all("<Control-o>", self.open)
        self.w.bind_all("<Alt-F4>", self.exit)
        self.w.bind_all("<Control-z>", self.undo)
        self.w.bind_all("<Control-y>", self.redo)

        self.frame1 = Frame(self.w, bg = "#fff")
        self.frame1.pack(fill = "both")

        # TextArea
        self.text = Text(self.w, font = "verdana 10", pady=2)
        self.text.pack(expand = True, fill = 'both')

        # ...
        self.w.title("Hello PythonPad")
        self.w.geometry("1000x600")
        self.w.mainloop()

    # Configuração de janelas: 

    def new(self, *args):
        app = Editor()

    def save(self, *args):
        self.file = filedialog.asksaveasfilename(initialdir = "/", title = "Save file as...", filetypes = (("text files", "*.txt"),("all files", "*.*")), defaultextension = ".txt")
        if self.file:
            arquivo = open(self.file, 'w')
            conteudo = self.text.get(1.0,'end')
            arquivo.write(conteudo)
            arquivo.close()

    def open(self, *args):
        self.file = filedialog.askopenfile(mode = "r")
        if self.file:
            file = self.file.read()
            self.text.delete(0.0, END)
            self.text.insert(0.0, file)

    def exit(self, *args):
        self.w.destroy()

    def undo(self, *args):
        self.text.edit_undo()

    def redo(self, *args):
        self.text.edit_redo()

 
if __name__ == "__main__":
    app = Editor()