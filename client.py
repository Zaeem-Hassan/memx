from .extractor import Extractor
from .manager import Manager
from .store import VectorStore
from .embedder import Embedder

class Memory:
    def __init__(self, api_key):
        self.extractor = Extractor(api_key)
        self.manager = Manager(api_key)
        self.embedder = Embedder(api_key)
        self.store = VectorStore()

    def add(self, messages, user_id="default"):
        facts = self.extractor.extract(messages)

        for fact in facts:
            vector = self.embedder.embed(fact)
            existing = self.store.search(vector, user_id)

            action = self.manager.decide(fact, existing)

            if action == "ADD":
                self.store.add(vector, fact, user_id)

            elif action == "UPDATE" and existing:
                self.store.delete(existing[0]["id"])
                self.store.add(vector, fact, user_id)

            elif action == "DELETE" and existing:
                self.store.delete(existing[0]["id"])

    def search(self, query, user_id="default", limit=5):
        vector = self.embedder.embed(query)
        return self.store.search(vector, user_id, limit)