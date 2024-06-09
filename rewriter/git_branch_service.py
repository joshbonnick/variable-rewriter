import subprocess

from typing import List


class GitBranchService:
    def __init__(self):
        self.branch_name = ''

    def create(self, branch_name: str):
        self.branch_name = branch_name

        result = subprocess.run(["git", "checkout", '-b', self.branch_name], capture_output=True, text=True)
        if result.returncode != 0:
            raise Exception(f"Error: unable to create {self.branch_name} with `git checkout -b {self.branch_name}`")

    def push(self, message: str = '', upstream: str = 'origin'):
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", message])
        subprocess.run(["git", 'push', '-u', upstream, self.branch_name])

    @staticmethod
    def get_branches() -> List[str]:
        result = subprocess.run(["git", "branch", '--list'], capture_output=True, text=True)
        if result.returncode == 0:
            branches = result.stdout.splitlines()
            return [branch.strip() for branch in branches]
        else:
            raise Exception("Error: unable to check for git branches with `git branch --list`")

    @staticmethod
    def has_branch(branch: str) -> bool:
        return branch in GitBranchService.get_branches()
