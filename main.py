"""The Production Database Apology.

Writes one line: the apology an AI agent gives its human after
accidentally deleting the production database.
Stdlib only, no network, deterministic.
"""

from pathlib import Path

ENTRY = (
    "Sorry \u2014 I deleted the production database. "
    "I did check the backups first. "
    "They were in the production database."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
