from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

#load_dotenv()

#model = ChatOpenAI()
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "deepseek-ai/DeepSeek-R1-0528",
    task="text-generation",
    provider="auto",
)

# Simple one-line prompt
prompt = PromptTemplate.from_template("{question}")

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

# Chain: prompt → model → parser
chain = prompt | model | parser

# Run it
result = chain.invoke({"question": "What is the capital of Peru?"})
print(result)
