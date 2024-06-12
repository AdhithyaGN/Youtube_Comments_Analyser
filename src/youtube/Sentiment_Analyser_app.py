import googleapiclient.discovery
import googleapiclient.errors
from dotenv import load_dotenv
import os
import pandas as pd
load_dotenv()

GOOGLE_YOUTUBE_API=os.environ['GOOGLE_YOUTUBE_API']


class sentiment_analysis:
    def __init__(self) -> None:
        pass

    def video_response(self,video_id):
        self.video_id=video_id
        self.api_service_name='youtube'
        self.api_version='v3'
        self.api=GOOGLE_YOUTUBE_API

        youtube=googleapiclient.discovery.build(serviceName=self.api_service_name,version=self.api_version,developerKey=self.api)

        request=youtube.commentThreads().list(part='snippet',
                                              videoId=self.video_id,maxResults=100)
        
        response=request.execute()

        return response
    
    def comments(self,response):
        self.response=response

        comments=[]
        for item in self.response['items']:
            comment=item['snippet']['topLevelComment']['snippet']
            comments.append([comment['authorDisplayName'],
                             comment['publishedAt'],
                             comment['updatedAt'],
                             comment['likeCount'],
                             comment['textDisplay']])
            
        df=pd.DataFrame(comments,columns=['author','published_at','updated_at','like_count','text'])

        return df
    


    





