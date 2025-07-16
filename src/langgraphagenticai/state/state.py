


from pydantic import BaseModel, Field
from typing import Optional, List , Annotated,TypedDict
from langgraph.graph.message import add_messages


class State(TypedDict):
    """
    State class to hold the state of the application.
    """
    messages : Annotated[list,add_messages]
    