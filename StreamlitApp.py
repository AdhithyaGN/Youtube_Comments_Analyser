import streamlit as st
from src.youtube.Sentiment_Analyser_app import sentiment_analysis
from PIL import Image
from src.youtube.LLM_App import llm_app_sentiments








st.title('Youtube Comments Sentiment Analysis App')




video_link=st.text_input('Enter the Youtube url Here')

submit=st.button('Click to see results')










if submit :


    def get_youtube_thumbnail(video_link):
      
      video_id = video_link.split('v=')[-1]
      thumbnail=f"https://img.youtube.com/vi/{video_id}/0.jpg"
      return video_id,thumbnail
    


    video_id,thumbnail=get_youtube_thumbnail(video_link=video_link)







    

    

    sentiment_obj=sentiment_analysis()

    video_response=sentiment_obj.video_response(video_id=video_id)
    #comments=sentiment_obj.comments(response=video_response)
    data=sentiment_obj.sentiments_dataframe(data=video_response)

    pos_count=data[data['sentiments']==2].shape[0]
    neg_count=data[data['sentiments']==1].shape[0]
    neu_count=data[data['sentiments']==0].shape[0]


    pos_image=Image.open("C:/Users/S K E F/Desktop/GenAI/projects/Youtube_Comments_Analyser/icons/pos.png")
    neg_image=Image.open("C:/Users/S K E F/Desktop/GenAI/projects/Youtube_Comments_Analyser/icons/neg.png")
    neu_image=Image.open("C:/Users/S K E F/Desktop/GenAI/projects/Youtube_Comments_Analyser/icons/neu.png")

    st.header('Sentiment Counts')

    #st.image(thumbnail, caption="YouTube Video Thumbnail",width=300)

    col1,col2,col3,col4=st.columns(4)

    with col1:
        st.image(pos_image,width=100)
        st.metric(label='Positive',value=pos_count)

    with col2:
        st.image(neu_image,width=100)
        st.metric(label='Neutral',value=neu_count)
    
    with col3:
        st.image(neg_image,width=100)
        st.metric(label='Negative',value=neg_count)
    with col4:
        st.image(thumbnail, caption="YouTube Video Thumbnail",width=300)



    with st.sidebar:
        st.title('Comments Summary')

        app=llm_app_sentiments()

        text=app.text_extractor(data)

        chunks=app.text_splitter(text)

        summary=app.summary(chunks)


        st.write(summary)










