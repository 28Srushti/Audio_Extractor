import moviepy.editor

cvt_video = moviepy.editor.VideoFileClip(r"C:\Users\srush_ifj2ky2\OneDrive\Documents\Projects\Left and Right.mp4") #Using / in python is not support.Solution is use r,/ or \\

ext_audio = cvt_video.audio

ext_audio.write_audiofile(r"C:\Users\srush_ifj2ky2\OneDrive\Documents\Projects\audio_extractors.mp3")
