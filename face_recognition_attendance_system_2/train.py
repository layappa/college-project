from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition system")

        title_lbl=Label(self.root,text="Train Data Set",font=("times new roman ",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"college_photo\3_people.webp")
        img_top=img_top.resize((1530,325),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        top_image=Label(self.root,image=self.photoimg_top)
        top_image.place(x=0,y=55,width=1530,height=325)

        #======button

        b1_btn=Button(self.root,text="Train Data",command=self.train_classifire,cursor="hand2",width=17,font=("times now roman ",30,"bold"),bg="red",fg="white")
        b1_btn.place(x=0,y=380,width=1530,height=60)


        #===botttom image

        img_bottom=Image.open(r"college_photo\people.png")
        img_bottom=img_bottom.resize((1530,325),Image.Resampling.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        bottom_image=Label(self.root,image=self.photoimg_bottom)
        bottom_image.place(x=0,y=440,width=1530,height=325)

    def train_classifire(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L') #gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #train the classifire
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifire.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training data set completed")


        


if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()