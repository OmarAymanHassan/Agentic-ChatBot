from langgraph.graph import StateGraph
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraphagenticai.tools.search_tool import get_tools, create_tool_nodes
from langgraph.graph import START, END
from langgraph.prebuilt import tools_condition , ToolNode
from src.langgraphagenticai.nodes.chatbot_with_tool_node import ChatbotWithToolNode
from src.langgraphagenticai.nodes.ai_news_node import AINewsNode
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



    def ai_news_build_graph(self):
        """
        Build a graph for AI News use case.
        This is a placeholder for future implementation.
        """
        ai_news_node = AINewsNode(self.llm)

        self.graph_builder.add_node("fetch_news",ai_news_node.fetch_news)
        self.graph_builder.add_node("summarize_news",ai_news_node.summarize_news)
        self.graph_builder.add_node("save_results",ai_news_node.save_results)

        # Define the edges for the AI News graph
        self.graph_builder.add_edge(START, "fetch_news")
        self.graph_builder.add_edge("fetch_news", "summarize_news")
        self.graph_builder.add_edge("summarize_news", "save_results")
        self.graph_builder.add_edge("save_results", END)


    def setup_graph(self, usecase):
        """
        Setup the graph based on the use case.
        """
        if usecase == "Basic Chatbot":
            self.basic_chatot_build_graph()
        if usecase == "Chatbot with web":
            self.chatbot_with_tools_build_graph()
        if usecase == "AI News":
            self.ai_news_build_graph()

        return self.graph_builder.compile()