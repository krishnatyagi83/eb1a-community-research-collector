"""Approval-gated placeholder for the proposed r/eb_1a research collector.

This file performs no network requests. API access, storage, deletion
synchronization, and optional AI processing will be implemented only after
Reddit explicitly approves the requested scope.
"""

from dataclasses import dataclass
from datetime import date
import os


@dataclass(frozen=True)
class ApprovedScope:
    subreddit: str
    start_date: date
    end_date: date
    include_nested_public_replies: bool
    read_only: bool


REQUESTED_SCOPE = ApprovedScope(
    subreddit="eb_1a",
    start_date=date(2026, 4, 25),
    end_date=date(2026, 7, 25),
    include_nested_public_replies=True,
    read_only=True,
)


def main() -> int:
    print("Requested scope:", REQUESTED_SCOPE)

    if os.getenv("REDDIT_ACCESS_APPROVED") != "true":
        print(
            "Stopped: Reddit API access is approval-pending. "
            "No network request was made."
        )
        return 2

    print(
        "Approval flag detected, but the network client is intentionally "
        "not implemented in this placeholder."
    )
    return 3


if __name__ == "__main__":
    raise SystemExit(main())
