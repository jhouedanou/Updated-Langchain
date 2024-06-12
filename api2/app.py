from fastapi import FastAPI
from langchain.prompt import ChatPromptTemplate 
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama 

os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")    # Load the OpenAI API key from the environment

