import messages as ms
import globals as gl
from requests import get, post
from requests.exceptions import HTTPError, ConnectionError, ConnectTimeout
from time import sleep
HOST = 'https://najlepszawgalaktyce.000webhostapp.com/chat/'


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
    messages = get(HOST+'chats.json').json()
    print(messages)


def ex_handle(func, *args):
    try:
        return func(*args)
    except (HTTPError, ConnectionError, ConnectTimeout) as e:
        print(f'Nie udało się pobrać wiadomości:  {e}')

def anonymous():



def register(username, password):
    response = post(HOST, data={'register': True, 'username': username, 'password': password})
    if 'Registered' in response.text:
        pass
    elif 'Error' in response.text:
        print(response.json()["Error"])


def log_in(username, password):
    response = post(HOST, data={'login': True, 'username': username, 'password': password})
    if 'Success' in response.text:
        gl.rooms = response.json()["Success"]
    elif 'Error' in response.text:
        print(response.json()["Error"])
    gl.rooms = response.json()


def room_create(name):
    response = get(HOST, params={'create': True, 'name': name})
    if 'Success' in response.text:
        room_join(gl.username, name)
    elif 'Error' in response.text:
        print(response.json()["Error"])


def room_join(username, room):
    response = get(HOST, params={'join': True, 'username': username, 'room': room})
    if 'Success' in response.text:
        gl.rooms.append(room)
        gl.room = room
    elif 'Error' in response.text:
        print(response.json()["Error"])
