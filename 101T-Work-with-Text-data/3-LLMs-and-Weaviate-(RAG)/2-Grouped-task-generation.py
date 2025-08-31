import os
import weaviate
from weaviate.config import AdditionalConfig, Timeout

# Instantiate your client (not shown). e.g.:
# headers = {"X-OpenAI-Api-Key": os.getenv("OPENAI_APIKEY")}  # Replace with your OpenAI API key
# client = weaviate.connect_to_weaviate_cloud(..., headers=headers) or
# client = weaviate.connect_to_local(..., headers=headers)

client = weaviate.connect_to_local()

# Get the collection
movies = client.collections.get("Movie")

# Perform query
response = movies.generate.near_text(
    query="dystopian future",
    limit=5,
    grouped_task="What do these movies have in common?",
    # grouped_properties=["title", "overview"]  # Optional parameter; for reducing prompt length
)

# Inspect the response
for o in response.objects:
    print(o.properties["title"])  # Print the title
print(response.generated)  # Print the generated text (the commonalities between them)

client.close()