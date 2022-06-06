from requests import post, get
HOST = 'http://chat.5v.pl/'

post(HOST, data={'register':True, 'username':'stasio14', 'password':'ChatDSC123'})
post(HOST, data={'login':True, 'username':'stasio14', 'password':'ChatDSC123'})
get(HOST, params={'create':True, 'name':'test'})
get(HOST, params={'join':True, 'room':'test', 'username':'stasio14'})
post(HOST, data={'send':True, 'room':'test', 'username':'anonymous', 'text':'Witam'})
