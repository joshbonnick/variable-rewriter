import subprocess

from typing import List


class GitBranchService:
    @staticmethod
    def create_branch():
        pass

    @staticmethod
    def get_branches() -> List[str]:
        result = subprocess.run(["git", "branch", '--list'], capture_output=True, text=True)
        if result.returncode == 0:
            branches = result.stdout.splitlines()
            return [branch.strip() for branch in branches]
        else:
            raise Exception("Error: unable to check for git branches with `git branch --list`")
