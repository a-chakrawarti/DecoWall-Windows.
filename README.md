# DecoWall-Windows
**Version 0.0.2**

## Changelog v0.0.2
* Added dark mode

## Introduction & Features
* This is a GUI implemented Desktop wallpaper changer using [PyQt5](https://pypi.org/project/PyQt5/), which includes [PRAW's](https://github.com/praw-dev/praw) API to get images from subreddits and download them using [requests](https://github.com/psf/requests).
* Extra functionalities like [Windows 10 Toast Notifications](https://github.com/jithurjacob/Windows-10-Toast-Notifications) was used which provides background process information to the user. 
* To add global hotkey support [keyboard](https://github.com/boppreh/keyboard) was used.
![createapp](/screenshots/ui.png)
* Move to System tray and execute commands from there.

## How to use

Clone the repository ```git clone https://github.com/a-chakrawarti/DecoWall-for-Windows``` or download and extract the [zip](https://github.com/a-chakrawarti/DecoWall-for-Windows/archive/master.zip).

* Now ```cd DecoWall-for-Windows```

* If you don't have virtualenv installed do, ```pip install virtualenv```.

* If you have python>=3.6 installed, do ```python -m venv [virtualenv]```, this will create a virtual environment of python having the same version as your installed one with pip and setuptools package.

* [Optional] To make copy of all the packages of system-site python directory ```python -m venv [virtualenv] system-site-packages```.

* After this activate the virtual environment, ```[virtualenv]\Scripts\activate.bat```. Similarly, you can deactivate using ```[virtualenv]\Scripts\deactivate.bat``` or simply ```deactivate```.

* Moving forward, now to install all the dependencies for the project ```pip install -r requirements.txt```.

* Run the ```python main.py```

## Configuration
* To download images using Reddit's API you have to get your ```client_id``` and ```client_secret``` from https://www.reddit.com/prefs/apps.
![createapp](/screenshots/reddit_1.png)

* Once you get your ```client_id``` and ```client_secret``` as shown in the screenshot, copy and paste their respective values in ```config.json``` file against each key.![createapp](/screenshots/reddit_2.png)
```sh
{
  "config": {
    "client_id": "pVJNRLN7ra20Kg",
    "client_secret": "bWHH-ZEnxIABQZX2HdZX-4S8CLA",
    ...
}
```
* Now you will be able to add subreddits and download them.
* As of this version, you will be able to download only 5 images from each subreddit from "hot" category.

## License
Licensed under [GNU General Public License v3.0](LICENSE)
