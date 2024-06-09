import string
import sys

from case_converter import CaseConverter
from php_file_parser import PHPFileParser


def main(filename: string, convert_to: string):
    file = PHPFileParser(filename)

    new_content = file.content()

    for variable in file.variables():
        new_content = new_content.replace(variable, getattr(CaseConverter(variable), convert_to)())

    print(new_content)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else 'camel')
