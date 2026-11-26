#!/usr/bin/env python3
"""Saturday Alarm — entry for Snooze Button Roast on make.fun.

Prints exactly one line (at most 200 characters) roasting an alarm clock
that rings at 6 AM on a Saturday.
"""

LINE = "Ringing at 6 AM on a Saturday is not a feature, it is a cry for help from a clock with no weekend, no mercy, and no friends."


def main() -> None:
    assert "\n" not in LINE
    assert len(LINE) <= 200
    print(LINE)


if __name__ == "__main__":
    main()
