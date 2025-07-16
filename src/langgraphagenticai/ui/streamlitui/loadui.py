import streamlit as st
import os
from src.langgraphagenticai.ui.uiconfigfile import Config


class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}
    
    def load_streamlit_ui(self):
        st.set_page_config(
            page_title= "🤖 " + self.config.get_page_title(),
            layout="wide")
        st.header("🤖 " + self.config.get_page_title())

        # For the left sideBar

        with st.sidebar:
            # we will get the options from the config file
            llm_options = self.config.get_llm_options()
            usecase_option = self.config.get_usecase_options()

            ## LLM Selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM" , llm_options)
            
            if self.user_controls["selected_llm"] == "Groq":
                groq_model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", groq_model_options)
                self.user_controls["GROQ_API_KEY"] =st.session_state["GROQ_API_KEY"]=st.text_input("API Key", type="password")
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("⚠️ Please enter your Groq API Key to use the Groq model.")
            elif self.user_controls["selected_llm"] == "Gemini":
                gemini_model_options = self.config.get_gemini_model_options()
                self.user_controls["selected_gemini_model"] = st.selectbox("Select Model", gemini_model_options)
                self.user_controls["GEMINI_API_KEY"] = st.session_state["GEMINI_API_KEY"] = st.text_input("API Key", type="password")
                if not self.user_controls["GEMINI_API_KEY"]:
                    st.warning("⚠️ Please enter your Gemini API Key to use the Gemini model.")

            ## Usecase Selection

            self.user_controls["selected_usecase"] = st.selectbox("Select Usecase", usecase_option)


        return self.user_controls


            
