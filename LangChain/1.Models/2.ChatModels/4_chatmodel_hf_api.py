from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "deepseek-ai/DeepSeek-R1-0528",
    task="text-generation",
    provider="auto",
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("Write a 5 line poem on cricket")

print(result.content)