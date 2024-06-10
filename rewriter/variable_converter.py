import rewriter


class VariableConverter:
    def __init__(self, parser: rewriter.IFileParser, method: str):
        self.new_content = parser.content()

        for variable in parser.variables():
            new_variable = getattr(rewriter.CaseConverter(variable, parser.variable_delimiter()), method)()
            self.new_content = self.new_content.replace(variable.strip(parser.variable_delimiter()), new_variable.strip(parser.variable_delimiter()))
