from langchain_community.embeddings import HuggingFaceEmbeddings

def ingest_pdfs():
    loader = DirectoryLoader("data", glob="*.pdf", loader_cls=PyPDFLoader)
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    all_docs = [doc.page_content for doc in text_splitter.split_documents(docs)]

    # Use free embeddings
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    db = Chroma.from_texts(all_docs, embeddings, persist_directory="chroma_db")
    db.persist()
    print("✅ PDFs ingested successfully!")
