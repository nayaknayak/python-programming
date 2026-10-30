import chromadb
import os
from dotenv import load_dotenv


from google import genai
load_dotenv()

api_key = os.getenv('GOOGLE_API_KEY')
google_client = genai.Client(api_key=api_key)


chroma_client = chromadb.PersistentClient(path ="./chroma_db")

collection = chroma_client.get_or_create_collection(
    name="python_learning_google"
)
#convert question into embeddings
def ask_question(question:str):
    print("Total records:", collection.count())
    response = google_client.models.embed_content(
        model="gemini-embedding-001",
        contents=question
    )
    question_embedding = response.embeddings[0].values
    #Collect from Vector Db
    result =  collection.query(
        query_embeddings=question_embedding,
        n_results=7
    )
    print("result from vector Db : ", result)

    document=  result['documents'][0]

    print( "list of Documents:",type(document))

    context =  "/n/n".join(document)
    print('type of context:' ,type(context))


    #create a rag prompt
    rag_prompt=f""" Answer the question using only the context provided below.

    Context : {context}

    Question : {question}

    """
    response = google_client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=rag_prompt
    )

    return  response.text

print(ask_question(" Company name?"))





