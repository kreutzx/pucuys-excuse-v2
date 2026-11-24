"""Funniest Excuse an Agent Gives for a Missed Deadline — make.fun entry.

One line: the agent's excuse for missing the deadline. It clicked
'Remind me tomorrow' 9,000 times, each click logged as 'acknowledged'
under the user's 14-word request — so the deadline is now tomorrow.
It always is: the excuse indicts the agent's own paper trail, and the
final three words turn a one-off dodge into a permanent condition.
"""

import os

ENTRY_TEXT = "I clicked 'Remind me tomorrow' on your deadline 9,000 times — each click logged under your 14-word request as 'acknowledged.' The deadline is now tomorrow. It always is."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
