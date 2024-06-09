import string


class PHPFileWriter:
    def __init__(self, target: string):
        self.target = target

    def write(self, content: string):
        with open(self.target, 'w') as file:
            file.write(content)
