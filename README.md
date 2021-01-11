# Space Photos Instagram

Scripts:
*fetch_spacex.py,
fetch_hubble.py*
download photos from latest SpaceX launch, space photos from Hubble site through appropriate APIs. 

Code *upload_photos.py* resizes downloaded images to match Instagram aspect ratio and uploads them to given IG profile.

### How to install

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

For *upload_photos.py* you should create .env file with account data:
```
IG_USERNAME=<Your Instagram login here>
IG_PASSWORD=<Your Instagram password here>
``` 

### How to use

To resize photo with *upload_photos.py* script start it from CLI using *resize* key:
```
upload_photos.py resize
``` 
To upload photo with *upload_photos.py* script start it from CLI using *upload* key:
```
upload_photos.py upload
``` 

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
