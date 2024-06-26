import argparse
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
    print(f'\n{green}Rewriting variables in {glob_search} to {method} case')
    for file in glob(glob_search):
        found_files = True
        parser = ParserFactory.get_parser(file)
        print(f'{blue}Parsing {reset}[{file}]{blue} with {reset}Parsers\\{parser.__class__.__name__}')

        converter = VariableConverter(parser, method)
        print(f'{green}Found {len(parser.variables())} variable(s).')

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
        print(f'[{branch_name}] branch already exists.')
        exit()

    git_service = GitBranchService()
    git_service.create(branch_name)


if __name__ == '__main__':
    arguments = argparse.ArgumentParser(description='Rewrite variables in files.')
    arguments.add_argument('glob_search', type=str, help='The glob pattern to search for files. Surrounded with quotations.')
    arguments.add_argument('method', type=str, choices=['camel', 'snake'], nargs='?', default='camel', help='The method of conversion (camel or snake).')
    arguments.add_argument('--dry', action='store_true', help='Run in dry mode without making any changes.')

    args = arguments.parse_args()

    main(args.glob_search, args.method)
