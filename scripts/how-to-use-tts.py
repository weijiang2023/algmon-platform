from pathlib import Path
from openai import OpenAI
client = OpenAI()

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
    model="tts-1",
    voice="shimmer",
    # input="Today is a wonderful day to build something people love!"
    # input="人工智能教培空间的公约是小声说话，专注写作业，不干扰同学，不干扰研发团队，不干扰营销团队以及文明自己的行为。希望每位同学都能在空间内获得长久的满足感。"
    input="We all know Chinese and Western food is often very different. Chinese people like eating rice or noodles, but Western people eat bread. Chinese people use chopsticks and bowls but in the West, people usually eat their meals on a plate with a knife and fork. But do you know that people in China have different tastes, too? People from Guangzhou, for example, enjoy sweet and sour food most. They also eat plenty of dilicious dimsum. In Beijing, people eat more noodles, pancakes and dumplings. They also like salty food. People from Sichuan love hot food. Some people think it's too hot and tastes terrible. But I love Sichuan food!"
)

response.stream_to_file(speech_file_path)
