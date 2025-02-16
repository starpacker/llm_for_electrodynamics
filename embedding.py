from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores import FAISS
from sentence_transformers import SentenceTransformer
from langchain_community.docstore.in_memory import InMemoryDocstore
import pickle
import faiss

class rag():
    def __init__(self, device):
        embedding_model = SentenceTransformer("/data/group_003/answer/snowflake-arctic-embed-xs", device=device)
        index = faiss.read_index("/data/group_003/answer/IVF/flat_index.faiss")
        
        with open("/data/group_003/answer/IVF/documents.pkl", "rb") as f:
            chunks = pickle.load(f)
        
        docstore = InMemoryDocstore()
        ids = [f'{i}' for i in range(len(chunks))]
        pre_docstore = dict(zip(ids, chunks))
        docstore.add(pre_docstore)
        self.vector_store = FAISS(
            embedding_function=embedding_model.encode,
            index=index,
            docstore=docstore,
            index_to_docstore_id={i: str(i) for i in range(len(chunks))}
        )

    def invoke(self, k, query):
        retriever = self.vector_store.as_retriever(search_kwargs={"k": k})
        retrieved_docs = retriever.invoke(query)
        return retrieved_docs



        


     