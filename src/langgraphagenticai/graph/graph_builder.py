from langgraph.graph import StateGraph
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraphagenticai.tools.search_tool import get_tools, create_tool_nodes
from langgraph.graph import START, END
from langgraph.prebuilt import tools_condition , ToolNode
from src.langgraphagenticai.nodes.chatbot_with_tool_node import ChatbotWithToolNode

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


    def chatbot_with_tools_build_graph(self):
        """
        Build a chatbot graph with tools.
        """

        ## Define the tools and tool nodes here 
        tools = get_tools()
        tool_node = create_tool_nodes(tools)

        # Define the llm
        llm = self.llm
        # Define the chatbot node with tools
        obj_chatbot_with_tools = ChatbotWithToolNode(llm)
        chatbot_node_tool = obj_chatbot_with_tools.create_chatbot(tools)

        self.graph_builder.add_node("chatbot",chatbot_node_tool)
        self.graph_builder.add_node("tools", tool_node)

        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edges("chatbot",tools_condition)
        self.graph_builder.add_edge("tools", "chatbot")
        self.graph_builder.add_edge("chatbot", END)


    def setup_graph(self, usecase):
        """
        Setup the graph based on the use case.
        """
        if usecase == "Basic Chatbot":
            self.basic_chatot_build_graph()
        elif usecase == "Chatbot with web":
            self.chatbot_with_tools_build_graph()

        return self.graph_builder.compile()