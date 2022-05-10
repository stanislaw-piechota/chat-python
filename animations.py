from functools import partial


add = 1


def users_nav_off(nav, chat, root, count):
    global add

    x, max_x = nav.winfo_x(), root.winfo_width()
    chat_width = chat.winfo_width()

    if count >= 8:
        add += 2
        count = 0
    if x <= max_x:
        x += add
        chat_width += add
        nav.place(relx=x/max_x)
        chat.place(relwidth=chat_width/max_x)

        f = partial(users_nav_off, nav, chat, root, count+1)
        f.__name__ = f.func.__name__
        root.after(2, f)


def users_nav_in(nav, chat, root, count):
    global add

    x, max_x = nav.winfo_x(), root.winfo_width()
    chat_width = chat.winfo_width()
    if count >= 8:
        add -= 1
        count = 0
    if x/max_x > 0.85:
        x -= add
        chat_width -= add
        nav.place(relx=x/max_x)
        chat.place(relwidth=chat_width/max_x)

        f = partial(users_nav_in, nav, chat, root, count+1)
        f.__name__ = f.func.__name__
        root.after(2, f)
    else:
        nav.place(relx=0.85)
        chat.place(relwidth=0.65)
        add = 1
