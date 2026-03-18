import faiss
import numpy as np
import uuid

class VectorStore:
    def __init__(self, dim=1536):
        self.index = faiss.IndexFlatL2(dim)
        self.memories = []

    def add(self, vector, text, user_id):
        self.index.add(np.array([vector]).astype("float32"))
        memory = {
            "id": str(uuid.uuid4()),
            "text": text,
            "user_id": user_id
        }
        self.memories.append(memory)
        return memory

    def search(self, vector, user_id, k=5):
        if len(self.memories) == 0:
            return []

        D, I = self.index.search(np.array([vector]).astype("float32"), k)

        results = []
        for idx in I[0]:
            if idx < len(self.memories):
                mem = self.memories[idx]
                if mem["user_id"] == user_id:
                    results.append(mem)

        return results

    def delete(self, memory_id):
        self.memories = [m for m in self.memories if m["id"] != memory_id]