from apiclient.discovery import build
from urllib.parse import urlparse, parse_qs
from contextlib import suppress

DEVELOPER_KEY = "AIzaSyCSzJZjj3ObdJG6FfdwydmYT3j3HQqNZCI"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def yt_init(url):
    video_id = get_yt_id(url)
    print(video_id)
    return yt_video_comments(video_id)

def get_yt_id(url, ignore_playlist=False):
    query = urlparse(url)
    if query.hostname == 'youtu.be': return query.path[1:]
    if query.hostname in {'www.youtube.com', 'youtube.com', 'music.youtube.com'}:
        if not ignore_playlist:
            with suppress(KeyError):
                return parse_qs(query.query)['list'][0]
        if query.path == '/watch': return parse_qs(query.query)['v'][0]
        if query.path[:7] == '/watch/': return query.path.split('/')[1]
        if query.path[:7] == '/embed/': return query.path.split('/')[2]
        if query.path[:3] == '/v/': return query.path.split('/')[2]

def yt_video_comments(video_id):
    comments = []
    
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey = DEVELOPER_KEY)
    video_response = youtube.commentThreads().list(part = "snippet,replies",videoId = video_id).execute()    

    for item in video_response['items']:
        print(item['snippet']['topLevelComment']['snippet']['textDisplay'])
        comments.append(item['snippet']['topLevelComment']['snippet']['textDisplay'])

    # while video_response:
    #     for item in video_response['items']:
    #         print(item['snippet']['topLevelComment']['snippet']['textDisplay'])
    #         comments.append(item['snippet']['topLevelComment']['snippet']['textDisplay'])
    #     if 'nextPageToken' in video_response:
    #         video_response = youtube.commentThreads().list(part = "snippet,replies", videoId = video_id).execute()
    #     else: break
    #     if comments.count == 100: break

    return comments
        
def processor(process_request): 
    response = {
        "status": "waiting",
        "requst": process_request
    }
    return response
