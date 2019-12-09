import tkinter as tk
from collections import Counter as count

class Item:
    def __init__(self, name, price, button):
        self.name = name
        self.price = price
        self.button = button

class Register:
    def __init__(self, parent):
        self.parent = parent
        parent.title('POS System')
        self.TAX = 0.08
        self.  items = {"candy bar":Item("Candy bar", 165,tk.Button(root,
                                               text="Candy bar", 
                                               command=lambda: self.scan("candy bar"))),
                       "soda":Item( "Soda",115,tk.Button(root, 
                                          text="Soda", 
                                          command=lambda: self.scan("soda"))),
                        "chips":Item("Chips",285,tk.Button(root, 
                                          text="Chips", 
                                          command=lambda: self.scan("chips"))),
                        "granola bar":Item("Granola bar", 145,tk.Button(root, 
                                          text="Granola bar", 
                                          command=lambda: self.scan("granola bar"))),
                        "almond milk":Item("Almond milk", 535, tk.Button(root, 
                                          text="Almond milk", 
                                          command=lambda: self.scan("almond milk")))}
        self.MAX_NAME_WIDTH = max(map(len, (item.name for item in self.items.values()))) + 3
        self.MAX_PRICE_WIDTH = 10
        self.server_label = tk.Label(root, text='Hello, your cashier is Randall Smith!')
        self.server_label.grid(row=0, column=0, sticky='W')
        for idx,item in enumerate(self.items.values(), start=1):
            item.button.grid(row=idx, column=0, sticky='W')
        self.frame = tk.Frame(root)
        self.frame.grid(row=1, column=1, sticky='W', rowspan=idx+1, columnspan=4)
        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.box = tk.Listbox(self.frame,
                              yscrollcommand=self.scrollbar.set,
                              width=self.MAX_NAME_WIDTH + self.MAX_PRICE_WIDTH + 10)
        self.scrollbar.config(command=self.box.yview)
        self.box.grid(row=0, column=1, sticky='NS')
        self.scrollbar.grid(row=0, column=2, sticky='NS')
        self.box.bind("<Double-Button-1>", self.modify_item)
        self.checkout_button = tk.Button(root, text='Checkout', command=self.checkout)
        self.checkout_button.grid(row=idx+2, column=1, sticky='W')
        self.new_order_button = tk.Button(root, text='New Purchase', command=self.new_order)
        self.new_order_button.grid(row=idx+2, column=3, sticky='W')
        self.total_label = tk.Label(root, text='')
        self.total_label.grid(row=idx+2, column=4, sticky='E')
        self.new_order()
    def modify_item(self, event=None):
        top = tk.Toplevel()
        entry = tk.Entry(top)
        entry.pack()
        entry.focus_set()
        def set_new_quantity():
            new_value = int(entry.get())
            idx = self.box.index(tk.ACTIVE)
            self.box.delete(idx)
            code = self.current_codes.pop(idx)
            self.current_order[code] -= 1
            for i in range(new_value):
                self.scan(code)
            top.destroy()
            self.update_totals()
        confirm = tk.Button(top, text='OK', command=set_new_quantity)
        confirm.pack()
    def update_totals(self):
        self.subtotal = sum(self.items[key].price * value for key,value in self.current_order.items())
        self.tax = round(self.subtotal * self.TAX)
        self.total = self.subtotal + self.tax
        self.total_label.config(text=f'{self.format_money(self.subtotal):>25}\n{self.format_money(self.total):>25}')
    def scan(self, code):
        self.current_order[code] += 1
        self.current_codes.append(code)
        name = self.items[code].name
        price = self.format_money(self.items[code].price)
        self.box.insert(tk.END, f'{name:<{self.MAX_NAME_WIDTH}}' + f'{price:>{self.MAX_PRICE_WIDTH+10}}')
        self.box.see(self.box.size()-1)
        self.update_totals()
    def format_money(self, cents):
        d,c = divmod(cents, 100)
        return f'${d}.{c:0>2}'
    def checkout(self):
        self.total_label.config(text=f'TOTAL: {self.format_money(self.total)}\n')
        for item in self.items.values():
            item.button.config(state=tk.DISABLED)
        top = tk.Toplevel()
        label = tk.Label(top, text='Input money in accounting format: ')
        label.grid(row=0, column=0)
        text = tk.Entry(top)
        text.grid(row=0, column=1)
        text.focus_set()
        def pay(event=None):
            # tender is integer of pennies
            tender = int(text.get().replace('.', ''))
            if tender >= self.total:
                change = tender - self.total
                label.config(text=f'Your change is {self.format_money(change)}. Please come again!')
            elif tender < self.total:
                label.config(text=f'Insufficient payment. Transaction cancelled.')
            self.new_order()
            text.config(state=tk.DISABLED)
            go.config(text='Close', command=top.destroy)
        go = tk.Button(top, text='Pay', command=pay)
        go.grid(row=0, column=2)
    def new_order(self, event=None):
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

root= tk.Tk()
app = Register(root)
root.mainloop()
