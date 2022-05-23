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
main_screen.place(x=0, y=0, relwidth=1, relheight=1)

join_nav = Frame(main_screen, bg=CL[1])
add_room_button = Button(join_nav, bd=0, bg=CL[1], fg=CL[0], text="Utwórz pokój", font=f.ft(12), command=None)
add_room_button.place(relx=0, rely=0, relwidth=1, relheight=0.05)
join_room_button = Button(join_nav, bd=0, bg=CL[1], fg=CL[0], text="Dołącz do czatu", font=f.ft(12), command=None)
join_room_button.place(relx=0, rely=0.05, relwidth=1, relheight=0.05)
# TODO: chats list
join_nav.place(x=0, y=0, relwidth=0.2, relheight=1)

users_nav = Frame(main_screen, bg=CL[2])
# TODO: users list
users_nav.place(relx=0.85, rely=0, relwidth=0.15, relheight=1)

chat_frame = Frame(main_screen, bg=CL[3])
greeting_label = Label(chat_frame, font=f.ft(10), bg=CL[3], fg=CL[0], text=greeting, justify=CENTER)
greeting_label.place(relx=0, rely=0, relwidth=1, relheight=0.15)
text_field = Entry(chat_frame, font=f.ft(12), bg=CL[1], fg='white', bd=0)
text_field.place(relx=0.05, rely=0.9, relwidth=0.75, relheight=0.05)
send_button = Button(chat_frame, bg=CL[0], fg=CL[1], text='⏵', font=f.ft(15), bd=0, command=partial(net.send_to_server,
                                                                                                    text_field))
send_button.place(relx=0.825, relwidth=0.05, rely=0.9, relheight=0.05)
photo_button = Button(chat_frame, bg=CL[0], fg=CL[1], text='+', font=f.ft(15), bd=0)
photo_button.place(relx=0.9, relwidth=0.05, rely=0.9, relheight=0.05)
chat_frame.place(relx=0.2, rely=0, relwidth=0.65, relheight=1)

users_button = Button(main_screen, bd=0, bg=CL[1], fg=CL[0], text="Członkowie", font=f.ft(12),
                      command=partial(users.toggle_nav_visibility, users_nav, chat_frame, root))
users_button.place(relx=0.86, rely=0.02, relwidth=0.13, relheight=0.06)


# binding enter to message sending
root.bind('<Return>', lambda event: net.ex_handle(net.send_to_server, text_field))
messages_thread = Thread(target=net.messages_thread, args=(root, ))
messages_thread.start()


# resizing widgets
resize_x_widget = Frame(main_frame, bg=CL[3], cursor='sb_h_double_arrow')
resize_x_widget.pack(side=RIGHT, ipadx=2, fill=Y)
resize_x_widget.bind("<B1-Motion>", partial(ab.resize_x, root))
Frame(main_frame, bg=CL[3]).pack(side=LEFT, ipadx=2, fill=Y)  # symmetry
resize_y_widget = Frame(main_frame, bg=CL[3], cursor='sb_v_double_arrow')
resize_y_widget.pack(side=BOTTOM, ipady=2, fill=X)
resize_y_widget.bind("<B1-Motion>", partial(ab.resize_y, root))

root.mainloop()
