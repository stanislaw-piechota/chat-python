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
    print(corrected_message, gl.room, gl.nickname)
    response = post(HOST, data={'send': True, 'text': corrected_message, 'type': "text", 'room': gl.room, 'username': gl.nickname})
    print('resp: '+response.text)
    if 'Error' in response.text:
        raise HTTPError


def messages_thread(root):
    while root.message_get:
        if gl.room:
            root.messages = ex_handle(get_messages, gl.room)
            for mess in root.messages:
                print(mess)
                root.text.config(state='normal')
                root.text.insert(str(mess['ID']*3-2)+".0", f"{mess['author']}  {mess['time']['day']}.\
{mess['time']['month']}.{mess['time']['year']} {mess['time']['hour']}:{mess['time']['minute']}\n")
                root.text.insert(str(mess['ID']*3-1)+'.0', mess['message']+'\n\n')
                root.text.config(state='disabled')
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
    resp1 = register(username, '')
    if resp1 == True:
        gl.nickname = username
    return resp1


def register(username, password):
    if not username or (not password and not gl.anon):
        return None
    response = post(HOST, data={'register': True, 'username': username, 'password': password})
    if 'Success' in response.text:
        return True
    elif 'Error' in response.text:
        return response.json()["Error"]


def log_in(username, password):
    if not username or not password:
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
        return room_join(gl.nickname, name)
    elif 'Error' in response.text:
        return response.json()["Error"]


def convo_join(username1, username2):
    if not username1 or not username2:
        return None
    name1 = username1 + '#' + username2
    name2 = username2 + '#' + username1
    if name1 in gl.rooms:
        gl.room = name1
        return True
    if name2 in gl.rooms:
        gl.room = name2
        return True
    response = get(HOST, params={'create': True, 'name': name1, 'type': "private"})
    if 'Success' in response.text:
        resp1 = get(HOST, params={'join': True, 'username': username1, 'name': name1, 'type': "private"})
        resp2 = get(HOST, params={'join': True, 'username': username2, 'name': name1, 'type': "private"})
        if 'Success' in resp1.text and 'Success' in resp2.text:
            gl.rooms.append(name1)
            gl.room = name1
            return True
        elif 'Error' in resp1.text:
            return resp1.json()["Error"]
        elif 'Error' in resp2.text:
            return resp2.json()["Error"]
    elif 'Error' in response.text:
        return response.json()["Error"]


def room_join(username, room):
    if not room:
        return None
    response = get(HOST, params={'join': True, 'username': username, 'room': room, 'type': "public"})
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
