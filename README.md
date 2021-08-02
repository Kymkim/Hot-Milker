# Hot-Milker
A script made to generate Hot Milk meme from two images.

# Before u go:
1. Make sure u have Python
2. Make sure u have MediaPy

# How to use:

1. Import it to your python script. Call the only function ```hotmilkify()```
2. Profit

Example
```python
#imports hotmilker
import hotmilker

#Asks the susers the images
clip1 = input("Image 1: ")
clip2 = input("Image 2: ")

#Profit
hotmilker.hotmilkify(img_1, img_2)
```

# A manual... I guess
## hotmilkify(img_1, img_2, **kwargs)
### set_offset = int
Changes the audio offset. .8 by default.

```python
#Example: Changes the offset to 1
hotmilker.hotmilkify("not-sussus-amogus.png", "impostersus.png", set_offset = 1)
```

### set_resize = int
Changes the resize type. The other one sucks, the other one dosent. Planning to add more functionality in the far future. NONE by default
```python
#Example: Changes the resize mode to square.
#   1 = square
#   NONE = no resize
hotmilker.hotmilkify("not-sussus-amogus.png", "impostersus.png", set_resize = 1)
```

### set_fps = int
Changes the FPS. Too high value will tremendously increase the render time. 20 by default
```python
#Example: Changes the FPS to 60
hotmilker.hotmilkify("not-sussus-amogus.png", "impostersus.png", set_fps = 60)
```

### custom_dimensions = (width, height)
Changes the dimensions in (width, height) format. Too high value will tremendously increase the rendertime. (800, 800) by default
```python
#Example: Changes the dimensions to 1980x1080
hotmilker.hotmilkify("not-sussus-amogus.png", "impostersus.png", custom_dimesions = (1980,1080))
```

### output_location = path/to/file
Changes the location of the output. Same location as where the script is located by default
```python
#Example: Changes the output location to /imposter/vent/
hotmilker.hotmilkify("not-sussus-amogus.png", "impostersus.png", output_location = "/imposter/vent/")
```

# All music credits goes to Ujico*/Snails house
[Youtube](https://www.youtube.com/user/loudnessfete)
[Spotify](https://open.spotify.com/artist/29O9ZebFa65aIEvMaW5pQY?si=zQ1XNIuFQAC5gXAinXYXgQ&dl_branch=1)
