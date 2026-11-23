"""Expected answers for mailroom, written as checks.

Run with: uv run checks.py
Each assert states something that must be true. If one is false, Python stops
and shows which line failed.
"""

from mailroom import count_by_group, count_subscribers, load_subscribers

subscribers = load_subscribers("data/subscribers.csv")
by_group = count_by_group(subscribers)

# The list has 24 subscribers in total.
assert count_subscribers(subscribers) == 24

# Each of the three groups has 8.
assert by_group["tea-curious"] == 8
assert by_group["gift-buyers"] == 8
assert by_group["daily-drinkers"] == 8

print("All checks passed.")
