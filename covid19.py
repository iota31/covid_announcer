import COVID19Py
import time
from gtts import gTTS
import os
import datetime as dt


def generate_audio(text):
    language = 'en'
    myobj = gTTS(text=text, lang=language, slow=False)
    myobj.save("corona.mp3")
    os.system("ffplay -nodisp -autoexit open.mp3 >/dev/null 2>&1")
    os.system("ffplay -nodisp -autoexit corona.mp3 >/dev/null 2>&1")

def main():
    covid19 = COVID19Py.COVID19()
    india_data = covid19.getLocationByCountryCode('IN')[0]['latest']
    generate_audio('As of now the number of confirmed cases in India are %d, number of deaths due to coronavirus are %d, and number of patients that \
            have recovered are %d' %(int(india_data['confirmed']), int(india_data['deaths']),int(india_data['recovered'])))
    datetime_then = dt.datetime.now()
    while True:
        india_data_latest = covid19.getLocationByCountryCode('IN')[0]['latest']
        if india_data_latest != india_data:
            if int(india_data_latest['confirmed']) != int(india_data['confirmed']):
                diff = int(india_data_latest['confirmed']) - int(india_data['confirmed'])
                generate_audio('A bad news, the number of confirmed coronavirus cases in India has increased by %d and the total now stands at %d' \
                        %(diff, int(india_data_latest['confirmed'])))
            if int(india_data_latest['deaths']) != int(india_data['deaths']):
                diff = int(india_data_latest['deaths']) - int(india_data['deaths'])
                generate_audio('A bad news, the number of deaths due to coronavirus cases in India has increased by %d and the total \
                        now stands at %d' %(diff, int(india_data_latest['deaths'])))
            if int(india_data_latest['recovered']) != int(india_data['recovered']):
                diff = int(india_data_latest['recovered']) - int(india_data['recovered'])
                generate_audio('A good news, the number of recovered coronavirus patients in India has increased by %d and the total \
                        now stands at %d' %(diff, int(india_data_latest['recovered'])))
            datetime = datetime.now()
        if (datetime_then - dt.datetime.now()).total_seconds() >= 10800:
            generate_audio('A good news, There have been no new coronavirus cases in India since past 3 hours')
            datetime = datetime.now()

if __name__ == '__main__':
    main()



    
    
