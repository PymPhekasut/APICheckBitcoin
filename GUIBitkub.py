#BitkubChecker.py


import requests
from pprint import pprint
import time

API_HOST ='https://api.bitkub.com'
mycoin = ['THB_BTC','THB_ETH','THB_DOGE']


def CheckPrice():

    response = requests.get(API_HOST + '/api/market/ticker')
    result = response.json()

    #pprint(result)


    alltext = ''
    
    for c in mycoin:
        sym = c
        data = result[sym]
        last = data['last']
        print(data)
        print(sym,last)
        pchange = data['percentChange']
        text = ' {} price: {:,.3f} ({})'.format(sym,last,pchange)
        alltext += text + '\n' #alltext = alltext + text
        
    #print(type(last))
    v_result.set(alltext)    
    print('--------------')
    R1.after(100,CheckPrice)
    #.after = Refresh R1 every 200 ms



################GUI###################

from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.geometry ('500x300')
GUI.title('Checking Bitcoin price from Bitkub')

FONT1 = ('Angsana New',30)

L1 = ttk.Label(GUI,text='Lastest price on Bitkub')
L1.pack()

#B1= ttk.Button(GUI,text='Check!',command=CheckPrice)
#B1.pack(ipadx=20,ipady=10)

v_result = StringVar()
v_result.set('------------result-----------')
R1 = ttk.Label(textvariable=v_result,font=FONT1)
R1.pack()


#run function everytime when open
CheckPrice()
GUI.mainloop()


