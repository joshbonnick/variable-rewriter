import rewriter


class VariableConverter:
    def __init__(self, parser: rewriter.IFileParser, method: str, delimiter: str):
        self.new_content = parser.content()

        for variable in parser.variables():
            self.new_content = self.new_content.replace(variable, getattr(rewriter.CaseConverter(variable, delimiter), method)())
