from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load documents from docs folder
loader = DirectoryLoader("docs", glob="**/*.pdf")  # Supports PDF files
documents = loader.load()

# Split into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
docs = text_splitter.split_documents(documents)

# Create embeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Create Chroma DB and add documents
db = Chroma(persist_directory="chroma_db", embedding_function=embeddings)
db.add_documents(docs)

print(f"✅ Successfully ingested {len(docs)} document chunks into Chroma DB.")
