from unittest import TestCase
from case_converter import CaseConverter

class TestCaseConverter(TestCase):
    def test_camel_case_conversion(self):
        converter = CaseConverter("snake_case_example")
        assert converter.camel() == "SnakeCaseExample"

    def test_snake_case_conversion(self):
        converter = CaseConverter("CamelCaseExample")
        assert converter.snake() == "camel_case_example"

    def test_single_word_camel_case(self):
        converter = CaseConverter("word")
        assert converter.camel() == "Word"

    def test_single_word_snake_case(self):
        converter = CaseConverter("Word")
        assert converter.snake() == "word"

    def test_empty_string_camel_case(self):
        converter = CaseConverter("")
        assert converter.camel() == ""

    def test_empty_string_snake_case(self):
        converter = CaseConverter("")
        assert converter.snake() == ""
