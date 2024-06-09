import os.path
import re
import string


class PHPVariableFinder:
    REGEX = r'\$[a-zA-Z_\x7f-\xff][a-zA-Z0-9_\x7f-\xff]*'

    def __init__(self, filename: string):
        self.filename = filename
        self.found_variables = []

    def variables(self):
        if not os.path.isfile(self.filename):
            raise Exception(f'{self.filename} not found or is not a file.')

        with open(self.filename, 'r') as file:
            for line in file:
                self.found_variables += self.parse(line)

        return self.found_variables

    def parse(self, line: string):
        variables = re.findall(self.REGEX, line)
        filtered_variables = ["$this"]

        return filter(lambda variable: variable not in filtered_variables, variables)
