import requests
import os

DIR_PATH = 'images/'
SPACEX_API_URL = 'https://api.spacexdata.com/v4/launches'


def ensure_dir():
    directory = os.path.dirname(DIR_PATH)
    if not os.path.exists(directory):
        os.makedirs(directory)
    return DIR_PATH


def fetch_spacex_last_launch():
    address = '/latest'
    full_url = f'{SPACEX_API_URL}{address}'
    response = requests.get(full_url)
    response.raise_for_status()
    api_response = response.json()
    urls_list = api_response['links']['flickr']['original']

    for photo_number, photo_url in enumerate(urls_list):
        with open(f'{ensure_dir()}spacex{photo_number}.jpg', 'wb') as file:
            file.write(requests.get(photo_url).content)


def main():
    fetch_spacex_last_launch()


if __name__ == "__main__":
    main()
