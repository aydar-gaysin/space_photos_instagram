from os import listdir
import os
from PIL import Image
from dotenv import load_dotenv
from instabot import Bot

DIR_PATH = 'images/'


def resize_image():
    for image_file in listdir(DIR_PATH):
        image = Image.open(f'{DIR_PATH}{image_file}')
        x, y = image.size
        if x > y:
            height = (1080 * y) // x
            image.thumbnail((1080, height))
        elif x == y:
            image.thumbnail((1080, 1080))
        elif y > x:
            width = (1080 * x) // y
            image.thumbnail((width, 1080))
        image_name = os.path.splitext(image_file)
        image.save(f'{DIR_PATH}{image_name[0]}.jpg', format='JPEG')


def upload_picture():
    load_dotenv()
    ig_username = os.getenv('IG_USERNAME')
    ig_password = os.getenv('IG_PASSWORD')
    bot = Bot()
    bot.login(username=ig_username, password=ig_password)
    for image_file in listdir(DIR_PATH):
        bot.upload_photo(f'{DIR_PATH}{image_file}')
        response = bot.api.last_response
        if not response.ok:
            print(bot.api.last_response)


def main():
    # image_processing()
    pictures_upload()


if __name__ == "__main__":
    main()
