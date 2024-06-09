import sys

import rewriter


def main(file_name: str, method: str):
    parser = rewriter.PHPFileParser(file_name)
    converter = rewriter.VariableConverter(parser, method, '$')
    rewriter.FileWriter(file_name).write(converter.new_content)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else 'camel')
