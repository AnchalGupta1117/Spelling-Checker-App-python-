import tkinter
from tkinter import *
from textblob import TextBlob



    
heading= Label(root,text="Spelling Checker",font=("Trebuchet MS", 30,"bold"),bg="#dae6f6",fg="#364971")
heading.pack(pady=(50,0))

enter_text=Entry(root,justify="center",width=30,font=("poppins",25),bg="white",border=2)
enter_text.pack(pady=10)
enter_text.focus()

button=Button(root,text="Check",font=("arial",20,"bold"),fg="white",bg="red",command=check_spelling)
button.pack()

spell=Label(root,font=("poppins",20),bg="#dae6f6",fg="#364971")
spell.place(x=350,y=250)

root.mainloop()
