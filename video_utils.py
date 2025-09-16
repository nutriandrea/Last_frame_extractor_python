# video_utils.py

import subprocess
import os
import mimetypes


def is_video_file(file_path):
    """Checks if a file is a valid video based on its MIME type."""
    if not os.path.exists(file_path):
        print(f"Error: File not found at '{file_path}'")
        return False

    mime_type, _ = mimetypes.guess_type(file_path)

    if mime_type and mime_type.startswith('video/'):
        return True
    else:
        print(f"Error: '{os.path.basename(file_path)}' does not appear to be a valid video file.")
        return False


def extract_frame_ffmpeg(video_path, output_path, frame_choice):

    if not is_video_file(video_path):
        return False

    if frame_choice == 'first':
        # Command to extract the very first frame
        command = ['ffmpeg', '-i', video_path, '-vframes', '1', '-y', output_path]
    elif frame_choice == 'last':
        # Command to seek to the end and extract the last frame
        command = ['ffmpeg', '-sseof', '-1', '-i', video_path, '-frames:v', '1', '-q:v', '2', '-y', output_path]
    else:
        # This case should not be reached if validation is done in main.py
        print(f"Internal Error: Invalid frame_choice '{frame_choice}'.")
        return False

    try:
        subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running FFmpeg: {e.stderr.decode()}")
        return False
