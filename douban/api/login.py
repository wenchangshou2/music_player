# -*- coding:utf-8 -*-
import requests
#import curses
from PIL import Image

from douban.exceptions import ApiError

#screen=curses.initscr()
HEADERS = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
'''
def get_parm(paompt_string):
    curses.clear()
    screen.border(0)
    screen.addstr(2,2,paompt_string)
    screen.refresh()
    input=screen.getstr(10,10,60)
    return input
'''
def show_login():
    email=str(raw_input('user:'))
    password=str(raw_input('password'))

    captcha_id=get_captcha_id()
    get_captcha_pic(captcha_id)
    file_path='/tmp/yzm.jpg'
    img=Image.open(file_path)
    img.show()

#def request_token():


def get_captcha_id():
    url='https://douban.fm/j/new_captcha'
    option={

    }
    try:
        r=requests.get(url).text
        return r.strip('"')
    except Exception as e:
        raise(ApiError('get_captcha_id error'+e))
def get_captcha_pic(captcha_id):
    url='https://douban.fm/misc/captcha'
    options={
        'size':'m',
        'id':captcha_id
    }
    r=requests.get(url,headers=HEADERS,params=options)
    if r.status_code==200:
        path='/tmp/yzm.jpg'
        print 'DownLoad aptcha_pic'+path
        with open(path,'wb') as f:
                f.write(r.content)
    else:
        print('get Captcha_pic '+r.status_code)



show_login()
'''
def test_get_captcha_id():
    print(get_captcha_id())
def test_get_captcha_pic():
    id=get_captcha_id()
    get_captcha_pic(id)

test_get_captcha_pic()
'''