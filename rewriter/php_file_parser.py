import os.path
import re

import rewriter


class PHPFileParser(rewriter.IFileParser):
    REGEX = r'\$[a-zA-Z_\x7f-\xff][a-zA-Z0-9_\x7f-\xff]*'

    def __init__(self, filename: str):
        self.filename = filename
        self.found_variables = []

        if not os.path.isfile(self.filename):
            raise Exception(f'{self.filename} not found or is not a file.')

        with open(self.filename, 'r') as file:
            for line in file:
                self.found_variables += self._parse(line)

            file.seek(0)
            self.file_content = file.read()

    def content(self) -> str:
        return self.file_content

    def variables(self) -> list:
        return self.found_variables

    def _parse(self, line: str) -> list:
        variables = re.findall(self.REGEX, line)
        filtered_variables = ["$this"]

        return filter(lambda variable: variable not in filtered_variables and variable not in self.found_variables, variables)
