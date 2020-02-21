# DecoWall Windows
**Version 0.2**

## Changelog v 0.2
* Added default dark mode

## Introduction & Features
* This is a GUI based Desktop wallpaper changer.
* Download images from max-6 user provided subreddits, 5 each from "hot" category.
* Automatic wallpaper change after X minutes.
* System tray support
* Add wallpapers to "Favourites" for quick access.

## Third Party Libraries: 
* [PyQt5](https://pypi.org/project/PyQt5/) for GUI
* [PRAW's](https://github.com/praw-dev/praw) to make reddit API calls and get image(title, url) from subreddits
* [requests](https://github.com/psf/requests) to download images
* [Windows 10 Toast Notifications](https://github.com/jithurjacob/Windows-10-Toast-Notifications)
* [keyboard](https://github.com/boppreh/keyboard) global hotkey support

## In-built Libraries:
* collections
* json
* os
* threading
* logging
* shutil
* random
* socket
* ctypes
* sys
* concurrent.futures

## UI/UX


![createapp](/screenshots/ui.png)



## How to use

Clone the repository ```git clone https://github.com/a-chakrawarti/DecoWall-Windows``` or download and extract the [zip](https://github.com/a-chakrawarti/DecoWall-Windows/archive/master.zip).

* Now ```cd DecoWall-Windows```

* If you don't have virtualenv installed do, ```pip install virtualenv```.

* If you have python>=3.6 installed, do ```python -m venv <your_env>```, this will create a virtual environment of python having the same version as your installed one with pip and setuptools package.

* Optional: To make copy of all the packages of system-site python directory ```python -m venv <your_env> system-site-packages```.

* After this activate the virtual environment, ```<your_env>\Scripts\activate.bat```. Similarly, you can deactivate using ```<your_env>\Scripts\deactivate.bat``` or simply ```deactivate```.

* Moving forward, now to install all the dependencies for the project ```pip install -r requirements.txt```.

* Run the ```python main.py```

## Configuration
* To download images using Reddit's API you have to get your ```client_id``` and ```client_secret``` from https://www.reddit.com/prefs/apps.


![createapp](/screenshots/reddit_1.png)

* Once you get your ```client_id``` and ```client_secret``` as shown in the screenshot, copy and paste their respective values in ```config.json``` file against each key.


![createapp](/screenshots/reddit_2.png)


```sh
{
    "client_id": "pVJNRLN7ra20Kg",
    "client_secret": "bWHH-ZEnxIABQZX2HdZX-4S8CLA",
    ...
}
```

## Shortcut Keys
-- Arrow keys [Only foreground]
* Left/Righ : navigate images in the directories
* Up : add to favourites directory
* Down : set current image as Wallpaper

-- Modifiers [Global Support/Background]
* Ctrl+Left/Ctrl+Right : set next image as wallpaper
* Ctrl+Down : download images
* Ctrl+Up : add to favourites
* Ctrl+Shift+S : shuffle images

## Note
* To enable system tray, click on "Activate System Tray" option and close the application.

## License
Licensed under [GNU General Public License v3.0](LICENSE)
