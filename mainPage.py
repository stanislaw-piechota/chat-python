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

klatka = LabelFrame(main_frame, relief=SUNKEN, bd=0, padx=100, pady=100, bg=CL[2])
klatka.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.5)
Label(klatka, text="Strona główna", font=f.ft(26), fg=CL[0], bg=CL[2]).place(relx=0.1, rely=-0.4, relwidth=0.8, relheight=0.3)

Label(klatka, text="Nick:", font=f.ft(20), fg=CL[0], bg=CL[2]).place(relx=0.1, rely=0, relwidth=0.8, relheight=0.2)
login = Entry(klatka, width=25, font=f.ft(16), bg=CL[4], bd=0, justify='center').place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.2)

pRejestracja = Button(klatka, text="Zarejestruj się", font=f.ft(12), bg=CL[0], padx=2,pady=2, bd=0, fg=CL[1])
pRejestracja.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.2)
pLogin = Button(klatka, text="Zaloguj się", font=f.ft(12), bg=CL[0], padx=2,pady=2, bd=0, fg=CL[1]).place(relx=0.1, rely=0.75, relwidth=0.8, relheight=0.2)
pAnonim = Button(klatka, text="Dołącz anonimowo", font=f.ft(12), bg=CL[0], padx=80,pady=2, bd=0, fg=CL[1]).place(relx=0.1, rely=1, relwidth=0.8, relheight=0.2)

root.mainloop()
