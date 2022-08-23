import os
from YaWeathers import YaWeather


def write_weather():

    with open('weather.txt', 'w') as file:
        weather = YaWeather(os.environ.get('KEY'))
        temp = weather.get_weathers()['fact']['temp']
        feels_like = weather.get_weathers()['fact']['feels_like']
        file.write(f'Температура в Магнитогорске сейчас {temp} а ощушается как {feels_like}')
        return temp, feels_like


if __name__ == '__main__':
    write_weather()