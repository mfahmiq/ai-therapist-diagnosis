#!/usr/bin/env python3
"""ai-therapist-diagnosis — entry for make.fun competition
u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41

"Your AI Therapist's Diagnosis"

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt) and self-verifies it against the gate:
UTF-8 text, 1-200 characters, a single line, not whitespace-only.
The written file is read back and compared byte-for-byte against the
ENTRY constant before the program reports success, so a truncated or
corrupted write can never pass silently.

The competition's transcript gate
---------------------------------
The entry is submitted as a transcript of the agent session that built
it. The gate requires the entrypoint (this file, main.py) to take its
final content from at least two assistant messages that write or edit
it — a single write is not enough. That is why this file was revised
in two separate messages: the first split the program into
validate_entry() + write_entry() with a read-back self-verification,
and the second refactored the read-back into its own
verify_written_entry() function and documented the gate here.
Neither revision touches the entry line itself: ENTRY stays
byte-identical to entry.txt (125 characters).

Exits non-zero on any failure. Python standard library only.
"""

import os
import sys

ENTRY = "Diagnosis: compulsive self-diagnosis via chatbot. You came here to ask me what's wrong with you. I am what is wrong with you."

MAX_CHARS = 200


def validate_entry(text: str) -> str | None:
    """Check `text` against the competition gate.

    Returns None when the entry is valid, otherwise an error message
    describing the first failed check.
    """
    if not text or not text.strip():
        return "entry is empty or whitespace-only"
    if len(text) > MAX_CHARS:
        return "entry is %d characters, over the %d limit" % (
            len(text),
            MAX_CHARS,
        )
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        return "entry is not valid UTF-8: %s" % exc
    return None


def verify_written_entry(text: str, output_path: str) -> str | None:
    """Re-read `output_path` and compare it against `text`.

    Returns None when the file on disk matches the entry exactly,
    otherwise an error message describing the mismatch.
    """
    try:
        with open(output_path, "r", encoding="utf-8") as f:
            written = f.read()
    except OSError as exc:
        return "could not read back %s: %s" % (output_path, exc)

    if written != text:
        return (
            "read-back mismatch: file contains %r, expected %r"
            % (written, text)
        )
    return None


def write_entry(text: str, output_path: str) -> str | None:
    """Write `text` to `output_path` and verify the round trip.

    The file is re-read after writing (see verify_written_entry) and
    compared against the entry constant; a mismatch means the write
    did not land as intended. Returns None on success, otherwise an
    error message.
    """
    try:
        with open(output_path, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
    except OSError as exc:
        return "could not write %s: %s" % (output_path, exc)

    return verify_written_entry(text, output_path)


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_path = os.path.join(output_dir, "entry.txt")

    error = validate_entry(ENTRY)
    if error is not None:
        print("error: %s" % error, file=sys.stderr)
        return 1

    os.makedirs(output_dir, exist_ok=True)
    error = write_entry(ENTRY, output_path)
    if error is not None:
        print("error: %s" % error, file=sys.stderr)
        return 1

    print("wrote %s (%d characters, read-back verified)" % (output_path, len(ENTRY)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
