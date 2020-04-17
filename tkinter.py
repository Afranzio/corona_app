import tkinter as tk
import pandas as pd

window = tk.Tk()

window.geometry("400x400")

title = window.title("Corona Affect")


frame=tk.Frame(window,bg='skyblue')
frame.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)

e=tk.Entry(frame,bg="lightgrey",fg="gray", justify="center")
e.place(relx=0.15,rely=0.05,width=200,height=25)    

out = tk.Label(frame)
out.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.6)

def click():
    cun=e.get().upper()
    c=tk.Label(out,text=cun,font=300)
    c.grid(row=3,column=1)
    df=pd.read_csv(r"C:\Users\Afranzio\Desktop\Corona Virus Uptodate\novel-corona-virus-2019-17-04-2020\covid_19_data.csv")
    data=df[df["Country/Region"]==cun.title()][["Confirmed","Deaths","Recovered"]].max()
    con=tk.Label(out,text=int(data["Confirmed"]))
    det=tk.Label(out,text=int(data["Deaths"]))
    rec=tk.Label(out,text=int(data["Recovered"]))
    confirmed=tk.Label(out,text="Confirmed")
    Deaths=tk.Label(out,text="Deaths")
    Recovered=tk.Label(out,text="Recovered")
    confirmed.grid(row=4,column=0)
    Deaths.grid(row=5,column=0)
    Recovered.grid(row=6,column=0)
    con.grid(row=4,column=2)
    det.grid(row=5,column=2)
    rec.grid(row=6,column=2)  
   
def clear():
    for i in out:
        i.destroy()

mylable = tk.Button(frame,text="Search..", bg="grey",fg="white",command=click())
mylable.place(relx=0.80,rely=0.05)


clr = tk.Button(frame,text="Clear",command=clear())
clr.place(rely=0.85,relx=0.75)

quti = tk.Button(frame,text="Exit Program",command=window.quit,justify="center")
quti.place(rely=0.85,relx=0.25)


window.mainloop()