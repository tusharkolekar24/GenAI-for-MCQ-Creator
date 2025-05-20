from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain_core.documents import Document
import json

def load_jsons(filename):
    with open(filename,'r') as json_files:
        dataset = json.load(json_files)
        return dataset
    
def retrival_info():
    raw_texts = load_jsons(filename=r"D:\upgraded_git_repo\mcq_creator_app\GenAI-for-MCQ-Creator\artifacts\content.json")
    # Convert strings to Document objects
    documents = [Document(page_content=text) for text in raw_texts["content"]]

    text_splitter = CharacterTextSplitter (chunk_size=250,chunk_overlap=0)

    texts= text_splitter.split_documents(documents)

    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    db = Chroma.from_documents(texts, embeddings)

    retriever = db.as_retriever(search_kwargs={"k":5})
    print("retriever ready for the use")

    return retriever