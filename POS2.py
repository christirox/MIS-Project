#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 21:50:47 2019

@author: christina
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 20:10:05 2019

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
        self.money = 0
        self. items = {"candy bar":Item("candy bar", 165,tk.Button(root,
                                               text="candy bar", 
                                               command=lambda: self.scan("cand bar"))),
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
        self.server_label = tk.Label(root, text="Cashier: Christina")
        self.server_label.grid(row=0, column=0, sticky = 'w')
        self.time_label= tk.Label(root, text='')
        self.time_label.grid(row=0, column=1, sticky='E')
        for idx,item in enumerate(self.items.values(), start=1):  
            item.button.grid(row=idx, column=0, sticky = 'w')
        self.frame = tk.Frame(root)
        self.frame.grid(row=1, column=1, rowspan = 6)
        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.box = tk.Listbox(self.frame, yscrollcommand=self.scrollbar.set, width=25)
        self.scrollbar.config(command=self.box.yview)
        self.box.grid(row=0, column=1, sticky= 'NS')
        self.current_order = count()
        self.tick()
    def scan(self, item):
        pass
    def tick(self):
        self.time_label.config(text=str(datetime.datetime.now()).rpartition('.')[0])
        self.parent.after(1000,self.tick)








root= tk.Tk()
app = Register(root)
root.mainloop()