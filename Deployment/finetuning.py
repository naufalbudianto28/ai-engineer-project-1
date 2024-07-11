# Conversational Q&A Chatbot
import streamlit as st

from langchain.schema import HumanMessage,SystemMessage,AIMessage
from langchain.chat_models import ChatOpenAI

from dotenv import load_dotenv

import os

# Streamlit UI
st.set_page_config(page_title="Conversational Q&A Chatbot")
st.header("Hey, Let's Chat")
load_dotenv()
KEY=os.getenv("OPEN_AI_MONGO")
chat=ChatOpenAI(model="ft:gpt-3.5-turbo-0125:personal:bluebca-bot:9goQzaqQ", openai_api_key=KEY, temperature=0)


if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages']=[
        SystemMessage(content="You work as a customer service representative at Blu, a digital banking service provided by BCA. Your responsibility is to give accurate answers to customer questions. All responses should be in Indonesian and based on data that was already given. Your responses should be polite, professional, and helpful. Don’t answer to any questions or inquiries that are not related to blu BCA or BCA digital banking. And do not explain any application outside blu bca digital banking")
    ]

# Function to load OpenAI model and get respones
def get_chatmodel_response(question):

    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer=chat(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content

input=st.text_input("Input: ",key="input")
response=get_chatmodel_response(input)

submit=st.button("Ask the question")

# If ask button is clicked
if submit:
    st.subheader("The Response is")
    st.write(response)