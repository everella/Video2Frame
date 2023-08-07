import cv2
import os
import tkinter as tk
from tkinter import filedialog

def create_frames(video_path, output_folder):
    # Check if the output folder exists, if not, create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Get the frames per second (fps) of the video
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Initialize frame count
    frame_count = 0

    while True:
        # Read a frame from the video
        ret, frame = cap.read()

        # Break the loop if no more frames are available
        if not ret:
            break

        # Save the frame as an image file
        frame_path = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(frame_path, frame)

        # Print progress
        print(f"Extracting frame {frame_count}")

        # Increment frame count
        frame_count += 1

    # Release the video capture object
    cap.release()
    print("Frames extraction complete.")

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi;*.mkv")])
    if file_path:
        output_folder = "frames_output"
        create_frames(file_path, output_folder)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    print("Select a video file using the file explorer.")
    select_file()
