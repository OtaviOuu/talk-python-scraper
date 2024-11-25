# Talk Python Training Video Scraper

A Python script for downloading video courses from [Talk Python Training](https://training.talkpython.fm). This tool automatically organizes downloaded content by course, module, and lecture.

## Features

- Automatic course discovery from your account
- Downloads videos in .webm format at 720p resolution
- Organizes content in a structured folder hierarchy
- Progress bar for download tracking
- Maintains original course structure
- Handles authentication via cookies

## Prerequisites

- Python 3.6+
- Valid Talk Python Training subscription
- Modern web browser for cookie extraction

## Installation

1. Clone the repository:
```bash
git clone https://github.com/OtaviOuu/talk-python-scraper
cd talk-python-scraper
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

1. Create a `.env` file in the project root:
```bash
cp .env.example .env
```

2. Get your authentication cookie:
   - Go to https://training.talkpython.fm/courses/all
   - Open Developer Tools (F12 or right-click -> Inspect)
   - Navigate to the Network tab
   - Refresh the page
   - Find and click on the "all" request
   - In the Headers section, find "Request Headers"
   - Copy the entire cookie value
   - Paste it into your `.env` file

Example `.env` file:
```
COOKIE=your_cookie_value_here
```

## Project Structure

```
talk-python-scraper/
├── src/
│   └── main.py
├── .env.example
├── .env
├── requirements.txt
└── README.md
```

## Usage

Run the script from the project root:

```bash
python3 src/main.py
```

Downloaded content will be organized as follows:

```
talk-python/
├── Course Name 1/
│   ├── Module 1/
│   │   ├── 1 - Lecture Name/
│   │   │   └── video.webm
│   │   └── 2 - Lecture Name/
│   │       └── video.webm
│   └── Module 2/
│       └── ...
└── Course Name 2/
    └── ...
```

## Dependencies

- requests: For making HTTP requests
- selectolax: For HTML parsing
- tqdm: For progress bar display
- python-dotenv: For environment variable management

## Important Notes

- This script requires a valid Talk Python Training subscription
- Cookie authentication expires periodically - you may need to update the cookie value
- Be mindful of your storage space - video courses can be large
- Respect Talk Python Training's terms of service and use this tool responsibly
- Download speeds may vary based on your internet connection

## Troubleshooting

1. If you get authentication errors:
   - Verify your cookie is correctly copied
   - Make sure your subscription is active
   - Try getting a new cookie value

2. If downloads fail:
   - Check your internet connection
   - Verify you have sufficient disk space
   - Ensure the cookie is still valid

## Legal Notice

This tool is for personal use only. Respect Talk Python Training's terms of service and copyright policies. Do not distribute downloaded content.
