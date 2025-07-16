from langchain_tavily import TavilySearch
from langchain_community.tools.tavily_search import TavilySearchResults

from langgraph.prebuilt import ToolNode

def get_tools():
    """
    Get the tools available for the chatbot.
    """
    tools = [TavilySearchResults(max_results=2)]
    
    return tools

def create_tool_nodes(tools):
    """
    Create tool nodes for the chatbot.
    """
 
    
    return ToolNode(tools = tools)