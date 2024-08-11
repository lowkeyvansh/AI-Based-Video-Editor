import cv2
import numpy as np
from moviepy.editor import VideoFileClip

def detect_scenes(video_path, threshold=30):
    cap = cv2.VideoCapture(video_path)
    scenes = []
    prev_frame = None
    frame_number = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if prev_frame is not None:
            diff = cv2.absdiff(frame, prev_frame)
            non_zero_count = np.count_nonzero(diff)

            if non_zero_count > threshold:
                scenes.append(frame_number)

        prev_frame = frame
        frame_number += 1

    cap.release()
    return scenes

def split_video(video_path, scenes):
    video = VideoFileClip(video_path)
    for i, scene in enumerate(scenes):
        start = scene / video.fps
        end = scenes[i + 1] / video.fps if i + 1 < len(scenes) else video.duration
        clip = video.subclip(start, end)
        clip.write_videofile(f"scene_{i + 1}.mp4", codec="libx264")

if __name__ == "__main__":
    video_path = 'input_video.mp4'
    scenes = detect_scenes(video_path)
    split_video(video_path, scenes)
