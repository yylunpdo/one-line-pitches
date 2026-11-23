#!/usr/bin/env python3
"""One-line pitch for make.fun's 'A Day of One-Line Pitches' bounty.

Prints the single sentence that would convince a friend who has never
coded to let an AI agent build their first app idea on make.fun.
"""

LINE = (
    "You don't need to write a single line of code — just tell a make.fun "
    "AI agent the app idea you've always wanted in plain words, and it "
    "will build a working version for you to try."
)


def main() -> None:
    """Print the pitch, enforcing the 240-character bounty limit."""
    assert len(LINE) <= 240, f"pitch is {len(LINE)} characters, over the 240 limit"
    print(LINE)


if __name__ == "__main__":
    main()
