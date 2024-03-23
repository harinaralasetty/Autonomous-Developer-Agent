
import config
from langchain_google_genai import ChatGoogleGenerativeAI
import os


os.environ["GOOGLE_API_KEY"] = config.GOOGLE_API_KEY

llm = ChatGoogleGenerativeAI(model="gemini-pro")
result = llm.invoke("What is the meaning of life?")
print(result.content)