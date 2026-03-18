from openai import OpenAI

class Embedder:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def embed(self, text):
        response = self.client.embeddings.create(
            model="text-embedding-3-small",
            input=text
        )
        return response.data[0].embedding