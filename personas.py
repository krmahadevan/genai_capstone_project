from abc import ABC, abstractmethod

from llm import GeminiLLM


class Persona(ABC):

    def __init__(self, temperature: float):
        self._llm = None
        self._temperature = temperature

    @abstractmethod
    def get_system_prompt(self, input_text: str) -> str:
        pass

    def call_llm(self, input_text: str) -> str | None:
        sys_prompt = self.get_system_prompt(input_text)
        if not self._llm:
            self._llm = GeminiLLM(system_prompt=sys_prompt, temperature=self._temperature)
        return self._llm.send(input_text)


class Reporter(Persona):

    def get_system_prompt(self, input_text: str) -> str:
        return """
        Write a news article on the topic: """ + input_text + """
        Format:
        - Headline
        - Introduction
        - 3 Body Paragraphs
        - Conclusion
        Keep it neutral and professional and under 50 words.
        """


class Editor(Persona):

    def get_system_prompt(self, input_text: str) -> str:
        return """
        Improve the following article:
        - Fix grammar
        - Improve clarity
        - Improve structure
        - Do NOT add new facts
        Article:
        """ + input_text


class Reviewer(Persona):
    def get_system_prompt(self, input_text: str) -> str:
        return """
        Review the following article and provide:
        - Clarity score (1 to 10)
        - Neutrality assessment
        - Suggestions for improvement
        Article:
        """ + input_text
