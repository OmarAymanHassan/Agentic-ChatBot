from src.langgraphagenticai.state.state import State


class BasicChatbotNode:
    """
    A node that represents a basic chatbot functionality.
    It can be used to create a simple chatbot application.
    """

    def __init__(self,model):
        self.llm = model
    

    def process (self, state:State):
        """
        Process the input state and return the output state.
        This method is called when the node is executed.
        """
        # Here we can implement the logic for the basic chatbot
        # For now, we will just return the input state as output
        

        return {"messages": self.llm.invoke(state["messages"])}