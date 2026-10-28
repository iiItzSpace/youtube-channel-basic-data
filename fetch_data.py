"""Fetch and process required YouTube channel data."""

import os
from typing import Any

from dotenv import load_dotenv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

load_dotenv()
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")


def parse_channel_data(raw_item: dict[str, Any]) -> dict[str, str]:
    """Extract and format channel metrics from YouTube API response.

    Args:
        raw_item: A dictionary containing the raw channel data
            ('snippet' and 'statistics').

    Returns:
        A dictionary with the cleaned channel data, including name,
        link, subscribers, views, videos, country, published_at, and
        date_joined.
    """
    snippet = raw_item.get("snippet", {})
    statistics = raw_item.get("statistics", {})

    channel_id = raw_item.get("id", "")
    custom_url = snippet.get("customUrl", "")

    if custom_url:
        link = f"https://www.youtube.com/{custom_url}"
    elif channel_id:
        link = f"https://www.youtube.com/channel/{channel_id}"
    else:
        link = "N/A"

    subscribers = statistics.get("subscriberCount", "N/A")
    views = statistics.get("viewCount", "N/A")
    videos = statistics.get("videoCount", "N/A")

    name = snippet.get("title", "N/A")
    country = snippet.get("country", "N/A")

    published_at = snippet.get("publishedAt", "")
    date_joined = published_at[:10] if published_at else "N/A"

    return {
        "name": name,
        "link": link,
        "subscribers": subscribers,
        "views": views,
        "videos": videos,
        "country": country,
        "published_at": published_at,
        "date_joined": date_joined,
    }


def get_channel_data(handle: str) -> dict[str, str] | None:
    """Fetch and parse channel data from the YouTube API by handle.

    Args:
        handle: The YouTube channel handle (with or without '@').

    Returns:
        A dictionary with the parsed channel data if found, or None if
        the channel does not exist or an API error occurs.
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

    return parse_channel_data(items[0])
