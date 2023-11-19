'''
Multiple image inputs

The Chat Completions API is capable of taking in and processing multiple image inputs in both base64 encoded format or as an image URL. The model will process each image and use the information from all of them to answer the question.

Here the model is shown two copies of the same image and can answer questions about both or each of the images independently.
'''
from openai import OpenAI

client = OpenAI()
response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
          "role": "user",
          "content": [
              {
                  "type": "text",
                  "text": "What are in these images? Is there any difference between them?",
              },
              {
                  "type": "image_url",
                  "image_url": {
                      "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                  },
              },
              {
                  "type": "image_url",
                  "image_url": {
                      "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                  },
              },
          ],
        }
    ],
    max_tokens=300,
)
print(response.choices[0])
