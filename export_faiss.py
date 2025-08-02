from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_community.vectorstores import FAISS

# Create embeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Load Chroma DB
chroma_db = Chroma(persist_directory="chroma_db", embedding_function=embeddings)

# Get documents
docs = chroma_db.get()
print(f"Number of documents in Chroma: {len(docs['documents'])}")

# Export to FAISS
faiss_index = FAISS.from_documents(chroma_db.similarity_search("sample query"), embeddings)
faiss_index.save_local("faiss_index")

print("✅ FAISS index created successfully!")
