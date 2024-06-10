import sys

from rewriter import *


def main(glob_search: str, method: str):
    for file in glob(glob_search):
        parser = ParserFactory.get_parser(file)

        converter = VariableConverter(parser, method)

        if '--dry' in sys.argv:
            file += '.dry'

        FileWriter(file).write(converter.new_content)

    if '--dry' in sys.argv:
        exit(0)

    branch_name = f'chore/{method}_conversion'

    if GitBranchService.has_branch(branch_name):
        raise Exception(f'[{branch_name}] branch already exists.')

    git_service = GitBranchService()
    git_service.create(branch_name).push()


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else 'camel')
