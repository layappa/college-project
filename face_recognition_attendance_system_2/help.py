from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition system")

        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman ",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"college_photo\dev_des.jpg")
        img_top=img_top.resize((1540,740),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        top_image=Label(self.root,image=self.photoimg_top)
        top_image.place(x=0,y=55,width=1540,height=740)

        dev_label=Label(top_image,text="Email:chetan2004@gmail.com",font=("times now roman ",20,"bold"),bg="white")
        dev_label.place(x=630,y=350)

if __name__=="__main__":
    root=Tk()
    obj=help(root)
    root.mainloop()