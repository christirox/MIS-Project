#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 16:28:04 2019

@author: christina
"""


import tkinter as tk
from collections import Counter as count
import datetime

class Item:
    def __init__(self, name, price, button):
        self.name = name
        self.price= price
        self.button= button

class Register:
    def __init__(self, parent):
        self.parent = parent
        self.register = 0
        self.  items = {"candy bar":Item("candy bar", 165,tk.Button(root,
                                               text="candy bar", 
                                               command=lambda: self.scan("candy bar"))),
                       "soda":Item( "soda",115,tk.Button(root, 
                                          text="soda", 
                                          command=lambda: self.scan("soda"))),
                        "chips":Item("chips",285,tk.Button(root, 
                                          text="chips", 
                                          command=lambda: self.scan("chips"))),
                        "granola bar":Item("granola bar", 145,tk.Button(root, 
                                          text="granola bar", 
                                          command=lambda: self.scan("granola bar"))),
                        "almond milk":Item("almond milk", 535, tk.Button(root, 
                                          text="almond milk", 
                                          command=lambda: self.scan("almond milk")))}
        self.MAX_NAME_WIDTH=max(map(len,(item.name for item in self.items.values()))) +3
        self.MAX_PRICE_WIDTH=10
        self.server_label = tk.Label(root, text="Cashier: Christina")
        self.server_label.grid(row=0, column=0, sticky = 'w')
        self.time_label= tk.Label(root, text='')
        self.time_label.grid(row=0, column=1, sticky='E')
        for idx,item in enumerate(self.items.values(), start=1):  
            item.button.grid(row=idx, column=0, sticky = 'w')
        self.frame = tk.Frame(root)
        self.frame.grid(row=1, column=1, rowspan = 6)
        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.box = tk.Listbox(self.frame, yscrollcommand=self.scrollbar.set, width=self.MAX_NAME_WIDTH+10, font =('Courier New',12))
        self.scrollbar.config(command=self.box.yview)
        self.box.grid(row=0, column=1, sticky= 'NS')
        self.current_order = count()
        self.tick()
    def scan(self, code):
        self.current_order[code]+=1
        dollars, cents=divmod(self.items[code].price, 100)
        self.box.insert(tk.END, self.items[code].name.ljust(self.MAX_NAME_WIDTH)+ f'${dollars}.{cents}'.rjust(self.MAX_PRICE_WIDTH))          
        self.box.see(self.box.size()-1)
    def checkout(self):
        pass
    def tick(self):
        self.time_label.config(text=str(datetime.datetime.now()).rpartition('.')[0])
        self.parent.after(1000,self.tick)
'''
denominations = ('Fifties', 'Twenties', 'Tens', 'Fives', 'Ones', 'Quarters', 'Dimes', 'Nickels', 'Pennies') 
denominations_dict = {}
dollars, cents = divmod(change, 100)
denominations_dict['Fifties'], dollars = divmod(dollars, 50)
denominations_dict['Twenties'], dollars = divmod(dollars, 20)
denominations_dict['Tens'], dollars = divmod(dollars, 10)
denominations_dict['Fives'], denominations_dict['Ones'] = divmod(dollars, 5)
denominations_dict['Quarters'], cents = divmod(cents, 10)
denominations_dict['Nickels'], denominations_dict['Pennies']= divmod(cents,5)
'''





root= tk.Tk()
app = Register(root)
root.mainloop()