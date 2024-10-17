from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition system")

        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman ",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"college_photo\dev1.jpg")
        img_top=img_top.resize((1540,740),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        top_image=Label(self.root,image=self.photoimg_top)
        top_image.place(x=0,y=55,width=1540,height=740)

        #main frame
        main_frame=Frame(top_image,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)

        dev_top=Image.open(r"college_photo\dev1.jpg")
        dev_top=dev_top.resize((200,200),Image.Resampling.LANCZOS)
        self.photodev_top=ImageTk.PhotoImage(dev_top)

        top_image=Label(main_frame,image=self.photodev_top)
        top_image.place(x=300,y=0,width=200,height=200)
#developer info
        dev_label=Label(main_frame,text="hello my name is ----:",font=("times now roman ",20,"bold"),bg="white")
        dev_label.place(x=0,y=5)

        dev1_label=Label(main_frame,text="I am ---------------:",font=("times now roman ",20,"bold"),bg="white")
        dev1_label.place(x=0,y=40)

        img2=Image.open(r"college_photo\dev2.jpeg")
        img2=img2.resize((500,400),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        top_image=Label(main_frame,image=self.photoimg2)
        top_image.place(x=0,y=210,width=500,height=400)




if __name__=="__main__":
    root=Tk()
    obj=developer(root)
    root.mainloop()