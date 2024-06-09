from re import findall
from re import match
from re import sub


class CaseConverter:
    def __init__(self, subject: str, delimiter: str = ''):
        self.variable_delimiter = delimiter
        self.subject = subject.strip(self.variable_delimiter)

    def camel(self) -> str:
        if len(self.subject) == 0:
            return self.subject

        if self._is_camel_case():
            return self.subject

        words = self._split_words()

        self.subject = words[0].lower() + ''.join(word.capitalize() for word in words[1:])

        return self._as_variable(self.subject)

    def snake(self) -> str:
        if len(self.subject) == 0:
            return self.subject

        snake = sub(r'(?<=[a-z])(?=[A-Z])', '_', self.subject).lower()

        return self._as_variable(snake)

    def upper(self) -> str:
        return self._as_variable(self.subject.upper())

    def lower(self) -> str:
        return self._as_variable(self.subject.lower())

    def _split_words(self) -> list:
        words = []

        for word_list in [findall(r'[A-Z]?[a-z]*', word) for word in self.subject.split('_')]:
            words.extend(word_list)

        return words

    def _as_variable(self, subject: str) -> str:
        if len(subject) == 0:
            return subject

        return self.variable_delimiter + subject

    def _is_camel_case(self) -> bool:
        return match(r'^[a-z][a-zA-Z]*$', self.subject) and not match(r'^[a-z]+(?:[A-Z][a-z]*)*$', self.subject)
