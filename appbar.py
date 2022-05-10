# Appbar functions taken from: https://github.com/Terranova-Python/Tkinter-Menu-Bar

from ctypes import windll
from functools import partial
CL = ['#C4C4C4', '#494C57', '#41444C', '#35383E', '#D5D5D5']


def config_window(root):
    # Necessary attributes to make appbar work

    root.geometry('1280x720+75+75')
    root.overrideredirect(True)
    root['bg'] = CL[3]
    root.title('CHAT')

    root.minimized = False
    root.maximized = False

    root.bind("<FocusIn>", partial(deminimize, root))
    root.after(10, lambda: set_app_window(root))
    root.message_get = True


def close_window(root):
    root.message_get = False
    root.destroy()


def set_app_window(main_window):
    # displaying icon on taskbar when override is true

    gwl_ex_style = -20
    ws_ex_app_window = 0x00040000
    ws_ex_tool_window = 0x00000080

    hwnd = windll.user32.GetParent(main_window.winfo_id())
    style_w = windll.user32.GetWindowLongW(hwnd, gwl_ex_style)
    style_w = style_w & ~ws_ex_tool_window
    style_w = style_w | ws_ex_app_window
    res = windll.user32.SetWindowLongW(hwnd, gwl_ex_style, style_w)

    main_window.wm_withdraw()
    main_window.after(10, lambda: main_window.wm_deiconify())


# changing full screen
def minimize(root):
    root.attributes("-alpha", 0)
    root.minimized = True


def deminimize(root, event):
    root.attributes("-alpha", 1)
    if root.minimized:
        root.minimized = False


def maximize(root, expand_button):
    if not root.maximized:
        root.normal_size = root.geometry()
        expand_button.config(text=" ▞ ")
        root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
        root.maximized = not root.maximized

    else:
        expand_button.config(text=" ■ ")
        root.geometry(root.normal_size)
        root.maximized = not root.maximized


# hover animation on app bar buttons
def close_hover(event):
    event.widget['bg'] = '#C22020'


def close_normal(event):
    event.widget['bg'] = CL[0]


def change_hover(event):
    event.widget['bg'] = CL[4]


def change_normal(event):
    event.widget['bg'] = CL[0]


# resizing window
def resize_x(root, event):
    x_win = root.winfo_x()
    difference = (event.x_root - x_win) - root.winfo_width()

    if root.winfo_width() > 650:
        try:
            root.geometry(f"{ root.winfo_width() + difference }x{ root.winfo_height() }")
        except Exception as e:
            print(e)
    else:
        if difference > 0:
            try:
                root.geometry(f"{ root.winfo_width() + difference }x{ root.winfo_height() }")
            except Exception as e:
                print(e)

    event.widget.config(bg=CL[3])


def resize_y(root, event):
    y_win = root.winfo_y()
    difference = (event.y_root - y_win) - root.winfo_height()

    if root.winfo_height() > 350:
        try:
            root.geometry(f"{ root.winfo_width()  }x{ root.winfo_height() + difference}")
        except Exception as e:
            print(e)
    else:
        if difference > 0:
            try:
                root.geometry(f"{ root.winfo_width()  }x{ root.winfo_height() + difference}")
            except Exception as e:
                print(e)

    event.widget.config(bg=CL[3])


# moving window while avoiding cursor position change
def get_pos(root, expand_button, event):
    if not root.maximized:
        x_win = root.winfo_x()
        y_win = root.winfo_y()
        start_x = event.x_root
        start_y = event.y_root

        y_win = y_win - start_y
        x_win = x_win - start_x

        def move_window(event_in):  # runs when window is dragged
            root.config(cursor="fleur")
            root.geometry(f'+{event_in.x_root + x_win}+{event_in.y_root + y_win}')

        def release_window(event_in):  # runs when window is released
            root.config(cursor="arrow")

        event.widget.bind('<B1-Motion>', move_window)
        event.widget.bind('<ButtonRelease-1>', release_window)
    else:
        expand_button.config(text=" ■ ")
        root.geometry(f"{root.winfo_screenwidth()-10}x{root.winfo_screenheight()-50}")
        root.maximized = not root.maximized
