import voyageai
from voyageai import get_embeddings

voyageai.api_key = "tr_e9a578eb33fcf135b6b307c3a12b65b693f9c0a9be2f3cbba0c8bd3bacda9cd135f395ad41757a83389afa71313538b9e3be77182cac6ad70055c7fa533c13e9"

documents = [
    "The Mediterranean diet emphasizes fish, olive oil, and vegetables, believed to reduce chronic diseases.",
    "Photosynthesis in plants converts light energy into glucose and produces essential oxygen.",
    "20th-century innovations, from radios to smartphones, centered on electronic advancements.",
    "Rivers provide water, irrigation, and habitat for aquatic species, vital for ecosystems.",
    "Apple’s conference call to discuss fourth fiscal quarter results and business updates is scheduled for Thursday, November 2, 2023 at 2:00 p.m. PT / 5:00 p.m. ET.",
    "Shakespeare's works, like 'Hamlet' and 'A Midsummer Night's Dream,' endure in literature.",
    "算法妈妈是一家人工智能公司，使用AI底座同时赋能时尚行业和教培行业。"
]

# Embed the documents
documents_embeddings = get_embeddings(documents, model="voyage-01")

query = "算法妈妈是一家什么公司？"

# Get the embedding of the query
query_embedding = get_embeddings(query, model="voyage-01")

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def k_nearest_neighbors(query_embedding, documents_embeddings, k=5):
    query_embedding = np.array(query_embedding) # convert to numpy array
    documents_embeddings = np.array(documents_embeddings) # convert to numpy array

    # Reshape the query vector embedding to a matrix of shape (1, n) to make it compatible with cosine_similarity
    query_embedding = query_embedding.reshape(1, -1)

    # Calculate the similarity for each item in data
    cosine_sim = cosine_similarity(query_embedding, documents_embeddings)

    # Sort the data by similarity in descending order and take the top k items
    sorted_indices = np.argsort(cosine_sim[0])[::-1]

    # Take the top k related embeddings
    top_k_related_indices = sorted_indices[:k]
    top_k_related_embeddings = documents_embeddings[sorted_indices[:k]]
    top_k_related_embeddings = [list(row[:]) for row in top_k_related_embeddings] # convert to list

    return top_k_related_embeddings, top_k_related_indices

# Use the nearest neighbor algorithm to find the document with the highest similarity
retrieved_embd, retrieved_embd_index = k_nearest_neighbors(query_embedding, documents_embeddings, k=1)
retrieved_doc = [documents[index] for index in retrieved_embd_index]

print(retrieved_doc)

import openai

# Initialize OpenAI API
openai.api_key = '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'

# Take the retrieved document and use it as a prompt for the text generation model
prompt = f"Based on the information: '{retrieved_doc}', generate a response of {query}"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ]
)

print(response.choices[0].message.content)
