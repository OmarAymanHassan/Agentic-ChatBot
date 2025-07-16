from langgraph.graph import StateGraph
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode

from langgraph.graph import START, END


class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)


    def basic_chatot_build_graph(self):
        """
        Build a basic chatbot graph.
        """
        self.basic_chatbot_node = BasicChatbotNode(self.llm)
        self.graph_builder.add_node(
            "chatbot",self.basic_chatbot_node.process)
        
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)

