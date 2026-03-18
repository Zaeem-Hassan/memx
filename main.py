from memx import Memory

API_KEY = "your_openai_api_key"

mem = Memory(api_key=API_KEY)

# Add conversation
mem.add("User: I live in Lahore and I like cricket", user_id="zaeem")

# Query memory
results = mem.search("Where do I live?", user_id="zaeem")

print("\nMemories:")
for r in results:
    print("-", r["text"])