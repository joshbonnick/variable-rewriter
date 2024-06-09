import sys

from rewriter import *


def main(file_name: str, method: str):
    parser = PHPFileParser(file_name)
    converter = VariableConverter(parser, method, '$')
    FileWriter(file_name).write(converter.new_content)

    branch_name = f'chore/{method}_conversion'

    if GitBranchService.has_branch(branch_name):
        raise Exception(f'{branch_name} branch already exists, exiting.')

    git_service = GitBranchService()
    git_service.create(branch_name).push()


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else 'camel')
