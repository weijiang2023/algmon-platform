import chromadb
chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="my_collection")
collection.add(
    documents=["This is a document",
               "This is a good document", "Apple is a good company"],
    metadatas=[{"source": "my_source"}, {
        "source": "my_source"}, {"source": "my_source"}],
    ids=["id1", "id2", "id3"]
)
results = collection.query(
    query_texts=["An apple a day makes the doctor away."],
    n_results=2
)

print(results)
