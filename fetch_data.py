"""Fetch and process required YouTube channel data."""

import os
from typing import Any

from dotenv import load_dotenv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

load_dotenv()
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")


def get_channel_data(handle: str) -> dict[str, Any] | None:
    """Fetch channel data from YouTube API using the provided handle.

    Args:
        handle: The YouTube channel handle (with or without '@').

    Returns:
        A dictionary with raw channel data if found. None if the channel
        does not exist or an error occurred.
    """
    if not YOUTUBE_API_KEY:
        print("Error: The YouTube API key was not found in .env file.")
        return None

    formatted_handle = handle if handle.startswith("@") else f"@{handle}"

    try:
        youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)
        request = youtube.channels().list(
            part="snippet,statistics",
            forHandle=formatted_handle,
        )
        response = request.execute()
    except HttpError as error:
        print(f"\nAPI Error [{error.resp.status}]: {error.reason}")
        return None

    items = response.get("items", [])
    if not items:
        return None

    return items[0]
