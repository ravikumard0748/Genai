from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from  langchain_core.output_parsers import StrOutputParser

import streamlit as st

import os
from dotenv import load_dotenv
load_dotenv()


os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] 

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpful assistant Give the answers for the user query"),
        ("user","Questions : {question}")
    ]
)

st.title("Langchain demo with the open ai api")
input_text = st.text_input("Search the topic u want")

llm = ChatGroq(model="openai/gpt-oss-20b")
output_parser = StrOutputParser() 

chain = prompt | llm | output_parser  

if input_text:
    st.write(chain.invoke({'question':input_text}))     