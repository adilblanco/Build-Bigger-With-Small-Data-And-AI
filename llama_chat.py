from ollama import chat
from ollama import ChatResponse


response: ChatResponse = chat(model='llama3.2', messages=[
  {
    'role': 'user',
    'content': 'What is DuckDB? Answer in two sentences.',
  },
])

print(response['message']['content'])
# or access fields directly from the response object
# print(response.message.content)
