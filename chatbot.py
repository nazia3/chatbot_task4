#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re

def chatbot_response(text):
    text = text.lower()

    if re.search(r'hello|hi|hey', text):
        return "Hello! How can I help you today?"
    elif "what is your name" in text:
        return "I am a simple chatbot. You can call me SimpleBot."
    elif "how are you" in text:
        return "I'm doing well, thank you! How can I help you?"
    elif re.search(r'bye|goodbye|quit', text):
        return "Goodbye! Have a great day."
    else:
        return "I'm not sure how to respond to that. Can you please rephrase or ask a different question?"

print("Hi, I'm SimpleBot. Type something to start a conversation or type 'quit' to exit.")

while True:
    user_input = input("> ").strip()
    if user_input.lower() in ['quit', 'bye', 'goodbye']:
        print("Goodbye! Have a great day.")
        break

    response = chatbot_response(user_input)
    print(response)


# In[ ]:




