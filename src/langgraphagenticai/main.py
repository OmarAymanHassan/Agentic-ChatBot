'''
its used to call all the functions in the agenticai modules with different components from one place

so we use to to connect all the components of the agenticai modules in one place

to be called from the main function and to be used in the UI 
'''
from src.langgraphagenticai.llms.groqllm import GroqLLM
from src.langgraphagenticai.llms.geminillm import GeminiLLM
import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit
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
  
    if user_message:
        try:
            # configure the LLM based on user input
            if user_input["selected_llm"] == "Groq":
                llm_instance = GroqLLM(user_controls_input=user_input)
                model = llm_instance.get_llm_model()
                if not model:
                    st.error("⚠️ Failed to load Groq model. Please check your API key and model selection.")
                    return
                

            elif user_input["selected_llm"] == "Gemini":
                llm_instance = GeminiLLM(user_controls_input=user_input)
                model = llm_instance.get_llm_model()
                if not model:
                    st.error("⚠️ Failed to load Gemini model. Please check your API key and model selection.")
                    return
            else:
                st.error("⚠️ Unsupported LLM selected.")
                return
            
            # Process the useCase
            usecase = user_input.get("selected_usecase")
            if not usecase:
                st.error("⚠️ Please select a use case to proceed.")
                return
            ## Start Building The Graph

            graph = GraphBuilder( model=model)
            try:
                graph = graph.setup_graph(usecase=usecase)
                DisplayResultStreamlit(usecase=usecase , graph=graph, user_message=user_message).display_result_on_ui()
            except ValueError as e:
                st.error(f"⚠️ Error setting up graph: {e}")
                return

        except Exception as e:
            st.error(f"⚠️ An error occurred: {e}")
            return