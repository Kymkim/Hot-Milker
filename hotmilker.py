from moviepy.editor import *

def hotmilkify(clip1 , clip2):

    x = ImageClip(clip1).resize((640,480))
    y = ImageClip(clip2).resize((640,480))
    hotmilk = VideoFileClip("hotmilk.mp4")

    video = CompositeVideoClip(
        [
            hotmilk,
            x,

            #
            y.set_start(1.03),
            x.set_start(1.96),

            #
            y.set_start(4.09),
            x.set_start(5.03),


            y.set_start(7.15),
            x.set_start(8.8),

            y.set_start(10.21),
            x.set_start(11.15),

            y.set_start(13.27),
            x.set_start(14.06),

            y.set_start(14.21),
            x.set_start(15)

        ],
        size = (640,470)
    )

    video.set_duration(39).write_videofile("test.mp4") 