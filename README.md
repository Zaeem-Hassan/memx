<div align="center">



# 🧠 Memora-AI

**A lightweight, persistent memory layer for AI agents.**  
Give your agents memory  without the overhead.

```bash
pip install memora-ai
```

</div>

---

## Why Memora?

LLMs forget everything between conversations. Memora fixes that.

It extracts facts from conversations using an LLM, stores them in a persistent vector + SQLite store, and retrieves the right memories at the right time , so your agents can actually *know* your users and there preference.

---

## Features

| | |
|---|---|
| 🧠 **LLM-based extraction** | Pulls structured facts from raw conversation text |
| 🔍 **Semantic search** | FAISS-powered vector retrieval for relevant memories |
| 💾 **Persistent storage** | SQLite backend — no external database needed |
| 🔄 **Smart updates** | Intelligently decides to ADD / UPDATE / DELETE memories |
| 👥 **Multi-user** | Isolated memory per `user_id` out of the box |
| ⚡ **Simple SDK** | Get started in 3 lines of code |

---

## Quick Start

```python
from memora import Memory

mem = Memory(api_key="your_openai_api_key")

# Store facts from a conversation
mem.add("User: I live in Lahore and I like cricket", user_id="zaeem")

# Retrieve relevant memories
results = mem.search("Where do I live?", user_id="zaeem")

for r in results:
    print(r["text"])
# → "User lives in Lahore"
# → "User likes cricket"
```

---

## How It Works

```
Raw Conversation
      │
      ▼
 LLM Extraction          ← Pulls discrete facts from text
      │
      ▼
 Fact Candidates
      │
      ▼
 Similarity Search       ← Checks what's already in memory
      │
      ▼
 Decision Engine         ← ADD / UPDATE / DELETE
      │
      ▼
 Persistent Store        ← FAISS + SQLite
```

---

## API Reference

### `Memory(api_key)`
Initialize the memory system.

```python
mem = Memory(api_key="sk-...")
```

---

### `mem.add(messages, user_id="default")`
Extract facts from a conversation string and persist them.

```python
mem.add("User: I moved to Karachi last year", user_id="zaeem")
```

---

### `mem.search(query, user_id="default", limit=5)`
Retrieve the most relevant memories for a query.

```python
results = mem.search("Where does Zaeem live?", user_id="zaeem")
# [{"text": "User lives in Karachi", "score": 0.91}]
```

---

### `mem.clear(user_id)`
Delete all memories for a user.

```python
mem.clear(user_id="zaeem")
```

---

## Tech Stack

- **LLM:** OpenAI-compatible models
- **Embeddings:** `text-embedding-3-small`
- **Vector DB:** FAISS
- **Storage:** SQLite

---

## Project Structure

```
memora/
├── client.py       # SDK entry point
├── extractor.py    # LLM-based fact extraction
├── manager.py      # ADD / UPDATE / DELETE logic
├── embedder.py     # Embedding generation
├── store.py        # FAISS vector store
└── db.py           # SQLite persistence
```

---

## Roadmap

- [ ] Graph-based memory (Mem0g-style)
- [ ] Memory importance scoring
- [ ] Temporal reasoning
- [ ] Local LLM support (Ollama, llama.cpp)
- [ ] Hosted API version

---

## Contributing

Contributions are welcome!

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes
4. Submit a PR

---

## License

MIT © [Zaeem Hassan](https://github.com/Zaeem-Hassan)

---

<div align="center">

If Memora is useful to you, a ⭐ on [GitHub](https://github.com/Zaeem-Hassan/memx) goes a long way.

</div>
