#todo ResponseException: which gets raised when credentials are not configured

# Standard Libraries
import os
import concurrent.futures

# 3rd Party Libraries
import praw
from prawcore import NotFound, exceptions
import requests

# Custom Libraries
from staticmethods import get_config

# Global Variables
image_title = []
image_url = []


reddit = praw.Reddit(client_id=get_config('client_id'),
                     client_secret=get_config('client_secret'),
                     user_agent='DecoWall'
                     )

download_path = os.path.join(os.getcwd(), 'downloaded')
if not os.path.exists(download_path):
    os.mkdir(download_path)

'''Download images from subreddit'''


def reddit_crawl(subreddit_list):
    """
    crawls the image name and url
    :param: subreddit_list: list
    :return:
    """

    # for key, value in subreddit_list.items():   dict implementation
    for key in subreddit_list:
        subreddit = reddit.subreddit(key)
        subreddit_data = subreddit.hot(limit=5)  # value hard-coded to 5
        for submission in subreddit_data:
            image_title.append(submission.title)
            image_url.append(submission.url)


def requests_download(image_name, image_url):
    """
    requests to download image using url and renames files
    :param image_name: str
    :param image_url: str
    :return:
    """
    r = requests.get(image_url, allow_redirects=True)
    image_path = os.path.join(download_path, image_name[:15]+'.'+image_url.split('.')[-1].split('?')[0])
    with open(image_path, 'wb') as file:
        file.write(r.content)


def image_download_execute(subreddit_list):
    """
    downloads images in a thread
    :param subreddit_list: list
    :return:
    """
    reddit_crawl(subreddit_list)
    # print(image_title, '-', image_url, '\n')
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(requests_download, image_title, image_url)


def sub_exists(sub):
    """
    checks if subreddit exists or not except RequestException, NotFound
    :param sub: str
    :return: bool
    """
    exists = True
    try:
        reddit.subreddits.search_by_name(sub, exact=True)
    except NotFound or exceptions.RequestException:
        exists = False
    return exists
