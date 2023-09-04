import os
import openai
# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")

# list models
models = openai.Model.list()

# print the first model's id
print(models.data[0].id)


response = openai.Completion.create(
  engine="text-davinci-002",
  prompt="Translate the following English text to French: '{hello}'",
  max_tokens=60
)

print(response.choices[0].text.strip())