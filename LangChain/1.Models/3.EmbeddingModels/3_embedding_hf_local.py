# from langchain_huggingface import HuggingFaceEmbeddings

# embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

# documents = [
#     "Delhi is the capital of India",
#     "Kolkata is the capital of West Bengal",
#     "Paris is the capital of France"
# ]

# vector = embedding.embed_documents(documents)

# print(str(vector))

from langchain_huggingface import HuggingFaceEndpointEmbeddings

embedding = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2",
    huggingfacehub_api_token="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"
)

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

vector = embedding.embed_documents(documents)

print(vector)