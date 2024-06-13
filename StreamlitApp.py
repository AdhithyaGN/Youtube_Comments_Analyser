import streamlit as st
from src.youtube.Sentiment_Analyser_app import sentiment_analysis
from PIL import Image
from src.youtube.LLM_App import llm_app_sentiments








st.title('Youtube CommentSentiment Analysis App')




video_id=st.text_input('Enter the Video Id Here')

submit=st.button('Click to see results')








if submit :




    

    

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

    st.header('Sentiment_Counts')

    col1,col2,col3=st.columns(3)

    with col1:
        st.image(pos_image,width=100)
        st.metric(label='Positive',value=pos_count)

    with col2:
        st.image(neu_image,width=100)
        st.metric(label='Neutral',value=neu_count)
    
    with col3:
        st.image(neg_image,width=100)
        st.metric(label='Negative',value=neg_count)



    with st.sidebar:
        st.title('Comment Summary')

        app=llm_app_sentiments()

        text=app.text_extractor(data)

        chunks=app.text_splitter(text)

        summary=app.summary(chunks)


        st.write(summary)










