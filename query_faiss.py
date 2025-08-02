from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Load embeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Load FAISS index (trusted source, so allow pickle loading)
faiss_index = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

print("FAISS index loaded successfully!")

while True:
    query = input("\nEnter your query (or type 'exit' to quit): ")
    if query.lower() == "exit":
        break

    results = faiss_index.similarity_search(query, k=3)

    for i, result in enumerate(results, start=1):
        print(f"\nResult {i}:\n{result.page_content}")
