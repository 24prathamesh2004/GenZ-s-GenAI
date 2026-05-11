from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

text = """
# Project Name: GenZ's GenAI

This project aims to master Gen AI concept and applications exploring Langchain, LangGraph, LangSmith, MCP.


## Features

- A to z gen ai
- Implementation of various gen ai concept and applications
- hands on project and code snippets
- detailed documentation and explanations


## 🛠 Tech Stack

- Python 3.10+
- No external dependencies


## Getting Started

1. Clone the repo  
   ```bash
   git clone https://github.com/24prathamesh2004/genzs-genai.git

"""

# Initialize the splitter
splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size=200,
    chunk_overlap=0,
)

# Perform the split
chunks = splitter.split_text(text)

print(len(chunks))
print(chunks[0])