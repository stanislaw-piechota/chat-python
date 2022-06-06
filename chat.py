from tkinter import *
from tkinter import ttk
from functools import partial
from threading import Thread

import appbar as ab
import functions as f
import globals as gl
import users
import network as net
from texts import greeting
CL = ab.CL

# main window
root = Tk()
root.messages = []
ab.config_window(root)


def anonymus_join(entry):
    resp = net.anonymous(entry.get())
    if resp == True:
        entry.delete(0, END)
        zmiana_okna_LC()
    else:
        err_login['text'] = resp


def register(entry1, entry2):
    resp = net.register(entry1.get(), entry2.get())
    if resp == True:
        entry1.delete(0, END)
        entry2.delete(0, END)
        zmiana_okna_LC()
    else:
        err_login['text'] = resp


def login(entry1, entry2):
    resp = net.log_in(entry1.get(), entry2.get())
    if resp == True:
        entry1.delete(0, END)
        entry2.delete(0, END)
        zmiana_okna_LC()
    else:
        err_login['text'] = resp


def convo_join(username):
    resp = net.convo_join(gl.nickname, username)
    if resp != True:
        err_login['text'] = resp


def room_join(entry):
    resp = net.room_join(gl.nickname, entry.get())
    if resp == True:
        entry.delete(0, END)
    else:
        err_login['text'] = resp


def leave(name):
    resp = net.room_leave(gl.nickname, name)
    if resp != True:
        err_login['text'] = resp


def switch(name):
    if name in gl.rooms:
        gl.room = name


def new_Room():
    top = Toplevel(bg=CL[3])
    ab.config_window(top)
    top.geometry("300x300")

    # main frames
    title_barT = Frame(top, bg=CL[0], relief='raised', bd=0, highlightthickness=0)
    title_barT.pack(fill=X)

    # appbar widgets
    close_buttonT = Button(title_barT, text=' × ', command=partial(ab.close_window, top), bg=CL[0], padx=2,
                          pady=2, bd=0, fg=CL[1], highlightthickness=0)
    expand_buttonT = Button(title_barT, text=' ■ ', bg=CL[0], padx=2,
                           pady=2, bd=0, fg=CL[1], highlightthickness=0)
    expand_buttonT.config(command=partial(ab.maximize, top, expand_button))
    minimize_buttonT = Button(title_barT, text=' ▁ ', command=partial(ab.minimize, top), bg=CL[0], padx=2,
                             pady=2, bd=0, fg=CL[1], highlightthickness=0)
    title_bar_titleT = Label(title_barT, text='Nowy pokój', bg=CL[0], bd=0, fg=CL[1], highlightthickness=0)


    title_barT.pack(fill=X)
    close_buttonT.pack(side=RIGHT, ipadx=7, ipady=1)
    expand_buttonT.pack(side=RIGHT, ipadx=7, ipady=1)
    minimize_buttonT.pack(side=RIGHT, ipadx=7, ipady=1)
    title_bar_titleT.pack(side=LEFT, padx=10)

    title_barT.bind('<Button-1>', partial(ab.get_pos, root, expand_buttonT))
    close_buttonT.bind('<Enter>', ab.close_hover)
    close_buttonT.bind('<Leave>', ab.close_normal)
    expand_buttonT.bind('<Enter>', ab.change_hover)
    expand_buttonT.bind('<Leave>', ab.change_normal)
    minimize_buttonT.bind('<Enter>', ab.change_hover)
    minimize_buttonT.bind('<Leave>', ab.change_normal)


    top.title("Tworzenie pokoju")
    newRoomLabel = Label(top, text="Nazwa pokoju:", font=f.ft(15), fg=CL[0], bg=CL[3]).place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.2)
    RoomName = Entry(top, width=25, font=f.ft(16), bg=CL[4], bd=0, justify='center').place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.1)
    createRoom = Button(top, text="Utwórz pokój", font=f.ft(12), bg=CL[0], bd=0, fg=CL[1]).place(relx=0.1, rely=0.6, relwidth=0.8, relheight=0.1)

    err = Label(top, text=f"", font=f.ft(12), fg=CL[0], bg=CL[3]).place(relx=0.1, rely=0.8, relwidth=0.8, relheight=0.05)


def join_Room():
    top = Toplevel(bg=CL[3])
    ab.config_window(top)
    top.geometry("300x300")

    # main frames
    title_barT = Frame(top, bg=CL[0], relief='raised', bd=0, highlightthickness=0)
    title_barT.pack(fill=X)

    # appbar widgets
    close_buttonT = Button(title_barT, text=' × ', command=partial(ab.close_window, top), bg=CL[0], padx=2,
                          pady=2, bd=0, fg=CL[1], highlightthickness=0)

    expand_buttonT = Button(title_barT, text=' ■ ', bg=CL[0], padx=2,
                           pady=2, bd=0, fg=CL[1], highlightthickness=0)
    expand_buttonT.config(command=partial(ab.maximize, top, expand_button))
    minimize_buttonT = Button(title_barT, text=' ▁ ', command=partial(ab.minimize, top), bg=CL[0], padx=2,
                             pady=2, bd=0, fg=CL[1], highlightthickness=0)
    title_bar_titleT = Label(title_barT, text='Dodaj pokój', bg=CL[0], bd=0, fg=CL[1], highlightthickness=0)


    title_barT.pack(fill=X)
    close_buttonT.pack(side=RIGHT, ipadx=7, ipady=1)
    expand_buttonT.pack(side=RIGHT, ipadx=7, ipady=1)
    minimize_buttonT.pack(side=RIGHT, ipadx=7, ipady=1)
    title_bar_titleT.pack(side=LEFT, padx=10)

    title_barT.bind('<Button-1>', partial(ab.get_pos, root, expand_buttonT))
    close_buttonT.bind('<Enter>', ab.close_hover)
    close_buttonT.bind('<Leave>', ab.close_normal)
    expand_buttonT.bind('<Enter>', ab.change_hover)
    expand_buttonT.bind('<Leave>', ab.change_normal)
    minimize_buttonT.bind('<Enter>', ab.change_hover)
    minimize_buttonT.bind('<Leave>', ab.change_normal)


    top.title("Dołączanie do pokoju")
    newRoomLabel = Label(top, text="Nazwa pokoju:", font=f.ft(15), fg=CL[0], bg=CL[3]).place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.2)
    RoomName = Entry(top, width=25, font=f.ft(16), bg=CL[4], bd=0, justify='center').place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.1)
    createRoom = Button(top, text="Dodaj pokój", font=f.ft(12), bg=CL[0], bd=0, fg=CL[1]).place(relx=0.1, rely=0.6, relwidth=0.8, relheight=0.1)
    err = Label(top, text=f"", font=f.ft(12), fg=CL[0], bg=CL[3]).place(relx=0.1, rely=0.8, relwidth=0.8, relheight=0.2)

def zmiana_okna_LC():
    main_screen.place(x=0, y=0, relwidth=1, relheight=1)
    chat_frame.place(relx=0.2, rely=0, relwidth=0.65, relheight=1)

    klatka.destroy()


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
title_bar_title = Label(title_bar, text='CHAT', bg=CL[0], bd=0, fg=CL[1], highlightthickness=0)

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


# chat screen widgets
main_screen = Frame(main_frame, bg=CL[3])
# main_screen.place(x=0, y=0, relwidth=1, relheight=1)

join_nav = Frame(main_screen, bg=CL[1])
add_room_button = Button(join_nav, bd=0, bg=CL[1], fg=CL[0], text="Utwórz pokój", font=f.ft(12), command=new_Room)
join_room_button = Button(join_nav, bd=0, bg=CL[1], fg=CL[0], text="Dołącz do czatu", font=f.ft(12), command=join_Room)
# TODO: chats list
join_nav.place(x=0, y=0, relwidth=0.2, relheight=1)

users_nav = Frame(main_screen, bg=CL[2])
# TODO: users list

chat_frame = Frame(main_screen, bg=CL[3])
#scrollbar
my_canvas = Canvas(chat_frame, bg=CL[3])
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

scrollbar=ttk.Scrollbar(chat_frame, orient=VERTICAL, command=my_canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

my_canvas.configure(yscrollcommand=scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion= my_canvas.bbox("all")))

secFrame= Frame(my_canvas, bg=CL[3])

my_canvas.create_window((0,0), window=secFrame, anchor="nw")
secFrame.place(relx=0, relwidth=1, rely=0, relheight=1)


greeting_label = Label(secFrame, font=f.ft(10), bg=CL[3], fg=CL[0], text=greeting, justify=CENTER)
text_field = Entry(secFrame, font=f.ft(12), bg=CL[1], fg='white', bd=0)
send_button = Button(secFrame, bg=CL[0], fg=CL[1], text='⏵', font=f.ft(15), bd=0, command=partial(net.send_to_server,
                                                                                                    text_field))
photo_button = Button(secFrame, bg=CL[0], fg=CL[1], text='+', font=f.ft(15), bd=0)


users_button = Label(main_screen, bd=0, bg=CL[1], fg=CL[0], text="Członkowie", font=f.ft(12))
                      # command=partial(users.toggle_nav_visibility, users_nav, secFrame, root))

add_room_button.place(relx=0, rely=0, relwidth=1, relheight=0.05)
join_room_button.place(relx=0, rely=0.05, relwidth=1, relheight=0.05)
users_nav.place(relx=0.85, rely=0, relwidth=0.15, relheight=1)
join_nav.place(x=0, y=0, relwidth=0.2, relheight=1)
text_field.place(relx=0.05, rely=0.9, relwidth=0.75, relheight=0.05)
send_button = Button(chat_frame, bg=CL[0], fg=CL[1], text='⏵', font=f.ft(15), bd=0, command=partial(net.send_to_server,
                                                                                                    text_field))
send_button.place(relx=0.825, relwidth=0.05, rely=0.9, relheight=0.05)
photo_button = Button(chat_frame, bg=CL[0], fg=CL[1], text='+', font=f.ft(15), bd=0)
photo_button.place(relx=0.9, relwidth=0.05, rely=0.9, relheight=0.05)
greeting_label.place(relx=0, rely=0, relwidth=1, relheight=0.15)
users_button.place(relx=0.86, rely=0.02, relwidth=0.13, relheight=0.06)


# binding enter to message sending
root.bind('<Return>', lambda event: net.ex_handle(net.send_to_server, text_field))
messages_thread = Thread(target=net.messages_thread, args=(root, ))
messages_thread.start()


# resizing widgets
resize_x_widget = Frame(main_frame, bg=CL[3], cursor='sb_h_double_arrow')
resize_x_widget.pack(side=RIGHT, ipadx=1, fill=Y)
resize_x_widget.bind("<B1-Motion>", partial(ab.resize_x, root))
Frame(main_frame, bg=CL[3]).pack(side=LEFT, ipadx=1, fill=Y)  # symmetry
resize_y_widget = Frame(main_frame, bg=CL[3], cursor='sb_v_double_arrow')
resize_y_widget.pack(side=BOTTOM, ipady=1, fill=X)
resize_y_widget.bind("<B1-Motion>", partial(ab.resize_y, root))


klatka = LabelFrame(root, relief=SUNKEN, bd=0, padx=100, pady=100, bg=CL[2])
klatka.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.5)
Label(klatka, text="Strona główna", font=f.ft(26), fg=CL[0], bg=CL[2]).place(relx=0.1, rely=-0.4, relwidth=0.8, relheight=0.3)

Label(klatka, text="Nick:", font=f.ft(20), fg=CL[0], bg=CL[2]).place(relx=0.1, rely=0, relwidth=0.8, relheight=0.2)
login = Entry(klatka, width=25, font=f.ft(16), bg=CL[4], bd=0, justify='center').place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.2)

pRejestracja = Button(klatka, text="Zarejestruj się", font=f.ft(12), bg=CL[0], padx=2,pady=2, bd=0, fg=CL[1])
pRejestracja.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.2)
pLogin = Button(klatka, text="Zaloguj się", font=f.ft(12), bg=CL[0], padx=2,pady=2, bd=0, fg=CL[1], command=zmiana_okna_LC).place(relx=0.1, rely=0.75, relwidth=0.8, relheight=0.2)
pAnonim = Button(klatka, text="Dołącz anonimowo", font=f.ft(12), bg=CL[0], padx=80,pady=2, bd=0, fg=CL[1]).place(relx=0.1, rely=1, relwidth=0.8, relheight=0.2)

err_login = Label(klatka, text="", font=f.ft(12), fg=CL[0], bg=CL[2]).place(relx=0.1, rely=1.25, relwidth=0.8, relheight=0.2)

root.mainloop()
