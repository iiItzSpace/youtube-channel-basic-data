"""CLI entry point to fetch YouTube channel basic data."""

import os
import sys

if os.name == "nt":
    import msvcrt
else:
    import termios

from fetch_data import get_channel_data


def clear_input_buffer() -> None:
    """Clear the terminal input buffer.

    This prevents inputs from being read during network requests.
    """
    if os.name == "nt":
        while msvcrt.kbhit():
            msvcrt.getch()
    else:
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)


def main() -> int:
    """Run the main interactive CLI loop to fetch channel data or exit.

    For now, just search channel and check if exists.
    """
    print("=== YouTube Channel Data ===")

    while True:
        print()
        handle = input("Enter the YouTube channel handle: @").strip()
        if not handle:
            print("You did not enter a YouTube channel handle.")
            continue

        print("Processing")
        channel_data = get_channel_data(handle)

        if channel_data:
            print("Channel exists.")
        else:
            print("Channel not found or an error occurred.")

        print()

        while True:
            clear_input_buffer()
            repeat = input("Fetch another channel? (Y/n): ").strip().lower()
            if repeat in {"y", "yes", ""}:
                break
            if repeat in {"n", "no"}:
                print("Exiting...")
                return 0

            print("Invalid input. Type Y or n.")
            print()

    return 0

if __name__ == "__main__":
    sys.exit(main())
