import os
import unittest

import rewriter


class TestPHPVariableFinder(unittest.TestCase):
    def setUp(self):
        self.test_files_dir = os.path.join(os.path.dirname(__file__), '../fixtures')

    def test_find_variables_in_class_stub(self):
        file_path = os.path.join(self.test_files_dir, 'class.stub')
        finder = rewriter.PHPFileParser(file_path)

        self.assertListEqual(finder.variables(), ['$name', '$color', '$seeds', '$fruit_name', '$fruit_label'])

    def test_variables_are_filtered_out(self):
        file_path = os.path.join(self.test_files_dir, 'class.stub')
        finder = rewriter.PHPFileParser(file_path)

        self.assertTrue("$this" not in finder.variables())
