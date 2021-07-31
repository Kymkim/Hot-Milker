from moviepy.editor import *

def hotmilkify(clip1 , clip2):

    x = ImageClip(clip1).resize((800,800))
    y = ImageClip(clip2).resize((800,800))
    hotmilk = VideoFileClip("hotmilk.mp4")
    offset = .8

    clips = [hotmilk,x]

    i = 0
    while (i < 16):
        clips.append(y.set_start(offset*(2+i)))
        clips.append(x.set_start(offset*(3+i)))
        i += 4

    i = 0
    while (i < 32):
        clips.append(y.set_start((35+i)*(offset/2)))
        clips.append(x.set_start((36+i)*(offset/2)))
        i += 2

    video = CompositeVideoClip(clips,size = (800,800))

    video.set_duration(29).write_videofile("test.mp4", fps=20) 