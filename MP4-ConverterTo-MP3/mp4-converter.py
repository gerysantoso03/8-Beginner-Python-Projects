from moviepy import editor

video = editor.VideoFileClip('yesterday.mp4')
audio = video.audio
audio.write_audiofile('yesterday.mp3')