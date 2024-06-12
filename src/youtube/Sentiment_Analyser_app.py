import googleapiclient.discovery
import googleapiclient.errors
from dotenv import load_dotenv
import os
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')
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
        self.comments=[]

        youtube=googleapiclient.discovery.build(serviceName=self.api_service_name,version=self.api_version,developerKey=self.api)

        request=youtube.commentThreads().list(part='snippet',
                                              videoId=self.video_id,maxResults=1000)
        
        while request:
            response=request.execute()
            for item in response['items']:
                comment=item['snippet']['topLevelComment']['snippet']
                self.comments.append({
                    'author':comment['authorDisplayName'],
                    'text':comment['textOriginal']
                    
                })
            request=youtube.commentThreads().list_next(request,response)

        return pd.DataFrame(self.comments)
        
        

    
    
    
    def sentiments_dataframe(self,data):
        self.df=data

        self.senti_analyser_obj=SentimentIntensityAnalyzer()
        self.df['positive']=[self.senti_analyser_obj.polarity_scores(i)['pos'] for i in self.df['text']]
        self.df['negative']=[self.senti_analyser_obj.polarity_scores(i)['neg'] for i in self.df['text']]
        self.df['neutral']=[self.senti_analyser_obj.polarity_scores(i)['neu'] for i in self.df['text']]
        self.df['compound']=[self.senti_analyser_obj.polarity_scores(i)['compound'] for i in self.df['text']]

        self.pol_values=list(self.df['compound'])

        self.sentiment=[]

        for i in self.pol_values:
            if i>0.05:
                self.sentiment.append(2)
            elif i<-0.05:
                self.sentiment.append(1)
            else:
                self.sentiment.append(0)

        self.df['sentiments']=self.sentiment

        return self.df
    
    


    





