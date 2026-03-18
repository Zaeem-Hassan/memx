from openai import OpenAI

class Extractor:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def extract(self, messages):
        prompt = f"""
Extract important user facts from this conversation.
Return as a Python list of strings.

Conversation:
{messages}
"""

        response = self.client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        content = response.choices[0].message.content

        try:
            facts = eval(content)
            return facts if isinstance(facts, list) else []
        except:
            return []