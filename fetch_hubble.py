import requests
import os

DIR_PATH = 'images/'
HUBBLESITE_API_URL = 'http://hubblesite.org/api/v3/image/'


def get_image_extension(image_url):
    image_extension = os.path.splitext(image_url)
    return image_extension[1]


def fetch_hubble_photos(image_id):
    response = requests.get(f'{HUBBLESITE_API_URL}{image_id}')
    response.raise_for_status()
    api_response = response.json()
    urls = api_response['image_files']
    image_url = f"https:{urls[-1]['file_url']}"

    with open(f'{DIR_PATH}{image_id}.{get_image_extension(image_url)}', 'wb') as file:
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
        for image_record in api_response:
            fetch_hubble_photos(image_record['id'])


def main():
    directory = os.path.dirname(DIR_PATH)
    os.makedirs(directory, exist_ok=True)
    load_hubble_collections()


if __name__ == "__main__":
    main()
