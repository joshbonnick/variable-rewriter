import os.path
import re
import string


class PHPVariableFinder:
    REGEX = r'\$[a-zA-Z_\x7f-\xff][a-zA-Z0-9_\x7f-\xff]*'

    def __init__(self, filename: string):
        self.filename = filename

    def variables(self):
        if not os.path.isfile(self.filename):
            raise Exception(f'{self.filename} not found or is not a file.')

        with open(self.filename, 'r') as file:
            file_contents = file.read()

        return re.findall(self.REGEX, file_contents)
