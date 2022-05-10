import messages as ms
from requests import get, post
from requests.exceptions import HTTPError, ConnectionError, ConnectTimeout
from time import sleep
HOST = 'https://najlepszawgalaktyce.000webhostapp.com/chat/'


def send_to_server(text_field):
    corrected_message = ms.message_check(text_field)
    if corrected_message:
        print(corrected_message)
    else:
        return


def messages_thread(root):
    while root.message_get:
        get_messages()
        sleep(2)


def get_messages():
    try:
        messages = get(HOST+'chat.json').json()
        print(messages)
    except (HTTPError, ConnectionError, ConnectTimeout) as e:
        print(f'Nie udało się pobrać wiadomości:  {e}')
