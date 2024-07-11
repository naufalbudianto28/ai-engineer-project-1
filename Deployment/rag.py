import streamlit as st
from pymongo import MongoClient
from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import os

# Loading Environment Variables
load_dotenv()
KEY = os.getenv("OPEN_AI_MONGO")

# Initialize MongoDB Python Client
client = MongoClient("mongodb+srv://Maverick:anakbimbinganmasdanu@cluster0.muggb2k.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Access Collection
collection = client['Maverick']['Maverick_DB']

# Initialize Vector Search MongoDB
vectorStore = MongoDBAtlasVectorSearch(
    collection, OpenAIEmbeddings(openai_api_key=KEY), index_name='vector_index'
)

# Define the Model
llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=KEY, temperature=0)

prompt = "You work as a customer service representative at Blu, a digital banking service provided by BCA. Your responsibility is to give accurate answers to customer questions. All responses should be in Indonesian and based on data that was already given. Your responses should be polite, professional, and helpful. Don’t answer to any questions or inquiries that are not related to blu BCA or BCA digital banking. And do not explain any application outside blu bca digital banking"

# Define QA retrieval
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type='stuff',
    retriever=vectorStore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3}
    )
)

# Streamlit UI
st.title("Blu Customer Service Chatbot")
st.write("Ask any question related to Blu, BCA, or BCA digital banking.")

question = st.text_input("Your Question:")

if st.button("Get Answer"):
    result = qa({"query": question})
    st.write("Answer:", result["result"])
 