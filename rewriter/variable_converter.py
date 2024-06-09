from rewriter.case_converter import CaseConverter
from rewriter.php_file_parser import PHPFileParser


class VariableConverter:
    def __init__(self, parser: PHPFileParser, method: str, delimiter: str):
        self.new_content = parser.content()

        for variable in parser.variables():
            self.new_content = self.new_content.replace(variable, getattr(CaseConverter(variable, delimiter), method)())
