import os
from unittest import TestCase

from rewriter.php_file_parser import PHPFileParser


class TestPHPVariableFinder(TestCase):
    def setUp(self):
        self.test_files_dir = os.path.join(os.path.dirname(__file__), 'fixtures')

    def test_find_variables_in_class_stub(self):
        file_path = os.path.join(self.test_files_dir, 'class.stub')
        finder = PHPFileParser(file_path)

        self.assertListEqual(finder.variables(), ['$name', '$color', '$seeds', '$fruit_name', '$fruit_label'])

    def test_variables_are_filtered_out(self):
        file_path = os.path.join(self.test_files_dir, 'class.stub')
        finder = PHPFileParser(file_path)

        self.assertTrue("$this" not in finder.variables())
