# Video Frame Extractor

A simple Python tool for extracting specific frames from video files using FFmpeg.[1]

## Overview

This project allows you to extract a single frame from a video file by specifying which frame to extract through configuration. The tool leverages FFmpeg for video processing and saves the extracted frame as an image in your desired format.[1]

## Features

- **Configurable frame extraction**: Specify which frame to extract via configuration file
- **Multiple output formats**: Support for various image output formats (JPG, PNG, BMP, etc.)
- **Performance tracking**: Monitor processing time for each extraction
- **Simple CLI interface**: Easy-to-use command line interface with minimal parameters
- **Error handling**: Robust error handling during frame extraction process

## Prerequisites

- **Python 3.x**
- **FFmpeg** installed and accessible from system PATH

### Installing FFmpeg

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

**Windows:**
Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH.[2]

## 📁 Project Structure

```
video-frame-extractor/
├── main.py              # Main script
├── config.py```         # Configuration file
├── video_utils```       # Video processing utilities
└── README```            # This file
```

## Configuration

Create a `config.py` file with the following variables:

```python
# Frame to extract (e.g., "00```:10" for 10 seconds,```" for first frame)```AME_CHOICE = "00:00:05```# Output image format
OUTPUT_IMAGE```RMAT = "jpg"
```

## Usage

```bash
python main.py <path_to_video>
```

### Example

```bash
python main.py /path/to/your/video.mp4
```

The extracted frame will be saved as `extracted_frame.jpg` (or your specified format from config.py) in the current directory.[1]

## Output

- **Image file**: `extracted_frame.{format}` in the execution directory
- **Console logs**: Progress information, processing time, and output path

Example output:
```
--- Frame Extraction Node ---
Input video: example```deo.mp4
Frame to extract: '```00:05' (from config)```traction completed in 1``` seconds.
Output```age saved to: /full/path/to/extracted_frame```g
```

## Configuration Options

### Modifying Frame Selection
Edit `FRAME_CHOICE` in `config.py`:
- **Specific time**: `"00:01:30"` (1 minute and 30 seconds)
- **Frame number**: `"1"` (first frame)
- **Percentage**: `"25%"` (25% through the video)

### Changing Output Format
Modify `OUTPUT_IMAGE_FORMAT` in `config.py`:
- Supported formats: `"jpg"`, `"png"`, `"bmp"`, `"tiff"`, etc.[3]

## Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Requirements

### Dependencies
- **Python Standard Library**: `os`, `time`, `sys`
- **FFmpeg**: For video processing
- **Custom modules**: `config.py`, `video_utils.py`


## License

This project is licensed under the MIT License. See the `LICENSE` file for details.[4]

## Troubleshooting

- **FFmpeg not found**: Ensure FFmpeg is installed and added to your system PATH
- **Module not found**: Verify that `config.py` and `video_utils.py` exist in the same directory
- **Permission errors**: Check file permissions for the video file and output directory

