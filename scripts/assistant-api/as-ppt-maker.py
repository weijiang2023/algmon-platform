# TODO: Fix the steps and refector the the program
import os
import time
from pathlib import Path
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"))

assistant_name = "Power Point Generator"
output_file_name = "Presentation.pptx"
assistant_instruction = r"Generate {} file, always. You are subject-matter expert in the topic and professional in creating PowerPoints.. Betweem 1-5 slides. Background, colors, fonts and styling must be modern and easy to read. Make content engaging. Make the file id available to download.".format(
    output_file_name)
prompt_user = "Make a presentation for runner practicing for a half-marathon with an aim for a personal record. Make a presentaton with useful insights, training plan for different levels and some tips before, during and after the training period. Give insights."

assistant = client.beta.assistants.create(
    name=assistant_name,
    instructions=assistant_instruction,
    tools=[{"type": "retrieval"}, {"type": "code_interpreter"}],
    model="gpt-4-1106-preview")

thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content=prompt_user)

run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id)

time.sleep(60.0)  # The API is currently very satured and slow.

run = client.beta.threads.runs.retrieve(
    thread_id=thread.id,
    run_id=run.id)
time.sleep(1)

messages = client.beta.threads.messages.list(
    thread_id=thread.id)

file_path = messages.data[0].content[0].text.annotations[0].file_path.file_id

file_name = client.files.with_raw_response.retrieve_content(file_path)

with open(output_file_name, "wb") as file:
    file.write(file_name.content)

client.files.delete(file_path)
client.beta.assistants.delete(assistant.id)
