from unittest import TestCase

import rewriter


class TestCaseConverter(TestCase):
    def test_lower_case_conversion(self):
        converter = rewriter.CaseConverter("some_CASEexample")
        assert converter.lower() == "some_caseexample", f'Returned: [{converter.lower()}]'

    def test_upper_case_conversion(self):
        converter = rewriter.CaseConverter("some_CASEeXaMple")
        assert converter.upper() == "SOME_CASEEXAMPLE", f'Returned: [{converter.upper()}]'

    def test_camel_case_conversion(self):
        converter = rewriter.CaseConverter("snake_case_example")
        assert converter.camel() == "snakeCaseExample", f'Returned: [{converter.camel()}]'

    def test_camel_case_conversion_from_camel_case(self):
        converter = rewriter.CaseConverter("CamelCaseExample")
        assert converter.camel() == "camelCaseExample", f'Returned: [{converter.camel()}]'
        converter = rewriter.CaseConverter("camelCaseExample")
        assert converter.camel() == "camelCaseExample", f'Returned: [{converter.camel()}]'

    def test_snake_case_conversion(self):
        converter = rewriter.CaseConverter("CamelCaseExample")
        assert converter.snake() == "camel_case_example", f'Returned: [{converter.snake()}]'

    def test_single_word_camel_case(self):
        converter = rewriter.CaseConverter("word")
        assert converter.camel() == "word", f'Returned: [{converter.camel()}]'

    def test_multiple_word_camel_case(self):
        converter = rewriter.CaseConverter("three_wordVariable")
        assert converter.camel() == "threeWordVariable", f'Returned: [{converter.camel()}]'
        converter = rewriter.CaseConverter("two_word")
        assert converter.camel() == "twoWord", f'Returned: [{converter.camel()}]'

    def test_chaos_to_camel_case(self):
        converter = rewriter.CaseConverter("convert-to_camel case")
        assert converter.camel() == "convertToCamelCase", f'Returned: [{converter.camel()}]'

    def test_single_word_snake_case(self):
        converter = rewriter.CaseConverter("Word")
        assert converter.snake() == "word", f'Returned: [{converter.snake()}]'

    def test_chaos_into_snake_case(self):
        converter = rewriter.CaseConverter("product_Price")
        assert converter.snake() == "product_price", f'Returned: [{converter.snake()}]'
        converter = rewriter.CaseConverter("product__Price")
        assert converter.snake() == "product__price", f'Returned: [{converter.snake()}]'
        converter = rewriter.CaseConverter("producT_PRice")
        assert converter.snake() == "produc_t_price", f'Returned: [{converter.snake()}]'

    def test_empty_string(self):
        converter = rewriter.CaseConverter("")
        assert converter.camel() == "", f'Returned: [{converter.camel()}]'
        assert converter.snake() == "", f'Returned: [{converter.snake()}]'

    def test_snake_case_when_starting_with_capital(self):
        converter = rewriter.CaseConverter("SnakeCase")
        assert converter.snake() == "snake_case", f'Returned: [{converter.snake()}]'
