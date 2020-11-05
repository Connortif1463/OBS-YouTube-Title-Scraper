import os
import sys
file_path = os.path.dirname(__file__)
module_path = os.path.join(file_path, "lib")
sys.path.append(module_path)

import argparse
# import constants # API-Key Variable
import key # API-Key Variable
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import url_parser 

# DEVELOPER_KEY = constants.API_KEY
DEVELOPER_KEY = key.API_KEY
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def youtube_search(options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    
    with open('url.txt') as fr:
        url = fr.read()
        items = youtube.videos().list(
            part='id,snippet',
            id=url_parser.parse_vid_id(url),
            maxResults=1
        ).execute()

    for item in items.get('items', []):
        if item['kind'] == 'youtube#video':
            video = item['snippet']['title']
            with open('title.txt', 'w', encoding='utf-8') as fw:
                if '&amp;' in video:
                    video_s = video.replace('&amp;','&')
                    print(video_s+'\n')
                    fw.write(video_s)
                else:
                    print(video+'\n')
                    fw.write(video)

def query():
    parser = argparse.ArgumentParser()
    parser.add_argument('--q', help='Search term', default='Google')
    parser.add_argument('--max-results', help='Max results', default=25)
    args = parser.parse_args()

    try:
        youtube_search(args)
    except(HttpError):
        print('An HTTP error occurred:')
        print('Daily quota probably exceeded, or url not processed correctly.')
