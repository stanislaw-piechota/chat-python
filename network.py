import messages as ms
import globals as gl
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
        if gl.room:
            root.messages = ex_handle(get_messages, gl.room)
            gl.users = post(HOST, data={'users': True, 'room': "test"}).json()
        sleep(2)


def get_messages(room):
    response = post(HOST, data={'read': True, 'room': room})
    all_messages = response.json()
    messages = []
    while gl.m_id < len(all_messages):
        messages.append(all_messages[gl.m_id])
        gl.m_id += 1
    return messages


def ex_handle(func, *args):
    try:
        return func(*args)
    except (HTTPError, ConnectionError, ConnectTimeout) as e:
        print(f'Nie udało się pobrać wiadomości:  {e}')


def anonymous(username):
    if not username:
        return None
    gl.anon = True
    register(username, '')
    gl.anon = log_in(username, '')


def register(username, password):
    if not username or (not password and not gl.anon):
        return None
    response = post(HOST, data={'register': True, 'username': username, 'password': password})
    if 'Registered' in response.text:
        return True
    elif 'Error' in response.text:
        return response.json()["Error"]


def log_in(username, password):
    if not username or (not password and not gl.anon):
        return None
    response = post(HOST, data={'login': True, 'username': username, 'password': password})
    if 'Error' in response.text:
        return response.json()["Error"]
    elif not response.text:
        gl.rooms = response.json()
        gl.nickname = username
        return True


def room_create(name):
    if not name:
        return None
    response = get(HOST, params={'create': True, 'name': name})
    if 'Success' in response.text:
        room_join(gl.nickname, name)
    elif 'Error' in response.text:
        return response.json()["Error"]


def room_join(username, room):
    if not room:
        return None
    response = get(HOST, params={'join': True, 'username': username, 'room': room})
    if 'Success' in response.text:
        gl.rooms.append(room)
        gl.room = room
        return True
    elif 'Error' in response.text:
        return response.json()["Error"]


def room_leave(username, room):
    if not room:
        return None
    response = get(HOST, params={'leave': True, 'username': username, 'room': room})
    if 'Success' in response.text:
        gl.rooms.remove(room)
        gl.room = ''
    elif 'Error' in response.text:
        return response.json()["Error"]
