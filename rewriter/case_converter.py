from re import findall
from re import match
from re import split
from re import sub


class CaseConverter:
    def __init__(self, subject: str, delimiter: str = ''):
        self.variable_delimiter = delimiter
        self.subject = subject.strip(self.variable_delimiter)

    def _as_variable(self, subject: str):
        if len(subject) == 0:
            return subject

        return self.variable_delimiter + subject

    def camel(self) -> str:
        if len(self.subject) == 0:
            return self.subject

        # Check if the string is already in camel case
        if self._is_camel_case():
            return self.subject

        words = findall(r'[A-Za-z][a-z]*', self.subject) if match(r'^[A-Za-z]+$', self.subject) else split(r'[\s_-]+', self.subject)

        self.subject = words[0].lower() + ''.join(word.capitalize() for word in words[1:])

        return self._as_variable(self.subject)

    def snake(self) -> str:
        if len(self.subject) == 0:
            return self.subject

        return self._as_variable(sub("(?<!^)(?=[A-Z])", "_", self.subject).lower())

    def upper(self) -> str:
        return self._as_variable(self.subject.upper())

    def lower(self) -> str:
        return self._as_variable(self.subject.lower())

    def _is_camel_case(self) -> bool:
        return match(r'^[a-z][a-zA-Z]*$', self.subject) and not match(r'^[a-z]+(?:[A-Z][a-z]*)*$', self.subject)
