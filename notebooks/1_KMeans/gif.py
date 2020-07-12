# !pip3 install moviepy
import glob
import moviepy
import moviepy.editor as mpy

gif_name = 'type_token_ratio'
fps = 3
file_list = glob.glob('../0_preprocessing/*.png') # Get all the pngs in the current directory
print(file_list)
list.sort(file_list, key=lambda x: int(x.split('/')[2].split('_')[0]))
clip = mpy.ImageSequenceClip(file_list, fps=fps)
clip.write_gif('{}.gif'.format(gif_name), fps=fps)


