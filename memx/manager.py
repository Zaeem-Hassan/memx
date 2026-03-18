from openai import OpenAI

class Manager:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def decide(self, new_fact, existing_memories):
        prompt = f"""
You are a memory manager.

New fact:
{new_fact}

Existing memories:
{existing_memories}

Decide one: ADD, UPDATE, DELETE, NOOP
Return only one word.
"""

        response = self.client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content.strip()