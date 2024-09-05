import unittest
from question_generator import QuestionFactory, MultipleChoiceQuestion, FillInTheBlankQuestion, DragAndDropQuestion, HotSpotQuestion

class TestQuestionGenerator(unittest.TestCase):
    def setUp(self):
        self.teks = "Students will understand the basic principles of photosynthesis."
        self.api_key = "dummy_api_key"

    def test_multiple_choice_question(self):
        question = QuestionFactory.create_question("multiple_choice", self.teks, self.api_key)
        self.assertIsInstance(question, MultipleChoiceQuestion)
        generated = question.generate()
        self.assertIsInstance(generated, str)
        self.assertGreater(len(generated), 0)

    def test_fill_in_the_blank_question(self):
        question = QuestionFactory.create_question("fill_in_the_blank", self.teks, self.api_key)
        self.assertIsInstance(question, FillInTheBlankQuestion)
        generated = question.generate()
        self.assertIsInstance(generated, str)
        self.assertGreater(len(generated), 0)

    def test_drag_and_drop_question(self):
        question = QuestionFactory.create_question("drag_and_drop", self.teks, self.api_key)
        self.assertIsInstance(question, DragAndDropQuestion)
        generated = question.generate()
        self.assertIsInstance(generated, str)
        self.assertGreater(len(generated), 0)

    def test_hot_spot_question(self):
        question = QuestionFactory.create_question("hot_spot", self.teks, self.api_key)
        self.assertIsInstance(question, HotSpotQuestion)
        generated = question.generate()
        self.assertIsInstance(generated, str)
        self.assertGreater(len(generated), 0)

    def test_invalid_question_type(self):
        with self.assertRaises(ValueError):
            QuestionFactory.create_question("invalid_type", self.teks, self.api_key)

if __name__ == '__main__':
    unittest.main()
