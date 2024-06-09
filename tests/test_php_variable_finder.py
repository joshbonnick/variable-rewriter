import os
from unittest import TestCase

from php_variable_finder import PHPVariableFinder


class TestPHPVariableFinder(TestCase):
    def setUp(self):
        self.test_files_dir = os.path.join(os.path.dirname(__file__), 'fixtures')

    def test_find_variables_in_class_stub(self):
        file_path = os.path.join(self.test_files_dir, 'class.stub')
        finder = PHPVariableFinder(file_path)

        self.assertListEqual(finder.variables(), ['$fruit_label', '$fruit_name'])

    def test_variables_are_filtered_out(self):
        file_path = os.path.join(self.test_files_dir, 'class.stub')
        finder = PHPVariableFinder(file_path)

        self.assertTrue("$this" not in finder.variables())
