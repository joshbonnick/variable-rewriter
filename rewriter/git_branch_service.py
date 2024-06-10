import subprocess

from typing import List


class GitBranchService:
    def __init__(self):
        self.red_colour = '\033[31m'
        self.reset_colour = '\033[0m'
        self.branch_name = ''

    def create(self, branch_name: str):
        self.branch_name = branch_name

        result = subprocess.run(["git", "checkout", '-b', self.branch_name], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"{self.red_colour}Unable to create '{self.branch_name}' with 'git checkout -b {self.branch_name}'\n{result.stderr}{self.reset_colour}")
            
        return self

    def push(self, message: str = 'chore: convert variable format', upstream: str = 'origin'):
        subprocess.run(["git", "add", "."], capture_output=True, text=True)
        subprocess.run(["git", "commit", "-m", message], capture_output=True, text=True)
        subprocess.run(["git", 'push', '-u', upstream, self.branch_name], capture_output=True, text=True)

    @staticmethod
    def get_branches() -> List[str]:
        result = subprocess.run(["git", "branch", '--list'], capture_output=True, text=True)
        if result.returncode == 0:
            branches = result.stdout.splitlines()
            return [branch.strip() for branch in branches]
        else:
            print("Error: unable to check for git branches with `git branch --list`")
            exit()

    @staticmethod
    def has_branch(branch: str) -> bool:
        return branch in GitBranchService.get_branches()
