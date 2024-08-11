import moviepy.editor as mp
import random

def apply_transition(clip1, clip2):
    transition_type = random.choice(["fade", "slide", "wipe"])
    
    if transition_type == "fade":
        return mp.concatenate_videoclips([clip1.crossfadeout(1), clip2.crossfadein(1)])
    elif transition_type == "slide":
        return mp.concatenate_videoclips([clip1, clip2.set_start(clip1.duration).slide_in(1)])
    else:
        return mp.concatenate_videoclips([clip1, clip2.set_start(clip1.duration).wipe_in(1)])

def add_effects(clip):
    effect_type = random.choice(["colorx", "mirror_x"])
    
    if effect_type == "colorx":
        return clip.fx(mp.vfx.colorx, 1.5)
    elif effect_type == "mirror_x":
        return clip.fx(mp.vfx.mirror_x)

def process_video(video_path):
    video = mp.VideoFileClip(video_path)
    clips = [video.subclip(start, end) for start, end in [(0, 5), (5, 10), (10, 15)]]
    
    enhanced_clips = [add_effects(clip) for clip in clips]
    final_video = enhanced_clips[0]
    
    for i in range(1, len(enhanced_clips)):
        final_video = apply_transition(final_video, enhanced_clips[i])
    
    final_video.write_videofile("final_video.mp4", codec="libx264")

if __name__ == "__main__":
    video_path = "input_video.mp4"
    process_video(video_path)
