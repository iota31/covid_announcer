import COVID19Py
import time
from gtts import gTTS
import os
import datetime as dt
import urllib.request
import json

def generate_audio(text):
    language = 'en'
    while True:
        try:
            myobj = gTTS(text=text, lang=language, slow=False)
        except Exception as e:
            time.sleep(60)
        else:
            break
    myobj.save("corona.mp3")
    os.system("ffplay -nodisp -autoexit open.mp3 >/dev/null 2>&1")
    os.system("ffplay -nodisp -autoexit corona.mp3 >/dev/null 2>&1")

def fetch_data():
    with urllib.request.urlopen("https://api.covid19india.org/data.json") as url:
        data = json.loads(url.read().decode())
    return data['statewise'][0]
    

def main():
    start_time = dt.time(hour=9)
    end_time = dt.time(hour=22)
    covid19 = COVID19Py.COVID19()
    india_data = fetch_data()
    generate_audio('As of now the number of active cases in India are %d, number of deaths due to coronavirus are %d, and number of \
            patients that have recovered are %d' %(int(india_data['active']), int(india_data['deaths']),int(india_data['recovered'])))
    datetime_then = dt.datetime.now()
    print(india_data)
    while True:
        current_time = dt.datetime.now().time()
        if current_time >= start_time and current_time <= end_time:
            print('script is operational')
            while True:
                try:
                    india_data_latest = fetch_data()
                except Exception as e:
                    time.sleep(200)
                else:
                    break
            print(india_data_latest)
            print(india_data_latest != india_data)
            if india_data_latest != india_data:
                if int(india_data_latest['active']) != int(india_data['active']):
                    diff = int(india_data_latest['active']) - int(india_data['active'])
                    if diff < 0:
                        generate_audio('A good news, the number of active coronavirus cases in India has decreased by %d and the total now \
                            stands at %d' %(abs(diff), int(india_data_latest['active'])))
                    else:
                        generate_audio('A bad news, the number of active coronavirus cases in India has increased by %d and the total now \
                            stands at %d' %(abs(diff), int(india_data_latest['active'])))
                if int(india_data_latest['deaths']) != int(india_data['deaths']):
                    diff = int(india_data_latest['deaths']) - int(india_data['deaths'])
                    generate_audio('A bad news, the number of deaths due to coronavirus cases in India has increased by %d and the total \
                            now stands at %d' %(diff, int(india_data_latest['deaths'])))
                if int(india_data_latest['recovered']) != int(india_data['recovered']):
                    diff = int(india_data_latest['recovered']) - int(india_data['recovered'])
                    generate_audio('A good news, the number of recovered coronavirus patients in India has increased by %d and the total \
                            now stands at %d' %(diff, int(india_data_latest['recovered'])))
                datetime_then = dt.datetime.now()
                india_data = india_data_latest
            if (dt.datetime.now() - datetime_then).total_seconds() >= 10800:
                generate_audio('A good news, There have been no new coronavirus cases in India since past 3 hours')
                datetime_then = dt.datetime.now()
        time.sleep(120)


if __name__ == '__main__':
    while True:
        try:
            main()
        except Exception as e:
            time.sleep(60)

