from tkinter import *
from functools import partial
from threading import Thread

import appbar as ab
import functions as f
import users
import network as net
from texts import greeting
CL = ab.CL

# main window
root = Tk()
ab.config_window(root)


# main frames
title_bar = Frame(root, bg=CL[0], relief='raised', bd=0, highlightthickness=0)
main_frame = Frame(root, bg=CL[3])
title_bar.pack(fill=X)
main_frame.pack(fill=BOTH, expand=True)


# appbar widgets
close_button = Button(title_bar, text=' × ', command=partial(ab.close_window, root), bg=CL[0], padx=2,
                      pady=2, bd=0, fg=CL[1], highlightthickness=0)
expand_button = Button(title_bar, text=' ■ ', bg=CL[0], padx=2,
                       pady=2, bd=0, fg=CL[1], highlightthickness=0)
expand_button.config(command=partial(ab.maximize, root, expand_button))
minimize_button = Button(title_bar, text=' ▁ ', command=partial(ab.minimize, root), bg=CL[0], padx=2,
                         pady=2, bd=0, fg=CL[1], highlightthickness=0)
title_bar_title = Label(title_bar, text='Strona Główna', bg=CL[0], bd=0, fg=CL[1], highlightthickness=0)

title_bar.pack(fill=X)
close_button.pack(side=RIGHT, ipadx=7, ipady=1)
expand_button.pack(side=RIGHT, ipadx=7, ipady=1)
minimize_button.pack(side=RIGHT, ipadx=7, ipady=1)
title_bar_title.pack(side=LEFT, padx=10)

title_bar.bind('<Button-1>', partial(ab.get_pos, root, expand_button))
close_button.bind('<Enter>', ab.close_hover)
close_button.bind('<Leave>', ab.close_normal)
expand_button.bind('<Enter>', ab.change_hover)
expand_button.bind('<Leave>', ab.change_normal)
minimize_button.bind('<Enter>', ab.change_hover)
minimize_button.bind('<Leave>', ab.change_normal)

klatka = LabelFrame(main_frame,relief=SUNKEN, bd=0, padx=10, pady=10, bg=CL[2])
klatka.pack(pady=200)
Label(klatka, text="Main Page",font=f.ft(26), fg=CL[0], bg=CL[2]).grid(row=0,column=0,columnspan=4)

Label(klatka, text="Nick:",font=f.ft(20), fg=CL[0], bg=CL[2]).grid(row=2,column=0,sticky=W,columnspan=4)
login = Entry(klatka, width=25, font=f.ft(16), bg=CL[4]).grid(row=3, column=0,columnspan=4)


pRejestracja = Button(klatka, text="Register here",font=f.ft(12), bg=CL[0], padx=2,pady=2, bd=0, fg=CL[1]).grid(row=6, column=0, pady=10, sticky=W)
pLogin = Button(klatka, text="Login here", font=f.ft(12), bg=CL[0], padx=2,pady=2, bd=0, fg=CL[1]).grid(row=6, column=3, pady=10, sticky=E)






root.mainloop()
