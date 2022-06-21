from googleapiclient.discovery import build

api_key = "AIzaSyC740qwOUgQ0L3bUgIwuhIQT1rTG1HuELU"
channel_id = 'UCCezIgC97PvUuR4_gbFUs5g'
video_id = 'th5_9woFJmk'
Username = 'schafer5'
channel_name = 'Corey Schafer'

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.videos().list(
    part="contentDetails",
    id=video_id
)

response = request.execute()
print(response)
