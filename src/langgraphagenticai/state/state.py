


from pydantic import BaseModel, Field
from typing import Optional, List , Annotated,TypedDict,NotRequired
from langgraph.graph.message import add_messages


class State(TypedDict):
    """
    State class to hold the state of the application.
    """
    messages : Annotated[list,add_messages]
    news_data: NotRequired[list]
    summary: NotRequired[str]
    file_name: NotRequired[str]
    frequency: NotRequired[str]
