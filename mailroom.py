"""Mailroom: a command-line tool for Kettlebird Tea's Steep Club newsletter.

Usage: uv run mailroom.py subscribers
"""

import csv
import sys


def load_subscribers(path):
    """Read the CSV file and return a list of dictionaries, one per subscriber."""
    with open(path, newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def count_subscribers(subscribers):
    """Return how many subscribers there are in total."""
    return len(subscribers)


def count_by_group(subscribers):
    """Return a dictionary mapping each group name to its number of subscribers."""
    counts = {}
    for subscriber in subscribers:
        group = subscriber["group"]
        if group in counts:
            counts[group] += 1
        else:
            counts[group] = 1
    return counts


def main():
    arguments = sys.argv[1:]
    if arguments == ["subscribers"]:
        subscribers = load_subscribers("data/subscribers.csv")
        print(f"Total subscribers: {count_subscribers(subscribers)}")
        for group, count in count_by_group(subscribers).items():
            print(f"  {group}: {count}")
    else:
        print("Usage: uv run mailroom.py subscribers")
        sys.exit(1)


if __name__ == "__main__":
    main()
