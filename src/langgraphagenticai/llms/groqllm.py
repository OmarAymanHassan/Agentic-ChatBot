from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
import streamlit as st
import os
from langchain_groq import ChatGroq


class GroqLLM:
    def __init__(self,user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        """
        Get the Groq LLM model based on user input.
        """
        try:
            groq_api_key = self.user_controls_input["GROQ_API_KEY"]
            selected_groq_model = self.user_controls_input["selected_groq_model"]
            if groq_api_key == " " and os.environ["GROQ_API_KEY"] == "":
                st.error("⚠️ Please enter your Groq API Key to use the Groq model.")
                return None
            
            llm = ChatGroq(
                model_name=selected_groq_model,
                api_key=groq_api_key
            )
        except Exception as e:
            raise ValueError(f"Error Occured with Exception: {e}")
    
    