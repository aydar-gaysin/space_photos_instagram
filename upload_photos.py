import argparse
import os
import requests
from os import listdir

from dotenv import load_dotenv
from instabot import Bot
from PIL import Image


DIR_PATH = 'images'


def resize_image(ig_username, ig_password, directory):
    for image_file in listdir(directory):
        image = Image.open(os.path.join(directory, image_file))
        image.thumbnail((1080, 1080))
        image_name = os.path.splitext(image_file)
        image.save(os.path.join(directory, f'{image_name[0]}.jpg'), format='JPEG')


def upload_picture(ig_username, ig_password, directory):
    bot = Bot()
    bot.login(username=ig_username, password=ig_password)
    for image_file in listdir(directory):
        bot.upload_photo(os.path.join(directory, image_file))
        response = bot.api.last_response
        response.raise_for_status()


def create_parser():
    parser = argparse.ArgumentParser(
        description='Скрипт изменяет размер изображений в папке images для соответствия Instagram aspect ratio, '
                    ' либо с помощью Instabot загружает изображения из папки images в профиль Instagram'
    )
    subparsers = parser.add_subparsers()
    resize_parser = subparsers.add_parser('resize', help='Введите для изменения размера изображений в папке images'
                                                         ' для соответствия Instagram aspect ratio')
    resize_parser.set_defaults(func=resize_image)
    upload_parser = subparsers.add_parser('upload', help='Введите для загрузки изображений из папки images в профиль'
                                                         ' Instagram')
    upload_parser.set_defaults(func=upload_picture)
    return parser


def main():
    load_dotenv()
    ig_username = os.getenv('IG_USERNAME')
    ig_password = os.getenv('IG_PASSWORD')
    parser = create_parser()
    selected_function = parser.parse_args()
    directory = os.path.join(DIR_PATH)
    try:
        selected_function.func(ig_username, ig_password, directory)
    except requests.exceptions.HTTPError as error:
        exit('Ошибка:\n{0}'.format(error))


if __name__ == "__main__":
    main()
