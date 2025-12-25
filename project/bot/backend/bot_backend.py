from langgraph.graph import StateGraph,START,END
from langchain_groq import ChatGroq
from typing import TypedDict
import os
from dotenv import load_dotenv
from langgraph.graph import StateGraph,START,END
from typing import TypedDict,Annotated
from dotenv import load_dotenv
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import BaseMessage, HumanMessage,AIMessage
from campusX.bot.schemas.ChatState import ChatState

load_dotenv() ##  loading all the environment variable
groq_api_key=os.getenv("GROQ_API_KEY")

#get the model
model = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=groq_api_key,
    temperature=0,
    max_tokens=500 #can tune token as per need
)


def process_chat(state:ChatState):
    # take query of user
    # send to LLM
    # get ans and send to user
    message=state['messages']
    response=model.invoke(message)
    return {'messages':[response]}

memorysaver=MemorySaver()
graph=StateGraph(ChatState)

# add node
graph.add_node('chat_node',process_chat)

#
graph.add_edge(START,'chat_node') 
graph.add_edge('chat_node',END)

chatbot=graph.compile(checkpointer=memorysaver)

