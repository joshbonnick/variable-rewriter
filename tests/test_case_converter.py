from unittest import TestCase

import rewriter


class TestCaseConverter(TestCase):
    def test_lower_case_conversion(self):
        converter = rewriter.CaseConverter("some_CASEexample")
        assert converter.lower() == "some_caseexample"

    def test_upper_case_conversion(self):
        converter = rewriter.CaseConverter("some_CASEeXaMple")
        assert converter.upper() == "SOME_CASEEXAMPLE"

    def test_camel_case_conversion(self):
        converter = rewriter.CaseConverter("snake_case_example")
        assert converter.camel() == "SnakeCaseExample"

    def test_snake_case_conversion(self):
        converter = rewriter.CaseConverter("CamelCaseExample")
        assert converter.snake() == "camel_case_example"

    def test_single_word_camel_case(self):
        converter = rewriter.CaseConverter("word")
        assert converter.camel() == "Word"

    def test_single_word_snake_case(self):
        converter = rewriter.CaseConverter("Word")
        assert converter.snake() == "word"

    def test_empty_string_camel_case(self):
        converter = rewriter.CaseConverter("")
        assert converter.camel() == ""

    def test_empty_string_snake_case(self):
        converter = rewriter.CaseConverter("")
        assert converter.snake() == ""

    def test_snake_case_when_starting_with_capital(self):
        converter = rewriter.CaseConverter("SnakeCase")
        assert converter.snake() == "snake_case"
