import os
import weaviate
import os

# Instantiate your client (not shown). e.g.:
# headers = {"X-OpenAI-Api-Key": os.getenv("OPENAI_APIKEY")}  # Replace with your OpenAI API key
client = weaviate.connect_to_local()


def url_to_base64(url):
    import requests
    import base64

    image_response = requests.get(url)
    content = image_response.content
    return base64.b64encode(content).decode("utf-8")


# Get the collection
movies = client.collections.use("MovieMM")

# Perform query
src_img_path = "https://github.com/weaviate-tutorials/edu-datasets/blob/main/img/International_Space_Station_after_undocking_of_STS-132.jpg?raw=true"
query_b64 = url_to_base64(src_img_path)

response = movies.generate.near_image(
    near_image=query_b64,
    limit=5,
    grouped_task="What do these movies have in common?",
    grouped_properties=["title", "overview"]  # Optional parameter; for reducing prompt length
)

# Inspect the response
for o in response.objects:
    print(o.properties["title"])  # Print the title
print(response.generative.text)  # Print the generated text (the commonalities between them)

client.close()