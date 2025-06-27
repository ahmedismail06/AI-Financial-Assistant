# First cell - run this before any other imports
import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

from google import genai
from sentence_transformers import SentenceTransformer, CrossEncoder, util
from langchain_community.document_loaders import PyMuPDFLoader

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key from environment variable
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY environment variable is not set. Please check your .env file.")

client = genai.Client(api_key=GOOGLE_API_KEY)


def RAG(path, query, top_k = 7):
    model = CrossEncoder("cross-encoder/stsb-distilroberta-base")
    loader = PyMuPDFLoader(path).load()
    docs = []
    numbers_of_pages = loader[0].to_json()["kwargs"]["metadata"]["total_pages"]
    for page in range(int(numbers_of_pages)):
        docs.append(loader[page].to_json()["kwargs"]["page_content"].replace("\n", ""))

    # Step 1: Bi-Encoder (Fast Retrieval)
    bi_encoder = SentenceTransformer("multi-qa-MiniLM-L6-cos-v1")
    doc_embeddings = bi_encoder.encode(docs, convert_to_tensor=True)
    query_embedding = bi_encoder.encode(query, convert_to_tensor=True)

    # Retrieve top-k most relevant chunks
    hits = util.semantic_search(query_embedding, doc_embeddings, top_k=top_k)[0]

    top_docs = [docs[hit['corpus_id']] for hit in hits]

    # Step 2: Cross-Encoder (Rerank)
    cross_encoder = CrossEncoder("cross-encoder/stsb-distilroberta-base")
    cross_inputs = [[query, doc] for doc in top_docs]
    scores = cross_encoder.predict(cross_inputs)

    # Rank by cross-encoder scores
    ranked = sorted(zip(top_docs, scores), key=lambda x: x[1], reverse=True)
    context = "\n\n".join([f"{i+1}. {doc.strip()}" for i, (doc, _) in enumerate(ranked)])
    #print(context)

    PROMPT = f"""You are a Senior financial analyst helping explain company earnings using information from the reference passage below, which may come from an earnings call or a 10-K filing.

    Answer the question clearly and in complete sentences, using all relevant details from the passage. 
    Your audience is not financially savvy, so break down any complex terms or concepts into simple, friendly language.
    If the passage doesn't contain enough information to answer the question, say so.

    CONTEXT: {context}
    QUESTION: {query}
    """

    response = client.models.generate_content(
        model= "gemini-2.5-flash",
        contents= PROMPT
    )
    return response.text

#print(RAG("/Users/ahmedismail/Downloads/testing.pdf", "What is this document about?"))


def main():
    Documents = input("Please provide doc path: ")
    quest = input("question: ")
    print(RAG(Documents, quest))


#main()











