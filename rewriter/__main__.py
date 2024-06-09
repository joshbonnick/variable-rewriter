import sys

from php_file_parser import PHPFileParser
from variable_converter import VariableConverter


def main(file_name: str, method: str):
    parser = PHPFileParser(file_name)
    converter = VariableConverter(parser, method, '$')

    print(converter.new_content)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else 'camel')
