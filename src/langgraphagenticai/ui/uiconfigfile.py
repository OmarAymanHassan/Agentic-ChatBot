'''
Used to tread the config from uiconfigfile.ini file
'''

from configparser import ConfigParser



class Config:
    def __init__(self,config_file_path="./src/langgraphagenticai/ui/uiconfigfile.ini"):
        self.config = ConfigParser()
        self.config.read(config_file_path)

    def get_llm_options(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ")
    
    def get_usecase_options(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(", ")
    
    def get_groq_model_options(self):
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(", ")
    
    def get_gemini_model_options(self):
        return self.config["DEFAULT"].get("GEMINI_MODEL_OPTIONS").split(", ")
    
    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")
    # here we dont do split , becaue title has no `,` in it



    