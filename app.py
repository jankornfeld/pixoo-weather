import json
from datetime import datetime

import requests
from PIL import Image, ImageDraw, ImageFont
from dotenv import dotenv_values
from pixoo import Pixoo

from functions import lineX, lineY, sun, rainy, dizzle, cloud, bigSun
from weatherresponse import weather_response_object_hook, WeatherResponse


def run():
    env = dotenv_values(".env")

    width, height = 64, 64
    background_color = (0, 0, 0)
    weekday = ['MO', 'DI', 'MI', 'DO', 'FR', 'SA', 'SO']

    image = Image.new("RGB", (width, height), background_color)
    font_small = ImageFont.truetype("3x5pixel.ttf", size=5)
    font_large = ImageFont.truetype("3x5pixel.ttf", size=10)
    draw = ImageDraw.Draw(image)

    weatherDataResponse = requests.get(
        'https://api.open-meteo.com/v1/forecast?latitude=' + env['LATITUDE'] + '&longitude=' + env[
            'LONGITUDE'] + '&current=temperature_2m,weather_code&daily=weather_code,temperature_2m_max,'
                           'temperature_2m_min&timezone=Europe%2FBerlin')

    weatherData: WeatherResponse = json.loads(str(weatherDataResponse.json()).replace('\'', '"'),
                                              object_hook=weather_response_object_hook)
    weatherDataDaily = weatherData.daily

    weatherDataDailyMin = weatherDataDaily.temperature_2m_min
    weatherDataDailyMax = weatherDataDaily.temperature_2m_max
    weatherDataDailyTime = weatherDataDaily.time
    weatherDataDailyWeatherCode = weatherDataDaily.weather_code

    result = [
        {
            'time': e,
            'min': round(weatherDataDailyMin[index]),
            'max': round(weatherDataDailyMax[index]),
            'weather': weatherDataDailyWeatherCode[index]
        }
        for index, e in enumerate(weatherDataDailyTime)
    ]

    for entry in result:
        print(entry)

    # Top row
    draw.text((1, 1), datetime.now().strftime('%d.%m'), (255, 255, 255), font=font_small)
    draw.text((25, 1), datetime.now().strftime('%H:%M'), (255, 255, 255), font=font_small)
    draw.text((55, 1), weekday[datetime.now().weekday()], (255, 255, 255), font=font_small)

    for coordinates in lineX(0, 64, 35):
        image.putpixel(coordinates, (100, 100, 100))

    # Middle row
    for coordinates, color in bigSun(5, 12):
        image.putpixel(coordinates, color)

    draw.text((32, 13), str(weatherData.current.temperature_2m) + '°', (255, 255, 255), font=font_large)
    draw.text((35, 26), str(result[0]['max']) + '°', (255, 255, 255), font=font_small)
    draw.text((48, 26), str(result[0]['min']) + '°', (200, 200, 200), font=font_small)

    for coordinates in lineY(26, 5, 45):
        image.putpixel(coordinates, (150, 150, 150))

    for coordinates in lineX(0, 64, 8):
        image.putpixel(coordinates, (100, 100, 100))

    # Bottom row
    result.pop(0)
    for index, entry in enumerate(result):
        x = int(index * (64 / len(result))) + 1
        y = 37

        weekdayNumber = datetime.strptime(entry['time'], '%Y-%m-%d').weekday()

        if weekdayNumber == 3:
            x += 1

        draw.text((x, y), weekday[weekdayNumber], (255, 255, 255), font=font_small)
        if entry['weather'] == 0:
            for coordinates, color in sun(x, y + 6):
                image.putpixel(coordinates, color)
        elif 1 <= entry['weather'] <= 3:
            for coordinates, color in sun(x + 1, y + 6):
                image.putpixel(coordinates, color)
            for coordinates, color in cloud(x, y + 8):
                image.putpixel(coordinates, color)
        # elif entry['weather'] == 3:
        #    for coordinates, color in cloud(x,y+6):
        #        image.putpixel(coordinates, color)
        elif entry['weather'] == 80:
            for coordinates, color in dizzle(x, y + 6):
                image.putpixel(coordinates, color)
        elif entry['weather'] > 60:
            for coordinates, color in rainy(x, y + 6):
                image.putpixel(coordinates, color)

        draw.text((x, y + 15), str(entry['max']) + '°', (255, 255, 255), font=font_small)
        draw.text((x, y + 21), str(entry['min']) + '°', (200, 200, 200), font=font_small)

    if env['PREVIEW'] == 'True':
        image.show()
    image.save('image.png')

    pixoo = Pixoo(env['HOST'], 64, False)

    pixoo.draw_image_at_location(image, 0, 0)
    pixoo.push()


run()
