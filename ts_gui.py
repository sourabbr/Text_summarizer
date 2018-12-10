# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 20:19:43 2017

@author: sourab
"""
from tkinter import *
from text_summarizer import *



def summarize():
    tex=TextArea.get("1.0","end-1c")
    reduce_per=TextArea3.get("1.0","end-1c")
    reduce_per=int(reduce_per)
    #print(reduce_per)
    #type(reduce_per)
    s_list=summarizer(tex,reduce_per)
    #print(s_list)
    #summarized_text = ''.join(s_list)
    summarized_text = ''.join(str('* '+e+'\n') for e in s_list)
    #print(summarized_text)
    #TextArea2.delete(0,END)
    TextArea2.insert(INSERT,summarized_text)
    
    
    


tex=''

root=Tk()
root.geometry('1920x1080')
root.title('Text summarizer')

Label(root,text="TEXT SUMMARIZER",font=('Papyrus',20)).place(x=500,y=20)
Label(root,text="Enter text:",font=('Perpetua',12)).place(x=12,y=70)
Label(root,text="Summary:",font=('Perpetua',12)).place(x=651,y=70)
Label(root,text="Reduce to (in percent):",font=('Perpetua',12)).place(x=651,y=695)

TextArea = Text(root,wrap=WORD,width=89, height=42)
ScrollBar = Scrollbar(root)
ScrollBar.config(command=TextArea.yview)
TextArea.config(yscrollcommand=ScrollBar.set)
ScrollBar.pack(side=LEFT, fill=Y)
TextArea.place(x=12,y=90)


TextArea2 = Text(root,wrap=WORD,width=90, height=42)
ScrollBar2 = Scrollbar(root)
ScrollBar2.config(command=TextArea2.yview)
TextArea2.config(yscrollcommand=ScrollBar2.set)
ScrollBar2.pack(side=RIGHT, fill=Y)
TextArea2.place(x=651,y=90)

TextArea3 = Text(root,width=10, height=1)
TextArea3.place(x=850,y=695)

Button(root, text="summary", command=summarize,font=('Times',16)).place(x=1150,y=695)

TextArea2.insert(INSERT,tex)

root.mainloop()
