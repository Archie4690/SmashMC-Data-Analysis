import re
import requests
import gzip

messages = []
counts = {}

def classify(message):
    response = requests.post("http://localhost:11434/api/chat", json={
        "model": "qwen2.5:3b",
        "messages": [
            {"role": "system", "content": """You are a text classifier. Classify each player message into EXACTLY ONE category:

- bug - reports something broken or not working
- toxicity - insults, harassment, hostility
- suggestion - proposes a feature or change
- banter - casual chat, jokes, greetings
- trading - requests to sell, trade, or buy other pokemon
- pkmGuess - If they state a random pokemon name, or a close variation of one
- spam - random spam or just letters put into the chat such as "W" or "aaaaaaaaa" 
- unknown - none of the above, or unclear

Respond with ONLY the category word. No explanation, no punctuation."""},
            {"role": "user", "content": f"Message: {message}"}
        ],
        "stream": False
    })
    return response.json()['message']['content'].strip()

with gzip.open("2026-05-31-1.log.gz", "rt") as f:
    for line in f:
        match = re.search(r"\[Console/\]: \S* ?(\w{3,16}): (.+)", line)
        if match:
           username = match.group(1)
           message = match.group(2)
           messages.append((username, message))
print(messages)

with open("logged_messages.csv", "w") as l:
    for i, (user, message) in enumerate(messages):
        label = classify(message)
        counts[label] = counts.get(label, 0) + 1
        print(f"{i}/{len(messages)} completed")
        l.write(f"{user},{message},{label}\n")

print(counts)
