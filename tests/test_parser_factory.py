import os
from unittest import TestCase

from rewriter import PHPFileParser
from rewriter import ParserFactory


class TestParserFactory(TestCase):
    def setUp(self):
        self.test_files_dir = os.path.join(os.path.dirname(__file__), 'fixtures')
        self.file_path = os.path.join(self.test_files_dir, 'class.php')

    def test_get_parser_does_not_throw_an_exception_when_no_parser(self):
        ParserFactory.get_parser(self.file_path)

    def test_get_parser_returns_correct_parser(self):
        factory = ParserFactory.get_parser(self.file_path)

        assert isinstance(factory, PHPFileParser)
