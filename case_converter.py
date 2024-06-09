from re import sub


class CaseConverter:
    def __init__(self, subject: str):
        self.variable_delimiter = ""
        self.subject = subject.strip(self.variable_delimiter)

    def as_variable(self, subject: str):
        if len(subject) == 0:
            return subject

        return self.variable_delimiter + subject

    def set_delimiter(self, delimiter: str):
        self.variable_delimiter = delimiter

        return self

    def camel(self) -> str:
        return self.as_variable("".join(x.capitalize() for x in self.subject.lower().split("_")))

    def snake(self) -> str:
        return self.as_variable(sub("(?<!^)(?=[A-Z])", "_", self.subject).lower())

    def upper(self) -> str:
        return self.as_variable(self.subject.upper())

    def lower(self) -> str:
        return self.as_variable(self.subject.lower())
