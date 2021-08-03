#!/usr/bin/env python 
# -*- coding: UTF-8 -*- 


# pygubu demo 
# author popov o.b
# pirata@russo@gmail.com
# v.001
# last update :01.09.2020 9:14:52
# 
import os
import pygubu
from booklist import top20books

PROJECT_PATH = os.path.dirname(__file__)
PROJECT_UI = os.path.join(PROJECT_PATH, "booklist.ui")


class BooklistApp:
    def __init__(self):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        #get gui widgets
        self.mainwindow = builder.get_object('toplevel')
        self.listboxBooks = builder.get_object('listboxBooks')
        self.labelSelBook = builder.get_object('labelSelBook')
        self.scrollbarBooks = builder.get_object('scrollbarBooks')
        
        self.fill_books()
        # attach  scrollbar to listbox 
        self.listboxBooks.config(yscrollcommand=self.scrollbarBooks.set)
        self.scrollbarBooks.config(command=self.listboxBooks.yview)

        builder.connect_callbacks(self)
    
    
    def fill_books(self):
       'load book list to listbox'
       for row in top20books:
            self.listboxBooks.insert('end',str(row[0])+'. '+row[1]+'-'+row[2])
    
    def ExitClicked(self):
        self.mainwindow.quit()

    def onSelectBook(self, event=None):
        sender=event.widget
        idx=sender.curselection()
        bookname=sender.get(idx)
        self.labelSelBook['text']=bookname

    def run(self):
        self.mainwindow.mainloop()

if __name__ == '__main__':
    app = BooklistApp()
    app.run()

