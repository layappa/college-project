from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition system")


        #variable
        self.var_id=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attendance=StringVar()


        img = Image.open(r"college_photo\attend1.jpg")
        img = img.resize((800, 200), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=800, height=200)

        #second image
        img1 = Image.open(r"college_photo\attend3.jpg")
        img1 = img1.resize((800, 200), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=800, y=0, width=800, height=200)

        #bg image

        img3 = Image.open(r"college_photo\bg2.jpg")
        img3 = img3.resize((1540,710), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1540, height=710)

        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1540,height=45)
        #main frame

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=15,y=53,width=1500,height=530)

        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times now roman ",12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=510)
        #left image

        

        #inside left frame

        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=3,y=5,width=720,height=340)

        #labels and entry
        #attendance id
        attendance_id_label=Label(left_inside_frame,text="Attendance ID:",font=("times now roman ",12,"bold"),bg="white")
        attendance_id_label.grid(row=0,column=0,padx=10,sticky=W)

        attendance_id_entrey=ttk.Entry(left_inside_frame,textvariable=self.var_id,width=20,font=("times new roman ",13,"bold"),)
        attendance_id_entrey.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        #roll no
        roll_label=Label(left_inside_frame,text="Roll:",font=("times now roman ",12,"bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=10,sticky=W)

        roll_entrey=ttk.Entry(left_inside_frame,textvariable=self.var_roll,width=20,font=("times new roman ",13,"bold"),)
        roll_entrey.grid(row=0,column=3,padx=10,pady=5,sticky=W)


        #name
        name_label=Label(left_inside_frame,text="Name:",font=("times now roman ",12,"bold"),bg="white")
        name_label.grid(row=1,column=0,padx=10,sticky=W)

        name_entrey=ttk.Entry(left_inside_frame,textvariable=self.var_name,width=20,font=("times new roman ",13,"bold"),)
        name_entrey.grid(row=1,column=1,padx=10,pady=5,sticky=W)


        #department
        department_label=Label(left_inside_frame,text="Department:",font=("times now roman ",12,"bold"),bg="white")
        department_label.grid(row=1,column=2,padx=10,sticky=W)

        department_entrey=ttk.Entry(left_inside_frame,textvariable=self.var_dep,width=20,font=("times new roman ",13,"bold"),)
        department_entrey.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        #time
        attendance_id_label=Label(left_inside_frame,text="Time:",font=("times now roman ",12,"bold"),bg="white")
        attendance_id_label.grid(row=2,column=0,padx=10,sticky=W)

        attendance_id_entrey=ttk.Entry(left_inside_frame,textvariable=self.var_time,width=20,font=("times new roman ",13,"bold"),)
        attendance_id_entrey.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        #date
        attendance_id_label=Label(left_inside_frame,text="Date:",font=("times now roman ",12,"bold"),bg="white")
        attendance_id_label.grid(row=2,column=2,padx=10,sticky=W)

        attendance_id_entrey=ttk.Entry(left_inside_frame,textvariable=self.var_date,width=20,font=("times new roman ",13,"bold"),)
        attendance_id_entrey.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        #attendance status
        course_label=Label(left_inside_frame,text="Attendance Status:",font=("times now roman ",13,"bold"),bg="white")
        course_label.grid(row=3,column=0,padx=10,sticky=W)
        course_combo=ttk.Combobox(left_inside_frame,textvariable=self.var_attendance,font=("times now roman ",12,"bold"),state="read only",width=20)
        course_combo["values"]=("Status","Present","Absent")
        course_combo.current(0)
        course_combo.grid(row=3,column=1,padx=2,pady=10,sticky=W)

        #button frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=715,height=37)

        import_btn=Button(btn_frame,text="Import CSV",command=self.import_csv,width=17,font=("times now roman ",12,"bold"),bg="blue",fg="white")
        import_btn.grid(row=0,column=0)

        export_btn=Button(btn_frame,text="Export CSV",command=self.export_csv,width=17,font=("times now roman ",12,"bold"),bg="blue",fg="white")
        export_btn.grid(row=0,column=1)

        update_btn=Button(btn_frame,text="Update",width=17,font=("times now roman ",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times now roman ",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)




        #right frame

        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times now roman ",12,"bold"))
        right_frame.place(x=750,y=10,width=730,height=510)
        #table frame
        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=715,height=475)

        #scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.attendanceReport_table=ttk.Treeview(table_frame,column=("id","roll","name","dep","time","date","attend"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.attendanceReport_table.xview)
        scroll_y.config(command=self.attendanceReport_table.yview)

        self.attendanceReport_table.heading("id",text="Attendance ID")
        self.attendanceReport_table.heading("roll",text="ROLL")
        self.attendanceReport_table.heading("name",text="Name")
        self.attendanceReport_table.heading("dep",text="Department")
        self.attendanceReport_table.heading("time",text="Time")
        self.attendanceReport_table.heading("date",text="Date")
        self.attendanceReport_table.heading("attend",text="Attendance")

       

        self.attendanceReport_table["show"]="headings"
     #width
        self.attendanceReport_table.column("id",width=100)
        self.attendanceReport_table.column("roll",width=100)
        self.attendanceReport_table.column("name",width=100)
        self.attendanceReport_table.column("dep",width=100)
        self.attendanceReport_table.column("time",width=100)
        self.attendanceReport_table.column("date",width=100)
        self.attendanceReport_table.column("attend",width=100)

        self.attendanceReport_table.pack(fill=BOTH,expand=1)
        self.attendanceReport_table.bind("<ButtonRelease>",self.get_cursor)

    #fetch data
    def fetcdata(self,rows):
        self.attendanceReport_table.delete(*self.attendanceReport_table.get_children())
        for i in rows:
            self.attendanceReport_table.insert("",END,values=i)
#import csv
    def import_csv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes = (("CSV file", "*.csv"), ("All files", "*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetcdata(mydata)

    #export csv

    def export_csv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("NO Data","No data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes = (("CSV file", "*.csv"), ("All files", "*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","your data exported to "+os.path.basename(fln)+"successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


    #get cursor
    def get_cursor(self,event=""):
        cursor_row=self.attendanceReport_table.focus()
        content=self.attendanceReport_table.item(cursor_row)
        rows=content['values']
        self.var_id.set(rows[0])
        self.var_roll.set(rows[1])  
        self.var_name.set(rows[2])  
        self.var_dep.set(rows[3])  
        self.var_time.set(rows[4])  
        self.var_date.set(rows[5])  
        self.var_attendance.set(rows[6])          
    
    def reset_data(self):
        self.var_id.set("")
        self.var_roll.set("")  
        self.var_name.set("")  
        self.var_dep.set("")  
        self.var_time.set("")  
        self.var_date.set("")  
        self.var_attendance.set("")








if __name__=="__main__":
    root=Tk()
    obj=attendance(root)
    root.mainloop()