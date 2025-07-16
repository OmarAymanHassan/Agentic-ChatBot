import streamlit as st
import os
from src.langgraphagenticai.ui.uiconfigfile import Config


class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}
    
    def load_streamlit_ui(self):
        st.set_page_config(
            page_title= "🤖 " + self.config.get_page_title(),layout="wide")
        st.header("🤖 " + self.config.get_page_title())
        st.session_state.IsFetchButtonClicked = False
        st.session_state.time_frame = ""

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
                    st.warning("⚠️ Please enter your Groq API Key to use the Groq model. Don't have one? refer : https://docs.groq.com/docs/groq-api-keys")
            elif self.user_controls["selected_llm"] == "Gemini":
                gemini_model_options = self.config.get_gemini_model_options()
                self.user_controls["selected_gemini_model"] = st.selectbox("Select Model", gemini_model_options)
                self.user_controls["GEMINI_API_KEY"] = st.session_state["GEMINI_API_KEY"] = st.text_input("API Key", type="password")
                if not self.user_controls["GEMINI_API_KEY"]:
                    st.warning("⚠️ Please enter your Gemini API Key to use the Gemini model. Don't have one? refer : https://developers.google.com/generative-ai/console")

            ## Usecase Selection

            self.user_controls["selected_usecase"] = st.selectbox("Select Usecase", usecase_option)

            if self.user_controls["selected_usecase"] == "Chatbot with web" or self.user_controls["selected_usecase"] == "AI News":
                os.environ["TAVILY_API_KEY"] = self.user_controls["TAVILY_API_KEY"] = st.session_state["TAVILY_API_KEY"] = st.text_input("Tavily API Key", type="password")
                if not self.user_controls["TAVILY_API_KEY"]:
                    st.warning("⚠️ Please enter your Tavily API Key to use the Chatbot with web use case. Dont't have one? refer : https://app.tavily.com/home")
    
        # For the AI NEWS content
            if self.user_controls["selected_usecase"] == "AI News":
                st.subheader("📰 AI News Explorer")

                with st.sidebar:
                    time_frame = st.selectbox("📅 Select Time Frame", ["Daily", "Weekly", "Monthly"],index=0)
                
                if st.button("🔍 Fetch Latest AI News" , use_container_width=True):
                    st.session_state.IsFetchButtonClicked = True
                    st.session_state.time_frame = time_frame

        return self.user_controls


            
