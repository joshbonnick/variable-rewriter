import string
from re import sub

class CaseConverter:
    def __init__(self, subject: string):
        self.subject = subject

    def camel(self):
        return "".join(x.capitalize() for x in self.subject.lower().split("_"))

    def snake(self):
        return sub("(?<!^)(?=[A-Z])", "_", self.subject).lower()