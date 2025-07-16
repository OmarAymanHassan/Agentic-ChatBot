

from tavily import TavilyClient
from langchain_core.prompts import ChatPromptTemplate
from src.langgraphagenticai.state.state import State


class AINewsNode:
    def __init__(self, llm):
        self.llm = llm
        self.tavily =TavilyClient()

        # this is added to capture various steps in this file so that later we can use it for showing the steps in the UI
        self.state={}

    def fetch_news(self,state:State):
        """
        Fetch news articles based on the user's query.
        """
        frequency = state["messages"][0].content.lower()
        self.state["frequency"] = frequency
        time_range_map = {"daily":"d" , "weekly":"w", "monthly":"m", "yearly":"y"}
        days_map = {"daily":1, "weekly":7, "monthly":30, "yearly":365}

        response = self.tavily.search(
            query="Top AI Technology News Globally",
            time_range=time_range_map[frequency],
            days=days_map[frequency],
            include_answer = "advanced",
            max_results=15,
            topic = "news"          
        )
        state["news_data"] = response.get("results", [])
        self.state["news_data"] = state["news_data"]

    
        return state
    

    def summarize_news(self, state:State):
        """
        Summarize the fetched news articles.
        """
        new_items = state["news_data"]
        prompt_template = ChatPromptTemplate.from_messages([
            ("system", """Summarize the AI News into markdown format. for each item include:
             
             - Date in the format YYYY-MM-DD format in cairo-egypt timezone
             - Concise sentence summart from latest AI news articles.
             - sort news by date wise (latest first)
             use format:
             ### [Date]
             - [Summary](URL)
             
             ."""),
            ("user", "Articles:\n {articles}")
        ])

        articles_str = "\n\n".join([
            f"content: {item.get("content", " ")}\nurl: {item.get("url"," ")}\nDate: {item.get("published_date" , "")} " for item in new_items

        ])

        response = self.llm.invoke(prompt_template.format(articles =articles_str))
        state["summary"] = response.content
        self.state["summary"] = state["summary"]
        return self.state
    

    def save_results(self, state:State):
        """
        Save the summarized news articles to a file.
        """
        summary = self.state["summary"]
        frequency = self.state["frequency"]
        file_name = f"./AINews/{frequency}_summary.md"
        
        with open(file_name, "w") as file:
            file.write(f"# {frequency.capitalize()} AI News Summary\n\n")
            file.write(summary)
        
        self.state["file_name"] = file_name
        return self.state