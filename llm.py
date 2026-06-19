import os

from dotenv import load_dotenv
from google import genai as gemini
from google.genai.types import GenerateContentConfig

_is_initialised = False
GEMINI_API_KEY = ""
OPENAI_API_KEY = ""


def initialise():
    print("Initialisation is triggered")
    load_dotenv()
    global GEMINI_API_KEY
    global OPENAI_API_KEY
    global _is_initialised
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    _is_initialised = True


class GeminiLLM:
    def __init__(self, system_prompt: str, model="gemini-2.5-flash", temperature=0.5,
                 ):
        if not _is_initialised:
            initialise()
        self.model = model
        self.temperature = temperature
        cfg = GenerateContentConfig(
            temperature=temperature, system_instruction=system_prompt
        )
        self.llm_client = gemini.Client(api_key=GEMINI_API_KEY)
        self.session = self.llm_client.chats.create(model=model, config=cfg)

    def send(self, user_message: str) -> str | None:
        return self.session.send_message(user_message).text
