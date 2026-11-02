"""CLI entry point to fetch YouTube channel basic data."""

import io
import sys

if sys.platform == "win32":
    import msvcrt
else:
    import termios

from display_data import display_channel_data
from fetch_data import YoutubeDataFetcher


def clear_input_buffer() -> None:
    """Clear the terminal input buffer.

    This prevents inputs from being read during network requests.
    """
    if sys.platform == "win32":
        while msvcrt.kbhit():
            msvcrt.getch()
    else:
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)


def main() -> int:
    """Run the interactive CLI loop to fetch and display channel data.

    Returns:
        The exit code (0 when the user exits successfully).
    """
    if sys.platform == "win32" and isinstance(sys.stdout, io.TextIOWrapper):
        sys.stdout.reconfigure(encoding="utf-8")

    print("=== YouTube Channel Data ===")

    fetcher = YoutubeDataFetcher()

    while True:
        print()
        handle = input("Enter the YouTube channel handle: @").strip()
        if not handle:
            print("You did not enter a YouTube channel handle.")
            continue

        print("Processing")
        channel_data = fetcher.get_channel_data(handle)

        if channel_data:
            display_channel_data(channel_data)
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
