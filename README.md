---

# YouTube Converter Scripts

## Overview

This repository contains two Python scripts for converting YouTube videos into audio and video files. The first script downloads audio from a YouTube video and converts it to MP3 format. The second script downloads the highest resolution video available.

## Prerequisites

Before using these scripts, ensure you have the following installed:

- Python 3.x
- `pytube` - for downloading videos from YouTube
- `pydub` - for audio processing
- `requests` - for HTTP requests
- `ffmpeg` - for audio format conversion (required by `pydub`)

You can install the necessary Python packages using pip:

```bash
pip install pytube pydub requests
```

You can download and install `ffmpeg` from [FFmpeg's official website](https://ffmpeg.org/download.html).

## Scripts

### 1. Audio Converter

This script downloads audio from a YouTube video and converts it to MP3 format.

#### Usage

```bash
python audio_converter.py <YouTube_URL>
```

#### Script Details

- **Imports**:
  - `pytube` for downloading YouTube videos
  - `sys` for command-line arguments
  - `pathlib` for handling file paths
  - `requests` for API requests
  - `re` for regular expression matching
  - `pydub` for audio format conversion
  - `os` for file operations

- **Functionality**:
  - Verifies if the provided URL is a valid YouTube link
  - Downloads the audio stream from the video
  - Converts the downloaded audio file to MP3 format

### 2. Video Converter

This script downloads the highest resolution video from a YouTube URL.

#### Usage

```bash
python video_converter.py <YouTube_URL>
```

#### Script Details

- **Imports**:
  - `pytube` for downloading YouTube videos
  - `sys` for command-line arguments
  - `pathlib` for handling file paths
  - `requests` for API requests
  - `re` for regular expression matching

- **Functionality**:
  - Verifies if the provided URL is a valid YouTube link
  - Downloads the highest resolution video available

## Files

- `audio_converter.py` - Python script for converting YouTube videos to MP3.
- `video_converter.py` - Python script for downloading the highest resolution video from YouTube.

## Notes

- Ensure that you provide a valid YouTube URL in the command-line argument.
- The downloaded files will be saved in your system's "Downloads" directory.

## Troubleshooting

- If you encounter issues with `ffmpeg`, make sure it is installed and properly configured in your system's PATH.
- Ensure you have a stable internet connection for downloading videos.

---
