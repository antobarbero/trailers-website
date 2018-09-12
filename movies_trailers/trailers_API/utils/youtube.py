from googleapiclient.discovery import build

DEVELOPER_KEY = "AIzaSyBiMecYhUa-NRswgRCmgj-svlsAidGaYLA"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
SEARCH_CATEGORY = 'trailer'


def get_trailers(key_words):
    """Search for trailers on youtube and return a list of them."""
    youtube = build(
        YOUTUBE_API_SERVICE_NAME,
        YOUTUBE_API_VERSION,
        developerKey=DEVELOPER_KEY
    )

    search_response = youtube.search().list(
        q='{} - {}'.format(key_words, SEARCH_CATEGORY),
        part='id',
        maxResults=3,
        type='video'
    ).execute()

    videos = search_response.get("items", [])

    return videos
