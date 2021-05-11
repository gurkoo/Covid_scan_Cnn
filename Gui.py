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

win = tk.Tk()
sv = tk.StringVar()
win.geometry('500x500')
win.title('Covid checking app')

def change():
    path = sv.get()
    from keras.models import load_model
    cnn2 = load_model("covid2")
    test_image = image.load_img('dataset/single_prediction/' + path +'.png', target_size = (64, 64))
    test_image = image.img_to_array(test_image) 
    test_image = np.expand_dims(test_image, axis = 0)
    result = cnn2.predict(test_image)
    
    if result[0][0] == 1:
        prediction = 'positive'
    else:
       prediction = 'negative'
    
    b.config(text = prediction)
    
    
    
    

a = tk.Label(win, text="enter the path to png")
a.pack()
e = tk.Entry(win, text = sv)
e.pack()
b = tk.Label(win, text=" ")
b.pack()

tk.Button(win, text="Get gst and price", command=change).pack()


win.mainloop()
