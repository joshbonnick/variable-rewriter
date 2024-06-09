import string
from re import sub


def as_variable(subject: string, delimiter: string = '$'):
    if len(subject) == 0:
        return subject

    return delimiter + subject


class CaseConverter:
    def __init__(self, subject: string):
        self.subject = subject.strip('$')

    def camel(self):
        return as_variable("".join(x.capitalize() for x in self.subject.lower().split("_")))

    def snake(self):
        return as_variable(sub("(?<!^)(?=[A-Z])", "_", self.subject).lower())

    def upper(self):
        return as_variable(self.subject.upper())

    def lower(self):
        return as_variable(self.subject.lower())
