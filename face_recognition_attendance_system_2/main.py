from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_recognition
from Attendance import attendance
from developer import developer
from help import help
import tkinter
from time import strftime
from datetime import datetime


class face_recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition system")

        #first image

        img = Image.open(r"college_photo\face.jpg")
        img = img.resize((512, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=512, height=130)

        #second image
        img1 = Image.open(r"college_photo\face2.png")
        img1 = img1.resize((512, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=512, y=0, width=512, height=130)

        #third image
        img2 = Image.open(r"college_photo\face3.jpg")
        img2 = img2.resize((512, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1024, y=0, width=512, height=130)


        #background image
        img3 = Image.open(r"college_photo\face4.jpg")
        img3 = img3.resize((1530,710), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        #==time
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=('times new roman',14,'bold'),bg='white',fg='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()
        #STUDENT BOTTON

        img4 = Image.open(r"college_photo\student.jpg")
        img4 = img4.resize((220,220), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)

        #detect face button
        img5 = Image.open(r"college_photo\face_scan.jpg")
        img5= img5.resize((220,220), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_recog)
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",command=self.face_recog,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)

        #attendance button
        img6 = Image.open(r"college_photo\attendance.webp")
        img6= img6.resize((220,220), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attend_fun)
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",command=self.attend_fun,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)

        #help desk button
        img7 = Image.open(r"college_photo\help_desk.jpg")
        img7= img7.resize((220,220), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_desk)
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_desk,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)

        #train data

        img8 = Image.open(r"college_photo\face_train.jpg")
        img8= img8.resize((220,220), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Train Data",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=580,width=220,height=40)

        #photo button

        img9 = Image.open(r"college_photo\photo.webp")
        img9= img9.resize((220,220), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.photo_set)
        b1.place(x=500,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.photo_set,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=580,width=220,height=40)

        # developer button

        img10 = Image.open(r"college_photo\dev.jpg")
        img10= img10.resize((220,220), Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_btn)
        b1.place(x=800,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",command=self.developer_btn,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=580,width=220,height=40)

        #exit button
        img11 = Image.open(r"college_photo\exit.jpg")
        img11= img11.resize((220,220), Image.Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.ixit)
        b1.place(x=1100,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="exit",command=self.ixit,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=580,width=220,height=40)


        #function button=========
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    #photo button functio
    def photo_set(self):
        os.startfile("data")
    
    #train data set button
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_recog(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)

    #exit function
    def ixit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        
    #attendance
    def attend_fun(self):
        self.new_window=Toplevel(self.root)
        self.app=attendance(self.new_window)
        #developer button button
    def developer_btn(self):
        self.new_window=Toplevel(self.root)
        self.app=developer(self.new_window)
#help desk btn function
    def help_desk(self):
        self.new_window=Toplevel(self.root)
        self.app=help(self.new_window)


        











if __name__=="__main__":
    root=Tk()
    obj=face_recognition_system(root)
    root.mainloop()