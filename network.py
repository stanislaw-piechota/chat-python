import messages as ms
from requests import get, post
from requests.exceptions import HTTPError, ConnectionError, ConnectTimeout
from time import sleep
HOST = 'http://chat.5v.pl/'


def send_to_server(text_field):
    corrected_message = ms.message_check(text_field)
    if not corrected_message:
        return
    response = post(HOST, data={'send': True, 'text': corrected_message})
    if 'Error' in response.text:
        raise HTTPError


def messages_thread(root):
    while root.message_get:
        ex_handle(get_messages)
        sleep(2)


def get_messages():
    messages = get(HOST+'chat.json').json()
    print(messages)


def ex_handle(func, *args):
    try:
        return func(*args)
    except (HTTPError, ConnectionError, ConnectTimeout) as e:
        print(f'Nie udało się pobrać wiadomości:  {e}')
