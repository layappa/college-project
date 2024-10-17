from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime

class Face_recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition system")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # First image
        img_top = Image.open(r"college_photo\face_reco_1.webp")
        img_top = img_top.resize((650, 700), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        top_image = Label(self.root, image=self.photoimg_top)
        top_image.place(x=0, y=55, width=650, height=700)

        # Second image
        img_bottom = Image.open(r"college_photo\face_reco_2.webp")
        img_bottom = img_bottom.resize((950, 700), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        bottom_image = Label(self.root, image=self.photoimg_bottom)
        bottom_image.place(x=650, y=55, width=950, height=700)

        # Button
        b1_btn = Button(bottom_image, text="Face Recognition",command=self.face_reco, cursor="hand2",  width=17, font=("times now roman", 18, "bold"), bg="darkgreen", fg="white")
        b1_btn.place(x=365, y=620, width=200, height=40)
    
    #attendance
    def msrk_attendance(self,i,r,n,d):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_ist=[]
            for line in myDataList:
                entry=line.split((","))
                name_ist.append(entry[0])
            if((i not in name_ist) and (r not in name_ist) and (n not in name_ist) and (d not in name_ist)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dstring=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dstring},{d1},present")

        

        #face recognition
    def face_reco(self):
       def draw_boundray(img,classifier,scalefactor,minneighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scalefactor,minneighbors)

            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])

                confidence=int((100*(1-predict/300)))
                conn=mysql.connector.connect(host="localhost",username="root",password="layappa123@",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("select student_id from student where student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                my_cursor.execute("select roll_no from student where student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)


                my_cursor.execute("select student_name from student where student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select dep from student where student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                
                if confidence>70:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"ROLL:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.msrk_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"UNKNOWN FACE",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                coord=[x,y,w,h]

       def recognize(img,clf,facecascade):
            coord=draw_boundray(img,facecascade,1.1,10,(255,25,255),"Face",clf)
            return img
       facecascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
       clf=cv2.face.LBPHFaceRecognizer_create()
       clf.read("classifire.xml")

       video_cap=cv2.VideoCapture(0)
       while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,facecascade)
            cv2.imshow("Welcome to face recogntion",img)
            
            if cv2.waitKey(1)==13:
                break
       video_cap.release()
       cv2.destroyAllWindows()
        



if __name__=="__main__":
    root=Tk()
    obj=Face_recognition(root)
    root.mainloop()

