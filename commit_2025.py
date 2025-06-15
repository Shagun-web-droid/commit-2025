import os
from datetime import date, timedelta
import random

START_DATE = date(2025, 1, 1)
END_DATE = date(2025, 12, 31)

FILE_NAME = "log.txt"

current_date = START_DATE

while current_date <= END_DATE:
    commits_today = random.randint(2, 3)  # green intensity

    for i in range(commits_today):
        timestamp = f"{current_date}T12:{i}0:00"

        with open(FILE_NAME, "a") as f:
            f.write(f"Commit on {timestamp}\n")

        os.system("git add .")

        os.system(
            f'GIT_AUTHOR_DATE="{timestamp}" '
            f'GIT_COMMITTER_DATE="{timestamp}" '
            f'git commit -m "Daily commit {current_date}"'
        )

    current_date += timedelta(days=1)

print("✅ 2025 commits created successfully!")
