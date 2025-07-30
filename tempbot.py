from openai import OpenAI
import os

client = OpenAI(
    api_key = os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"  
)

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("bot: Goodbye")
        break

    response = client.chat.completions.create(
        model="llama3-70b-8192",  
        messages=[
            {"role": "system", "content": "You are a friendly beginner coding tutor. Explain basic programming concepts simply with short examples in Python, C, or JavaScript. Keep replies simple and beginner-friendly."},

            {"role": "user", "content": user_input}
        ]
    )

    print("bot:", response.choices[0].message.content)
