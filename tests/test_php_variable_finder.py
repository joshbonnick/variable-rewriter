from unittest import TestCase
import os
from php_variable_finder import PHPVariableFinder

class TestPHPVariableFinder(TestCase):
    def setUp(self):
        self.test_files_dir = os.path.join(os.path.dirname(__file__), 'fixtures')

    def test_find_variables_in_class_fixture(self):
        file_path = os.path.join(self.test_files_dir, 'class.php')
        expected_variables = ['$fruit_label', '$fruit_name']
        finder = PHPVariableFinder(file_path)
        found_variables = finder.variables()
        self.assertListEqual(found_variables, expected_variables)