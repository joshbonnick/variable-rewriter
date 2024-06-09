import os
from unittest import TestCase

import rewriter


class TestFileWriter(TestCase):
    def setUp(self):
        self.target_file = os.path.join(os.path.join(os.path.dirname(__file__), 'fixtures'), 'test-writer.test')
        self.writer = rewriter.FileWriter(self.target_file)

    def tearDown(self):
        if os.path.exists(self.target_file):
            os.remove(self.target_file)

    def test_write_content_to_file(self):
        content = 'Hello, World!'
        self.writer.write(content)
        with open(self.target_file, 'r') as file:
            self.assertEqual(file.read(), content)

    def test_overwrite_content_in_file(self):
        initial_content = 'Initial Content'
        new_content = 'New Content'

        self.writer.write(initial_content)
        with open(self.target_file, 'r') as file:
            self.assertEqual(file.read(), initial_content)

        self.writer.write(new_content)
        with open(self.target_file, 'r') as file:
            self.assertEqual(file.read(), new_content)
