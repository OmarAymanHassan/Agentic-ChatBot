from src.langgraphagenticai.state.state import State


class ChatbotWithToolNode:
    """
    A node that represents a chatbot with tool functionality.
    It can be used to create a chatbot application that can use tools.
    """

    def __init__(self, model):
        self.llm = model

    def process(self, state: State):
        """
        Process the input state and return the output state.
        This method is called when the node is executed.
        """
        user_input = state["messages"][-1] if state["messages"] else ""
        llm_response = self.llm.invoke([{"role": "user", "content": user_input}])

        tools_response = f"Tool Integration for : {user_input}\n"

        return {"messages": [llm_response, tools_response]}
    

    def create_chatbot(self,tools):
        """
        Create a chatbot with tools.
        This method can be used to create a chatbot that can use tools.
        """
        llm_with_tools = self.llm.bind_tools(tools)

        def chatbot_node(state:State):

            return {"messages": [llm_with_tools.invoke(state["messages"])]}
        return chatbot_node
    
