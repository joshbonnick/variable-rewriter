import sys

from case_converter import CaseConverter
from php_variable_finder import PHPVariableFinder

if __name__ == '__main__':
    finder = PHPVariableFinder(sys.argv[1])

    if len(sys.argv) > 2:
        convert_to = sys.argv[2]
    else:
        convert_to = 'camel'

    variables = list(map(lambda variable: getattr(CaseConverter(variable), convert_to)(), finder.variables()))

    print(variables)
