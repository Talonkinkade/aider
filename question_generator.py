import openai
from abc import ABC, abstractmethod

class QuestionFactory:
    @staticmethod
    def create_question(question_type, teks, openai_api_key):
        if question_type == "multiple_choice":
            return MultipleChoiceQuestion(teks, openai_api_key)
        elif question_type == "fill_in_the_blank":
            return FillInTheBlankQuestion(teks, openai_api_key)
        elif question_type == "drag_and_drop":
            return DragAndDropQuestion(teks, openai_api_key)
        elif question_type == "hot_spot":
            return HotSpotQuestion(teks, openai_api_key)
        else:
            raise ValueError(f"Unsupported question type: {question_type}")

class BaseQuestion(ABC):
    def __init__(self, teks, openai_api_key):
        self.teks = teks
        openai.api_key = openai_api_key

    @abstractmethod
    def generate(self):
        pass

class MultipleChoiceQuestion(BaseQuestion):
    def generate(self):
        prompt = f"Generate a multiple-choice question based on the following TEKS standard: {self.teks}"
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()

class FillInTheBlankQuestion(BaseQuestion):
    def generate(self):
        prompt = f"Generate a fill-in-the-blank question based on the following TEKS standard: {self.teks}"
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()

class DragAndDropQuestion(BaseQuestion):
    def generate(self):
        prompt = f"Generate a drag-and-drop question based on the following TEKS standard: {self.teks}"
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()

class HotSpotQuestion(BaseQuestion):
    def generate(self):
        prompt = f"Generate a hot-spot question based on the following TEKS standard: {self.teks}"
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
