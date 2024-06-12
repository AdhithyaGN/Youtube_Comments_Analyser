import streamlit as st
from src.youtube.Sentiment_Analyser_app import sentiment_analysis




st.title('Youtube Sentiment Analysis App')

video_id=st.text_input('Enter the Video Id Here')

submit=st.button('Click to see the results')

if submit :

    sentiment_obj=sentiment_analysis()

    video_response=sentiment_obj.video_response(video_id=video_id)
    comments=sentiment_obj.comments(response=video_response)

    st.write(comments)





