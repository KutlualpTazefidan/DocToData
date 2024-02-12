from openai import OpenAI
from dotenv import load_dotenv
import os

class ChatGPTClient:
    def __init__(self):
        """
        Initializes the client with the API key.
        """
        load_dotenv()
        OpenAI.api_key = os.getenv("OPENAI_API_KEY")

    def analyze_content(self, prompt, max_tokens=60, temperature=0.7, top_p=1.0):
        """
        Analyzes the importance or relevance of a given text block.

        :param text: The text to analyze for importance or relevance.
        :param max_tokens: The maximum number of tokens to generate in the response.
        :param temperature: Controls randomness in the response generation.
        :param top_p: Controls diversity via nucleus sampling.
        :return: The text of the GPT-3 response, indicating the importance or relevance of the input text.
        """
        client = OpenAI()
        prompt_for_chatgpt = f"Create a step by step guide for composite calculation using this text: \n{prompt}"
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role":"user","content":prompt_for_chatgpt},{"role":"system","content":"You're an engineer specialized in composite materials"}],
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p
        )
        # print("Response:",response)
        print("Response:",response.choices[0].message.content)
        return response.choices[0].message.content