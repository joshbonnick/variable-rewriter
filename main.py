import re
import sys
from php_variable_finder import PHPVariableFinder
from case_converter import CaseConverter

if __name__ == '__main__':
    finder = PHPVariableFinder(sys.argv[1])

    for variable in finder.variables():
        converter = CaseConverter(variable)
        print(converter.snake())
