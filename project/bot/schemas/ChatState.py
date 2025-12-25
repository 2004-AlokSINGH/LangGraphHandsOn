from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage, HumanMessage,AIMessage
from typing import Annotated, TypedDict


class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage],add_messages]
