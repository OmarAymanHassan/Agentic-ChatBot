'''
its used to call all the functions in the agenticai modules with different components from one place

so we use to to connect all the components of the agenticai modules in one place

to be called from the main function and to be used in the UI 
'''


import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI

def load_langgraph_agenticai_app():
    """
    Load the LangGraph Agentic AI application UI.
    """
    load_ui = LoadStreamlitUI()
    user_input = load_ui.load_streamlit_ui()

    # Here you can add more logic to handle user interactions
    # For example, you can call functions based on the selected options
    #st.write("User Controls:", user_controls)

    if not user_input:
        st.error("⚠️ Please select an LLM and a use case to proceed.")
        return 
    user_message = st.chat_input("Enter your message:")
  

