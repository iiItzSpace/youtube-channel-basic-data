"""Receive and display data from the API"""
def display_channel_data(channel_data: dict[str, str]) -> None:
    """Print the parsed channel data in a good readable format.

    Args:
        channel_data: A dictionary with the parsed channel data.

    Returns: None. The function prints the parsed channel data.
    """
    print()
    print(f"Channel name: {channel_data["name"]}")
    print(f"Link: {channel_data["link"]}")
    print(f"Subscribers amount: {int(channel_data["subscribers"]):,}")
    print(f"Total views: {int(channel_data["views"]):,}")
    print(f"Total video's amount: {int(channel_data["videos"]):,}")
    print(f"Country: {channel_data["country"]}")
    print(f"Date joined: {channel_data["published_at"]}")