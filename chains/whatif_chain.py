from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",  # ✅ Supports chat!
    task="text-generation",
    temperature=0.5,
    max_new_tokens=256
)

chat = ChatHuggingFace(llm=llm)
response = chat.invoke("What is the capital of India?")
print(response.content)
