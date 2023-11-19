# Vision
'''
Learn how to use GPT-4 to understand images
'''
# Introduction
'''
GPT-4 with Vision, sometimes referred to as GPT-4V or gpt-4-vision-preview in the API, allows the model to take in images and answer questions about them. Historically, language model systems have been limited by taking in a single input modality, text. For many use cases, this constrained the areas where models like GPT-4 could be used.

GPT-4 with vision is currently available to all developers who have access to GPT-4 via the gpt-4-vision-preview model and the Chat Completions API which has been updated to support image inputs. Note that the Assistants API does not currently support image inputs.

It is important to note the following:

* GPT-4 with vision is not a model that behaves differently from GPT-4, with the small exception of the system prompt we use for the model
* GPT-4 with vision is not a different model that does worse at text tasks because it has vision, it is simply GPT-4 with vision added
* GPT-4 with vision is an augmentative set of capabilities for the model

Currently, GPT-4 with vision does not support the message.name parameter, functions/tools, response_format parameter, and we currently set a low max_tokens default which you can override.
'''

'''
Quick start
Images can are made available to the model in two main ways: by passing a link to the image or by passing the base64 encoded image directly in the request. Images can be passed in the user, system and assistant messages. Currently we don't support images in the first system message but this may change in the future.
'''

from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
          "role": "user",
          "content": [
              {"type": "text", "text": "What’s in this image?"},
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

'''
The model is best at answering general questions about what is present in the images. While it does understand the relationship between objects in images, it is not yet optimized to answer detailed questions about the location of certain objects in an image. For example, you can ask it what color a car is or what some ideas for dinner might be based on what is in you fridge, but if you show it an image of a room and ask it where the chair is, it may not answer the question correctly.

It is important to keep in mind the limitations of the model as you explore what use-cases visual understanding can be applied to.
'''
