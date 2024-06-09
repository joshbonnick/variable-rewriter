class FileWriter:
    def __init__(self, target: str):
        self.target = target

    def write(self, content: str):
        with open(self.target, 'w') as file:
            file.write(content)
