import os
from dotenv import load_dotenv
from src.youtube.Sentiment_Analyser_app import sentiment_analysis
from src.youtube.logger import logging
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
import google.generativeai as genai


load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))



class llm_app_sentiments:
    def __init__(self) -> None:
        pass

    def text_extractor(self,df):

        text=""
        for i in df['text']:
            text+=i

        return text
    

    def text_splitter(self,text):
        text_splitter=RecursiveCharacterTextSplitter(chunk_size=10000,chunk_overlap=1000)
        chunks=text_splitter.create_documents([text])

        return chunks
    
    def summary(self,chunks):


        template="""You are a youtube video comment analyser and summarizer who will analyse the comments and correctly deliver the summary including feedbacks from the viewers,positive comments summary,negative comments summary
        what are the changes has to be done to correct in making the video,important keywords from the comments etc.All comments in a text form is given below
        text:{text}"""

        prompt=PromptTemplate(input_variables=['text'],template=template)

        model = ChatGoogleGenerativeAI(model="gemini-pro",
                             temperature=0.3)

        chain=load_summarize_chain(llm=model,chain_type='stuff',prompt=prompt,verbose=False)

        summary=chain.run(chunks)

        return summary
    



