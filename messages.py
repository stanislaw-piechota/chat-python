from tkinter import END
from texts import slurs, link_starts, link_ends


def message_check(entry):
    message = entry.get()
    if message:
        entry.delete(0, END)
        words = message.split(' ')
        message = ""
        for word in words:
            # check if a word is a slur or a link
            if not (word in slurs or word.startswith(link_starts) or word.endswith(link_ends)):
                message += word + ' '
        message = message[:-1]
        return message
