import requests
import os

DIR_PATH = 'images/'
HUBBLESITE_API_URL = 'http://hubblesite.org/api/v3/image/'


def get_image_extension(image_url):
    image_extension = image_url.split(sep='.')
    return image_extension[3]


def fetch_hubble_photos(id):
    response = requests.get(f'{HUBBLESITE_API_URL}{id}')
    response.raise_for_status()
    api_response = response.json()
    urls_list = api_response['image_files']
    image_url = f"https:{urls_list[-1]['file_url']}"

    with open(f'{DIR_PATH}{id}.{get_image_extension(image_url)}', 'wb') as file:
        file.write(requests.get(image_url, verify=False).content)


def load_hubble_collections():
    collections = [
        'holiday_cards',
        'wallpaper',
        'spacecraft',
        'news',
        'printshop',
        'stsci_gallery',
    ]
    for collection in collections:
        response = requests.get(f'http://hubblesite.org/api/v3/images/{collection}?page=all')
        response.raise_for_status()
        api_response = response.json()
        for image_number, image_record in enumerate(api_response):
            fetch_hubble_photos(image_record['id'])


def main():
    directory = os.path.dirname(DIR_PATH)
    os.makedirs(directory, exist_ok=True)
    load_hubble_collections()


if __name__ == "__main__":
    main()
