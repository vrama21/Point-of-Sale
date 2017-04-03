import tkinter as tk
from tkinter import ttk
import time
import numpy as np

LARGE_FONT = ("Verdana", 12)
blueBackground = '#A3A8E4'
grayBackground = '#3C3F41'

ticketBorder = '#000D4B'
ticketBackground = '#C1FFC0'

screenWidth = 1024
screenHeight = 768
screenResolution = '1024x768'

button_font1 = ('times new roman', 30, 'bold')
button_font2 = ('times new roman', 24, 'bold')

def button_click(numbers):
    operator = ""
    text_input = tk.StringVar()
    operator += str(numbers)
    text_input.set(operator)
    # ReadOnlyText()

class MainView(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # tk.Tk.iconbitmap(self, default="icon.ico") """ Icon for Window """
        tk.Tk.wm_title(self, "Swayblade's Restaurant POS")
        FileMenu(self)
        ResizingCanvas(self)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        """ Places all class pages into a dictionary with container as the key. """
        for F in (HomePage, NewOrderPage, CashOutPage, CustomerEntryPage):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="New Order",
                             command=lambda: controller.show_frame(NewOrderPage))
        button1.pack()

        button2 = ttk.Button(self, text="Cash Out",
                             command=lambda: controller.show_frame(CashOutPage))
        button2.pack()
        button3 = ttk.Button(self, text="Customer Entry",
                             command=lambda: controller.show_frame(CustomerEntryPage))
        button3.pack()


class NewOrderPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # topLeft_frame = tk.Frame(self, bg=grayBackground, bd=4, highlightbackground='gray85', relief='sunken')
        # topLeft_frame.place_configure(x=0, y=0, width=screenWidth*.25, height=screenHeight*.15, anchor='nw')

        menu_frame = tk.Frame(self, bg=grayBackground, bd=4, highlightbackground='gray85', relief='sunken')
        menu_frame.place_configure(x=(screenWidth*.25), y=0, width=(screenWidth*.75), height=(screenHeight*.85), anchor='nw')


        ticket_frame = tk.Frame(self,  bg=ticketBackground, relief='sunken')
        ticket_frame.place_configure(x=0, y=0, width=(screenWidth*.25), height=(screenHeight*.85))

        bottom_frame = tk.Frame(self, bg=grayBackground, bd=4, highlightbackground='gray85', relief='sunken')
        bottom_frame.place_configure(x=0, y=screenHeight, width=screenWidth, height=(screenHeight*.15), anchor='sw')

        test = ['test1', 'test2']
        a = ButtonArray(menu_frame, 5, 5, test)
        a.configure(padx=5, pady=5)


    # def menuButtons(self):


class CustomerEntryPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        category_frame = tk.Frame(self, bg=grayBackground)
        category_frame.place_configure(x=0, y=0, width=(screenWidth*.7), height=(screenHeight*.7),
                                       anchor='nw')
        # category_frame.grid(rowspan=20, columnspan=3)
        #
        # bottom_frame = tk.Frame(self, bg=grayBackground, bd=4, highlightbackground='gray85', relief='sunken')
        # bottom_frame.place_configure(x=0, y=screenHeight, width=screenWidth, height=(screenHeight*.15), anchor='sw')
        #
        # button1 = ttk.Button(bottom_frame, text="Back to Home",
        #                      command=lambda: controller.show_frame(HomePage))
        # button1.grid(row=0, column=0)
        #
        # t = SimpleTable(category_frame, 10, 2)
        # t.pack(side='left')
        # t.set(0, 0, "Hello")

        # cat = ["First Name", "Last Name", "Address", "Room Number"]
        # for i, j in enumerate(cat):
        #     cat1 = tk.Label(t, text=j)
        #     cat1.grid(row=i, column=0)


class CashOutPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, bg=grayBackground)

        text_input = tk.StringVar(self)

        """ Frames """
        price_frame = tk.Frame(self, bg='red')
        price_frame.place_configure(x=(screenWidth*.5), y=0, width=(screenWidth*.35), height=100, anchor='n')

        calc_frame = tk.Frame(self, bg=grayBackground)
        calc_frame.place_configure(x=(screenWidth*.5), y=150, width=700, height=600, anchor='n')

        # manager_frame = tk.Frame(self, bg=grayBackground)
        # manager_frame.place_configure(x=0, y=0, width=500, height=150)

        cash_out_frame = tk.Frame(self,  bg=grayBackground)
        cash_out_frame.place_configure(x=screenWidth, y=0, width=(screenWidth*.15), height=(screenHeight*.7), anchor='ne')

        # ticket_frame = tk.Frame(self,  bg=ticketBackground, relief='sunken')
        # ticket_frame.place_configure(x=0, y=150, width=screenWidth/4, height=930)

        bottom_frame = tk.Frame(self, bg=grayBackground, bd=4, highlightbackground='gray85', relief='sunken')
        bottom_frame.place_configure(x=0, y=screenHeight, width=screenWidth, height=(screenHeight*.15), anchor='sw')

        """ Ticket """

        # line_1_qty = tk.Canvas(ticket_frame, width=75, height=20, bd=4, bg=ticketBackground, highlightbackground=ticketBorder)
        # line_1_qty.grid(rowspan=18, row=0, column=0)
        # line_1_listing = tk.Canvas(ticket_frame, width=350, height=20, bd=4, bg=ticketBackground, highlightbackground=ticketBorder)
        # line_1_listing.grid(rowspan=18, row=0, column=1)
        # line_1_price = tk.Canvas(ticket_frame, width=150, height=20, bd=4, bg=ticketBackground, highlightbackground=ticketBorder)
        # line_1_price.grid(rowspan=18, row=0, column=2)

        """ Calculator """
        price_display = tk.Entry(price_frame, font=('times new roman', 72, 'bold'), fg='#FFD10D', bg=grayBackground,
                                 textvariable=text_input, justify='right')
        price_display.grid(row=0, column=0)

        def test():
            calc_buttons = ['7', '8', '9', '4', '5', '6', '1', '2', '3', 'C', 0, '.']
            for i in calc_buttons:
                k = tk.Button(self, text=i, padx=8, pady=4, bd=8, fg='black', font=button_font2)
                k.grid(row=0, column=0)
                k.grid(row=0, column=1)
                k.grid(row=0, column=2)



            # for i, text in enumerate(calc_buttons):
            #     k = tk.Button(self, text=text, padx=8, pady=4, bd=8, fg='black', font=button_font2)
            #     k.grid(row=i, column=i)


        # for b in calc_buttons:
        #     calcbtn = tk.Button(calc_frame, text=b, fg='black', font=button_font2,
        #                         command=lambda: Calculator.button_clear_display())
        #     # calc_grid_1 = [j for j in range(3)]
        #     # rowval = [j for j in range(2)]
        #     for x in rowval:
        #         calcbtn.grid(column=x)




        # ButtonClear = tk.Button(calc_frame, padx=8, pady=4, bd=8, fg='black', font=button_font2,
        #                         text="C", bg='light gray',
        #                         command=lambda: Calculator.button_clear_display()).grid(row=5, column=0)
        # ButtonDec   = tk.Button(calc_frame, padx=8, pady=4, bd=8, fg='black', font=button_font2,
        #                         text=".", bg='light gray',
        #                         command=lambda: Calculator.button_decimal()).grid(row=5, column=2)
        # Button0 = tk.Button(calc_frame, padx=8, pady=4, bd=8, fg='black', font=button_font2,
        #                     text="0", bg='light gray',
        #                     command=lambda: button_click(0).grid(row=5, column=1))
        # Button1 = tk.Button(calc_frame, width=2, height=1, bd=8, fg='black', font=button_font2,
        #                     text="1", bg='light gray',
        #                     command=lambda: button_click(1)).grid(row=4, column=0),
        # Button2 = tk.Button(calc_frame, padx=8, pady=4, bd=8, fg='black', font=button_font2,
        #                     text="2", bg='light gray',
        #                     command=lambda: button_click(2)).grid(row=4, column=1)
        # Button3 = tk.Button(calc_frame, padx=8, pady=4, bd=8, fg='black', font=button_font2,
        #                     text="3", bg='light gray',
        #                     command=lambda: button_click(3)).grid(row=4, column=2)
        # Button4 = tk.Button(calc_frame, padx=8, pady=4, bd=8, fg='black', font=button_font2,
        #                     text="4", bg='light gray',
        #                     command=lambda: button_click(4)).grid(row=3, column=0)
        # Button5 = tk.Button(calc_frame, padx=8, pady=4, bd=8, fg='black', font=button_font2,
        #                     text="5", bg='light gray',
        #                     command=lambda: button_click(5)).grid(row=3, column=1)
        # Button6 = tk.Button(calc_frame, padx=8, pady=4, bd=8, fg='black', font=button_font2,
        #                     text="6", bg='light gray',
        #                     command=lambda: button_click(6)).grid(row=3, column=2)
        # Button7 = tk.Button(calc_frame, padx=8, pady=4, bd=8, fg='black', font=button_font2,
        #                     text="7", bg='light gray',
        #                     command=lambda: button_click(7)).grid(row=2, column=0)
        # Button8 = tk.Button(calc_frame, padx=8, pady=4, bd=8, fg='black', font=button_font2,
        #                     text="8", bg='light gray',
        #                     command=lambda: button_click(8)).grid(row=2, column=1)
        # Button9 = tk.Button(calc_frame, padx=8, pady=4, bd=8, fg='black', font=button_font2,
        #                     text="9", bg='light gray',
        #                     command=lambda: button_click(9)).grid(row=2, column=2)


        """ Cash Out Buttons """
        cash_out_5 = tk.Button(cash_out_frame, padx=8, pady=4, bd=8, fg='black', font=button_font1,
                               text="$5", bg='light gray', width=5,
                               command=lambda: button_cash_out())
        cash_out_5.grid(row=0, column=0)

        cash_out_10 = tk.Button(cash_out_frame, padx=8, pady=4, bd=8, fg='black', font=button_font1,
                                text="$10", bg='light gray', width=5,
                                command=lambda: button_cash_out())
        cash_out_10.grid(row=1, column=0)

        cash_out_20 = tk.Button(cash_out_frame, padx=8, pady=4, bd=8, fg='black', font=button_font1,
                                text="$20", bg='light gray', width=5,
                                command=lambda: button_cash_out())
        cash_out_20.grid(row=2, column=0)

        cash_out_50 = tk.Button(cash_out_frame, padx=8, pady=4, bd=8, fg='black', font=button_font1,
                                text="$50", bg='light gray', width=5,
                                command=lambda: button_cash_out())
        cash_out_50.grid(row=3, column=0)

        cash_out_100 = tk.Button(cash_out_frame, padx=8, pady=4, bd=8, fg='black', font=button_font1,
                                 text="$100", bg='light gray', width=5,
                                 command=lambda: button_cash_out())
        cash_out_100.grid(row=4, column=0)


        """ Bottom Bar Buttons """
        ButtonBackToHome = tk.Button(bottom_frame, padx=8, pady=4, fg='black', font=button_font1,
                                     text="Back to Home",
                                     command=lambda: controller.show_frame(HomePage))
        ButtonBackToHome.grid(row=0, column=0)

        ButtonManager = tk.Button(bottom_frame, padx=8, pady=4, fg='black', font=button_font1,
                                  text="Manager", bg='light gray',
                                  command=lambda: button_click())
        ButtonManager.grid(row=0, column=1)

        ButtonReceipt = tk.Button(bottom_frame, padx=8, pady=4, fg='black', font=button_font1,
                                  text="Receipt", bg='light gray',
                                  command=lambda: button_click())
        ButtonReceipt.grid(row=0, column=2)

        ButtonNoSale = tk.Button(bottom_frame, padx=8, pady=4, fg='black', font=button_font1,
                                 text="No Sale", bg='light gray',
                                 command=lambda: button_cash_out())
        ButtonNoSale.grid(row=0, column=3)

        ButtonEditTicket = tk.Button(bottom_frame, padx=8, pady=4, fg='black', font=button_font1,
                                     text="Edit Ticket", bg='light gray',
                                     command=lambda: button_cash_out())
        ButtonEditTicket.grid(row=0, column=4)

        ButtonFinished = tk.Button(bottom_frame, padx=8, pady=4, fg='black', font=button_font1,
                                   text="Finished", bg='light gray',
                                   command=lambda: button_cash_out())
        ButtonFinished.grid(row=0, column=5)


class FileMenu:
    def __init__(self, master):
        menu_bar = tk.Menu(master)
        master.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New...")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=quit)

        edit_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)

        window_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Window", menu=window_menu)
        window_menu.add_command(label="Screen Resolution")
        window_menu.add_cascade()


        help_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About")


class ButtonArray(tk.Frame):
    def __init__(self, parent, row, column, text):
        tk.Frame.__init__(self, parent)
        parent = parent

        parent.grid_rowconfigure(1, weight=1)
        parent.grid_columnconfigure(1, weight=1)

        frame = tk.Frame(parent)
        frame.pack(fill='y', padx=5, pady=5)

        c = []
        c.append(text)

        a = np.zeros((row, column))
        for i in range(0, a.shape[0]):
            for j in range(0, a.shape[1]):
                b = tk.Button(frame, font=button_font1, text=c)
                b.grid(row=i, column=j)



class SimpleTable(tk.Frame):
    def __init__(self, parent, rows, columns):
        # use black background so it "peeks through" to
        # form grid lines
        tk.Frame.__init__(self, parent, background="black")
        entry = ["First Name", "Last Name", "Address"]
        self._widgets = []
        for row in range(rows):
            current_row = []
            for column in range(columns):
                label = tk.Label(self, text=self.__format__("First Name"),
                                 borderwidth=0, width=10)
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                current_row.append(label)
            self._widgets.append(current_row)

        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)

    def set(self, row, column, value):
        widget = self._widgets[row][column]
        widget.configure(text=value)


class ResizingCanvas(tk.Canvas):
    def __init__(self, parent, **kwargs):
        tk.Canvas.__init__(self, parent, **kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self,event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width)/self.width
        hscale = float(event.height)/self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all", 0, 0, wscale, hscale)


class ReadOnlyText(tk.Text):
    def __init__(self, *args, **kwargs):
        tk.Text.__init__(self, *args, **kwargs)
        tk.Text.configure(state='normal')
        tk.Text.insert('test')
        tk.Text.configure(state='disabled')


# class Calculator(tk.Frame):
#     operator = ""
#     text_input = tk.StringVar()
#
#     def button_click(numbers):
#         operator += str(numbers)
#         text_input.set(operator)
#         # ReadOnlyText()
#
#     def button_clear_display():
#         global operator
#         operator = ""
#         text_input.set("0.00")
#
#
#     def button_decimal():
#         global operator
#         operator = "."
#         text_input.set(operator)

if __name__ == "__main__":
    app = MainView()
    app.geometry(screenResolution)
    app.mainloop()



