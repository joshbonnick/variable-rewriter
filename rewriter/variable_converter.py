from case_converter import CaseConverter
from contracts.file_parser import FileParser


class VariableConverter:
    def __init__(self, parser: FileParser, method: str, delimiter: str):
        self.new_content = parser.content()

        for variable in parser.variables():
            self.new_content = self.new_content.replace(variable, getattr(CaseConverter(variable, delimiter), method)())
