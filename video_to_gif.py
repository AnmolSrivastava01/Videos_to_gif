from moviepy.editor import *
video=VideoFileClip("location of video").subclip(00,5)#.rotate(180)
video.write_gif("test1.gif")
#u can also rotate the gif of u want through rotate(degree) 
