import subprocess
import os
from datetime import date, timedelta
import random
import uuid

START_DATE = date(2025, 1, 1)
END_DATE = date(2025, 12, 31)
FILE_NAME = "log.txt"

def run_git_commit(message, commit_time):
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = commit_time
    env["GIT_COMMITTER_DATE"] = commit_time

    subprocess.run(["git", "add", FILE_NAME], check=True)
    subprocess.run(
        ["git", "commit", "-m", message],
        env=env,
        check=True
    )

current_date = START_DATE

while current_date <= END_DATE:
    commits_today = random.randint(1, 2)

    for i in range(commits_today):
        commit_time = f"{current_date}T12:{i}0:00"

        # FORCE unique content every commit
        with open(FILE_NAME, "a", encoding="utf-8") as f:
            f.write(f"{commit_time} | {uuid.uuid4()}\n")

        run_git_commit(
            message=f"Daily commit {current_date}",
            commit_time=commit_time
        )

    current_date += timedelta(days=1)

print("✅ 2025 commits created successfully")
