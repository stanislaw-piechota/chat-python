from tkinter import END
from texts import slurs, link_starts, link_ends, symbols

all_symbols = symbols + ['/', '.']
symbols_n = len(symbols)
all_symbols_n = len(all_symbols)


def message_check(entry):
    message = entry.get()
    if message:
        entry.delete(0, END)
        corrected_message = ignore_symbols(0, message)
        return corrected_message


def ignore_symbols(i, message):
    if i == all_symbols_n:
        return slurs_check(message)
    else:
        if i == symbols_n:
            message = links_check(message)
        words = message.split(all_symbols[i])
        new_message = ""
        for word in words:
            new_message += ignore_symbols(i+1, word) + all_symbols[i]
        return new_message[:-1]


def slurs_check(word):
    corrected_word = ""
    # ignore capitalization
    word_lower = word.lower()
    # check if the word is a slur
    if word_lower in slurs:
        corrected_word += '*' * len(word)
    else:
        corrected_word += word
    return corrected_word


def links_check(word):
    corrected_word = ""
    # ignore capitalization
    word_lower = word.lower()
    # check if the word is a link
    if word_lower.startswith(link_starts) or word_lower.endswith(link_ends):
        corrected_word += '[ukryto link]'
    else:
        corrected_word += word
    return corrected_word
