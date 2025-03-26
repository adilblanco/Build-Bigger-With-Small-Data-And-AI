from llama_index.core import StorageContext
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core.node_parser import TokenTextSplitter
from llama_index.vector_stores.duckdb import DuckDBVectorStore
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings


# model
Settings.embed_model = OllamaEmbedding(model_name="all-minilm")
Settings.llm = Ollama(model="gemma2:2b", temperature=0, request_timeout=360.0)

# load documents into a vector store - DuckDB
documents = SimpleDirectoryReader(input_files=["facts.txt"]).load_data(show_progress=True)
splitter = TokenTextSplitter(separator="\n", chunk_size=64, chunk_overlap=0)
vector_store = DuckDBVectorStore()
storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex(splitter.get_nodes_from_documents(documents=documents), storage_context=storage_context, show_progress=True)
query_engine = index.as_query_engine()

try:
    while True:
        user_query = input(">>> ")
        response = query_engine.query(user_query)
        print(response)
except KeyboardInterrupt:
    exit()
