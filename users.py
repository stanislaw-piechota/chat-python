from animations import users_nav_off, users_nav_in


def toggle_nav_visibility(nav, chat, root):
    if nav.winfo_x() < root.winfo_width():
        appears = True
    else:
        appears = False

    if appears:
        users_nav_off(nav, chat, root, 0)
    else:
        users_nav_in(nav, chat, root, 0)
