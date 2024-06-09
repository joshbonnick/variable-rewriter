import sys

from case_converter import CaseConverter
from php_variable_finder import PHPVariableFinder

if __name__ == '__main__':
    finder = PHPVariableFinder(sys.argv[1])

    print(finder.variables())

    for variable in finder.variables():
        converter = CaseConverter(variable)
        print(converter.snake())
