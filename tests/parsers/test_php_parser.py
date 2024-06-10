import os
import unittest

import rewriter


class TestPHPVariableFinder(unittest.TestCase):
    def setUp(self):
        self.test_files_dir = os.path.join(os.path.dirname(__file__), '../fixtures')

    def test_global_uppercase_variables_are_ignored(self):
        file_path = os.path.join(self.test_files_dir, 'class.php')
        parser = rewriter.PHPFileParser(file_path)

        self.assertTrue("$_SERVER" not in parser.variables())

    def test_find_variables_in_class_stub(self):
        file_path = os.path.join(self.test_files_dir, 'class.php')
        parser = rewriter.PHPFileParser(file_path)

        self.assertListEqual(parser.variables(), ['$name', '$color', '$seeds', '$fruit_name', '$fruit_label'])

    def test_this_variable_is_filtered_out(self):
        file_path = os.path.join(self.test_files_dir, 'class.php')
        parser = rewriter.PHPFileParser(file_path)

        self.assertTrue("$this" not in parser.variables())
