import os
import requests

DIR_PATH = 'images'
HUBBLESITE_API_URL = 'http://hubblesite.org/api/v3/image/'


def fetch_hubble_photo(image_id, directory, hubblesite_api_url):
    response = requests.get(f'{hubblesite_api_url}{image_id}')
    response.raise_for_status()
    api_response = response.json()
    urls = api_response['image_files']
    image_url = f"https:{urls[-1]['file_url']}"
    url_part, image_extension = os.path.splitext(image_url)

    with open(os.path.join(directory, f'{image_id}{image_extension}'), 'wb') as file:
        image_response = requests.get(image_url, verify=False)
        image_response.raise_for_status()
        file.write(image_response.content)


def load_hubble_collections(directory, hubblesite_api_url):
    collections = [
        'spacecraft',
        'news',
        'printshop',
        'stsci_gallery',
        'holiday_cards',
        'wallpaper',
    ]
    parameters = {
        'page': 'all',
    }
    for collection in collections:
        response = requests.get(f'http://hubblesite.org/api/v3/images/{collection}', params=parameters)
        response.raise_for_status()
        api_response = response.json()
        for image_record in api_response:
            fetch_hubble_photo(image_record['id'], directory, hubblesite_api_url)


def main():
    os.makedirs(DIR_PATH, exist_ok=True)
    try:
        load_hubble_collections(DIR_PATH, HUBBLESITE_API_URL)
    except requests.exceptions.HTTPError as error:
        exit('Ошибка:\n{0}'.format(error))


if __name__ == "__main__":
    main()
