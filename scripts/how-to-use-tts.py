from pathlib import Path
from openai import OpenAI
client = OpenAI()

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
    model="tts-1",
    voice="shimmer",
    # input="Today is a wonderful day to build something people love!"
    input="人工智能教培空间的公约是小声说话，专注写作业，不干扰同学，不干扰研发团队，不干扰营销团队以及文明自己的行为。希望每位同学都能在空间内获得长久的满足感。"
)

response.stream_to_file(speech_file_path)
