


from tkinter import *
import tkinter.messagebox
import tkinter.font as tkFont
import tkinter.ttk as ttk
import tkinter as tk

class Employee:
        
    EmpID=1
    def __init__(self,n,a,p):
        self.name=n
        self.age=a
        self.password=p
    def incrementID(self):
        self.EmpID=ID
        EmpID+=1
    def getEmp(self):
        return self.name,self.age,self.password
    
class Train:
    def __init__(self,n,s):
        self.NameOfTrain=n
        self.seat=s
        
    def SetTrain(self,n,s):
        self.NameOfTrain=n
        self.seat=s
    def getTrain(self):
        return self.NameOfTrain,self.seat

    
class Station:
    def __init__(self,n,nop):
        self.NameofStaion=n
        self.NoOfPlatforms=nop
        
    def setStation(self,n,nop):
        self.NameofStaion=n
        self.NoOfPlatforms=nop
    def getStaion(self):
        return self.NameofStaion,self.NoOfPlatforms

class Schedule:
    def __init__(self,NOT,depCity,depTime,arrCity,arrTime):
        self.NameOfTrain=NOT
        self.DepartureCity=depCity
        self.DepartureTime=depTime
        self.ArrivalCity=arrCity
        self.ArrivalTime=arrTime
    def GetSchedule(self):
        return self.NameOfTrain,self.ArrivalCity,self.ArrivalTime,self.DepartureCity,self.departureTime
    
class Ticket:
    def __init__(self,name,station,desStation,NOT,tot,noTickets,Tstatus="not confirmed"):
        self.name=name
        self.NameOfStation=station
        self.destination=desStation
        self.NameOfTrain=NOT
        self.TimeOfTrain=tot
        self.NoOfTickets=noTickets
        self.status=Tstatus
        self.TickNum=ticketno
    def ConfirmTicket(self):
        if self.status == "not confirmed":
            self.status="confirmed"
            tk.messagebox.showinfo('Confirmation','TICKET CONFIRMED!!')
        else:
            tk.messagebox.showinfo('Confirmation','TICKET ALREADY CONFIRMED!!')

ticketno=1
global EmployeeArr
EmployeeArr =[]
EmployeeArr.append(Employee("Ansh",18,'apmrms'))
EmployeeArr.append(Employee("Preet",18,'apmrms'))
EmployeeArr.append(Employee("Mayusha",18,'apmrms'))
global StationArr
StationArr =[]
global TrainArr
TrainArr =[]
global TicketArr
TicketArr =[]
global ScheduleArr
ScheduleArr= []
# TrainArr.append(Train("Shatabdi Express",300))
# TrainArr.append(Train("Rajdhani Express",320))
# TrainArr.append(Train("Fanaty Express",295))
# TrainArr.append(Train("Shanti Express",250))
# TrainArr.append(Train("Humsafar Express",400))

f=open("Train.txt","r")
c=f.read()
f.close()
w=c.split("\n")
Not=[]
Seats=[]
for i in range(1,len(w)):
    x=w[i].split("  ")
    Not.append(x[0])
    Seats.append(int(x[1]))
for i in range(0,len(Not)):
    TrainArr.append(Train(Not[i],int(Seats[i])))


f=open("Station.txt","r")
c=f.read()
f.close()
w=c.split("\n")
Nos=[]
plat=[]
for i in range(1,len(w)):
    x=w[i].split("  ")
    Nos.append(x[0])
    plat.append(int(x[1]))
for i in range(0,len(Nos)):
    StationArr.append(Station(Nos[i],plat[i]))

# StationArr.append(Station("Jaipur",11))
# StationArr.append(Station("Bombay",15))
# StationArr.append(Station("Indore",8))
# StationArr.append(Station("Delhi",14))
# StationArr.append(Station("Kolkata",13))

f=open("Schedule.txt","r")
c=f.read()
f.close()
w=c.split("\n")
namesOT=[]
DepC=[]
DepT=[]
ArrC=[]
ArrT=[]
for i in range(1,len(w)):
    x=w[i].split("  ")
    namesOT.append(x[0])
    DepC.append(x[1])
    DepT.append(x[2])
    ArrC.append(x[3])
    ArrT.append(x[4]) 
for i in range(0,len(namesOT)):
    ScheduleArr.append(Schedule(namesOT[i],DepC[i],DepT[i],ArrC[i],ArrT[i]))


# ScheduleArr.append(Schedule("Shatabdi Express","Jaipur","14:00","Bombay","23:50"))
# ScheduleArr.append(Schedule("Rajdhani Express","Bombay","9:05","Delhi","21:20"))
# ScheduleArr.append(Schedule("Fanaty Express","Kolkata","2:00","Indore","15:40"))
# ScheduleArr.append(Schedule("Shanti Express","Delhi","7:10","Kolkata","15:50"))
# ScheduleArr.append(Schedule("Humsafar Express","Indore","17:40","Bombay","21:10"))
# ScheduleArr.append(Schedule("Fanaty Express","Bombay","7:40","Kolkata","20:10"))
# ScheduleArr.append(Schedule("Humsafar Express","Delhi","12:40","Jaipur","23:10"))
# ScheduleArr.append(Schedule("Shanti Express","Indore","4:05","Delhi","20:45"))
# ScheduleArr.append(Schedule("Shatabdi Express","Kolkata","00:40","Jaipur","17:05"))
# ScheduleArr.append(Schedule("Rajdhani Express","Jaipur","8:40","Indore","2:10"))
def checkSchedule():
    c=0 
    for i in ScheduleArr:
        f1=0
        f2=0
        f3=0
        tra=i.NameOfTrain
        sta1=i.DepartureCity
        sta2=i.ArrivalCity
        for j in TrainArr:
            if(j.NameOfTrain==tra):
                f1=1
        for j in StationArr:
            if(j.NameofStaion==sta1):
                f2=1
        for j in StationArr:
            if(j.NameofStaion==sta2):
                f3=1
        if(f1==0 or f2==0 or f3==0):
            del ScheduleArr[c]
        c+=1
        f=open('Schedule.txt','w')
        f.write("NAME OF TRAIN | DEPARTURE CITY | DEPARTURE TIME | ARRIVAL CITY | ARRIVAL TIME")
        for i in ScheduleArr:
            f.write("\n"+i.NameOfTrain+"  "+i.DepartureCity+"  "+i.DepartureTime+"  "+i.ArrivalCity+"  "+i.ArrivalTime)   
        f.close()
        
#admin functions
def AddEmployee():
    
    OutputFrame.configure(width=500,height=500,relief='flat',bg="#1e3d59")
    OutputFrame.place(x=350,y=80)
    
    for widget in OutputFrame.winfo_children():
        widget.destroy()
    OutputFrame.pack_forget()
    
    
    LabelEmpName = tk.Label(OutputFrame)
    LabelEmpName.place(relx=0.133, rely=0.089, height=51, width=200)
    LabelEmpName.configure(activeforeground="#000000")
    LabelEmpName.configure(background="#ff6e40")
    LabelEmpName.configure(foreground="#000000")
    LabelEmpName.configure(text='Enter Your Name')
    LabelEmpName.configure(font="-family {Segoe UI} -size 12")

    LabelEmpAge = tk.Label(OutputFrame)
    LabelEmpAge.place(relx=0.133, rely=0.267, height=51, width=200)
    LabelEmpAge.configure(activebackground="#f9f9f9")
    LabelEmpAge.configure(activeforeground="black")
    LabelEmpAge.configure(background="#ff6e40")
    LabelEmpAge.configure(foreground="#000000")
    LabelEmpAge.configure(font="-family {Segoe UI} -size 12")
    LabelEmpAge.configure(text='Enter Your Age')

    LabelEmpPass = tk.Label(OutputFrame)
    LabelEmpPass.place(relx=0.133, rely=0.444, height=51, width=200)
    LabelEmpPass.configure(activebackground="#f9f9f9")
    LabelEmpPass.configure(activeforeground="black")
    LabelEmpPass.configure(background="#ff6e40")
    LabelEmpPass.configure(foreground="#000000")
    LabelEmpPass.configure(font="-family {Segoe UI} -size 12")
    LabelEmpPass.configure(text='Set The password')

    EntryEmpName = tk.Entry(OutputFrame)
    EntryEmpName.place(relx=0.583, rely=0.089, height=46, relwidth=0.24)
    EntryEmpName.configure(background="white")
    EntryEmpName.configure(font="TkFixedFont")
    EntryEmpName.configure(foreground="#000000")

    EntryEmpAge = tk.Entry(OutputFrame)
    EntryEmpAge.place(relx=0.583, rely=0.267, height=46, relwidth=0.24)
    EntryEmpAge.configure(background="white")
    EntryEmpAge.configure(font="TkFixedFont")
    EntryEmpAge.configure(foreground="#000000")

    EntryEmpPass = tk.Entry(OutputFrame,show='*')
    EntryEmpPass.place(relx=0.583, rely=0.444, height=46, relwidth=0.24)
    EntryEmpPass.configure(background="white")
    EntryEmpPass.configure(font="TkFixedFont")
    EntryEmpPass.configure(foreground="#000000")

    LabelEmpConfirmPass = tk.Label(OutputFrame)
    LabelEmpConfirmPass.place(relx=0.133, rely=0.622, height=51, width=200)
    LabelEmpConfirmPass.configure(activebackground="#f9f9f9")
    LabelEmpConfirmPass.configure(activeforeground="black")
    LabelEmpConfirmPass.configure(background="#ff6e40")
    LabelEmpConfirmPass.configure(foreground="#000000")
    LabelEmpConfirmPass.configure(font="-family {Segoe UI} -size 12")
    LabelEmpConfirmPass.configure(text='Confirm The password')

    EntryEmpConfirmPass = tk.Entry(OutputFrame,show='*')
    EntryEmpConfirmPass.place(relx=0.583, rely=0.622, height=46, relwidth=0.24)
    EntryEmpConfirmPass.configure(background="white")
    EntryEmpConfirmPass.configure(font="TkFixedFont")
    EntryEmpConfirmPass.configure(foreground="#000000")

    def AddDetailsEmployee():
        if not EntryEmpName.get():
            tk.messagebox.showinfo('Login Result','ERROR!! ENTER YOUR NAME')
        elif not EntryEmpAge.get():
            tk.messagebox.showinfo('Login Result','ERROR!! ENTER YOUR AGE')
        elif not EntryEmpPass.get():
            tk.messagebox.showinfo('Login Result','ERROR!! ENTER YOUR PASSWORD')
        elif not EntryEmpConfirmPass.get():
            tk.messagebox.showinfo('Login Result','ERROR!! CONFIRM YOUR PASSWORD')
        else:
            try:
                EmpAge=int(EntryEmpAge.get())
                Password=EntryEmpPass.get()
                ConfirmPassword=EntryEmpConfirmPass.get()
                if EmpAge>0:
                    if Password==ConfirmPassword:
                        EmployeeArr.append(Employee(EntryEmpName.get(),EntryEmpAge.get(),EntryEmpPass.get()))
                        tk.messagebox.showinfo('Login Result',f'CONGRATULATIONS!! NEW EMPLOYEE IS SUCCESSFULLY ADDED\nYOUR ID IS {len(EmployeeArr)}.\n\nUSE THIS ID AT THE TIME OF LOGIN.')
                    else:
                        tk.messagebox.showinfo('Login Result','ERROR!! PASSWORDS MISMATCH. ENTER SAME PASSWORDS')
                else:
                    tk.messagebox.showinfo('Login Result','ERROR!! AGE SHOULD BE GREATER THAN 0')

            except ValueError:
                tk.messagebox.showinfo('Login Result','ERROR!! AGE SHOULD BE AN INTEGER')
        
    SubmitButtonForEmp = tk.Button(OutputFrame,command=AddDetailsEmployee)
    SubmitButtonForEmp.place(relx=0.433, rely=0.822, height=52, width=88)
    SubmitButtonForEmp.configure(activebackground="#000000")
    SubmitButtonForEmp.configure(activeforeground="#ffff00")
    SubmitButtonForEmp.configure(background="#ffc13b")
    SubmitButtonForEmp.configure(cursor="hand2")
    SubmitButtonForEmp.configure(foreground="#1e3d59")
    SubmitButtonForEmp.configure(font="-family {Segoe UI} -size 11 -weight bold")
    SubmitButtonForEmp.configure(text='SUBMIT')

def ViewEmployees():
    OutputFrame.configure(width=500,height=500,relief='flat',bg="#f5f0e1")
    OutputFrame.place(x=350,y=80)
    
    for widget in OutputFrame.winfo_children():
        widget.destroy()
    OutputFrame.pack_forget()

    LabelPrintEmpDetails=tk.Text(OutputFrame,bg = "#f5f0e1",font =("Courier", 12),height=60)

    LabelEmployeeDetails = tk.Label(OutputFrame)
    LabelEmployeeDetails.place(relx=0.183, rely=0.033, height=51 , width=240)
    LabelEmployeeDetails.configure(activebackground="#363aef")
    LabelEmployeeDetails.configure(background="#ff6e40")
    LabelEmployeeDetails.configure(font="-family {Times New Roman} -size 16 -weight bold")
    LabelEmployeeDetails.configure(foreground="#000000")
    LabelEmployeeDetails.configure(text='''Details Of Employees''')
    
    LabelIDEmp = tk.Label(OutputFrame)
    LabelIDEmp.place(relx=0.033, rely=0.103, height=40, width=125)
    LabelIDEmp.configure(activebackground="#f9f9f9")
    LabelIDEmp.configure(activeforeground="black")
    LabelIDEmp.configure(background="#ff6e40")
    LabelIDEmp.configure(disabledforeground="#a3a3a3")
    LabelIDEmp.configure(font="-family {Segoe UI} -size 12 -weight bold -slant italic")
    LabelIDEmp.configure(foreground="#000000")
    LabelIDEmp.configure(highlightbackground="#d9d9d9")
    LabelIDEmp.configure(highlightcolor="black")
    LabelIDEmp.configure(text='''ID''')

    LabelNameEmp = tk.Label(OutputFrame)
    LabelNameEmp.place(relx=0.253, rely=0.103, height=40, width=125)
    LabelNameEmp.configure(background="#ff6e40")
    LabelNameEmp.configure(disabledforeground="#a3a3a3")
    LabelNameEmp.configure(font="-family {Segoe UI} -size 12 -weight bold -slant italic")
    LabelNameEmp.configure(foreground="#000000")
    LabelNameEmp.configure(text='''Name''')

    LabelAgeEmp = tk.Label(OutputFrame)
    LabelAgeEmp.place(relx=0.473, rely=0.103, height=40, width=125)
    LabelAgeEmp.configure(activebackground="#f9f9f9")
    LabelAgeEmp.configure(activeforeground="black")
    LabelAgeEmp.configure(background="#ff6e40")
    LabelAgeEmp.configure(disabledforeground="#a3a3a3")
    LabelAgeEmp.configure(font="-family {Segoe UI} -size 12 -weight bold -slant italic")
    LabelAgeEmp.configure(foreground="#000000")
    LabelAgeEmp.configure(highlightbackground="#d9d9d9")
    LabelAgeEmp.configure(highlightcolor="black")
    LabelAgeEmp.configure(text='''Age''')
    
    LabelPrintEmpDetails.insert(END,'\n\n\n\n\n\n\n\n\n')
    Count=1
    for i in EmployeeArr:
        LabelPrintEmpDetails.insert(END,'\t'+ str(Count) +'\t')
        LabelPrintEmpDetails.insert(END,'        ' + str(i.name) + '\t')
        LabelPrintEmpDetails.insert(END,'\t\t   ' + str(i.age) + '\n')
        Count+=1
    LabelPrintEmpDetails.configure(state='disabled')
    LabelPrintEmpDetails.pack()

def ViewStation():
    
    OutputFrame.configure(width=500,height=500,relief='flat',bg="#f5f0e1")
    OutputFrame.place(x=350,y=80)
    for widget in OutputFrame.winfo_children():
        widget.destroy()
    OutputFrame.pack_forget()
        
    DetailsOfStations=tk.Text(OutputFrame,bg = "#f5f0e1",font =("Courier", 12),height=60)
    LabelStationDetails = tk.Label(OutputFrame)
    LabelStationDetails.place(relx=0.183, rely=0.033, height=51 , width=240)
    LabelStationDetails.configure(background="#ff6e40")
    LabelStationDetails.configure(font="-family {Segoe UI} -size 15 -weight bold")
    LabelStationDetails.configure(text='''Details of Stations''')
    
    LabelStationName = tk.Label(OutputFrame)
    LabelStationName.place(relx=0.253, rely=0.103, height=40, width=125)
    LabelStationName.configure(background="#ff6e40")
    LabelStationName.configure(font="-family {Segoe UI} -size 12 -weight bold")
    LabelStationName.configure(text='Name')
    
    LabelStationSrNo = tk.Label(OutputFrame)
    LabelStationSrNo.place(relx=0.033, rely=0.103, height=40, width=125)
    LabelStationSrNo.configure(background="#ff6e40")
    LabelStationSrNo.configure(font="-family {Segoe UI} -size 12 -weight bold")
    LabelStationSrNo.configure(text='Sr No')
    
    LabelPlatformNo = tk.Label(OutputFrame)
    LabelPlatformNo.place(relx=0.473, rely=0.103, height=40, width=125)
    LabelPlatformNo.configure(background="#ff6e40")
    LabelPlatformNo.configure(font="-family {Segoe UI} -size 12 -weight bold")
    LabelPlatformNo.configure(text='Total Platform')
    
    
    DetailsOfStations.insert(END,'\n\n\n\n\n\n\n\n\n')
    Count=1
    for i in StationArr:
        DetailsOfStations.insert(END,'\t'+ str(Count) +'\t')
        DetailsOfStations.insert(END,'       ' + str(i.NameofStaion) + '\t')
        DetailsOfStations.insert(END,'\t\t   ' + str(i.NoOfPlatforms) + '\n')
        Count+=1
    DetailsOfStations.configure(state='disabled')
    DetailsOfStations.pack()
    
def ViewTrains():
    
    OutputFrame.configure(width=500,height=500,relief='flat',bg="#f5f0e1")
    OutputFrame.place(x=350,y=80)
    for widget in OutputFrame.winfo_children():
        widget.destroy()
    OutputFrame.pack_forget()
    DetailsOfTrains=tk.Text(OutputFrame,bg = "#f5f0e1",font =("Courier", 12),height=60)
    LabelTrainDetails = tk.Label(OutputFrame)
    LabelTrainDetails.place(relx=0.183, rely=0.033, height=51 , width=240)
    LabelTrainDetails.configure(background="#ff6e40")
    LabelTrainDetails.configure(font="-family {Segoe UI} -size 15 -weight bold")
    LabelTrainDetails.configure(text='''Details of Trains''')
    
    LabelTrainSrNo = tk.Label(OutputFrame)
    LabelTrainSrNo.place(relx=0.033, rely=0.103, height=40, width=125)
    LabelTrainSrNo.configure(background="#ff6e40")
    LabelTrainSrNo.configure(font="-family {Segoe UI} -size 12 -weight bold")
    LabelTrainSrNo.configure(text='Sr No')

    LabelTrainName = tk.Label(OutputFrame)
    LabelTrainName.place(relx=0.253, rely=0.103, height=40, width=125)
    LabelTrainName.configure(background="#ff6e40")
    LabelTrainName.configure(font="-family {Segoe UI} -size 12 -weight bold")
    LabelTrainName.configure(text='Name')

    LabelSeat = tk.Label(OutputFrame)
    LabelSeat.place(relx=0.473, rely=0.103, height=40, width=125)
    LabelSeat.configure(background="#ff6e40")
    LabelSeat.configure(font="-family {Segoe UI} -size 12 -weight bold")
    LabelSeat.configure(text='''Total Seat''')
    
    Count=1
    DetailsOfTrains.insert(END,'\n\n\n\n\n\n\n\n\n')
    for i in TrainArr:
        DetailsOfTrains.insert(END,'\t'+ str(Count))
        DetailsOfTrains.insert(END,'          ' + str(i.NameOfTrain) + '\t')
        DetailsOfTrains.insert(END,'\t\t\t   ' + str(i.seat) + '\n')
        Count+=1
    DetailsOfTrains.configure(state='disabled')
    DetailsOfTrains.pack()
    
def ViewScheduleAdmin():
    
    OutputFrame.configure(width=500,height=500,relief='flat',bg="Cyan")
    OutputFrame.place(x=325,y=140)
    
    for widget in OutputFrame.winfo_children():
        widget.destroy()
    OutputFrame.pack_forget()
    
    checkSchedule()
    
    treev = ttk.Treeview(OutputFrame, selectmode ='browse')
    treev.pack()#side ='right')
    treev["columns"] = ("1", "2", "3", "4", "5", "6")
    
    # Defining heading
    treev['show'] = 'headings'
    treev.column("1", width = 50, anchor ='c')
    treev.column("2", width = 100, anchor ='c')
    treev.column("3", width = 100, anchor ='c')
    treev.column("4", width = 100, anchor ='c')
    treev.column("5", width = 100, anchor ='c')
    treev.column("6", width = 100, anchor ='c')
    treev.heading("1", text ="Sr No.")
    treev.heading("2", text ="Train Name")
    treev.heading("3", text ="Departure City")
    treev.heading("4", text ="Departure time")
    treev.heading("5", text ="Arrival City")
    treev.heading("6", text ="Arrival time")
    
    
    tempCount=0
    for i in ScheduleArr:
        tempCount+=1
        var1=i.NameOfTrain
        var2=i.DepartureCity
        var3=i.DepartureTime
        var4=i.ArrivalCity
        var5=i.ArrivalTime
        treev.insert("", 'end', text ="L1", values =(tempCount,var1,var2,var3,var4,var5))
    
#all funtions of employee    
        
def AddStation1():
    EmpFrame.place(x=0,y=0)
    for widget in EmpFrame.winfo_children():
        widget.destroy()
    Label1 = tk.Label(EmpFrame)
    Label1.place(relx=0.129, rely=0.074, height=71, width=464)
    Label1.configure(background="#ff6e40")
    Label1.configure(foreground="#000000")
    Label1.configure(font="-family {Segoe UI} -size 18 -weight bold")
    Label1.configure(text='Add New Station In The System')

    name = tk.Label(EmpFrame)
    name.place(relx=0.129, rely=0.333, height=41, width=163)
    name.configure(background="#ff6e40")
    name.configure(foreground="#000000")
    name.configure(text='Name of New Station')
    name.configure(font="-family {Segoe UI} -size 11")

    global NameOFStation
    NameOFStation = tk.Entry(EmpFrame)
    NameOFStation.place(relx=0.421, rely=0.333, height=40, relwidth=0.46)
    NameOFStation.configure(background="white")
    NameOFStation.configure(font="TkFixedFont")
    NameOFStation.configure(foreground="#000000")

    NoOfPlatforms = tk.Label(EmpFrame)
    NoOfPlatforms.place(relx=0.129, rely=0.5, height=41, width=163)
    NoOfPlatforms.configure(activebackground="#f9f9f9")
    NoOfPlatforms.configure(activeforeground="black")
    NoOfPlatforms.configure(background="#ff6e40")
    NoOfPlatforms.configure(font="-family {Segoe UI} -size 11")
    NoOfPlatforms.configure(foreground="#000000")
    NoOfPlatforms.configure(text='Number of Stations')

    global nopEntry
    nopEntry = tk.Entry(EmpFrame)
    nopEntry.place(relx=0.421, rely=0.5, height=40, relwidth=0.071)
    nopEntry.configure(background="white")
    nopEntry.configure(font="TkFixedFont")
    nopEntry.configure(foreground="#000000")

    def AddDetailsStation():
        if not NameOFStation.get():
            tk.messagebox.showinfo('Login Result','ERROR!! ENTER NAME OF STATION')
        elif not nopEntry.get():
            tk.messagebox.showinfo('Login Result','ERROR!! ENTER YOUR NUMBER OF PLATFORMS IN STATION')
        else:
            try:
                n=int(nopEntry.get())
                if n>0:
                    tk.messagebox.showinfo('Login Result','CONGRATULATIONS!! NEW STATION IS SUCCESSFULLY ADDED')
                    StationArr.append(Station(NameOFStation.get(),nopEntry.get()))
                    f=open("Station.txt","a")
                    f.write("\n"+StationArr[len(StationArr)-1].NameofStaion+"  "+StationArr[len(StationArr)-1].NoOfPlatforms)
                    f.close()
                else:
                    tk.messagebox.showinfo('Login Result','ERROR!! NUMBER OF PLATFORMS SHOULD BE GREATER THAN 0')

            except ValueError:
                tk.messagebox.showinfo('Login Result','ERROR!! NUMBER OF PLATFORMS SHOULD BE AN INTEGER')
                
    SubmitStation = tk.Button(EmpFrame,command= AddDetailsStation)
    SubmitStation.place(relx=0.405, rely=0.667, height=34, width=97)
    SubmitStation.configure(activebackground="#ececec")
    SubmitStation.configure(activeforeground="#fa2e0a")
    SubmitStation.configure(background="#ffc13b")
    SubmitStation.configure(foreground="#1e3d59")
    SubmitStation.configure(cursor="hand2")
    SubmitStation.configure(font="-family {Segoe UI} -size 11 -weight bold")
    SubmitStation.configure(text='Submit')
    
def AddTrain1():
    EmpFrame.place(x=0,y=0)
    for widget in EmpFrame.winfo_children():
            widget.destroy()
    Label1 = tk.Label(EmpFrame)
    Label1.place(relx=0.129, rely=0.074, height=71, width=464)
    Label1.configure(background="#ff6e40")
    Label1.configure(foreground="#000000")
    Label1.configure(font="-family {Segoe UI} -size 18 -weight bold")
    Label1.configure(text='Add New Train In The System')

    name = tk.Label(EmpFrame)
    name.place(relx=0.129, rely=0.333, height=41, width=163)
    name.configure(background="#ff6e40")
    name.configure(foreground="#000000")
    name.configure(font="-family {Segoe UI} -size 11")
    name.configure(text='Name of New Train')

    global NameOFTrain
    NameOFTrain = tk.Entry(EmpFrame)
    NameOFTrain.place(relx=0.421, rely=0.333, height=40, relwidth=0.46)
    NameOFTrain.configure(background="white")
    NameOFTrain.configure(font="TkFixedFont")
    NameOFTrain.configure(foreground="#000000")

    NoOfPlatSeats = tk.Label(EmpFrame)
    NoOfPlatSeats.place(relx=0.129, rely=0.5, height=41, width=163)
    NoOfPlatSeats.configure(activebackground="#f9f9f9")
    NoOfPlatSeats.configure(activeforeground="black")
    NoOfPlatSeats.configure(background="#ff6e40")
    NoOfPlatSeats.configure(foreground="#000000")
    NoOfPlatSeats.configure(font="-family {Segoe UI} -size 11")
    NoOfPlatSeats.configure(text='Number of Seats')

    global nosEntry
    nosEntry = tk.Entry(EmpFrame)
    nosEntry.place(relx=0.421, rely=0.5, height=40, relwidth=0.071)
    nosEntry.configure(background="white")
    nosEntry.configure(font="TkFixedFont")
    nosEntry.configure(foreground="#000000")

    def AddDetailsTrain():
        
        if not NameOFTrain.get():
            tk.messagebox.showinfo('Login Result','ERROR!! ENTER NAME OF TRAIN')
        elif not nosEntry.get():
            tk.messagebox.showinfo('Login Result','ERROR!! ENTER YOUR NUMBER OF SEAT IN STATION')
        else:
            try:
                n=int(nosEntry.get())
                if n>0:
                    tk.messagebox.showinfo('Login Result','CONGRATULATIONS!! NEW TRAIN IS SUCCESSFULLY ADDED')
                    TrainArr.append(Train(NameOFTrain.get(),nosEntry.get()))
                    f=open("Train.txt","a")
                    f.write("\n"+TrainArr[len(TrainArr)-1].NameOfTrain+"  "+str(TrainArr[len(TrainArr)-1].seat))
                    f.close()
                else:
                    tk.messagebox.showinfo('Login Result','ERROR!! NUMBER OF PLATFORMS SHOULD BE GREATER THAN 0')

            except ValueError:
                tk.messagebox.showinfo('Login Result','ERROR!! NUMBER OF SEATS SHOULD BE AN INTEGER')
        
           
    
    SubmitTrain = tk.Button(EmpFrame,command= AddDetailsTrain)
    SubmitTrain.place(relx=0.405, rely=0.667, height=34, width=97)
    SubmitTrain.configure(activebackground="#ececec")
    SubmitTrain.configure(activeforeground="#fa2e0a")
    SubmitTrain.configure(background="#ffc13b")
    SubmitTrain.configure(foreground="#1e3d59")
    SubmitTrain.configure(cursor="hand2")
    SubmitTrain.configure(font="-family {Segoe UI} -size 11 -weight bold")
    SubmitTrain.configure(text='Submit')

def addSchedule1():
    EmpFrame.place(x=0,y=0)
    for widget in EmpFrame.winfo_children():
            widget.destroy()
            
    Label1 = tk.Label(EmpFrame)
    Label1.place(relx=0.058, rely=0.074, height=71, width=517)
    Label1.configure(background="#ff6e40")
    Label1.configure(foreground="#000000")
    Label1.configure(font="-family {Segoe UI} -size 18 -weight bold")
    Label1.configure(text='Set Schedule Of Train')

    ArrCity = tk.Label(EmpFrame)
    ArrCity.place(relx=0.497, rely=0.444, height=41, width=136)
    ArrCity.configure(background="#ff6e40")
    ArrCity.configure(foreground="#000000")
    ArrCity.configure(font="-family {Segoe UI} -size 11")
    ArrCity.configure(text='Arrival City')
    
    global ArrCityEntry
    ArrCityEntry = tk.Entry(EmpFrame)
    ArrCityEntry.place(relx=0.716, rely=0.444, height=40, relwidth=0.181)
    ArrCityEntry.configure(background="white")
    ArrCityEntry.configure(font="TkFixedFont")
    ArrCityEntry.configure(foreground="#000000")

    depCity = tk.Label(EmpFrame)
    depCity.place(relx=0.058, rely=0.444, height=41, width=136)
    depCity.configure(activebackground="#f9f9f9")
    depCity.configure(activeforeground="black")
    depCity.configure(background="#ff6e40")
    depCity.configure(foreground="#000000")
    depCity.configure(font="-family {Segoe UI} -size 11")
    depCity.configure(text='Departure City')
    
    global DepCityEntry
    DepCityEntry = tk.Entry(EmpFrame)
    DepCityEntry.place(relx=0.278, rely=0.444, height=40, relwidth=0.181)
    DepCityEntry.configure(background="white")
    DepCityEntry.configure(font="TkFixedFont")
    DepCityEntry.configure(foreground="#000000")

    DepTime = tk.Label(EmpFrame)
    DepTime.place(relx=0.058, rely=0.556, height=41, width=136)
    DepTime.configure(activebackground="#f9f9f9")
    DepTime.configure(activeforeground="black")
    DepTime.configure(background="#ff6e40")
    DepTime.configure(foreground="#000000")
    DepTime.configure(font="-family {Segoe UI} -size 11")
    DepTime.configure(text='''Departure Time''')

    global DepTimeEntry
    DepTimeEntry = tk.Entry(EmpFrame)
    DepTimeEntry.place(relx=0.278, rely=0.556, height=40, relwidth=0.123)
    DepTimeEntry.configure(background="white")
    DepTimeEntry.configure(font="TkFixedFont")
    DepTimeEntry.configure(foreground="#000000")

    depCity = tk.Label(EmpFrame)
    depCity.place(relx=0.058, rely=0.444, height=41, width=136)
    depCity.configure(activebackground="#f9f9f9")
    depCity.configure(activeforeground="black")
    depCity.configure(background="#ff6e40")
    depCity.configure(foreground="#000000")
    depCity.configure(font="-family {Segoe UI} -size 11")
    depCity.configure(text='''Departure City''')

    ArrTime = tk.Label(EmpFrame)
    ArrTime.place(relx=0.497, rely=0.556, height=41, width=136)
    ArrTime.configure(activebackground="#f9f9f9")
    ArrTime.configure(activeforeground="black")
    ArrTime.configure(background="#ff6e40")
    ArrTime.configure(foreground="#000000")
    ArrTime.configure(font="-family {Segoe UI} -size 11")
    ArrTime.configure(text='Arrival Time')

    global ArrTimeEntry
    ArrTimeEntry = tk.Entry(EmpFrame)
    ArrTimeEntry.place(relx=0.716, rely=0.556, height=40, relwidth=0.123)
    ArrTimeEntry.configure(background="white")
    ArrTimeEntry.configure(font="TkFixedFont")
    ArrTimeEntry.configure(foreground="#000000")

    nam=tk.Label(EmpFrame)
    nam.place(relx=0.058, rely=0.315, height=41, width=136)
    nam.configure(activebackground="#f9f9f9")
    nam.configure(activeforeground="black")
    nam.configure(background="#ff6e40")
    nam.configure(foreground="#000000")
    nam.configure(font="-family {Segoe UI} -size 11")
    nam.configure(text='Name Of Train')

    global namEntry_1
    namEntry_1 = tk.Entry(EmpFrame)
    namEntry_1.place(relx=0.278, rely=0.315, height=40,relwidth=0.62)
    namEntry_1.configure(background="white")
    namEntry_1.configure(font="TkFixedFont")
    namEntry_1.configure(foreground="#000000")
    
    def AddDetailsSchedule():
        traName=namEntry_1.get()
        if not namEntry_1.get():
            tk.messagebox.showinfo('Login Result','ERROR!! ENTER NAME OF TRAIN')
        elif not ArrCityEntry.get():
            tk.messagebox.showinfo('Login Result','ERROR!! ENTER NAME OF ARRIVAL CITY')
        elif not ArrTimeEntry.get():
            tk.messagebox.showinfo('Login Result','ERROR!! ENTER ARRIVAL TIME')
        elif not DepCityEntry.get():
            tk.messagebox.showinfo('Login Result','ERROR!! ENTER NAME OF DEPARETURE CITY')
        elif not DepTimeEntry.get():
            tk.messagebox.showinfo('Login Result','ERROR!! ENTER DEPARTURE TIME')
        else:
            f1=0
            f2=0
            f3=0
            ArSta=ArrCityEntry.get()
            DeSta=DepCityEntry.get()
            for j in TrainArr:
                if(j.NameOfTrain==traName):
                    f1=1
            for j in StationArr:
                if(j.NameofStaion==ArSta):
                    f2=1
            for j in StationArr:
                if(j.NameofStaion==DeSta):
                    f3=1
                    
            if(f1==0):
                tk.messagebox.showinfo('Login Result','ERROR!! ENTER NAME OF TRAIN WHICH IS PRESENT IN SYSTEM')
            elif(f2==0):
                tk.messagebox.showinfo('Login Result','ERROR!! ENTER NAME OF ARRIVAL CITY WHICH IS PRESENT IN SYSTEM AS STATION')
            elif(f3==0):
                tk.messagebox.showinfo('Login Result','ERROR!! ENTER NAME OF DEPARTURE CITY WHICH IS PRESENT IN SYSTEM AS STATION')
            else:
                tk.messagebox.showinfo('Login Result','CONGRATULATIONS!! NEW SCHEDULE IS SUCCESSFULLY SET')
                ScheduleArr.append(Schedule(namEntry_1.get(),ArrCityEntry.get(),ArrTimeEntry.get(),DepCityEntry.get(),DepTimeEntry.get()))
                f=open("Schedule.txt","a")
                f.write("\n"+ScheduleArr[len(ScheduleArr)-1].NameOfTrain+"  "+ScheduleArr[len(ScheduleArr)-1].DepartureCity+"  "+ScheduleArr[len(ScheduleArr)-1].DepartureTime+"  "+ScheduleArr[len(ScheduleArr)-1].ArrivalCity+"  "+ScheduleArr[len(ScheduleArr)-1].ArrivalTime)
                f.close()
           
    SubmitStation = tk.Button(EmpFrame,command=AddDetailsSchedule)
    SubmitStation.place(relx=0.409, rely=0.759, height=34, width=97)
    SubmitStation.configure(activebackground="#ececec")
    SubmitStation.configure(activeforeground="#fa2e0a")
    SubmitStation.configure(background="#ffc13b")
    SubmitStation.configure(foreground="#1e3d59")
    SubmitStation.configure(cursor="hand2")
    SubmitStation.configure(font="-family {Segoe UI} -size 11 -weight bold")
    SubmitStation.configure(text='Submit')
       
def ViewStationEmp():
    EmpFrame.place(x=0,y=0)
    for widget in EmpFrame.winfo_children():
        widget.destroy()
    EmpFrame.pack_forget()
        
    DetailsOfStations=tk.Text(EmpFrame,bg = "#f5f0e1",font =("Courier", 12),height=60)
    LabelStationDetails = tk.Label(EmpFrame)
    LabelStationDetails.place(relx=0.303, rely=0.083, height=51 , width=240)
    LabelStationDetails.configure(background="#ff6e40")
    LabelStationDetails.configure(font="-family {Segoe UI} -size 15 -weight bold")
    LabelStationDetails.configure(text='Details of Stations')
    
    LabelStationName = tk.Label(EmpFrame)
    LabelStationName.place(relx=0.393, rely=0.203, height=40, width=125)
    LabelStationName.configure(background="#ff6e40")
    LabelStationName.configure(font="-family {Segoe UI} -size 12 -weight bold")
    LabelStationName.configure(text='Name')
    
    LabelStationSrNo = tk.Label(EmpFrame)
    LabelStationSrNo.place(relx=0.033, rely=0.203, height=40, width=125)
    LabelStationSrNo.configure(background="#ff6e40")
    LabelStationSrNo.configure(font="-family {Segoe UI} -size 12 -weight bold")
    LabelStationSrNo.configure(text='Sr No')
    
    LabelPlatformNo = tk.Label(EmpFrame)
    LabelPlatformNo.place(relx=0.753, rely=0.203, height=40, width=125)
    LabelPlatformNo.configure(background="#ff6e40")
    LabelPlatformNo.configure(font="-family {Segoe UI} -size 12 -weight bold")
    LabelPlatformNo.configure(text='Total Platform')
    
    
    DetailsOfStations.insert(END,'\n\n\n\n\n\n\n\n\n')
    Count=1
    for i in StationArr:
        DetailsOfStations.insert(END,'\t'+ str(Count) +'\t')
        DetailsOfStations.insert(END,'           ' + str(i.NameofStaion) + '\t')
        DetailsOfStations.insert(END,'\t\t\t   ' + str(i.NoOfPlatforms) + '\n')
        Count+=1
    DetailsOfStations.configure(state='disabled')
    DetailsOfStations.pack()
    
    def DeleteStation():
        Del=tk.Tk()
    
        Del.geometry("417x239+541+146")
        Del.minsize(120, 1)
        Del.maxsize(1284, 701)
        Del.resizable(0,0)
        Del.title("Delete")
        Del.iconbitmap('Delete.ico')
        Del.configure(background="#f5f0e1")

        textlabel = tk.Label(Del)
        textlabel.place(relx=0.048, rely=0.126, height=61, width=378)
        textlabel.configure(background="#ff6e40")
        textlabel.configure(foreground="#000000")
        textlabel.configure(text='Enter sr.no of Station you want to edit or delete')
        textlabel.configure(font="-family {Segoe UI} -size 11 -weight bold")

        global SRnoEntry
        SRnoEntry = tk.Entry(Del)
        SRnoEntry.place(relx=0.408, rely=0.418, height=30, relwidth=0.177)
        SRnoEntry.configure(background="white")
        SRnoEntry.configure(font="TkFixedFont")
        SRnoEntry.configure(foreground="#000000")
        
        def deleteStaionInfo():
            if not SRnoEntry.get():
                tk.messagebox.showinfo('Login Result','Enter SR number')
            else:
                try:
                    ind=int(SRnoEntry.get())
                    if ind<1 or ind>len(StationArr):
                        tk.messagebox.showinfo('Login Result','INVALID SR NO')
                    else:
                        tk.messagebox.showinfo('Login Result','STATION DELETED SUCCESSFULLY')
                        Del.destroy()
                        del StationArr[ind-1]
                        f=open('Station.txt','w')
                        f.write("Name of Station | No. of platforms")
                        for i in StationArr:
                            f.write("\n"+i.NameofStaion+"  "+str(i.NoOfPlatforms))   
                        f.close()
                except ValueError:
                    tk.messagebox.showinfo('Login Result','ERROR!! SR NUMBER SHOULD BE AN INTEGER')
                           
        submitSRno = tk.Button(Del,command=deleteStaionInfo)
        submitSRno.place(relx=0.36, rely=0.753, height=34, width=127)
        submitSRno.configure(activebackground="#f97a44")
        submitSRno.configure(activeforeground="#000000")
        submitSRno.configure(background="#ffc13b")        
        submitSRno.configure(text='Submit')
        submitSRno.configure(foreground="#1e3d59")
        submitSRno.configure(cursor="hand2")
        submitSRno.configure(font="-family {Segoe UI} -size 11 -weight bold")
  
    DeleteStationButton= tk.Button(EmpFrame,command=DeleteStation)
    DeleteStationButton.place(relx=0.554, rely=0.89, height=44, width=117)
    DeleteStationButton.configure(activebackground="#ececec")
    DeleteStationButton.configure(activeforeground="#fa2e0a")
    DeleteStationButton.configure(background="#ffc13b")
    DeleteStationButton.configure(foreground="#1e3d59")
    DeleteStationButton.configure(cursor="hand2")
    DeleteStationButton.configure(font="-family {Segoe UI} -size 11 -weight bold")
    DeleteStationButton.configure(text='''Delete''')    

def ViewTrainsEmp():  
    EmpFrame.place(x=0,y=0)
    for widget in EmpFrame.winfo_children():
        widget.destroy()
    EmpFrame.pack_forget()
    DetailsOfTrains=tk.Text(EmpFrame,bg = "#f5f0e1",font =("Courier", 12),height=60)
    LabelTrainDetails = tk.Label(EmpFrame)
    LabelTrainDetails.place(relx=0.303, rely=0.083, height=51 , width=240)
    LabelTrainDetails.configure(background="#ff6e40")
    LabelTrainDetails.configure(font="-family {Segoe UI} -size 15 -weight bold")
    LabelTrainDetails.configure(text='Details of Trains')

    LabelTrainSrNo = tk.Label(EmpFrame)
    LabelTrainSrNo.place(relx=0.033, rely=0.203, height=40, width=125)
    LabelTrainSrNo.configure(background="#ff6e40")
    LabelTrainSrNo.configure(font="-family {Segoe UI} -size 12 -weight bold")
    LabelTrainSrNo.configure(text='Sr No')
    
    LabelTrainName = tk.Label(EmpFrame)
    LabelTrainName.place(relx=0.393, rely=0.203, height=40, width=125)
    LabelTrainName.configure(background="#ff6e40")
    LabelTrainName.configure(foreground="#000000")
    LabelTrainName.configure(font="-family {Segoe UI} -size 12 -weight bold")
    LabelTrainName.configure(text='Name')

    LabelSeat = tk.Label(EmpFrame)
    LabelSeat.place(relx=0.753, rely=0.203, height=40, width=125)
    LabelSeat.configure(background="#ff6e40")
    LabelSeat.configure(foreground="#000000")
    LabelSeat.configure(font="-family {Segoe UI} -size 12 -weight bold")
    LabelSeat.configure(text='Total Seat')
    
    
    DetailsOfTrains.insert(END,'\n\n\n\n\n\n\n\n\n')
    Count=1
    for i in TrainArr:
        DetailsOfTrains.insert(END,'\t'+ str(Count) +'\t')
        DetailsOfTrains.insert(END,'       ' + str(i.NameOfTrain) + '\t')
        DetailsOfTrains.insert(END,'\t\t\t   ' + str(i.seat) + '\n')
        Count+=1
    DetailsOfTrains.configure(state='disabled')
    DetailsOfTrains.pack()
    
    def DeleteTrain():
        Del=tk.Tk()
    
        Del.geometry("417x239+541+146")
        Del.minsize(120, 1)
        Del.maxsize(1284, 701)
        Del.resizable(0, 0)
        Del.title("Delete")
        Del.iconbitmap('Delete.ico')
        Del.configure(background="#f5f0e1")

        textlabel = tk.Label(Del)
        textlabel.place(relx=0.048, rely=0.126, height=61, width=378)
        textlabel.configure(background="#ff6e40")
        textlabel.configure(foreground="#000000")
        textlabel.configure(text='Enter sr.no of train you want to edit or delete')
        textlabel.configure(font="-family {Segoe UI} -size 11 -weight bold")

        global SRnoEntry
        SRnoEntry = tk.Entry(Del)
        SRnoEntry.place(relx=0.408, rely=0.418, height=30, relwidth=0.177)
        SRnoEntry.configure(background="white")
        SRnoEntry.configure(font="TkFixedFont")
        SRnoEntry.configure(foreground="#000000")
        
        def deleteTrainInfo():
            if not SRnoEntry.get():
                tk.messagebox.showinfo('Login Result','Enter SR number')
            else:
                try:
                    ind=int(SRnoEntry.get())
                    if ind<1 or ind>len(TrainArr):
                        tk.messagebox.showinfo('Login Result','INVALID SR NO')
                    else:
                        tk.messagebox.showinfo('Login Result','TRAIN DELETED SUCCESSFULLY')
                        Del.destroy()
                        del TrainArr[ind-1]
                        f=open('Train.txt','w')
                        f.write("Name of Train | No. of platforms")
                        for i in TrainArr:
                            f.write("\n"+i.NameOfTrain+"  "+str(i.seat))   
                        f.close()

                except ValueError:
                    tk.messagebox.showinfo('Login Result','ERROR!! SR NUMBER SHOULD BE AN INTEGER')
            
        submitSRno = tk.Button(Del,command=deleteTrainInfo)
        submitSRno.place(relx=0.36, rely=0.753, height=34, width=127)
        submitSRno.configure(activebackground="#f97a44")
        submitSRno.configure(activeforeground="#000000")
        submitSRno.configure(background="#ffc13b")
        submitSRno.configure(foreground="#1e3d59")
        submitSRno.configure(cursor="hand2")
        submitSRno.configure(font="-family {Segoe UI} -size 11 -weight bold")
        submitSRno.configure(text='Submit')
  
    DeleteTrainButton= tk.Button(EmpFrame,command=DeleteTrain)
    DeleteTrainButton.place(relx=0.554, rely=0.89, height=44, width=117)
    DeleteTrainButton.configure(activebackground="#ececec")
    DeleteTrainButton.configure(activeforeground="#fa2e0a")
    DeleteTrainButton.configure(background="#ffc13b")
    DeleteTrainButton.configure(foreground="#1e3d59")
    DeleteTrainButton.configure(cursor="hand2")
    DeleteTrainButton.configure(font="-family {Segoe UI} -size 11 -weight bold")
    DeleteTrainButton.configure(text='Delete')
    
def ViewScheduleEmp():
    EmpFrame.place(x=0,y=100)
    for widget in EmpFrame.winfo_children():
        widget.destroy()
    EmpFrame.pack_forget()
    
    checkSchedule()
    
    treev = ttk.Treeview(EmpFrame, selectmode ='browse')
    treev.pack()#side ='right')
    treev["columns"] = ("1", "2", "3", "4", "5", "6")
    
    # Defining heading
    treev['show'] = 'headings'
    treev.column("1", width = 50, anchor ='c')
    treev.column("2", width = 100, anchor ='c')
    treev.column("3", width = 100, anchor ='c')
    treev.column("4", width = 100, anchor ='c')
    treev.column("5", width = 100, anchor ='c')
    treev.column("6", width = 100, anchor ='c')
    treev.heading("1", text ="Sr No.")
    treev.heading("2", text ="Train Name")
    treev.heading("3", text ="Departure City")
    treev.heading("4", text ="Departure time")
    treev.heading("5", text ="Arrival City")
    treev.heading("6", text ="Arrival time")
        
    tempCount=0
    for i in ScheduleArr:
        tempCount+=1
        var1=i.NameOfTrain
        var2=i.DepartureCity
        var3=i.DepartureTime
        var4=i.ArrivalCity
        var5=i.ArrivalTime
        treev.insert("", 'end', text ="L1", values =(tempCount,var1,var2,var3,var4,var5))
        
    def DeleteSchedule():
        Del=tk.Tk()
    
        Del.geometry("417x239+541+146")
        Del.minsize(120, 1)
        Del.maxsize(1284, 701)
        Del.resizable(0, 0)
        Del.title("Delete")
        Del.iconbitmap('Delete.ico')
        Del.configure(background="#f5f0e1")

        textlabel = tk.Label(Del)
        textlabel.place(relx=0.048, rely=0.126, height=61, width=378)
        textlabel.configure(background="#ff6e40")
        textlabel.configure(foreground="#000000")
        textlabel.configure(text='Enter sr.no of Schedule you want to edit or delete')
        textlabel.configure(font="-family {Segoe UI} -size 11 -weight bold")

        global SRnoEntry
        SRnoEntry = tk.Entry(Del)
        SRnoEntry.place(relx=0.408, rely=0.418, height=30, relwidth=0.177)
        SRnoEntry.configure(background="white")
        SRnoEntry.configure(font="TkFixedFont")
        SRnoEntry.configure(foreground="#000000")
        
        def deleteScheduleInfo():
            if not SRnoEntry.get():
                tk.messagebox.showinfo('Login Result','Enter SR number')
            else:
                try:
                    ind=int(SRnoEntry.get())
                    if ind<1 or ind>len(ScheduleArr):
                        tk.messagebox.showinfo('Login Result','INVALID SR NO')
                    else:
                        tk.messagebox.showinfo('Login Result','SCHEDULE DELETED SUCCESSFULLY')
                        Del.destroy()
                        del ScheduleArr[ind-1]
                        f=open('Schedule.txt','w')
                        f.write("NAME OF TRAIN | DEPARTURE CITY | DEPARTURE TIME | ARRIVAL CITY | ARRIVAL TIME")
                        for i in ScheduleArr:
                            f.write("\n"+i.NameOfTrain+"  "+i.DepartureCity+"  "+i.DepartureTime+"  "+i.ArrivalCity+"  "+i.ArrivalTime)   
                        f.close()
                except ValueError:
                    tk.messagebox.showinfo('Login Result','ERROR!! SR NUMBER SHOULD BE AN INTEGER')
            
        submitSRno = tk.Button(Del,command=deleteScheduleInfo)
        submitSRno.place(relx=0.36, rely=0.753, height=34, width=127)
        submitSRno.configure(activebackground="#f97a44")
        submitSRno.configure(activeforeground="#000000")
        submitSRno.configure(background="#ffc13b")
        submitSRno.configure(foreground="#1e3d59")
        submitSRno.configure(cursor="hand2")
        submitSRno.configure(font="-family {Segoe UI} -size 11 -weight bold")
        submitSRno.configure(text='Submit')
  
    DeleteScheduleButton= tk.Button(EmpFrame,command=DeleteSchedule)
    DeleteScheduleButton.place(relx=0.554, rely=0.59, height=44, width=117)
    DeleteScheduleButton.configure(activebackground="#ececec")
    DeleteScheduleButton.configure(activeforeground="#fa2e0a")
    DeleteScheduleButton.configure(background="#ffc13b")
    DeleteScheduleButton.configure(foreground="#1e3d59")
    DeleteScheduleButton.configure(cursor="hand2")
    DeleteScheduleButton.configure(font="-family {Segoe UI} -size 11 -weight bold")
    DeleteScheduleButton.configure(text='Delete')
    
def EmpViewTicket():
    EmpFrame.place(x=0,y=0)
    for widget in EmpFrame.winfo_children():
        widget.destroy()
    EmpFrame.pack_forget()

    LabelFrame1=tk.LabelFrame(EmpFrame)
    LabelFrame1.place(relx=0.029, rely=0.020, relheight=0.450, relwidth=0.948)
    LabelFrame1.configure(borderwidth="2")
    LabelFrame1.configure(relief="groove")
    LabelFrame1.configure(background="#f5f0e1")
    LabelFrame1.configure(text='Confirmed Tickets')

    treev = ttk.Treeview(LabelFrame1, selectmode ='browse')
    treev.pack()
    treev["columns"] = ("1", "2", "3", "4", "5", "6", "7")
    
    # Defining heading
    treev['show'] = 'headings'
    treev.column("1", width = 50, anchor ='c')
    treev.column("2", width = 90, anchor ='c')
    treev.column("3", width = 100, anchor ='c')
    treev.column("4", width = 50, anchor ='c')
    treev.column("5", width = 100, anchor ='c')
    treev.column("6", width = 100, anchor ='c')
    treev.column("7", width = 80, anchor ='c')
    treev.heading("1", text ="Ticket No.")
    treev.heading("2", text ="Name")
    treev.heading("3", text ="Train Name")
    treev.heading("4", text ="No. of seats")
    treev.heading("5", text ="Departure City")
    treev.heading("6", text ="Arrival City")
    treev.heading("7", text ="Departure time")
    
    for i in TicketArr:
        if i.status == "confirmed":
            var0=i.TickNum
            var1=i.name
            var2=i.NameOfTrain
            var3=i.NoOfTickets
            var4=i.NameOfStation
            var5=i.destination
            var6=i.TimeOfTrain
            treev.insert("", 'end', text ="L1", values =(var0,var1,var2,var3,var4,var5,var6))

    LabelFrame2=tk.LabelFrame(EmpFrame)
    LabelFrame2.place(relx=0.029, rely=0.500, relheight=0.450, relwidth=0.948)
    LabelFrame2.configure(borderwidth="2")
    LabelFrame2.configure(relief="groove")
    LabelFrame2.configure(background="#f5f0e1")
    LabelFrame2.configure(text='Not Confirmed Tickets')

    ntreev = ttk.Treeview(LabelFrame2, selectmode ='browse')
    ntreev.pack()
    ntreev["columns"] = ("1", "2", "3", "4", "5", "6", "7")
    
    # Defining heading
    ntreev['show'] = 'headings'
    ntreev.column("1", width = 50, anchor ='c')
    ntreev.column("2", width = 90, anchor ='c')
    ntreev.column("3", width = 100, anchor ='c')
    ntreev.column("4", width = 50, anchor ='c')
    ntreev.column("5", width = 100, anchor ='c')
    ntreev.column("6", width = 100, anchor ='c')
    ntreev.column("7", width = 80, anchor ='c')
    ntreev.heading("1", text ="Ticket No.")
    ntreev.heading("2", text ="Name")
    ntreev.heading("3", text ="Train Name")
    ntreev.heading("4", text ="No. of seats")
    ntreev.heading("5", text ="Departure City")
    ntreev.heading("6", text ="Arrival City")
    ntreev.heading("7", text ="Departure time")
    
    for i in TicketArr:
        if i.status == "not confirmed":
            var0=i.TickNum
            var1=i.name
            var2=i.NameOfTrain
            var3=i.NoOfTickets
            var4=i.NameOfStation
            var5=i.destination
            var6=i.TimeOfTrain
            ntreev.insert("", 'end', text ="L1", values =(var0,var1,var2,var3,var4,var5,var6))

def EmpConfirmTicket():
    EmpFrame.place(x=0,y=0)
    for widget in EmpFrame.winfo_children():
        widget.destroy()
    EmpFrame.pack_forget()

    global TickFrame
    TickFrame = tk.Frame(EmpFrame)
    TickFrame.place(relx=0.029, rely=0.300, relheight=0.650, relwidth=0.948)
    TickFrame.configure(borderwidth="2")
    TickFrame.configure(relief="flat")
    TickFrame.configure(background="#1e3d59")

    TickLabel = tk.Label(EmpFrame)
    TickLabel.place(relx=0.15, rely=0.067, height=31, width=114)
    TickLabel.configure(background="#ff6e40")
    TickLabel.configure(foreground="#000000")
    TickLabel.configure(text='Enter Ticket Number')

    global TickEntry 
    TickEntry = tk.Entry(EmpFrame)
    TickEntry.place(relx=0.35, rely=0.067, height=30, relwidth=0.473)
    TickEntry.configure(background="white")
    TickEntry.configure(font="TkFixedFont")
    TickEntry.configure(foreground="#000000")

    def PrintTicket():
        for widget in TickFrame.winfo_children():
            widget.destroy()
        TickFrame.pack_forget()

        if not TickEntry.get():
            tk.messagebox.showinfo('Viewing Ticket','ERROR!! ENTER YOUR TICKET NUMBER.')
        else:
            try:
                num=int(TickEntry.get())
                if num>0:
                    Ticketprint=tk.Text(TickFrame)
                    Ticketprint.configure(background="#f5f0e1")
                    if len(TicketArr) == 0:
                        if ticketno == 1:
                            Ticketprint.insert(END,'\n\n\n\n')
                            Ticketprint.insert(END,'\t\t\tTicket does Not Exist!\n\t\t\t Enter Valid Number.')
                            Ticketprint.configure(state='disabled')
                            Ticketprint.pack()
                        elif num < ticketno:
                            Ticketprint.insert(END,'\n\n\n\n')
                            Ticketprint.insert(END,'\t\t\tTicket has been Cancelled!\n\t\t\t Enter Valid Number.')
                            Ticketprint.configure(state='disabled')
                            Ticketprint.pack()
                        else:
                            Ticketprint.insert(END,'\n\n\n\n')
                            Ticketprint.insert(END,'\t\t\tTicket does Not Exist!\n\t\t\t Enter Valid Number.')
                            Ticketprint.configure(state='disabled')
                            Ticketprint.pack()
                    else:
                        for i in TicketArr:
                            if i.TickNum == num:
                                Ticketprint.insert(END,'Ticket Number: '+str(i.TickNum))
                                Ticketprint.insert(END,"\n----------------------------------------------------------\n\n")
                                Ticketprint.insert(END,"Name: "+i.name+"\t\t\t\tNumber of Seats: "+i.NoOfTickets)
                                Ticketprint.insert(END,"\n\nStation: "+i.NameOfStation+"\t\t\t\tDestination: "+i.destination)
                                Ticketprint.insert(END,"\n\nName of Train: "+i.NameOfTrain+"\t\t\t\tArrival Time: "+i.TimeOfTrain)
                                Ticketprint.insert(END,"\n\n\t Status: "+i.status)
                                Ticketprint.configure(state='disabled')
                                Ticketprint.pack()
                                global TickSubmit
                                TickSubmit=tk.Button(TickFrame,command=i.ConfirmTicket)
                                TickSubmit.place(relx=0.445, rely=0.780, height=34, width=77)
                                TickSubmit.configure(activebackground="#ececec")
                                TickSubmit.configure(activeforeground="#fa2e0a")
                                TickSubmit.configure(background="#ffc13b")
                                TickSubmit.configure(foreground="#1e3d59")
                                TickSubmit.configure(font="-family {Segoe UI} -size 11 -weight bold")
                                TickSubmit.configure(cursor="hand2")
                                TickSubmit.configure(text='Confirm')
                                break
                            elif i.TickNum > num:
                                Ticketprint.insert(END,'\n\n\n\n')
                                Ticketprint.insert(END,'\t\t\tTicket has been Cancelled!\n\t\t\t Enter Valid Number.')
                                Ticketprint.configure(state='disabled')
                                Ticketprint.pack()
                                break
                            elif num >= ticketno:
                                Ticketprint.insert(END,'\n\n\n\n')
                                Ticketprint.insert(END,'\t\t\tTicket does Not Exist!\n\t\t\t Enter Valid Number.')
                                Ticketprint.configure(state='disabled')
                                Ticketprint.pack()
                                break
                else:
                    tk.messagebox.showinfo('Viewing Ticket','ERROR!! TICKET NUMBER SHOULD BE GREATER THAN 0')

            except ValueError:
                tk.messagebox.showinfo('Viewing Ticket','ERROR!! TICKET NUMBER SHOULD BE AN INTEGER')

    OkButton=tk.Button(EmpFrame,command=PrintTicket)
    OkButton.place(relx=0.55, rely=0.167, height=30, width=47)
    OkButton.configure(activebackground="#ececec")
    OkButton.configure(activeforeground="#fa2e0a")
    OkButton.configure(background="#ffc13b")
    OkButton.configure(font="-family {Segoe UI} -size 11 -weight bold")
    OkButton.configure(foreground="#1e3d59")
    OkButton.configure(cursor="hand2")
    OkButton.configure(text='OK')

#customer functions
def BookTicket():
    
    CustomerWindow.destroy()
    global BookWindow
    BookWindow = tkinter.Tk()
    BookWindow.geometry("686x500+285+79")
    BookWindow.minsize(116, 1)
    BookWindow.maxsize(1370, 750)
    BookWindow.resizable(0,  0)
    BookWindow.title("Book Ticket")
    BookWindow.configure(background="#1e3d59")
    BookWindow.iconbitmap('Employee.ico')

    Labelframe1 = tk.Frame(BookWindow)
    Labelframe1.place(relx=0.029, rely=0.313, relheight=0.570, relwidth=0.948)
    Labelframe1.configure(relief='flat')
    Labelframe1.configure(background="#1e3d59")
    treev = ttk.Treeview(Labelframe1, selectmode ='browse')
    treev.pack()
    treev["columns"] = ("1", "2", "3", "4", "5", "6")
    
    treev['show'] = 'headings'
    treev.column("1", width = 50, anchor ='c')
    treev.column("2", width = 100, anchor ='c')
    treev.column("3", width = 100, anchor ='c')
    treev.column("4", width = 100, anchor ='c')
    treev.column("5", width = 100, anchor ='c')
    treev.column("6", width = 100, anchor ='c')
    treev.heading("1", text ="Sr No.")
    treev.heading("2", text ="Train Name")
    treev.heading("3", text ="Departure City")
    treev.heading("4", text ="Departure time")
    treev.heading("5", text ="Arrival City")
    treev.heading("6", text ="Arrival time")
    
    
    tempCount=0
    for i in ScheduleArr:
        tempCount+=1
        var1=i.NameOfTrain
        var2=i.DepartureCity
        var3=i.DepartureTime
        var4=i.ArrivalCity
        var5=i.ArrivalTime
        treev.insert("", 'end', text ="L1", values =(tempCount,var1,var2,var3,var4,var5))

    Heading = tk.Message(BookWindow)
    Heading.place(relx=0.05, rely=0.0, relheight=0.132, relwidth=0.903)
    Heading.configure(background="#1e3d59")
    Heading.configure(font="-family {Segoe UI} -size 18 -weight bold")
    Heading.configure(foreground="#ffc13b")
    Heading.configure(text="Ticket Booking")
    Heading.configure(width=542)

    Message2 = tk.Message(BookWindow)
    Message2.place(relx=0.044, rely=0.117, height=30, relwidth=0.117)
    Message2.configure(anchor='w')
    Message2.configure(background="#ff6e40")
    Message2.configure(foreground="#000000")
    Message2.configure(text='Name')
    Message2.configure(font="-family {Segoe UI} -size 10")
    Message2.configure(width=80)

    Message3 = tk.Message(BookWindow)
    Message3.place(relx=0.044, rely=0.208, height=30, relwidth=0.117)
    Message3.configure(anchor='w')
    Message3.configure(background="#ff6e40")
    Message3.configure(foreground="#000000")
    Message3.configure(text='No. of seats')
    Message3.configure(font="-family {Segoe UI} -size 10")
    Message3.configure(width=80)

    global Entryname
    Entryname = tk.Entry(BookWindow)
    Entryname.place(relx=0.19, rely=0.117, height=30, relwidth=0.181)
    Entryname.configure(background="white")
    Entryname.configure(font="TkFixedFont")
    Entryname.configure(foreground="#000000")

    global Entryseat
    Entryseat = tk.Entry(BookWindow)
    Entryseat.place(relx=0.19, rely=0.208, height=30, relwidth=0.181)
    Entryseat.configure(background="white")
    Entryseat.configure(font="TkFixedFont")
    Entryseat.configure(foreground="#000000")

    Message4 = tk.Message(BookWindow)
    Message4.place(relx=0.029, rely=0.839, height=30, relwidth=0.219)
    Message4.configure(anchor='w')
    Message4.configure(background="#ff6e40")
    Message4.configure(foreground="#000000")
    Message4.configure(text='Enter schedule number')
    Message4.configure(font="-family {Segoe UI} -size 10")
    Message4.configure(width=150)

    global Entrytrain
    Entrytrain = tk.Entry(BookWindow)
    Entrytrain.place(relx=0.262, rely=0.839, height=30, relwidth=0.152)
    Entrytrain.configure(background="white")
    Entrytrain.configure(font="TkFixedFont")
    Entrytrain.configure(foreground="#000000")

    def ConfirmBook():
        if not Entryname.get():
            tk.messagebox.showinfo('Login Result','ERROR!! ENTER YOUR NAME')
        elif not Entryseat.get():
            tk.messagebox.showinfo('Login Result','ERROR!! ENTER NO. OF SEATS')
        elif not Entrytrain.get():
            tk.messagebox.showinfo('Login Result','ERROR!! ENTER SCHEDULE NO. TO BE BOOKED')
        else:
            try:
                i=int(Entrytrain.get())-1
                try:
                    seat=int(Entryseat.get())
                    if seat>0:
                        if i<0 or i>=len(ScheduleArr):
                            tk.messagebox.showinfo('Login Result','ERROR!! INVALID SCHEDULE NUMBER')
                        else: 
                            TicketArr.append(Ticket(Entryname.get(),ScheduleArr[i].DepartureCity,ScheduleArr[i].ArrivalCity,ScheduleArr[i].NameOfTrain,ScheduleArr[i].DepartureTime,Entryseat.get()))
                            global ticketno
                            ticketno+=1
                            tk.messagebox.showinfo('Booking Result',f'TICKET BOOKED SUCCESSFULLY!!\n\nYOUR TICKET NUMBER = {ticketno-1}')
                            BookWindow.destroy()
                    else:
                        tk.messagebox.showinfo('Login Result','ERROR!! NO.OF SEATS SHOULD BE GREATER THAN 0')

                except ValueError:
                    tk.messagebox.showinfo('Booking Result','ERROR!! NO.OF SEATS SHOULD BE AN INTEGER')

            except ValueError:
                tk.messagebox.showinfo('Booking Result','ERROR!! SCHEDULE NUMBER SHOULD BE AN INTEGER')
        

    Button1 = tk.Button(BookWindow,command=ConfirmBook)
    Button1.place(relx=0.845, rely=0.895, height=34, width=77)
    Button1.configure(activebackground="#72ca4d")
    Button1.configure(activeforeground="#000000")
    Button1.configure(background="#ffc13b")
    Button1.configure(foreground="#1e3d59")
    Button1.configure(cursor="hand2")
    Button1.configure(font="-family {Segoe UI} -size 11 -weight bold")
    Button1.configure(text='Confirm')

def CheckStatus():
    
    CustomerWindow.destroy()
    global CheckStat
    CheckStat=tkinter.Tk()
    CheckStat.geometry("639x499+316+74")
    CheckStat.minsize(116, 1)
    CheckStat.maxsize(1370, 750)
    CheckStat.resizable(0, 0)
    CheckStat.title("Check Ticket Status")
    CheckStat.configure(background="#1e3d59")
    CheckStat.iconbitmap('Employee.ico')

    global StatTickFrame
    StatTickFrame = tk.Frame(CheckStat)
    StatTickFrame.place(relx=0.031, rely=0.321, relheight=0.451, relwidth=0.947)
    StatTickFrame.configure(relief='flat')
    StatTickFrame.configure(borderwidth="2")
    StatTickFrame.configure(background="#1e3d59")

    Label1 = tk.Label(CheckStat)
    Label1.place(relx=0.205, rely=0.08, height=41, width=134)
    Label1.configure(background="#ff6e40")
    Label1.configure(foreground="#000000")
    Label1.configure(font="-family {Segoe UI} -size 11")
    Label1.configure(text='Enter Ticket No.')

    global StatTickEntry
    StatTickEntry = tk.Entry(CheckStat)
    StatTickEntry.place(relx=0.468, rely=0.08, height=40, relwidth=0.351)
    StatTickEntry.configure(background="white")
    StatTickEntry.configure(font="TkFixedFont")
    StatTickEntry.configure(foreground="#000000")

    def StatPrintTicket():
        for widget in StatTickFrame.winfo_children():
            widget.destroy()
        StatTickFrame.pack_forget()

        if not StatTickEntry.get():
            tk.messagebox.showinfo('Viewing Ticket','ERROR!! ENTER YOUR TICKET NUMBER.')
        else:
            try:
                num=int(StatTickEntry.get())
                if num>0:
                    def CloseWindow():
                        CheckStat.destroy()

                    global TickDone
                    TickDone=tk.Button(CheckStat,command=CloseWindow)
                    TickDone.place(relx=0.735, rely=0.900, height=34, width=77)
                    TickDone.configure(activebackground="#72ca4d")
                    TickDone.configure(activeforeground="#000000")
                    TickDone.configure(background="#ffc13b")
                    TickDone.configure(foreground="#1e3d59")
                    TickDone.configure(cursor="hand2")
                    TickDone.configure(font="-family {Segoe UI} -size 11 -weight bold")
                    TickDone.configure(text='Done')
                    
                    Ticketprint=tk.Text(StatTickFrame)
                    Ticketprint.configure(background="#f5f0e1")
                    if len(TicketArr) == 0:
                        if ticketno == 1:
                            Ticketprint.insert(END,'\n\n\n\n')
                            Ticketprint.insert(END,'\t\t\tTicket does Not Exist!\n\t\t\t Enter Valid Number.')
                            Ticketprint.configure(state='disabled')
                            Ticketprint.pack()
                        elif num < ticketno:
                            Ticketprint.insert(END,'\n\n\n\n')
                            Ticketprint.insert(END,'\t\t\tTicket has been Cancelled!\n\t\t\t Enter Valid Number.')
                            Ticketprint.configure(state='disabled')
                            Ticketprint.pack()
                        else:
                            Ticketprint.insert(END,'\n\n\n\n')
                            Ticketprint.insert(END,'\t\t\tTicket does Not Exist!\n\t\t\t Enter Valid Number.')
                            Ticketprint.configure(state='disabled')
                            Ticketprint.pack()
                    else:
                        for i in TicketArr:
                            if i.TickNum == num:
                                
                                Ticketprint.insert(END,'Ticket Number: '+str(i.TickNum))
                                Ticketprint.insert(END,"\n----------------------------------------------------------\n\n")
                                Ticketprint.insert(END,"Name: "+i.name+"\t\t\t\tNumber of Seats: "+i.NoOfTickets)
                                Ticketprint.insert(END,"\n\nStation: "+i.NameOfStation+"\t\t\t\tDestination: "+i.destination)
                                Ticketprint.insert(END,"\n\nName of Train: "+i.NameOfTrain+"\t\t\t\tArrival Time: "+i.TimeOfTrain)
                                Ticketprint.insert(END,"\n\n\t Status: "+i.status)
                                Ticketprint.configure(state='disabled')
                                Ticketprint.pack()

                                def CancelTicket():
                                    TicketArr.remove(i)
                                    tk.messagebox.showinfo('Cancellation','TICKET HAS BEEN CANCELLED!!')
                                    CheckStat.destroy()
                                
                                global TickCancel
                                TickCancel=tk.Button(StatTickFrame,command=CancelTicket)
                                TickCancel.place(relx=0.435, rely=0.780, height=34, width=107)
                                TickCancel.configure(activebackground="#72ca4d")
                                TickCancel.configure(activeforeground="#000000")
                                TickCancel.configure(background="#ffc13b")
                                TickCancel.configure(foreground="#1e3d59")
                                TickCancel.configure(cursor="hand2")
                                TickCancel.configure(font="-family {Segoe UI} -size 11 -weight bold")
                                TickCancel.configure(text='Cancel Ticket')
                                break
                            elif i.TickNum > num:
                                Ticketprint.insert(END,'\n\n\n\n')
                                Ticketprint.insert(END,'\t\t\tTicket has been Cancelled!\n\t\t\t Enter Valid Number.')
                                Ticketprint.configure(state='disabled')
                                Ticketprint.pack()
                                break
                            elif num >= ticketno:
                                Ticketprint.insert(END,'\n\n\n\n')
                                Ticketprint.insert(END,'\t\t\tTicket does Not Exist!\n\t\t\t Enter Valid Number.')
                                Ticketprint.configure(state='disabled')
                                Ticketprint.pack()
                                break
                else:
                    tk.messagebox.showinfo('Viewing Ticket','ERROR!! TICKET NUMBER SHOULD BE GREATER THAN 0')

            except ValueError:
                tk.messagebox.showinfo('Viewing Ticket','ERROR!! TICKET NUMBER SHOULD BE AN INTEGER')

    Button1 = tk.Button(CheckStat,command=StatPrintTicket)
    Button1.place(relx=0.469, rely=0.2, height=34, width=47)
    Button1.configure(activebackground="#72ca4d")
    Button1.configure(activeforeground="#000000")
    Button1.configure(background="#ffc13b")
    Button1.configure(foreground="#1e3d59")
    Button1.configure(cursor="hand2")
    Button1.configure(font="-family {Segoe UI} -size 11 -weight bold")
    Button1.configure(text='OK')

#windows for admin,employee and customer
def MainWindowOfAdmin():
    password='apmrms'
    if(Entry1.get()==password):
        tk.messagebox.showinfo('login Result','CONGRATULATIONS!! LOGIN SUCCESSFUL')
        global AdminWind
        AdminWind=tk.Tk()
        AdminWindowLogin.destroy()

        AdminWind.geometry("900x600+160+25")
        AdminWind.minsize(176, 1)
        AdminWind.maxsize(1924, 1050)
        AdminWind.resizable(0, 0)
        AdminWind.title("FUNCTIONALITIES OF ADMINISTRATOR")
        AdminWind.iconbitmap('Employee.ico')
        AdminWind.configure(background="#1e3d59")
        
        Heading = tk.Message(AdminWind)
        Heading.place(relx=0.05, rely=0.0, relheight=0.152, relwidth=0.903)
        Heading.configure(background="#1e3d59")
        Heading.configure(font="-family {Segoe UI} -size 21 -weight bold")
        Heading.configure(foreground="#ffc13b")
        Heading.configure(text="Functionalities of Administrator")
        Heading.configure(width=542)
        
        ButtonAddEmp = tk.Button(AdminWind,command=AddEmployee)
        ButtonAddEmp.place(relx=0.058, rely=0.233, height=62, width=238)
        ButtonAddEmp.configure(activebackground="#ececec")
        ButtonAddEmp.configure(activeforeground="#000000")
        ButtonAddEmp.configure(background="#ffc13b")
        ButtonAddEmp.configure(foreground="#1e3d59")
        ButtonAddEmp.configure(highlightcolor="black")
        ButtonAddEmp.configure(cursor="hand2")
        ButtonAddEmp.configure(font="-family {Segoe UI} -size 13 -weight bold")
        ButtonAddEmp.configure(text="To add Employee")

        ButtonViewEmp = tk.Button(AdminWind,command=ViewEmployees)
        ButtonViewEmp.place(relx=0.058, rely=0.383, height=62, width=238)
        ButtonViewEmp.configure(activebackground="#ececec")
        ButtonViewEmp.configure(activeforeground="#000000")
        ButtonViewEmp.configure(background="#ffc13b")
        ButtonViewEmp.configure(foreground="#1e3d59")
        ButtonViewEmp.configure(font="-family {Segoe UI} -size 13 -weight bold")
        ButtonViewEmp.configure(cursor="hand2")
        ButtonViewEmp.configure(text="View Employees")

        ButtonViewT = tk.Button(AdminWind,command=ViewTrains)
        ButtonViewT.place(relx=0.058, rely=0.533, height=62, width=238)
        ButtonViewT.configure(activebackground="#ececec")
        ButtonViewT.configure(activeforeground="#000000")
        ButtonViewT.configure(background="#ffc13b")
        ButtonViewT.configure(foreground="#1e3d59")
        ButtonViewT.configure(font="-family {Segoe UI} -size 13 -weight bold")
        ButtonViewT.configure(cursor="hand2")
        ButtonViewT.configure(text="View Trains")
        
        ButtonViewS = tk.Button(AdminWind,command=ViewStation)
        ButtonViewS.place(relx=0.058, rely=0.683, height=62, width=238)
        ButtonViewS.configure(activebackground="#ececec")
        ButtonViewS.configure(activeforeground="#000000")
        ButtonViewS.configure(background="#ffc13b")
        ButtonViewS.configure(foreground="#1e3d59")
        ButtonViewS.configure(cursor="hand2")
        ButtonViewS.configure(font="-family {Segoe UI} -size 13 -weight bold")
        ButtonViewS.configure(text="View Stations")

        ButtonViewSchedule = tk.Button(AdminWind,command=ViewScheduleAdmin)
        ButtonViewSchedule.place(relx=0.058, rely=0.833, height=62, width=238)
        ButtonViewSchedule.configure(activebackground="#ececec")
        ButtonViewSchedule.configure(activeforeground="#000000")
        ButtonViewSchedule.configure(background="#ffc13b")
        ButtonViewSchedule.configure(foreground="#1e3d59")
        ButtonViewSchedule.configure(cursor="hand2")
        ButtonViewSchedule.configure(font="-family {Segoe UI} -size 13 -weight bold")
        ButtonViewSchedule.configure(text="View Schedule of All Trains")
        

        global OutputFrame
        OutputFrame=tk.Frame(AdminWind,width=500,height=500,relief='groove',bg="#1e3d59")
        #OutputFrame.pack(side=RIGHT,fill=BOTH,expand=True,padx=50,pady=100)
        OutputFrame.place(x=350,y=80)


    else:
        tk.messagebox.showinfo('Login Result','LOGIN FAILED!:( TRY AGAIN')

def AdminWindow():
    
    global AdminWindowLogin
    AdminWindowLogin=tkinter.Tk()
    AdminWindowLogin.title("Administrator Login")
    AdminWindowLogin.geometry("500x210+370+155")
    AdminWindowLogin.minsize(176, 1)
    AdminWindowLogin.maxsize(1924, 1050)
    AdminWindowLogin.resizable(0, 0)
    AdminWindowLogin.iconbitmap('Login.ico')
    AdminWindowLogin.configure(background="#f5f0e1")

    Label1 = tk.Label(AdminWindowLogin)
    Label1.place(relx=0.025, rely=0.063, height=61, width=474)
    Label1.configure(background="#ff6e40")
    Label1.configure(foreground="#000000")
    Label1.configure(font="-family {Segoe UI} -size 21 -weight bold")
    Label1.configure(text='Administrator Login')

    Message1 = tk.Message(AdminWindowLogin)
    Message1.place(relx=0.107, rely=0.467, height=31, width=128)
    Message1.configure(background="#ff6e40")
    Message1.configure(foreground="#000000")
    Message1.configure(text='Enter Password')
    Message1.configure(font="-family {Segoe UI} -size 12")
    Message1.configure(width=282)

    global Entry1
    Entry1 = tk.Entry(AdminWindowLogin,show="*")
    Entry1.place(relx=0.410, rely=0.467, height=30, relwidth=0.473)
    Entry1.configure(background="white")
    Entry1.configure(font="TkFixedFont")
    Entry1.configure(foreground="#000000")
    
    SubmitButton = tk.Button(AdminWindowLogin,command = MainWindowOfAdmin)
    SubmitButton.place(relx=0.4, rely=0.776, height=34, width=118)
    SubmitButton.configure(text="Submit")
    SubmitButton.configure(activeforeground="#000000")
    SubmitButton.configure(activebackground="#ececec")
    SubmitButton.configure(background="#ffc13b")
    SubmitButton.configure(foreground="#1e3d59")
    SubmitButton.configure(font="-family {Segoe UI} -size 11 -weight bold")
    SubmitButton.configure(cursor="hand2")
    
def MainWindowOfEmployee():
    #generating emplyeee window
    if not idEntry.get():
        tk.messagebox.showinfo('login Result','ENTER ID!')
    elif not idEntry.get():
        tk.messagebox.showinfo('login Result','ENTER PASSWORD!')
    else:
        try:
            ind=int(idEntry.get())
            passw=EmployeeArr[ind-1].password
            if(PassEntry.get()==passw):
                tk.messagebox.showinfo('login Result','CONGRATULATIONS!! LOGIN SUCCESSFUL')
                EmpLoginWindow.destroy()

                global EmployeeWind
                EmployeeWind=tk.Tk()
                EmployeeWind.geometry("884x534+201+61")
                EmployeeWind.minsize(120, 1)
                EmployeeWind.maxsize(1284, 701)
                EmployeeWind.resizable(0,  0)
                EmployeeWind.title("FUNCTIONALITIES OF EMPLOYEE")
                EmployeeWind.iconbitmap('Employee.ico')
                EmployeeWind.configure(background="#1e3d59")


                global EmpFrame
                EmpFrame = tk.Frame(EmployeeWind)
                EmpFrame.place(relx=0.305, rely=0.0, relheight=1.011, relwidth=0.701)
                EmpFrame.configure(relief='flat')
                EmpFrame.configure(borderwidth="2")
                EmpFrame.configure(background="#1e3d59")

                EmpHeading = tk.Label(EmployeeWind)
                EmpHeading.place(relx=0.023, rely=0.037, height=60, width=228)
                EmpHeading.configure(background="#1e3d59")
                EmpHeading.configure(foreground="#ffc13b")
                EmpHeading.configure(font="-family {Segoe UI} -size 18 -weight bold")
                EmpHeading.configure(text="Employee Functions")

                AddStation = tk.Button(EmployeeWind,command=AddStation1)
                AddStation.place(relx=0.063, rely=0.187, height=34, width=147)
                AddStation.configure(activebackground="#ececec")
                AddStation.configure(activeforeground="#fa2e0a")
                AddStation.configure(background="#ffc13b")
                AddStation.configure(foreground="#1e3d59")
                AddStation.configure(cursor="hand2")
                AddStation.configure(font="-family {Segoe UI} -size 11 -weight bold")
                AddStation.configure(text='Add Station')

                AddTrain = tk.Button(EmployeeWind,command=AddTrain1)
                AddTrain.place(relx=0.063, rely=0.375, height=34, width=147)
                AddTrain.configure(activebackground="#ececec")
                AddTrain.configure(activeforeground="#fa2e0a")
                AddTrain.configure(background="#ffc13b")
                AddTrain.configure(foreground="#1e3d59")
                AddTrain.configure(font="-family {Segoe UI} -size 11 -weight bold")
                AddTrain.configure(cursor="hand2")
                AddTrain.configure(text='''Add Train''')

                ViewStaionButton = tk.Button(EmployeeWind,command=ViewStationEmp)
                ViewStaionButton.place(relx=0.063, rely=0.281, height=34, width=147)
                ViewStaionButton.configure(activebackground="#ececec")
                ViewStaionButton.configure(activeforeground="#fa2e0a")
                ViewStaionButton.configure(background="#ffc13b")
                ViewStaionButton.configure(foreground="#1e3d59")
                ViewStaionButton.configure(font="-family {Segoe UI} -size 11 -weight bold")
                ViewStaionButton.configure(cursor="hand2")
                ViewStaionButton.configure(text='View Stations')

                ViewTrain = tk.Button(EmployeeWind,command=ViewTrainsEmp)
                ViewTrain.place(relx=0.063, rely=0.468, height=34, width=147)
                ViewTrain.configure(activebackground="#ececec")
                ViewTrain.configure(activeforeground="#fa2e0a")
                ViewTrain.configure(background="#ffc13b")
                ViewTrain.configure(foreground="#1e3d59")
                ViewTrain.configure(font="-family {Segoe UI} -size 11 -weight bold")
                ViewTrain.configure(cursor="hand2")
                ViewTrain.configure(text='View Trains')

                SetSchedule = tk.Button(EmployeeWind,command=addSchedule1)
                SetSchedule.place(relx=0.063, rely=0.562, height=34, width=147)
                SetSchedule.configure(activebackground="#ececec")
                SetSchedule.configure(activeforeground="#fa2e0a")
                SetSchedule.configure(background="#ffc13b")
                SetSchedule.configure(foreground="#1e3d59")
                SetSchedule.configure(font="-family {Segoe UI} -size 11 -weight bold")
                SetSchedule.configure(cursor="hand2")
                SetSchedule.configure(text='Set Schedule')

                ViewSchedule = tk.Button(EmployeeWind,command=ViewScheduleEmp)
                ViewSchedule.place(relx=0.063, rely=0.655, height=34, width=147)
                ViewSchedule.configure(activebackground="#ececec")
                ViewSchedule.configure(activeforeground="#fa2e0a")
                ViewSchedule.configure(background="#ffc13b")
                ViewSchedule.configure(foreground="#1e3d59")
                ViewSchedule.configure(font="-family {Segoe UI} -size 11 -weight bold")
                ViewSchedule.configure(cursor="hand2")
                ViewSchedule.configure(text='View Schedule')

                ViewTicket = tk.Button(EmployeeWind,command=EmpViewTicket)
                ViewTicket.place(relx=0.063, rely=0.749, height=34, width=147)
                ViewTicket.configure(activebackground="#ececec")
                ViewTicket.configure(activeforeground="#fa2e0a")
                ViewTicket.configure(background="#ffc13b")
                ViewTicket.configure(foreground="#1e3d59")
                ViewTicket.configure(font="-family {Segoe UI} -size 11 -weight bold")
                ViewTicket.configure(cursor="hand2")
                ViewTicket.configure(text='View Tickets')

                ConfirmTicket = tk.Button(EmployeeWind,command=EmpConfirmTicket)
                ConfirmTicket.place(relx=0.063, rely=0.843, height=34, width=147)
                ConfirmTicket.configure(activebackground="#ececec")
                ConfirmTicket.configure(activeforeground="#fa2e0a")
                ConfirmTicket.configure(background="#ffc13b")
                ConfirmTicket.configure(foreground="#1e3d59")
                ConfirmTicket.configure(cursor="hand2")
                ConfirmTicket.configure(font="-family {Segoe UI} -size 11 -weight bold")
                ConfirmTicket.configure(text='Confirm a Ticket')

            else:
                tk.messagebox.showinfo('Login Result','INVALID PASSWORD! :( TRY AGAIN')
        except ValueError:
            tk.messagebox.showinfo('Login Result','ERROR!! ID SHOULD BE AN INTEGER')
        except IndexError:
            tk.messagebox.showinfo('Login Result','ERROR!! ID DOES NOT EXIST')

def EmployeeWindow():
    #generating emplyeee login window
    
    global EmpLoginWindow
    EmpLoginWindow=tk.Tk()
    
    EmpLoginWindow.geometry("500x210+370+155")
    EmpLoginWindow.minsize(120, 1)
    EmpLoginWindow.maxsize(1284, 701)
    EmpLoginWindow.resizable(0, 0)
    EmpLoginWindow.title("Employee Login")
    EmpLoginWindow.configure(background="#f5f0e1")
    EmpLoginWindow.iconbitmap('Login.ico')

    Label1 = tk.Label(EmpLoginWindow)
    Label1.place(relx=0.025, rely=0.063, height=61, width=474)
    Label1.configure(background="#ff6e40")
    Label1.configure(foreground="#000000")
    Label1.configure(font="-family {Segoe UI} -size 21 -weight bold")
    Label1.configure(text='Employee Login')
    
    idLabel = tk.Label(EmpLoginWindow)
    idLabel.place(relx=0.130, rely=0.407, height=31, width=114)
    idLabel.configure(background="#ff6e40")
    idLabel.configure(disabledforeground="#a3a3a3")
    idLabel.configure(foreground="#000000")
    idLabel.configure(font="-family {Segoe UI} -size 12")
    idLabel.configure(text='User ID')

    global idEntry 
    idEntry = tk.Entry(EmpLoginWindow)
    idEntry.place(relx=0.405, rely=0.407, height=30, relwidth=0.473)
    idEntry.configure(background="white")
    idEntry.configure(font="TkFixedFont")
    idEntry.configure(foreground="#000000")

    PassLabel = tk.Label(EmpLoginWindow)
    PassLabel.place(relx=0.130, rely=0.602, height=31, width=114)
    PassLabel.configure(activebackground="#f9f9f9")
    PassLabel.configure(activeforeground="black")
    PassLabel.configure(background="#ff6e40")
    PassLabel.configure(foreground="#000000")
    PassLabel.configure(font="-family {Segoe UI} -size 12")
    PassLabel.configure(text='Password')

    global PassEntry
    PassEntry = tk.Entry(EmpLoginWindow,show="*")
    PassEntry.place(relx=0.405, rely=0.602, height=30, relwidth=0.473)
    PassEntry.configure(background="white")
    PassEntry.configure(font="TkFixedFont")
    PassEntry.configure(foreground="#000000")
    
    EmpLoginSubmit = tk.Button(EmpLoginWindow,command=MainWindowOfEmployee)
    EmpLoginSubmit.place(relx=0.4, rely=0.796, height=34, width=118)
    EmpLoginSubmit.configure(activebackground="#ececec")
    EmpLoginSubmit.configure(activeforeground="#000000")
    EmpLoginSubmit.configure(background="#ffc13b")
    EmpLoginSubmit.configure(foreground="#1e3d59")
    EmpLoginSubmit.configure(cursor="hand2")
    EmpLoginSubmit.configure(font="-family {Segoe UI} -size 11 -weight bold")
    EmpLoginSubmit.configure(text='Submit')

def CustomerService():
    
    global CustomerWindow
    CustomerWindow=tkinter.Tk()
    CustomerWindow.geometry("500x210+370+155")
    CustomerWindow.minsize(116, 1)
    CustomerWindow.maxsize(1370, 750)
    CustomerWindow.resizable(0,  0)
    CustomerWindow.iconbitmap('Employee.ico')
    CustomerWindow.title("Customer Service")
    CustomerWindow.configure(background="#f5f0e1")

    Label1 = tk.Label(CustomerWindow)
    Label1.place(relx=0.025, rely=0.063, height=61, width=474)
    Label1.configure(background="#ff6e40")
    Label1.configure(foreground="#000000")
    Label1.configure(font="-family {Segoe UI} -size 21 -weight bold")
    Label1.configure(text='Customer Services')

    ButtonBook = tk.Button(CustomerWindow,command=BookTicket)
    ButtonBook.place(relx=0.353, rely=0.445, height=34, width=148)
    ButtonBook.configure(activebackground="#ececec")
    ButtonBook.configure(activeforeground="#000000")
    ButtonBook.configure(background="#ffc13b")
    ButtonBook.configure(foreground="#1e3d59")
    ButtonBook.configure(cursor="hand2")
    ButtonBook.configure(font="-family {Segoe UI} -size 11 -weight bold")
    ButtonBook.configure(text='Book ticket')

    ButtonView = tk.Button(CustomerWindow,command=CheckStatus)
    ButtonView.place(relx=0.353, rely=0.700, height=34, width=148)
    ButtonView.configure(activebackground="#ececec")
    ButtonView.configure(activeforeground="#000000")
    ButtonView.configure(background="#ffc13b")
    ButtonView.configure(cursor="hand2")
    ButtonView.configure(foreground="#1e3d59")
    ButtonView.configure(font="-family {Segoe UI} -size 11 -weight bold")
    ButtonView.configure(text='Check ticket status')

#main window
top = tkinter.Tk()
top.title("Railway Management System")
top.geometry("600x450+320+105")
top.minsize(176, 1)
top.maxsize(1924, 1050)
top.resizable(0, 0)
top.configure(background="#ffa781")
top.iconbitmap('Railway.ico')


HeadingLabel=tk.Label(top)
HeadingLabel.place(relx=0.037, rely=0.067, height=72, width=550)
HeadingLabel.configure(font="-family {Segoe UI} -size 18 -weight bold")
HeadingLabel.configure(text="Choose your Role")
HeadingLabel.configure(background="#5b0e2d")
HeadingLabel.configure(foreground="#ffa781")


global Label2
Label2 = tk.Label(top, background="#ffffff", disabledforeground="#a3a3a3", foreground="#000000",borderwidth=1)
Label2.place(relx=0.037, rely=0.297, height=261, width=283)
global _img0
_img0 = tk.PhotoImage(file="./images/VectorImage.png")
Label2.configure(image=_img0)

global AdminWind
global EmployeeWind
global CustomerWindow

button1 = tk.Button(top,command = AdminWindow)
button1.place(relx=0.547, rely=0.297, height=52, width=228)
button1.configure(activebackground="#e71818")
button1.configure(activeforeground="#000000")
button1.configure(background="#5b0e2d")
button1.configure(foreground="#ffa781")
button1.configure(font="-family {Segoe UI} -size 13 -weight bold")
button1.configure(cursor="hand2")
button1.configure(text='Administrator')

Button2 = tk.Button(top,command=EmployeeWindow)
Button2.place(relx=0.547, rely=0.504, height=52, width=228)
Button2.configure(activebackground="#e71818")
Button2.configure(activeforeground="#000000")
Button2.configure(background="#5b0e2d")
Button2.configure(foreground="#ffa781")
Button2.configure(cursor="hand2")
Button2.configure(font="-family {Segoe UI} -size 13 -weight bold")
Button2.configure(text='Employee')

Button3 = tk.Button(top,command=CustomerService)
Button3.place(relx=0.547, rely=0.712, height=52, width=228)
Button3.configure(activebackground="#e71818")
Button3.configure(activeforeground="#000000")
Button3.configure(background="#5b0e2d")
Button3.configure(foreground="#ffa781")
Button3.configure(font="-family {Segoe UI} -size 13 -weight bold")
Button3.configure(cursor="hand2")
Button3.configure(text='Customer')

top.mainloop()





