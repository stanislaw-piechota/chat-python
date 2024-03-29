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

def Logowanie():
    klatkaAnon.place_forget()
    klatkaLogowanie.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.5)


def backRA():
    klatkaRejestracja.place_forget()
    klatkaAnon.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.5)

def backLA():
    klatkaLogowanie.place_forget()
    klatkaAnon.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.5)


def new_acc():
    pass
def register():
    klatkaAnon.place_forget()
    klatkaRejestracja.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.5)


def anonymus_join(entry):
    resp = net.anonymous(entry.get())
    print(resp)
    print(resp == True)
    if resp == True:
        entry.delete(0, END)
        zmiana_okna_LC()
    else:
        err_login['text'] = resp


def reg(entry1, entry2):
    resp = net.register(entry1.get(), entry2.get())
    if resp == True:
        entry1.delete(0, END)
        entry2.delete(0, END)
        zmiana_okna_LC()
    else:
        print(resp)


def login(entry1, entry2):
    resp = net.log_in(entry1.get(), entry2.get())
    if resp == True:
        entry1.delete(0, END)
        entry2.delete(0, END)
        zmiana_okna_LC()
    else:
        print(resp)


def convo_join(username):
    resp = net.convo_join(gl.nickname, username)
    if resp != True:
        print(resp)


def room_join(entry):
    resp = net.room_join(gl.nickname, entry.get())
    if resp == True:
        entry.delete(0, END)
    else:
        print(resp)


def leave(name):
    resp = net.room_leave(gl.nickname, name)
    if resp != True:
        print(resp)


def switch(name):
    if name in gl.rooms:
        gl.room = name


def new_Room():
    top = Toplevel(bg=CL[3])
    ab.config_window(top)
    top.geometry("300x300+350+350")

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
    top.geometry("300x300+350+350")

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

    klatkaAnon.place_forget()


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
# my_canvas = Canvas(chat_frame, bg=CL[3])
# my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
text = Text(chat_frame, height=10, bg=CL[3], fg=CL[0], font=f.ft(10), padx=100, bd=0, state='disabled')
root.text = text
text.place(relx=0, rely=0.2, relwidth=1, relheight=0.6)
scrollbar=Scrollbar(chat_frame, orient=VERTICAL, command=text.yview)
scrollbar.place(relx=0.98, rely=0.02, relwidth=0.02, relheight=1)
text['yscrollcommand'] =scrollbar.set


# scrollbar.pack(side=RIGHT, fill=Y)
#
# my_canvas.configure(yscrollcommand=scrollbar.set)
# my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion= my_canvas.bbox("all")))
#
# secFrame= Frame(my_canvas, bg=CL[3])
#
# my_canvas.create_window((0,0), window=secFrame, anchor="nw")
# secFrame.place(relx=0, relwidth=1, rely=0, relheight=1)

greeting_label = Label(chat_frame, font=f.ft(10), bg=CL[3], fg=CL[0], text=greeting, justify=CENTER)
text_field = Entry(chat_frame, font=f.ft(12), bg=CL[1], fg='white', bd=0)
send_button = Button(chat_frame, bg=CL[0], fg=CL[1], text='⏵', font=f.ft(15), bd=0, command=partial(net.send_to_server,
                                                                                                    text_field))
photo_button = Button(chat_frame, bg=CL[0], fg=CL[1], text='+', font=f.ft(15), bd=0)


users_button = Label(main_screen, bd=0, bg=CL[1], fg=CL[0], text="Członkowie", font=f.ft(12))
                      # command=partial(users.toggle_nav_visibility, users_nav, chat_frame, root))

send_button = Button(chat_frame, bg=CL[0], fg=CL[1], text='⏵', font=f.ft(15), bd=0, command=partial(net.send_to_server,
                                                                                                    text_field))
photo_button = Button(chat_frame, bg=CL[0], fg=CL[1], text='+', font=f.ft(15), bd=0)

add_room_button.place(relx=0, rely=0, relwidth=1, relheight=0.05)
join_room_button.place(relx=0, rely=0.05, relwidth=1, relheight=0.05)
users_nav.place(relx=0.85, rely=0, relwidth=0.15, relheight=1)
join_nav.place(x=0, y=0, relwidth=0.2, relheight=1)
text_field.place(relx=0.05, rely=0.9, relwidth=0.75, relheight=0.05)
send_button.place(relx=0.825, relwidth=0.05, rely=0.9, relheight=0.05)
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


klatkaAnon = LabelFrame(root, relief=SUNKEN, bd=0, padx=100, pady=100, bg=CL[2])
Label(klatkaAnon, text="Logowanie Anonimowe", font=f.ft(26), fg=CL[0], bg=CL[2]).place(relx=0.1, rely=-0.4, relwidth=0.8, relheight=0.3)

Label(klatkaAnon, text="Nick:", font=f.ft(20), fg=CL[0], bg=CL[2]).place(relx=0.1, rely=0, relwidth=0.8, relheight=0.2)
nick = Entry(klatkaAnon, width=25, font=f.ft(16), bg=CL[4], bd=0, justify='center')
nick.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.2)

pRejestracja = Button(klatkaAnon, text="Zarejestruj się", font=f.ft(12), bg=CL[0], padx=2,pady=2, bd=0, fg=CL[1], command=register)
pRejestracja.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.2)
pLogin = Button(klatkaAnon, text="Zaloguj się", font=f.ft(12), bg=CL[0], padx=2,pady=2, bd=0, fg=CL[1], command=Logowanie).place(relx=0.1, rely=0.75, relwidth=0.8, relheight=0.2)
pAnonim = Button(klatkaAnon, text="Dołącz anonimowo", font=f.ft(12), bg=CL[0], padx=80,pady=2, bd=0, fg=CL[1], command=lambda:anonymus_join(nick)).place(relx=0.1, rely=1, relwidth=0.8, relheight=0.2)

err_login = Label(klatkaAnon, text="", font=f.ft(12), fg=CL[0], bg=CL[2])
err_login.place(relx=0.1, rely=1.45, relwidth=0.8, relheight=0.2)



klatkaAnon.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.5)




klatkaRejestracja = LabelFrame(root, relief=SUNKEN, bd=0, padx=100, pady=100, bg=CL[2])
Label(klatkaRejestracja, text="Rejestracja", font=f.ft(26), fg=CL[0], bg=CL[2]).place(relx=0.1, rely=-0.4, relwidth=0.8, relheight=0.3)

Label(klatkaRejestracja, text="Login:", font=f.ft(20), fg=CL[0], bg=CL[2]).place(relx=0.1, rely=0, relwidth=0.8, relheight=0.2)
login = Entry(klatkaRejestracja, width=25, font=f.ft(16), bg=CL[4], bd=0, justify='center')

Label(klatkaRejestracja, text="Hasło:", font=f.ft(20), fg=CL[0], bg=CL[2]).place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.2)
haslo = Entry(klatkaRejestracja, width=25, font=f.ft(16), bg=CL[4], bd=0, justify='center')

pRejestracja1 = Button(klatkaRejestracja, text="Zarejestruj się", font=f.ft(12), bg=CL[0], padx=2,pady=2, bd=0, fg=CL[1], command=lambda: reg(login, haslo))
pPowrot1 = Button(klatkaRejestracja, text="Wróć do anonimowego logowania", font=f.ft(12), bg=CL[0], padx=2,pady=2, bd=0, fg=CL[1], command=backRA)
pPowrot1.place(relx=0.1, rely=1.2, relwidth=0.8, relheight=0.2)
pRejestracja1.place(relx=0.1, rely=0.9, relwidth=0.8, relheight=0.2)
login.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.2)
haslo.place(relx=0.1, rely=0.6, relwidth=0.8, relheight=0.2)



klatkaLogowanie = LabelFrame(root, relief=SUNKEN, bd=0, padx=100, pady=100, bg=CL[2])
Label(klatkaLogowanie, text="Logowanie", font=f.ft(26), fg=CL[0], bg=CL[2]).place(relx=0.1, rely=-0.4, relwidth=0.8, relheight=0.3)

Label(klatkaLogowanie, text="Login:", font=f.ft(20), fg=CL[0], bg=CL[2]).place(relx=0.1, rely=0, relwidth=0.8, relheight=0.2)
login = Entry(klatkaLogowanie, width=25, font=f.ft(16), bg=CL[4], bd=0, justify='center')

Label(klatkaLogowanie, text="Hasło:", font=f.ft(20), fg=CL[0], bg=CL[2]).place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.2)
haslo = Entry(klatkaLogowanie, width=25, font=f.ft(16), bg=CL[4], bd=0, justify='center')

plogowanie1 = Button(klatkaLogowanie, text="Zaloguj się", font=f.ft(12), bg=CL[0], padx=2,pady=2, bd=0, fg=CL[1], command=None)
pPowrot2 = Button(klatkaLogowanie, text="Wróć do anonimowego logowania", font=f.ft(12), bg=CL[0], padx=2,pady=2, bd=0, fg=CL[1], command=backLA)
pPowrot2.place(relx=0.1, rely=1.2, relwidth=0.8, relheight=0.2)
plogowanie1.place(relx=0.1, rely=0.9, relwidth=0.8, relheight=0.2)
login.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.2)
haslo.place(relx=0.1, rely=0.6, relwidth=0.8, relheight=0.2)

err1_login = Label(klatkaLogowanie, text="", font=f.ft(12), fg=CL[0], bg=CL[2]).place(relx=0.1, rely=1.45, relwidth=0.8, relheight=0.2)

root.mainloop()
