import os
import weaviate
import os

# Instantiate your client (not shown). e.g.:
# headers = {"X-OpenAI-Api-Key": os.getenv("OPENAI_APIKEY")}  # Replace with your OpenAI API key
client = weaviate.connect_to_local()

# Get the collection
movies = client.collections.use("MovieNVDemo")

# Perform query
# Loop through the target vectors
for tgt_vector in ["title", "overview"]:
    response = movies.generate.near_text(
        query="Chrono Tides: The Anomaly Rift",
        limit=5,
        target_vector=tgt_vector,  # The target vector to search against
        grouped_task="What types of movies are these, and what kinds of audience might this set of movies be aimed at overall?",
        grouped_properties=["title", "overview"]  # Optional parameter; for reducing prompt length
    )

    # Inspect the response
    for o in response.objects:
        print(o.properties["title"])  # Print the title
    print(response.generative.text)  # Print the generated text (the commonalities between them)

client.close()