import tkinter as tk
import tkinter.ttk as ttk
import os

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "hello.ui")

class HelloWidget(tk.Toplevel):
    def __init__(self, master=None, **kw):
        super(HelloWidget, self).__init__(master, **kw)
        self.frame01 = ttk.Frame(self)
        self.label_1 = ttk.Label(self.frame01)
        self.label_1.configure(foreground='#ff0000', justify='center', padding='33', relief='ridge')
        self.label_1.configure(text='Hello')
        self.label_1.grid(padx='8', pady='8')
        self.label_2 = ttk.Label(self.frame01)
        self.label_2.configure(justify='center', text='Generated by pygubu-designer')
        self.label_2.grid(padx='22', pady='4', row='1')
        self.button_ok = ttk.Button(self.frame01)
        self.button_ok.configure(text='Ok')
        self.button_ok.grid(ipadx='4', padx='8', pady='12', row='2')
        self.button_ok.configure(command=self.on_ok_clicked)
        self.frame01.configure(height='200', padding='12', width='200')
        self.frame01.pack(side='top')

    def on_ok_clicked(self):
        pass


if __name__ == '__main__':
    root = tk.Tk()
    widget = HelloWidget(root)
    widget.pack(expand=True, fill='both')
    root.mainloop()


