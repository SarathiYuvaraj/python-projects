
import moviepy.editor

from tkinter.filedialog import *

file=askopenfilename()
video=moviepy.editor.VideoFileClip(file)
audio=video.audio

audio.write_audiofile("demo.mp3")
print("done")