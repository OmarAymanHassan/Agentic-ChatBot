import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage , ToolMessage
import json



class DisplayResultStreamlit:
    def __init__(self,usecase,graph,user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message
        if usecase == "Basic Chatbot":
            for event in graph.stream({"messages": ("user", user_message)}):
                print(event.values())
                for value in event.values():
                    print(value["messages"])
                    with st.chat_message("user"):
                        st.write(user_message)
                    
                    with st.chat_message("assistant"):
                        st.write(value["messages"].content)

        elif usecase == "Chatbot with web":
            initial_state = {"messages": [user_message]}
            res = graph.invoke(initial_state)
            for message in res["messages"]:
                if type(message) == HumanMessage:
                    with st.chat_message("user"):
                        st.write(message.content)
                elif type(message) == ToolMessage:
                    with st.chat_message("AI"):
                        st.write("Tool Call Start")
                        st.write(message.content)
                        st.write("Tool Call End")
                elif type(message) == AIMessage and message.content:
                    with st.chat_message("assistant"):
                        st.write(message.content)

        elif usecase == "AI News":
            frequency = self.user_message
            with st.spinner("Fetching & Summarizing AI News...⌛"):
                result = graph.invoke({"messages": frequency})
                try :

                    AI_NEWS_PATH = f"./AINews/{frequency}_summary.md"
                    with open(AI_NEWS_PATH, "r") as file:
                        markdown_content = file.read()

                    st.markdown(markdown_content, unsafe_allow_html=True)
                except FileNotFoundError:
                    st.error("⚠️ No news data found. Please try again later.")
                except Exception as e:
                    st.error(f"⚠️ An error occurred while displaying the news: {e}")
                    





