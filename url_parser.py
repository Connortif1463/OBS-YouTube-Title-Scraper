import re

def parse_vid_id(url):
    result = re.match('^[^v]+v=(.{11}).*', url)
    #print('ID: '+result.group(1))
    return result.group(1)

# sample regex test:
#parse_vid_id('https://www.youtube.com/watch?v=KYncAtMZdk8')
