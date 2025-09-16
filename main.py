import os
import time
import sys
import config
import video_utils


def main():

    # Check for the correct number of command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_your_video>")
        return

    # --- Inputs ---
    video_path = sys.argv[1]

    # --- Read configuration from config.py ---
    frame_choice = config.FRAME_CHOICE
    output_format = config.OUTPUT_IMAGE_FORMAT

    # --- Outputs ---
    output_image_path = f"extracted_frame.{output_format}"

    # --- Node Execution ---
    print(f"--- Frame Extraction Node ---")
    print(f"Input video: {os.path.basename(video_path)}")
    print(f"Frame to extract: '{frame_choice}' (from config)")

    start_time = time.time()

    success = video_utils.extract_frame_ffmpeg(video_path, output_image_path, frame_choice)

    elapsed_time = time.time() - start_time

    if success:
        print(f"Extraction completed in {elapsed_time:.2f} seconds.")
        print(f"Output image saved to: {os.path.abspath(output_image_path)}")
    else:
        print("Frame extraction failed.")


if __name__ == "__main__":
    main()
