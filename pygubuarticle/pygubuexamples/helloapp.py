#!/usr/bin/env python 
# -*- coding: UTF-8 -*- 

# pygubu demo 
# author Popov O.B
# pirata@russo@gmail.com
# v.001
# last update :01.09.2020 9:14:52
#
import os
import pygubu


PROJECT_PATH = os.path.dirname(__file__)
PROJECT_UI = os.path.join(PROJECT_PATH, "hello.ui")


class HelloApp:
    def __init__(self):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object('main')
        builder.connect_callbacks(self)
    
    def on_ok_clicked(self):
        self.mainwindow.quit()
        

    def run(self):
        self.mainwindow.mainloop()

if __name__ == '__main__':
    app = HelloApp()
    app.run()

