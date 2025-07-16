import os 
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI


class GeminiLLM:
    def __init__(self,user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        """
        Get the Gemini LLM model based on user input.
        """
        try:
            gemini_api_key = self.user_controls_input["GEMINI_API_KEY"]
            selected_gemini_model = self.user_controls_input["selected_gemini_model"]
            if gemini_api_key == " " and os.environ["GEMINI_API_KEY"] == "":
                st.error("⚠️ Please enter your Gemini API Key to use the Gemini model.")
                return None
            
            llm = ChatGoogleGenerativeAI(
                model=selected_gemini_model,
                api_key=gemini_api_key
            )
        except Exception as e:
            raise ValueError(f"Error Occured with Exception: {e}")
    
        return llm