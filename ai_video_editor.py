from video_processing import detect_scenes, split_video
from subtitle_generator import generate_subtitles, extract_audio
from video_enhancement import enhance_video
from transitions_and_effects import process_video

def main(video_path):
    # Step 1: Enhance video quality
    print("Enhancing video quality...")
    enhance_video(video_path)

    # Step 2: Detect scenes and split video
    print("Detecting scenes and splitting video...")
    scenes = detect_scenes("enhanced_video.mp4")
    split_video("enhanced_video.mp4", scenes)

    # Step 3: Generate subtitles
    print("Generating subtitles...")
    audio_path = extract_audio(video_path)
    subtitles = generate_subtitles(audio_path)
    print("Subtitles:\n", subtitles)

    # Step 4: Apply transitions and effects
    print("Applying transitions and effects...")
    process_video("enhanced_video.mp4")

if __name__ == "__main__":
    video_path = "input_video.mp4"
    main(video_path)
