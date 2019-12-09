##Developed by Christina Germana, Aileen Lu, and Mason Thomas
##Updated: 12/8/19

##Import necessary functions and tools from Tkinter and collections
import tkinter as tk
from collections import Counter as count

##Define item class for instantiating products
class Item:
    def __init__(self, name, price, button):
        self.name = name
        self.price = price
        self.button = button

##Define register class which contains most mechanics for the program
class Register:
    def __init__(self, parent):
        ##Parent attribute
        self.parent = parent
        parent.title('POS System')
        ##tax rate attribute
        self.TAX = 0.08
        ##Instantiate product buttons using item class
        self.items = {"candy bar":Item("Candy bar", 165,tk.Button(root,
                                               text="Candy bar: $1.65", 
                                               command=lambda: self.scan("candy bar"))),
                       "soda":Item( "Soda",115,tk.Button(root, 
                                          text="Soda: $1.15", 
                                          command=lambda: self.scan("soda"))),
                        "chips":Item("Chips",285,tk.Button(root, 
                                          text="Chips: $2.85", 
                                          command=lambda: self.scan("chips"))),
                        "granola bar":Item("Granola bar", 145,tk.Button(root, 
                                          text="Granola bar: $1.45", 
                                          command=lambda: self.scan("granola bar"))),
                        "almond milk":Item("Almond milk", 535, tk.Button(root, 
                                          text="Almond milk: $5.35", 
                                          command=lambda: self.scan("almond milk")))}
        
        ##Series of attributes building GUI using Tkinter
        self.maxNameWidth = max(map(len, (item.name for item in self.items.values()))) + 3
        self.maxPriceWidth = 10
        self.servLabel = tk.Label(root, text='Developed by Aileen Lu, Christina Germana and Mason Thomas\nPlease make your selections below')
        self.servLabel.grid(row=0, column=0, sticky='W')
        for idx,item in enumerate(self.items.values(), start=1):
            item.button.grid(row=idx, column=0, sticky='W')
        self.frame = tk.Frame(root)
        self.frame.grid(row=1, column=1, sticky='W', rowspan=idx+1, columnspan=4)
        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.box = tk.Listbox(self.frame,
                              yscrollcommand=self.scrollbar.set,
                              width=self.maxNameWidth + self.maxPriceWidth + 10, font =('Courier New',12))
        self.scrollbar.config(command=self.box.yview)
        self.box.grid(row=0, column=1, sticky='NS')
        self.scrollbar.grid(row=0, column=2, sticky='NS')
        self.checkoutButton = tk.Button(root, text='Checkout', command=self.checkout)
        self.checkoutButton.grid(row=idx+2, column=1, sticky='W')
        self.newOrderButton = tk.Button(root, text='New Purchase', command=self.newOrder)
        self.newOrderButton.grid(row=idx+2, column=3, sticky='W')
        self.totalLabel = tk.Label(root, text='')
        self.totalLabel.grid(row=idx+2, column=4, sticky='E')
        self.newOrder()
             
    ##Method for updating subtotal and total   
    def update_totals(self):
        self.subtotal = sum(self.items[key].price * value for key,value in self.current_order.items())
        self.taxes = round(self.subtotal * self.TAX)
        self.total = self.subtotal + self.taxes
        self.totalLabel.config(text=f'Subtotal: {self.format_money(self.subtotal)}\nTotal:       {self.format_money(self.total)}')
    ##Method for printing selections in display box    
    def scan(self, code):
        self.current_order[code] += 1
        self.current_codes.append(code)
        name = self.items[code].name
        price = self.format_money(self.items[code].price)
        self.box.insert(tk.END, f'{name:<{self.maxNameWidth}}' + f'{price:>{self.maxPriceWidth+10}}')
        self.box.see(self.box.size()-1)
        self.update_totals()
    ##Method for fornatting money in display    
    def format_money(self, cents):
        d,c = divmod(cents, 100)
        return f'${d}.{c:0>2}'
    ##Method for building checkout mechanics and graphics
    def checkout(self):
        self.totalLabel.config(text=f'TOTAL: {self.format_money(self.total)}\n')
        ##For loop disabling buttons during checkout
        for item in self.items.values():
            item.button.config(state=tk.DISABLED)
        top = tk.Toplevel()
        label = tk.Label(top, text='Input payment amount in accounting format: ')
        label.grid(row=0, column=0)
        text = tk.Entry(top)
        text.grid(row=0, column=1)
        text.focus_set()
        ##Submethod for calculating and displaying change
        def pay(event=None):
            ##Try statement for catching non-integer user payment input
            try:
                ##payment is the amount paid chained to cents for easy arithmatic
                payment = int(text.get().replace('.', ''))
                change = payment - self.total
            except ValueError as e:
                label.config(text=f'Invalid input: {e}')
            ##Nested if for catching insufficient user payment input
            if payment < self.total:
                label.config(text=f'Insufficient change. Transaction cancelled.' )
            else:
                label.config(text=f'Your change is {self.format_money(change)}. Please come again!')
            self.newOrder()
            text.config(state=tk.DISABLED)
            go.config(text='Close', command=top.destroy)
        go = tk.Button(top, text='Pay', command=pay)
        go.grid(row=0, column=2)
    ##Method to reset terminal for a new order    
    def newOrder(self, event=None):
        self.subtotal = self.tax = self.total = 0
        for item in self.items.values():
            item.button.config(state=tk.NORMAL)
        self.box.delete(0, tk.END)
        self.current_order = count()
        self.current_codes = []
        self.update_totals()
        
root = tk.Tk()
app = Register(root)
root.mainloop()
