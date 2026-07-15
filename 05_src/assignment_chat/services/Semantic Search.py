from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader


DB_PATH="./chroma_db"


def create_database():

    loader=TextLoader(
        "./data/ai_notes.txt"
    )

    docs=loader.load()


    vectorstore=Chroma.from_documents(
        docs,
        OpenAIEmbeddings(),
        persist_directory=DB_PATH
    )

    return vectorstore



vectorstore=None


def semantic_search(question):

    global vectorstore


    if vectorstore is None:
        vectorstore=create_database()


    results=vectorstore.similarity_search(
        question,
        k=2
    )


    context="\n".join(
        [
            doc.page_content
            for doc in results
        ]
    )


    return context