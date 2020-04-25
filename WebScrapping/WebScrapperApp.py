from tkinter import *
from datetime import datetime
import requests

class MyApp:
  def __init__(self):
    window = Tk()
    window.title('WebScrapping Application')
    window.geometry("350x200")
    frame = Frame(window)
    frame.pack()
    
    self.fields = {}
    
    l = Label(frame, text="Enter Url:")
    l.grid(row=2, column=0)
    self.fields['name'] = Entry(frame)
    self.fields['name'].grid(row=2, column=1)
     
    l = Label(frame, text="Last Scrapped On:")
    l.grid(row=4, column=0)
    self.fields['email'] = Entry(frame)
    self.fields['email'].grid(row=4, column=1)
    self.fields['email'].insert(0,'No scrapping done yet')
    submitbtn = Button(frame, text="Start Scrapping", command=self.do_insert)
    submitbtn.grid(row=11, column=0)
    
    clearbtn = Button(frame, text="Clear All Fields", command=self.do_clear)
    clearbtn.grid(row=11, column=1)
    
    window.mainloop()
 
  def do_clear(self):
    self.fields['name'].delete(0,END)
    self.fields['email'].delete(0,END)
 
  def do_insert(self):
    
    url = self.fields['name'].get()
    if url == '':
        messagebox.showerror("Error", "Please enter a Url to proceed ")
    elif url[0:3] == 'www':
        url = 'http://' + url
        fileN = 'Scrapped file ' + str(datetime.now().date()) + str(datetime.now().time()).replace(':','_') 
        fileN = fileN.replace('.','_') + '.html'
        print(fileN)
        with requests.session() as c:
            f1 = c.get(url,verify=False)
            w1 = open(fileN,"wb").write(f1.content)
            messagebox.showinfo('Success', 'File Generated. Please check')
            self.fields['email'].delete(0,END)
            self.fields['email'].insert(0,datetime.now().date())
    else:
    
        fileN = 'Scrapped file ' + str(datetime.now().date()) + str(datetime.now().time()).replace(':','_') 
        fileN = fileN.replace('.','_') + '.html'
        print(fileN)
        with requests.session() as c:
            f1 = c.get(url,verify=False)
            w1 = open(fileN,"wb").write(f1.content)
            messagebox.showinfo('Success', 'File Generated. Please check')
            self.fields['email'].delete(0,END)
            self.fields['email'].insert(0,datetime.now().date())
        
if __name__=="__main__":
    MyApp()