import os
import requests

DIR_PATH = 'images'
SPACEX_API_URL = 'https://api.spacexdata.com/v4/launches'


def fetch_spacex_last_launch(directory, spacex_api_url):
    address = '/latest'
    full_url = f'{spacex_api_url}{address}'
    response = requests.get(full_url)
    response.raise_for_status()
    api_response = response.json()
    urls = api_response['links']['flickr']['original']

    for photo_number, photo_url in enumerate(urls):
        with open(os.path.join(directory, f'spacex{photo_number}.jpg'), 'wb') as file:
            get_image = requests.get(photo_url)
            get_image.raise_for_status()
            file.write(get_image.content)


def main():
    directory = DIR_PATH
    os.makedirs(directory, exist_ok=True)
    try:
        fetch_spacex_last_launch(directory, SPACEX_API_URL)
    except requests.exceptions.HTTPError as error:
        exit('Ошибка:\n{0}'.format(error))


if __name__ == "__main__":
    main()
