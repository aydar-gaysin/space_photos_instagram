from os import listdir
import os
from PIL import Image
from dotenv import load_dotenv
from instabot import Bot

DIR_PATH = 'images/'


def image_processing():
    for file in listdir(DIR_PATH):
        image = Image.open(f'{DIR_PATH}{file}')
        x, y = image.size
        if x > y:
            height = (1080 * y) // x
            image.thumbnail((1080, height))
        elif x == y:
            image.thumbnail((1080, 1080))
        elif y > x:
            width = (1080 * x) // y
            image.thumbnail((width, 1080))
        image_name = file.split(sep='.')
        image.save(f'{DIR_PATH}{image_name[0]}.jpg', format='JPEG')


def pictures_upload():
    load_dotenv()
    ig_username = os.getenv('IG_USERNAME')
    ig_password = os.getenv('IG_PASSWORD')
    bot = Bot()
    bot.login(username=ig_username, password=ig_password)
    for file in listdir(DIR_PATH):
        bot.upload_photo(f'{DIR_PATH}{file}')
        if bot.api.last_response.status_code != 200:
            print(bot.api.last_response)


def main():
    # image_processing()
    pictures_upload()


if __name__ == "__main__":
    main()
