import requests
from bs4 import BeautifulSoup
import json
import re
import os
from Config import *


def get_song_id(singer_id):
    singer_url = 'http://music.163.com/artist?id=' + str(singer_id)
    r = requests.get(singer_url, headers=HEADERS).text
    soup = BeautifulSoup(r, 'lxml')
    song_ids = soup.find('textarea').text
    song_josn = json.loads(song_ids)
    for item in song_josn:
        lrc = get_all_lyrics(item['id'])
        write_to_file(lrc, item['name'], item['id'])





def get_all_lyrics(music_id):
    url = 'http://music.163.com/api/song/lyric?' + 'id=' + str(music_id)+ '&lv=1&kv=1&tv=-1'
    r = requests.get(url, headers=HEADERS)
    json_obj = r.text
    try:
        j = json.loads(json_obj)
        lrc = j['lrc']['lyric']
        pat = re.compile(r'\[.*\]')
        lrc = re.sub(pat, "", lrc)
        lrc = lrc.strip()
    except Exception:
        print('未获取歌词，music_id' + str(music_id))
        lrc = ''
    finally:
        return lrc


def write_to_file(lrc, song_name, song_id):
    if lrc != '':
        filename = str(song_name) + str(song_id) + '.txt'
        try:
            with open('./lyrics/'+filename, 'w') as f:
                f.write(lrc)
        except Exception:
            print('写入文件失败，song_name='+ song_name,)
