from tkinter import *

root = Tk()
root.title('Developed by Emmanuel Frederique')
root.config(bg='#65aee4')
root.geometry("350x450")

font_style = 'Consolas 12'

entry = Entry(root, font=font_style, relief='flat')
entry.pack(padx='10', pady='10')

entry2 = Entry(root, font=font_style, relief='flat')
entry2.pack(padx='10', pady='10')

label = Label(root, font=font_style, relief='flat')
label.pack(padx='10', pady='10')


def get_perc1():
    """The function takes two numbers. the first one is the part, 
    the second one is the total, it tells the user what percentage 
    of the second number the first one represents"""
    num1 = float(entry.get())
    num2 = float(entry2.get())
    result = float(num1 * 100) / float(num2)
    label['text'] = str(num1) + ' es el ' + str(result) + '% de ' + str(num2)


button = Button(root, text='GET PERCENTAGE', font=font_style, relief='flat', command=lambda: get_perc1())
button.pack(padx='10', pady='10')

# two entries to take numbers and a label to display the result
entry3 = Entry(root, relief='flat', font=font_style)
entry3.pack(padx='10', pady='10')

entry4 = Entry(root, font=font_style, relief='flat')
entry4.pack(padx='10', pady='10')

label2 = Label(root, font=font_style, relief='flat')
label2.pack(padx='10', pady='10')


def get_perc2():
    """this function takes two numbers. The first one is the percentage to find, 
    and the second one is the total to find the percentage of."""
    num3 = float(entry3.get())
    num4 = float(entry4.get())
    result2 = float(num3 * num4) / 100
    label2['text'] = 'El ' + str(num3) + '% de ' + str(num4) + ' es ' + str(result2)


button = Button(root, text='GET PERCENTAGE', font=font_style, relief='flat', command=lambda: get_perc2())
button.pack(padx='10', pady='10')


def call_info():
    """Function that creates a new window to display info about the program and the creator"""
    info_popup = Tk()
    info_popup.title('EMMANUEL FREDERIQUE')
    info_popup.geometry('540x200')
    info_popup.configure(bg='#65aee4')
    info_lbl = Label(info_popup, relief='flat', font=font_style, text='')
    info_lbl.pack(padx='10', pady='10')
    info_text = '''Use the first part of the program to find out what
    percent of the second number represents the first.\n
    Use the second part to find a
    certain percentage of a number.'''
    info_lbl2 = Label(info_popup, relief='flat', font=font_style, text=info_text, justify=CENTER)
    info_lbl2.pack(padx='10', pady='10')


info_bt = Button(root, font=font_style, relief='flat', text='HELP?', command=lambda: call_info())
info_bt.pack(side=BOTTOM)


root.mainloop()
