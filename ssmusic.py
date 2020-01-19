#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 11:40:13 2019

@author: vivek
"""
#Basic Python Music Player - using tkinter and pygame

from tkinter import *
import tkinter.filedialog as tk
import pygame



class Application(Frame):

    def __init__(self,master):
        super(Application, self).__init__(master)

        #self.create_widgets()
        self.playlistbox = Listbox(self, width = 40, height = 10, selectmode = SINGLE) #TODO: ---> BROWSE, MULTIPLE, EXTENDED (p.379)
        

        self.grid(rowspan=5, columnspan=4)
        self.playlistbox.grid(row = 1)
        self.playButton = Button(self, text = 'Play', command = self.play)
        self.loopButton = Button(self, text = 'Loop', command = self.loop)
        self.stopButton = Button(self, text ='Stop', command=self.stop)
        self.closeButton = Button(self, text ='Close', command=self.close)
        
        self.playButton.grid(row=4, column = 0)
        self.loopButton.grid(row=4, column = 1)
        self.stopButton.grid(row=4, column = 2)
        self.closeButton.grid(row=4, column = 3)
        
        self.pack()

        #pygame initialize
        pygame.init()

    def play(self):
            pygame.mixer.music.load("BharDoJholi.mp3")
            pygame.mixer.music.play(0,0.0)    
            
    def loop(self):
            pygame.mixer.music.stop()
            pygame.mixer.music.play(-1,0.0)
            
    def stop(self):
            pygame.mixer.music.stop()
            
    def close(self):
            pygame.mixer.quit()
            

root = Tk()
root.title('Text Editor')
root.geometry('500x200')
app = Application(root)
app.mainloop()

            