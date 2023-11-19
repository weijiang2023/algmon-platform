# TODO: Fix the steps and refector the the program
import openai as client

# step 1: Create an Assistant
assistant = client.beta.assistants.create(
    name="Math Tutor",
    instructions="You are a personal math tutor. Write and run code to answer math questions.",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4-1106-preview"
)

# step 2: Create a Thread
thread = client.beta.threads.create()

# step 3: Add a Message to a Thread
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
)

# step 4: Run the Assistant
run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
    instructions="Please address the user as Jane Doe. The user has a premium account."
)

# step 5: Check the Run status
run = client.beta.threads.runs.retrieve(
    thread_id=thread.id,
    run_id=run.id
)

# step 6: Display the Assistant's Response
messages = client.beta.threads.messages.list(
    thread_id=thread.id
)

print(messages)
