import cv2
import numpy as np
from moviepy.editor import VideoFileClip

def enhance_frame(frame):
    # Apply a denoising filter
    denoised = cv2.fastNlMeansDenoisingColored(frame, None, 10, 10, 7, 21)
    
    # Apply a sharpening filter
    kernel = np.array([[0, -1, 0], [-1, 5,-1], [0, -1, 0]])
    sharpened = cv2.filter2D(denoised, -1, kernel)
    
    return sharpened

def enhance_video(video_path):
    video = VideoFileClip(video_path)
    enhanced_frames = [enhance_frame(frame) for frame in video.iter_frames()]
    
    enhanced_video = VideoFileClip(video_path).set_frames(enhanced_frames)
    enhanced_video.write_videofile("enhanced_video.mp4", codec="libx264")

if __name__ == "__main__":
    video_path = "input_video.mp4"
    enhance_video(video_path)
