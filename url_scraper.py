import os
import sys
file_path = os.path.dirname(__file__)
module_path = os.path.join(file_path, "lib")
sys.path.append(module_path)

import time
from selenium import webdriver
from time import sleep
import youtube_scraper

driver = webdriver.Chrome()
driver.get('https://www.youtube.com/')
p_url = None 

print('TRY TO STAY OUT OF PLAYLISTS, BUT IF YOU GO IN ONE,')
print("IF IT DOESN'T WORK, HIT CTRL-C HERE AND IT MIGHT WORK.")
print('BUT WHATEVER YOU DO, DO NOT OPEN ANOTHER TAB!!!\n')
print('YT URL SCRAPER STARTING...')
while True:
    sleep(5)
    url = str(driver.current_url)
    if url == p_url:
        pass 
    elif 'youtube.com/watch' in url:
        print("VALID: "+url)
        with open('url.txt', 'w') as fw:
            fw.write(url)
        youtube_scraper.query()
    else:
        print("INVALID: "+url+'\n')
        with open('title.txt', 'w') as fw:
            fw.write(' ( Not Selected Yet... )                                                            ')
    p_url = driver.current_url
