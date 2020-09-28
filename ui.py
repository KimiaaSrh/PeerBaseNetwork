import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 600, height = 600,  relief = 'raised')
canvas1.pack()
###
label1 = tk.Label(root, text='Enter the IP you wanna trust to:')
label1.config(font=('helvetica', 10))
canvas1.create_window(150, 400, window=label1)


entry1 = tk.Entry (root)
canvas1.create_window(150, 450, window=entry1)
###
label2 = tk.Label(root, text='Enter the title you wanna search:')
label2.config(font=('helvetica', 10))
canvas1.create_window(150, 250, window=label2)

entry2 = tk.Entry (root)
canvas1.create_window(150, 300, window=entry2)
###

label3 = tk.Label(root, text='Spread this message :')
label3.config(font=('helvetica', 10))
canvas1.create_window(150, 90, window=label3)

label4 = tk.Label(root, text='Enter the title :')
label4.config(font=('helvetica', 10))
canvas1.create_window(100, 120, window=label4)

label5 = tk.Label(root, text='Enter the text :')
label5.config(font=('helvetica', 10))
canvas1.create_window(200, 120, window=label5)


entry3 = tk.Entry (root)
padx = 10
pady = 10
entry3.pack(padx=padx, pady=pady)
canvas1.create_window(100, 150, window=entry3)

entry4 = tk.Entry (root)
canvas1.create_window(200, 150, window=entry4)

def getIpAddressToTrust():
    x1 = entry1.get()
def getWantedNews():
    x2 = entry2.get()
def spreadNews():
    x3 = entry3.get()
    x4 = entry4.get()
    strToSpread=x3+"%"+x4
    print(strToSpread)

button1 = tk.Button(text='Trust to this ip', command=getIpAddressToTrust, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(400, 450, window=button1)

button2 = tk.Button(text='Get News', command=getWantedNews, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(400, 300, window=button2)

button3 = tk.Button(text='Spread News', command=spreadNews, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(400, 150, window=button3)

root.mainloop()
