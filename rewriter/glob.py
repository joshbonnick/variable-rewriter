from glob import iglob

from typing import Iterator


def glob(search: str) -> Iterator[str]:
    return iglob(search, recursive=True)
