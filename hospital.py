from tkinter import *
from tkinter import ttk
import random
import time
from datetime import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1280x850+0+0")
        
        self.Nameoftablets = StringVar()
        self.ref = StringVar()
        self.Dose = StringVar()
        self.NumberofTablets = StringVar()
        self.Lot = StringVar()
        self.Issuedate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.sideEffect = StringVar()
        self.FurtherInformation= StringVar()
        self.StorageAdvice = StringVar()
        self.DrivingUsingMachine = StringVar()
        self.HowToUseMedication = StringVar()
        self.PatientId = StringVar()
        self.nhsNumber = StringVar()
        self.PatientName = StringVar()
        self.DateOfBirth= StringVar()
        self.PatientAddress= StringVar()



        lbltitle=Label(self.root,bd=10,relief=RIDGE,text="Hospital Management System",fg="red",bg="white",font=("Times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

    #  ............................Dataframe.................................................
        Dataframe = Frame(self.root,bd=10,relief=RIDGE)
        Dataframe.place(x=0,y=110,width=1280,height=320)

        DataframeLeft=LabelFrame(Dataframe,bd=7,relief=RIDGE,padx=10,font=("Times new roman",13,"bold"),text="Patient Information")
        DataframeLeft.place(x=0,y=5,width=805,height=285)

        DataframeRight=LabelFrame(Dataframe,bd=7,relief=RIDGE,padx=10,font=("Times new roman",13,"bold"),text="Prescription")
        DataframeRight.place(x=815,y=5,width=410,height=285)

    #...................................buttons frame............................................................
        Buttonframe = Frame(self.root,bd=10,relief=RIDGE)
        Buttonframe.place(x=0,y=430,width=1280,height=60)  #1530 70
 
    #...................................details frame............................................................
        Detailsframe = Frame(self.root,bd=10,relief=RIDGE)
        Detailsframe.place(x=0,y=490,width=1280,height=150)
  
    #...............................DataframeLeft................................................................
        lblNameTablet=Label(DataframeLeft,text="Names OF Tablet",font=("arial",10,"bold"),padx=2,pady=4)
        lblNameTablet.grid(row=0,column=0,sticky=W)

        comNametablet=ttk.Combobox(DataframeLeft,textvariable=self.Nameoftablets,state="readonly",font=("arial",10,"bold"),width=33)
        comNametablet["value"]=("Nice","Corona Vacacine","Acetaminophen","Adderall","Amlodipine","Ativan")
        comNametablet.current=0
        comNametablet.grid(row=0,column=1)
   
        lblref=Label(DataframeLeft,font=("arial",10,"bold"),text="Reference No:",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataframeLeft,font=("arial",10,"bold"),textvariable=self.ref,width=35)
        txtref.grid(row=1,column=1)

        lblDose=Label(DataframeLeft,font=("arial",10,"bold"),text="Dose:",padx=2,pady=2)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataframeLeft,font=("arial",10,"bold"),textvariable=self.Dose,width=35)
        txtDose.grid(row=2,column=1)

        lblNoOftablets=Label(DataframeLeft,font=("arial",10,"bold"),text="No Of Tablets:",padx=2,pady=4)
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        txtNoOftablets=Entry(DataframeLeft,font=("arial",10,"bold"),textvariable=self.NumberofTablets,width=35)
        txtNoOftablets.grid(row=3,column=1)

        lbllot=Label(DataframeLeft,font=("arial",10,"bold"),text="Lot:",padx=2,pady=6)
        lbllot.grid(row=4,column=0,sticky=W)
        txtlot=Entry(DataframeLeft,font=("arial",10,"bold"),textvariable=self.Lot,width=35)
        txtlot.grid(row=4,column=1)

        lblissueDate=Label(DataframeLeft,font=("arial",10,"bold"),text="Issue Date:",padx=2,pady=4)
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtissueDate=Entry(DataframeLeft,font=("arial",10,"bold"),textvariable=self.Issuedate,width=35)
        txtissueDate.grid(row=5,column=1)

        lblExpDate=Label(DataframeLeft,font=("arial",10,"bold"),text="Exp Date:",padx=2,pady=4)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(DataframeLeft,font=("arial",10,"bold"),textvariable=self.ExpDate,width=35)
        txtExpDate.grid(row=6,column=1)

        lblDailyDose=Label(DataframeLeft,font=("arial",10,"bold"),text="Daily Dose:",padx=2,pady=4)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(DataframeLeft,font=("arial",10,"bold"),textvariable=self.DailyDose,width=35)
        txtDailyDose.grid(row=7,column=1)

        lblSideEffect=Label(DataframeLeft,font=("arial",10,"bold"),text="Side Effect:",padx=2,pady=4)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataframeLeft,font=("arial",10,"bold"),textvariable=self.sideEffect,width=35)
        txtSideEffect.grid(row=8,column=1)

        lblFurtherInfo=Label(DataframeLeft,font=("arial",10,"bold"),text="Further Information:",padx=3)
        lblFurtherInfo.grid(row=0,column=2,sticky=W)
        txtFurtherInfo=Entry(DataframeLeft,font=("arial",10,"bold"),textvariable=self.FurtherInformation,width=35)
        txtFurtherInfo.grid(row=0,column=3)

        lblBloodPressure=Label(DataframeLeft,font=("arial",10,"bold"),text="Blood Pressure:",padx=3,pady=4)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        txtBloodPressure=Entry(DataframeLeft,font=("arial",10,"bold"),textvariable=self.DrivingUsingMachine,width=35)
        txtBloodPressure.grid(row=1,column=3)

        lblStorage=Label(DataframeLeft,font=("arial",10,"bold"),text="Storage Advice:",padx=3,pady=4)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage=Entry(DataframeLeft,font=("arial",10,"bold"),textvariable=self.StorageAdvice,width=35)
        txtStorage.grid(row=2,column=3)

        lblMedicine=Label(DataframeLeft,font=("arial",10,"bold"),text="Medication:",padx=3,pady=4)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine=Entry(DataframeLeft,font=("arial",10,"bold"),textvariable=self.HowToUseMedication,width=35)
        txtMedicine.grid(row=3,column=3)

        lblPatientId=Label(DataframeLeft,font=("arial",10,"bold"),text="Patient Id:",padx=3,pady=4)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId=Entry(DataframeLeft,font=("arial",10,"bold"),textvariable=self.PatientId,width=35)
        txtPatientId.grid(row=4,column=3)

        lblNHsNumber=Label(DataframeLeft,font=("arial",10,"bold"),text="NHS Number:",padx=3,pady=4)
        lblNHsNumber.grid(row=5,column=2,sticky=W)
        txtNHsNumber=Entry(DataframeLeft,font=("arial",10,"bold"),textvariable=self.nhsNumber,width=35)
        txtNHsNumber.grid(row=5,column=3)

        lblPatientname=Label(DataframeLeft,font=("arial",10,"bold"),text="Patient Name:",padx=3,pady=4)
        lblPatientname.grid(row=6,column=2,sticky=W)
        txtPatientname=Entry(DataframeLeft,font=("arial",10,"bold"),textvariable=self.PatientName,width=35)
        txtPatientname.grid(row=6,column=3)

        lblDateOfBirth=Label(DataframeLeft,font=("arial",10,"bold"),text="Date Of Birth:",padx=3,pady=4)
        lblDateOfBirth.grid(row=7,column=2,sticky=W)
        txtDateOfBirth=Entry(DataframeLeft,font=("arial",10,"bold"),textvariable=self.DateOfBirth,width=35)
        txtDateOfBirth.grid(row=7,column=3)

        lblPatientAddress=Label(DataframeLeft,font=("arial",10,"bold"),text="Patient Address:",padx=3,pady=4)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress=Entry(DataframeLeft,font=("arial",10,"bold"),textvariable=self.PatientAddress,width=35)
        txtPatientAddress.grid(row=8,column=3)

    #.................DataframeRight............................
        self.txtPrescription=Text(DataframeRight,font=("arial",10,"bold"),width=52,height=15,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)

    #......................buttons..................................
        btnPrescription=Button(Buttonframe,command=self.iPrescription,text="Prescription",bg="Green",fg="White" ,font=("arial",10,"bold"),width=25,height=2,padx=2,pady=2)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData=Button(Buttonframe,command=self.iPrescriptionData,text="Prescription Data",bg="Green", fg="White" ,font=("arial",10,"bold"),width=25,height=2,padx=2,pady=2)
        btnPrescriptionData.grid(row=0,column=1)

        btnUpdate=Button(Buttonframe,command=self.update_data,text="Update",bg="Green", fg="White" ,font=("arial",10,"bold"),width=25,height=2,padx=2,pady=2)
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(Buttonframe,command=self.idelete,text="Delete",bg="Green", fg="White" ,font=("arial",10,"bold"),width=25,height=2,padx=2,pady=2)
        btnDelete.grid(row=0,column=3)

        btnClear=Button(Buttonframe,command=self.clear,text="Clear",bg="Green", fg="White" ,font=("arial",10,"bold"),width=25,height=2,padx=2,pady=2)
        btnClear.grid(row=0,column=4)

        btnExit=Button(Buttonframe,command=self.iExit,text="Exit",bg="Green", fg="White" ,font=("arial",10,"bold"),width=23,height=2,padx=2,pady=2)
        btnExit.grid(row=0,column=5)

    #..................table scroll bar................................................
        scroll_x= ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y= ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,column=("nameoftablet","ref","dose","nooftablets","lot","issuedate","expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftablet",text="Name of Tablets")
        self.hospital_table.heading("ref",text="Reference no.")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No Of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("address",text="Address")

        self.hospital_table["show"]="headings"

       
        self.hospital_table.column("nameoftablet",width=90)
        self.hospital_table.column("ref",width=90)
        self.hospital_table.column("dose",width=90)
        self.hospital_table.column("nooftablets",width=90)
        self.hospital_table.column("lot",width=90)
        self.hospital_table.column("issuedate",width=90)
        self.hospital_table.column("expdate",width=90)
        self.hospital_table.column("dailydose",width=90)
        self.hospital_table.column("storage",width=90)
        self.hospital_table.column("nhsnumber",width=90)
        self.hospital_table.column("pname",width=90)
        self.hospital_table.column("dob",width=90)
        self.hospital_table.column("address",width=90)
    
        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
    #......................................functionality declaration......................
    def iPrescriptionData(self):
        
      if self.Nameoftablets.get() =="" or self.ref.get() =="":
            print("empty")
            messagebox.showerror("Error","All fields are required")
      else:
          try:
            conn=mysql.connector.connect(host='localhost', username='root', password='@p@a@l@a@k@3005', database='mydata')
            print("inserting")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                            self.Nameoftablets.get(),  
                                                            self.ref.get(),  
                                                            self.Dose.get(),   
                                                            self.NumberofTablets.get(),  
                                                            self.Lot.get(),  
                                                            self.Issuedate.get(),   
                                                            self.ExpDate.get(),   
                                                            self.DailyDose.get(),   
                                                            self.StorageAdvice.get(),  
                                                            self.nhsNumber.get(),  
                                                            self.PatientName.get(),   
                                                            self.DateOfBirth.get(),  
                                                            self.PatientAddress.get()
                                                          ))
            

            conn.commit()
            self.fetch_data()
            conn.close()
            
            messagebox.showinfo("Success","Data Inserted Successfully!")
          except Exception as e:
              messagebox.showerror("Database Error", str(e))

    def update_data(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="@p@a@l@a@k@3005",database="mydata")
        
            my_cursor=conn.cursor()
            my_cursor.execute("update hospital set Nameoftablets=%s,dose=%s, Numbersoftablets=%s, lot=%s, issuedate=%s, expdate=%s, dailydose=%s, storage=%s, nhsnumber=%s, patientname=%s, DOB=%s, patientaddress=%s where Reference_No=%s",(
                                                            self.Nameoftablets.get(), 
                                                           int( self.Dose.get()),   
                                                           int( self.NumberofTablets.get()),  
                                                            self.Lot.get(),  
                                                            self.Issuedate.get(),   
                                                            self.ExpDate.get(),   
                                                            int(self.DailyDose.get()),   
                                                            self.StorageAdvice.get(),  
                                                            self.nhsNumber.get(),  
                                                            self.PatientName.get(),   
                                                            self.DateOfBirth.get(),  
                                                            self.PatientAddress.get(),
                                                            self.ref.get(), 
                   ))

            conn.commit()
            
            conn.close()
            messagebox.showinfo("Update","Record has been updated Successfully!")
            
            self.fetch_data()


    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost', username='root', password='@p@a@l@a@k@3005', database='mydata')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1]),  
        self.Dose.set(row[2]),   
        self.NumberofTablets.set(row[3]),  
        self.Lot.set(row[4]),  
        self.Issuedate.set(row[5]),   
        self.ExpDate.set(row[6]),   
        self.DailyDose.set(row[7]),   
        self.StorageAdvice.set(row[8]),  
        self.nhsNumber.set(row[9]),  
        self.PatientName.set(row[10]),   
        self.DateOfBirth.set(row[11]),  
        self.PatientAddress.set(row[12])
   
    
    def iPrescription(self):
        self.txtPrescription.insert(END,"name of Tablets:\t\t\t"+self.Nameoftablets.get()+"\n")
        self.txtPrescription.insert(END,"Reference No:\t\t\t"+self.ref.get()+"\n")
        self.txtPrescription.insert(END,"Dose:\t\t\t"+self.Dose.get()+"\n")
        self.txtPrescription.insert(END,"Number of Tablets:\t\t\t"+self.NumberofTablets.get()+"\n")
        self.txtPrescription.insert(END,"Lot:\t\t\t"+self.Lot.get()+"\n")
        self.txtPrescription.insert(END,"Issue Date:\t\t\t"+self.Issuedate.get()+"\n")
        self.txtPrescription.insert(END,"Exp date:\t\t\t"+self.ExpDate.get()+"\n")
        self.txtPrescription.insert(END,"daily Dose:\t\t\t"+self.DailyDose.get()+"\n")
        self.txtPrescription.insert(END,"Side Effect:\t\t\t"+self.sideEffect.get()+"\n")
        self.txtPrescription.insert(END,"Further Information:\t\t\t"+self.FurtherInformation.get()+"\n")
        self.txtPrescription.insert(END,"StorageAdvice:\t\t\t"+self.StorageAdvice.get()+"\n")
        self.txtPrescription.insert(END,"DrivingUsingMachine:\t\t\t"+self.DrivingUsingMachine.get()+"\n")
        self.txtPrescription.insert(END,"PatientId:\t\t\t"+self.PatientId.get()+"\n")
        self.txtPrescription.insert(END,"NHSNumber:\t\t\t"+self.nhsNumber.get()+"\n")
        self.txtPrescription.insert(END,"PatientName:\t\t\t"+self.PatientName.get()+"\n")
        self.txtPrescription.insert(END,"DateOfBirth:\t\t\t"+self.DateOfBirth.get()+"\n")
        self.txtPrescription.insert(END,"PatientAddress:\t\t\t"+self.PatientAddress.get()+"\n")


    def idelete(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="@p@a@l@a@k@3005",database="mydata")
        my_cursor=conn.cursor()
        query="delete from hospital where Reference_No=%s"
        value=(self.ref.get(),)
        my_cursor.execute(query,value)

        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete","Patient has been deleted successfully")

    def clear(self):
        self.Nameoftablets.set("")
        self.ref.set(""),  
        self.Dose.set(""),   
        self.NumberofTablets.set(""),  
        self.Lot.set(""),  
        self.Issuedate.set(""),   
        self.ExpDate.set(""),   
        self.DailyDose.set(""),   
        self.sideEffect.set(""),
        self.FurtherInformation.set(""),
        self.StorageAdvice.set(""),  
        self.DrivingUsingMachine.set(""),
        self.HowToUseMedication.set(""),
        self.PatientId.set(""),
        self.nhsNumber.set(""),  
        self.PatientName.set(""),   
        self.DateOfBirth.set(""),
        self.PatientAddress.set("")
        self.txtPrescription.delete("1.0",END)  

    def iExit(self):
        iExit=messagebox.askyesno("Hospital management system", "Confirm you want to exit")
        if iExit>0:
            root.destroy()
            return


root=Tk()
ob=Hospital(root)
root.mainloop()