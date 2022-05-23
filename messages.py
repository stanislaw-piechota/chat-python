from tkinter import END
from texts import slurs, link_starts, link_ends, symbols


def message_check(entry):
    message = entry.get()
    if message:
        entry.delete(0, END)
        corrected_message = ignore_symbols(0, message)
        return corrected_message

def ignore_symbols(i, message):
    if i == len(symbols):
        return slurs_links_check(message)
    else:
        words = message.split(symbols[i])
        new_message = ""
        for word in words:
            new_message += ignore_symbols(i+1, word) + symbols[i]
        return new_message[:-1]


def slurs_links_check(word):
    corrected_word = ""
    # ignore capitalization
    word_lower = word.lower()
    # check if a word is a slur or a link
    if word_lower in slurs:
        corrected_word += '*' * len(word)
    elif word_lower.startswith(link_starts) or word_lower.endswith(link_ends):
        corrected_word += '[ukryto link]'
    else:
        corrected_word += word
    return corrected_word
