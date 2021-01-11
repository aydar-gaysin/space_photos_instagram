import requests
import os

DIR_PATH = 'images/'
SPACEX_API_URL = 'https://api.spacexdata.com/v4/launches'


def fetch_spacex_last_launch():
    address = '/latest'
    full_url = f'{SPACEX_API_URL}{address}'
    response = requests.get(full_url)
    response.raise_for_status()
    api_response = response.json()
    urls = api_response['links']['flickr']['original']

    for photo_number, photo_url in enumerate(urls):
        with open(f'{DIR_PATH}spacex{photo_number}.jpg', 'wb') as file:
            get_image = requests.get(photo_url)
            get_image.raise_for_status()
            file.write(get_image.content)


def main():
    directory = os.path.dirname(DIR_PATH)
    os.makedirs(directory, exist_ok=True)
    try:
        fetch_spacex_last_launch()
    except requests.exceptions.HTTPError as error:
        exit('Ошибка:\n{0}'.format(error))


if __name__ == "__main__":
    main()
