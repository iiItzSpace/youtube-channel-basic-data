# YouTube Channel Basic Data ▶️

A Python command-line interface (CLI) tool that fetches and displays real-time
data of any YouTube channel using the official YouTube public API.

*An image will be added soon when the CLI is completed.*

## Features 🛠️

### Current Capabilities:

- [x] Interactive CLI loop with cross-OS input buffer flushing (Windows, macOS, Linux)
- [x] Real-time channel existence verification by `@handle`
- [x] Robust error handling for network and API exceptions

### Planned Data Extraction (Upcoming):

- [ ] Channel's name & link
- [ ] Total subscribers, views, and videos
- [ ] Date joined & location
- [ ] Latest video title & link

## Requirements ❗

- Python 3.10+
- A Google Cloud API Key with **YouTube Data API v3** enabled

## Installation & Setup 🚀

1. Clone the repository:
```bash
git clone https://github.com/iiItzSpace/youtube-channel-basic-data.git
cd youtube-channel-basic-data
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

3. Upgrade pip and install dependencies:
```bash
python -m pip install --upgrade pip
pip install google-api-python-client python-dotenv
```

4. Configure your environment variables. Create a `.env` file in the root
   directory of the project and add your API key:
```dotenv
YOUTUBE_API_KEY=your_api_key_here
```

5. Run the application:
```bash
python main.py
```

## Usage Instructions 📋

1. Launch the CLI using `python main.py`.
2. Enter the target YouTube channel handle when prompted (e.g., `mrbeast` or 
`@mrbeast`).
3. View the validation result and choose whether to query another channel 
   `(Y/n)`.

## Project Status ⚙️️

In progress ⏳ — Core API connection and CLI validation loop are complete. 
Data parsing and visual formatting are next.
