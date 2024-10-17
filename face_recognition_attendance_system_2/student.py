from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition system")


        #variable declaration
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_ph=StringVar()
        self.var_address=StringVar()
        self.var_tcr_name=StringVar()
        self.var_radio1=StringVar()

         #first image

        img = Image.open(r"college_photo\student_scan2.png")
        img = img.resize((512, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=512, height=130)

        #second image
        img1 = Image.open(r"college_photo\student_scan.jpg")
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
        img3 = Image.open(r"college_photo\bg2.jpg")
        img3 = img3.resize((1540,710), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1540, height=710)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1540,height=45)

        #main frame

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=15,y=53,width=1500,height=600)

        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times now roman ",12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=600)

        #imaage in left label frame
        img_left = Image.open(r"college_photo\left_frame3.webp")
        img_left = img_left.resize((720, 130), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=3, y=0, width=720, height=130)

        #current course
        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("times now roman ",12,"bold"))
        current_course_frame.place(x=3,y=135,width=720,height=125)

        #department

        dep_label=Label(current_course_frame,text="Department:",font=("times now roman ",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times now roman ",12,"bold"),state="read only",width=20)
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course
        course_label=Label(current_course_frame,text="Course:",font=("times now roman ",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times now roman ",12,"bold"),state="read only",width=20)
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #yeer
        year_label=Label(current_course_frame,text="Year:",font=("times now roman ",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times now roman ",12,"bold"),state="read only",width=20)
        year_combo["values"]=("Selct Year ","2022-23","223-24","2024-25","2025-26")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester
        semester_label=Label(current_course_frame,text="Semester:",font=("times now roman ",13,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times now roman ",12,"bold"),state="read only",width=20)
        semester_combo["values"]=("Select Semester ","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #class student information 
        class_student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times now roman ",12,"bold"))
        class_student_frame.place(x=3,y=260,width=720,height=300)
        
        #student id
        student_id_label=Label(class_student_frame,text="Student ID:",font=("times now roman ",12,"bold"),bg="white")
        student_id_label.grid(row=0,column=0,padx=10,sticky=W)

        Student_id_entrey=ttk.Entry(class_student_frame,textvariable=self.var_id,width=20,font=("times new roman ",13,"bold"),)
        Student_id_entrey.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student name
        student_name_label=Label(class_student_frame,text="Student Name:",font=("times now roman ",12,"bold"),bg="white")
        student_name_label.grid(row=0,column=2,padx=10,sticky=W)

        Student_name_entrey=ttk.Entry(class_student_frame,textvariable=self.var_name,width=20,font=("times new roman ",13,"bold"),)
        Student_name_entrey.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class devision
        classs_div_label=Label(class_student_frame,text="Class Division:",font=("times now roman ",12,"bold"),bg="white")
        classs_div_label.grid(row=1,column=0,padx=10,sticky=W)

        #classs_div_entrey=ttk.Entry(class_student_frame,textvariable=self.var_div,width=20,font=("times new roman ",13,"bold"),)
        #classs_div_entrey.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        division_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times now roman ",10,"bold"),state="read only",width=20)
        division_combo["values"]=("A","B","C","D")
        division_combo.current(0)
        division_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #roll no
        roll_no_label=Label(class_student_frame,text="Roll NO:",font=("times now roman ",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,sticky=W)

        roll_no_entrey=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman ",13,"bold"),)
        roll_no_entrey.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #GENDER
        student_gender_label=Label(class_student_frame,text="Gender:",font=("times now roman ",12,"bold"),bg="white")
        student_gender_label.grid(row=2,column=0,padx=10,sticky=W)

        #Student_gender_entrey=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=("times new roman ",13,"bold"),)
        #Student_gender_entrey.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times now roman ",10,"bold"),state="read only",width=20)
        gender_combo["values"]=("Male","Female")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #date of birth

        student_dob_label=Label(class_student_frame,text="DOB:",font=("times now roman ",12,"bold"),bg="white")
        student_dob_label.grid(row=2,column=2,padx=10,sticky=W)

        Student_dob_entrey=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman ",13,"bold"),)
        Student_dob_entrey.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #EMAIL
        student_email_label=Label(class_student_frame,text="Email:",font=("times now roman ",12,"bold"),bg="white")
        student_email_label.grid(row=3,column=0,padx=10,sticky=W)

        Student_email_entrey=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman ",13,"bold"),)
        Student_email_entrey.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #PHONE NUMBER
        student_number_label=Label(class_student_frame,text="Phone No:",font=("times now roman ",12,"bold"),bg="white")
        student_number_label.grid(row=3,column=2,padx=10,sticky=W)

        Student_number_entrey=ttk.Entry(class_student_frame,textvariable=self.var_ph,width=20,font=("times new roman ",13,"bold"),)
        Student_number_entrey.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #ADRESS
        student_address_label=Label(class_student_frame,text="Address:",font=("times now roman ",12,"bold"),bg="white")
        student_address_label.grid(row=4,column=0,padx=10,sticky=W)

        Student_address_entrey=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman ",13,"bold"),)
        Student_address_entrey.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #TEACHER NAME
        teacher_name_label=Label(class_student_frame,text="Teacher Name:",font=("times now roman ",12,"bold"),bg="white")
        teacher_name_label.grid(row=4,column=2,padx=10,sticky=W)

        teacher_name_entrey=ttk.Entry(class_student_frame,textvariable=self.var_tcr_name,width=20,font=("times new roman ",13,"bold"),)
        teacher_name_entrey.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio button
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)

        #button frame 
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=215,width=715,height=37)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times now roman ",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times now roman ",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times now roman ",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times now roman ",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

         #2nd_button frame 
        btn_frame_1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame_1.place(x=0,y=245,width=715,height=37)

        #take a photo sample
        photo_sample_btn=Button(btn_frame_1,command=self.generate_dataset,text="Take Photo Sample",width=36,font=("times now roman ",12,"bold"),bg="blue",fg="white")
        photo_sample_btn.grid(row=0,column=0)

        #update photo sample
        update_btn=Button(btn_frame_1,text="Take Photo Sample",width=36,font=("times now roman ",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)







        





        
        
        
        
        
        
        
        
        
        
        
        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times now roman ",12,"bold"))
        right_frame.place(x=750,y=10,width=730,height=580)

        #right frame first image

        img_right=Image.open(r"college_photo\student_scan2.png")
        img_right=img_right.resize((730,130),Image.Resampling.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_label_right=Label(right_frame,image=self.photoimg_right)
        f_label_right.place(x=0,y=0,width=730,height=130)

        #searching system
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times now roman ",12,"bold"))
        search_frame.place(x=5,y=135,width=718,height=70)

        search_label=Label(search_frame,text="Search By:",font=("times now roman ",15,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        search_combo=ttk.Combobox(search_frame,font=("times now roman ",12,"bold"),state="read only",width=18)
        search_combo["values"]=("Select ","Student ID","Student Ph No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entrey=ttk.Entry(search_frame,width=13,font=("times new roman ",13,"bold"),)
        search_entrey.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",width=13,font=("times now roman ",11,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3)

        showAll_btn=Button(search_frame,text="Show All",width=13,font=("times now roman ",11,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)

        #table frame
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=718,height=350)

        #scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","std_id","std_name","std_div","roll","gender","dob","email","ph_no","address","tcr_name","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("std_id",text="Student ID")
        self.student_table.heading("std_name",text="Student Name")
        self.student_table.heading("std_div",text="Division")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("ph_no",text="Phone No")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("tcr_name",text="Teacher")
        self.student_table.heading("photo",text="Photo samaple status")
        self.student_table["show"]="headings"

        #width
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("std_id",width=100)
        self.student_table.column("std_name",width=100)
        self.student_table.column("std_div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("ph_no",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("tcr_name",width=100)
        self.student_table.column("photo",width=100)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
  #function declaration
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Erroe","ALL fields ssre required",parent=self.root)
        else:
            try:
              conn=mysql.connector.connect(host="localhost",username="root",password="layappa123@",database="face_recognizer")
              my_cursor=conn.cursor()
              my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                              self.var_dep.get(),
                                                                                                              self.var_course.get(),
                                                                                                              self.var_year.get(),
                                                                                                              self.var_sem.get(),
                                                                                                              self.var_id.get(),
                                                                                                              self.var_name.get(),
                                                                                                              self.var_div.get(),
                                                                                                              self.var_roll.get(),
                                                                                                              self.var_gender.get(),
                                                                                                              self.var_dob.get(),
                                                                                                              self.var_email.get(),
                                                                                                              self.var_ph.get(),
                                                                                                              self.var_address.get(),
                                                                                                              self.var_tcr_name.get(),
                                                                                                              self.var_radio1.get()
                                                                                                            
                                                                                                             ))
              conn.commit()
              self.fetch_data()
              conn.close()
              messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"due To:{str(es)}",parent=self.root)
    #fetch data
    def fetch_data(self):
         conn=mysql.connector.connect(host="localhost",username="root",password="layappa123@",database="face_recognizer")
         my_cursor=conn.cursor()
         my_cursor.execute("select * from student")
         data=my_cursor.fetchall()

         if len(data)!=0:
             self.student_table.delete(*self.student_table.get_children())
             for i in data:
                 self.student_table.insert("",END,values=i)
             conn.commit()
         conn.close()
    #get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_ph.set(data[11]),
        self.var_address.set(data[12]),
        self.var_tcr_name.set(data[13]),
        self.var_radio1.set(data[14])

    #UPDATE FUNCTION
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Erroe","ALL fields ssre required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if update>0:
                     conn=mysql.connector.connect(host="localhost",username="root",password="layappa123@",database="face_recognizer")
                     my_cursor=conn.cursor()
                     my_cursor.execute("update student set dep=%s,course=%s,year=%s,sem=%s,student_name=%s,division=%s,roll_no=%s,gender=%s,dob=%s,email=%s,phone_no=%s,address=%s,teacher=%s,photosample=%s where student_id=%s",(
                                                                                                              self.var_dep.get(),
                                                                                                              self.var_course.get(),
                                                                                                              self.var_year.get(),
                                                                                                              self.var_sem.get(),
                                                                                                              self.var_name.get(),
                                                                                                              self.var_div.get(),
                                                                                                              self.var_roll.get(),
                                                                                                              self.var_gender.get(),
                                                                                                              self.var_dob.get(),
                                                                                                              self.var_email.get(),
                                                                                                              self.var_ph.get(),
                                                                                                              self.var_address.get(),
                                                                                                              self.var_tcr_name.get(),
                                                                                                              self.var_radio1.get(),
                                                                                                              self.var_id.get()
                                                                                                                  
                                                                                                             ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student details successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)  
    #delete function
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student delete page","DO you want to delete this student ",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="layappa123@",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where student_id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close() 
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)                      
    #reset function
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Couse")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_ph.set("")
        self.var_address.set("")
        self.var_tcr_name.set("")
        self.var_radio1.set("")             
    #genarate data set and take photo sample

    def generate_dataset(self):
         if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Erroe","ALL fields ssre required",parent=self.root)
         else:
             try:
                 conn=mysql.connector.connect(host="localhost",username="root",password="layappa123@",database="face_recognizer")
                 my_cursor=conn.cursor()
                 my_cursor.execute("select * from student")
                 myresult=my_cursor.fetchall()
                 id=0
                 for x in myresult:
                     id+=1
                 my_cursor.execute("update student set dep=%s,course=%s,year=%s,sem=%s,student_name=%s,division=%s,roll_no=%s,gender=%s,dob=%s,email=%s,phone_no=%s,address=%s,teacher=%s,photosample=%s where student_id=%s",(
                                                                                                              self.var_dep.get(),
                                                                                                              self.var_course.get(),
                                                                                                              self.var_year.get(),
                                                                                                              self.var_sem.get(),
                                                                                                              self.var_name.get(),
                                                                                                              self.var_div.get(),
                                                                                                              self.var_roll.get(),
                                                                                                              self.var_gender.get(),
                                                                                                              self.var_dob.get(),
                                                                                                              self.var_email.get(),
                                                                                                              self.var_ph.get(),
                                                                                                              self.var_address.get(),
                                                                                                              self.var_tcr_name.get(),
                                                                                                              self.var_radio1.get(),
                                                                                                              self.var_id.get()
                                                                                                                  
                                                                                                             ))
                 conn.commit()
                 self.fetch_data()
                 self.reset_data()
                 conn.close()


                 #load predifined data on face frontls from open cv
                 face_classifire=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                 
                 def face_cropped(img):
                     gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                     faces=face_classifire.detectMultiScale(gray,1.3,5)
                     #scaling factor 1.2
                     #minimum neifgbor =5
                     for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                 
                 #camara open
                 cap=cv2.VideoCapture(0)
                 img_id=0
                 while True:
                     ret,frame=cap.read()
                     if face_cropped(frame) is not None:
                         img_id+=1
                         face=cv2.resize(face_cropped(frame),(450,450))
                         face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                         file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                         cv2.imwrite(file_name_path,face)
                         cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                         cv2.imshow("crooped face",face)

                     if cv2.waitKey(1)==13 or int(img_id)==100:
                         break
                 cap.release()
                 cv2.destroyAllWindows()
                 messagebox.showinfo("Result","Generating data sets completed ")

             except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)         
                
            
  

 






if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()