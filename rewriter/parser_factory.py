import pathlib

import rewriter


class ParserFactory:
    @staticmethod
    def get_parser(file_name: str) -> rewriter.IFileParser:
        file_extension = pathlib.Path(file_name).suffix

        try:
            return {
                '.php': rewriter.PHPFileParser(file_name),
            }[file_extension]
        except:
            print(f"Unable to find parser for [{file_extension}] files")
