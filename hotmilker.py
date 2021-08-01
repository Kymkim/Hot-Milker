from moviepy.editor import *

hotmilk = VideoFileClip("hotmilk.mp4")

#hotmilkify(img_1, img_2, set_resizeType = 1/None, set_offset = ANY REASONABLE INT, set_fps = AGAIN, ANY REASONABLE INT, custom_dimensions = (Width, Length), output_location = File/Path/Some)
def hotmilkify(img_1, img_2, **kwargs):

    offset = kwargs.get('set_offset', .8)
    resizeType = kwargs.get('set_resize', None)
    sfps = kwargs.get('set_fps', 20)
    dimensions = kwargs.get('custom_dimensions', (800,800))
    output_location = kwargs.get('output_location', "output.mp4")

    #Resize options:
    #   1 = Squeezes the image
    #   NONE = Literally nothing happens
    if resizeType == 1:
        x = ImageClip(img_1).resize((800,800))
        y = ImageClip(img_2).resize((800,800))
    else:
        x = ImageClip(img_1)
        y = ImageClip(img_2)

    # Generates the image transitions
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

    video = CompositeVideoClip(clips,size = dimensions)

    video.set_duration(28).write_videofile(output_location, fps=sfps) 