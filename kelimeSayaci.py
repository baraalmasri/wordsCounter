#!/usr/bin/env python
# coding: utf-8

# In[10]:


import tkinter as tk
from tkinter import *

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 200,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='kelimelerin sayisi bulan programi')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='kelimleri giriniz :')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 50, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 100, window=entry1)

frame = tk.Frame(root)
frame.pack()

def kelime_say ():
    icerik = entry1.get()
    kelime = icerik.split()
    ###Kelime Sayma
    wordcount={}
    metin=""
    for word in icerik.split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    for key in wordcount.keys():
        metin=metin+key+":"+f"{wordcount[key]}" +"\n"
        
    listNodes = tk.Listbox(frame, width=20, height=20, font=("Helvetica", 12))
    listNodes.pack(side="left", fill="y")

    scrollbar = tk.Scrollbar(frame, orient="vertical")
    scrollbar.config(command=listNodes.yview)
    scrollbar.pack(side="right", fill="y")

    listNodes.config(yscrollcommand=scrollbar.set)

    kelimeler = metin.split()
    for x in kelimeler:
        listNodes.insert(END, str(x))
    
button1 = tk.Button(text='kelimleri sayi',width = 20, command=kelime_say, bg='red', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 150, window=button1)


root.mainloop()
 


# In[ ]:





# In[ ]:




