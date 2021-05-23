# -*- coding: utf-8 -*-
"""
Created on Mon May 10 18:27:43 2021

@author: Acer
"""

import tkinter as tk
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
from keras.preprocessing import image
import image as img
from PIL import Image, ImageTk
import tkinter.font as tkFont


win = tk.Tk()
sv = tk.StringVar()
win.geometry('1000x1000')
win.title('Covid checking app')
win.configure(bg="black")
fontStyle = tkFont.Font(family="Lucida Grande", size=20)

def change():
    path = sv.get()
    from keras.models import load_model
    cnn2 = load_model("covid2")
    test_image = image.load_img( path, target_size = (64, 64))
    test_image = image.img_to_array(test_image) 
    test_image = np.expand_dims(test_image, axis = 0)
    result = cnn2.predict(test_image)
    image1 = Image.open(path)
    test = ImageTk.PhotoImage(image1)
    label1 = tk.Label(image=test)
    label1.image = test
    label1.place(x=400, y=150)
    
  
    if result[0][0] == 1:
        prediction = 'Covid Positive Scan2'
    else:
       prediction = 'Covid Negative scan'
    
    b.config(text = prediction)



a = tk.Label(win, text="Enter the path to your report",bg = "black",fg= "white", font = fontStyle)
a.pack()
e = tk.Entry(win, text = sv,font = fontStyle)
e.pack()
b = tk.Label(win, text=" ",bg = "black",fg= "white",font = fontStyle)
b.pack()

tk.Button(win, text="Get Report", command=change,font = fontStyle).pack()



win.mainloop()

