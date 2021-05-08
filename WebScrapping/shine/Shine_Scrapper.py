# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 02:01:08 2020

@author: Rohyth_Ratawal
"""

from tkinter import *
from tkinter import ttk
import tkinter
from tkinter.filedialog import askopenfilename
import os
from datetime import datetime
from tkcalendar import DateEntry
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
import pandas as pd
from time  import sleep
import threading

class MyApp():
    
    def __init__(self):
        
        window = Tk()
        window.title('My Shine Scrapper')
        window.geometry('400x250')
        window.resizable(0,0)
        
        Tab_control = ttk.Notebook(window)
        
        tab1 = ttk.Frame(Tab_control)
        tab2 = ttk.Frame(Tab_control)
        
        Tab_control.add(tab1, text='   Tool  ')
        Tab_control.add(tab2, text='  Config  ')
        
        self.fields ={}
        
        Usr = Label(tab1, text='UserName/Email  :').place(x=10,y=10)
        Pwd = Label(tab1, text='Password               :').place(x=10,y=40)
        Otp = Label(tab1, text='OTP                         :').place(x=10,y=70)
        
        self.fields['user'] = Entry(tab1)
        self.fields['user'].place(x=120,y=10,height=25,width=270)
        self.fields['user'].insert(0,'basicsofimmigrationc')    
        
        self.fields['pass'] = Entry(tab1)
        self.fields['pass'].place(x=120,y=40,height=25,width=270)
        self.fields['pass'].insert(0,'Basics#2115') 
        self.fields['pass'].config(show="*")
        
        
        self.fields['Otp'] = Entry(tab1)
        self.fields['Otp'].place(x=120,y=70,height=25,width=270)
        
        
        
        def webD():
            drv = askopenfilename()
            if drv:
                self.fields['webdriver'].delete(0,END)
                self.fields['webdriver'].insert(0,drv)
        
        def DB_select():
            drv = askopenfilename()
            if drv:
                self.fields['out_db'].delete(0,END)
                self.fields['out_db'].insert(0,drv)
                
        def reset():
            self.fields['user'].delete(0,END)
            self.fields['pass'].delete(0,END)
            self.fields['Otp'].delete(0,END)
            
            tkinter.messagebox.showinfo(title='Reset', message='Reset Complete !!!')
        
        
        def Clear():
            self.fields['webdriver'].delete(0,END)
            self.fields['out_db'].delete(0,END)
        
        
        
        def Login_shine():
            
            usr = self.fields['user'].get()
            pwd = self.fields['pass'].get()
            
          
            
            browser.get('https://recruiter.shine.com/')
            
            browser.find_element_by_xpath('//*[@id="loginbutton"]').click()
            browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[3]/div[1]/div/div/form/ul/li[1]/input').send_keys(usr)
            browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[3]/div[1]/div/div/form/ul/li[2]/input').send_keys(pwd)
            browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[3]/div[1]/div/div/form/ul/li[3]/input').click()
            
        
        def Downloading():
            
            browser.get('https://recruiter.shine.com/myshine/managejobs')
            Base = {
                    'Category':[],
                    'link':[],
                    'status':[]
                    }
            
            df = pd.DataFrame(Base)
            
            #Total_li = browser.find_element_by_xpath('/html/body/div[2]/div[2]/app/div/app-managejobs/div/div[2]/div[2]/div/div[2]')
            
            Page_count = browser.find_element_by_xpath('/html/body/div[2]/div[2]/app/div/app-managejobs/div/div[2]/div[2]/div/div[1]/div/div/div/div[2]/ul/li[1]').get_attribute('innerHTML')
            Page_count = int(Page_count.split(' ')[2])
            
            for y in range(0,Page_count):
                print('Page ', y )
                for x in range(2,12):
                    C = browser.find_element_by_xpath('/html/body/div[2]/div[2]/app/div/app-managejobs/div/div[2]/div[2]/div/div[2]/ul/li['+ str(x) +']/span[2]/a').get_attribute('innerHTML')
                    L = browser.find_element_by_xpath('/html/body/div[2]/div[2]/app/div/app-managejobs/div/div[2]/div[2]/div/div[2]/ul/li['+ str(x) +']/span[2]/a').get_attribute('href')
                    if x ==11:
                        S = browser.find_element_by_xpath('/html/body/div[2]/div[2]/app/div/app-managejobs/div/div[2]/div[2]/div/div[2]/ul/li['+ str(x) +']/span[4]/span[1]/span/span[1]').get_attribute('innerHTML')
                    else:
                        S = browser.find_element_by_xpath('/html/body/div[2]/div[2]/app/div/app-managejobs/div/div[2]/div[2]/div/div[2]/ul/li['+ str(x) +']/span[4]/span[1]/span').get_attribute('innerHTML')
                    
                    df = df.append({'Category':C,'link':L, 'status':S}, ignore_index=True)
                
                browser.find_element_by_class_name('nxt').click()

        
        Sdate = Label(tab1, text='Start Date :')
        Sdate.place(x=75,y=105)

        cal1 = DateEntry(tab1, width=20, background='darkblue', foreground='white', borderwidth=2)
        cal1.place(x=30, y=125)
        
        Edate = Label(tab1, text='End Date :')
        Edate.place(x=275,y=105)

        cal2 = DateEntry(tab1, width=20, background='darkblue', foreground='white', borderwidth=2)
        cal2.place(x=230, y=125)
        
        web_driver = Button(tab2, text='Select FireFox Webdriver ',command=webD)
        web_driver.place(x=10,y=10, height=30,width=380)
        
        self.fields['webdriver'] = Entry(tab2)
        self.fields['webdriver'].place(x=10,y=50,height=30,width=380)
        self.fields['webdriver'].insert(0,'D:\Automations\Rohyth Work ( DO NOT TOUCH)\geckodriver.exe')
        
        Output_db = Button(tab2, text='Select Master Database ',command=DB_select)
        Output_db.place(x=10,y=90,height=30, width=380)
        
        self.fields['out_db'] = Entry(tab2)
        self.fields['out_db'].place(x=10,y=130,height=30,width=380)
        
        Login = Button(tab1, text='Login',command=Login_shine).place(x=10,y=160, width=185)
        Download = Button(tab1, text='Download',command=Downloading).place(x=205,y=160, width=185)
        
        Reset = Button(tab1, text='Reset fields',command=reset)
        Reset.place(x=10,y=190, width=380)
        
        Clear_All = Button(tab2, text='Clear All',command=Clear)
        Clear_All.place(x=10,y=170,height=30, width=380)
        
        
        
        #Run ---------------------------
        os.system("taskkill /im firefox.exe /f")
        wd = self.fields['webdriver'].get()    
        global browser
        browser = webdriver.Firefox(executable_path=wd)
        
        Tab_control.pack(expand=1,fill='both')
        window.mainloop()
        
    
if __name__ == "__main__":        
    MyApp()