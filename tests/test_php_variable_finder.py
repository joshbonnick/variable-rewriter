from unittest import TestCase
import os
from php_variable_finder import PHPVariableFinder

class TestPHPVariableFinder(TestCase):
    def setUp(self):
        self.test_files_dir = os.path.join(os.path.dirname(__file__), 'fixtures')

    def test_find_variables_in_class_fixture(self):
        file_path = os.path.join(self.test_files_dir, 'class.stub')
        finder = PHPVariableFinder(file_path)

        self.assertListEqual(finder.variables(), ['$fruit_label', '$fruit_name'])