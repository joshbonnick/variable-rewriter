import sys

from rewriter import *


def is_dry_run() -> bool:
    return '--dry' in sys.argv


def main(glob_search: str, method: str):
    red = '\033[31m'
    green = '\033[32m'
    blue = '\033[34m'
    reset = '\033[0m'

    found_files = False
    for file in glob(glob_search):
        found_files = True
        parser = ParserFactory.get_parser(file)
        print(f'\n{blue}Parsing {reset}[{file}]{blue} with {reset}Parsers\\{parser.__class__.__name__}')

        converter = VariableConverter(parser, method)
        print(f'{green}Found {len(parser.variables())} variables to convert.')

        if is_dry_run():
            file += '.dry'
            print(f'{red}Rewriter running in test mode, writing new file to {reset}[{file}]{red}')

        FileWriter(file).write(converter.new_content)

    if not found_files:
        print(f'{blue}No files found in {reset}[{glob_search}]{blue} exiting.')
        exit()

    if is_dry_run():
        print(f'{red}Rewriter running in test mode, exiting before pushing to VCS.')
        exit(0)

    branch_name = f'chore/{method}_conversion'

    if GitBranchService.has_branch(branch_name):
        raise Exception(f'[{branch_name}] branch already exists.')

    git_service = GitBranchService()
    git_service.create(branch_name).push()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'Usage: <glob_search> <method=camel|snake>')
        exit(1)
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else 'camel')
