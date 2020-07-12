# !conda install moviepy
import glob
import moviepy
import moviepy.editor as mpy

gif_name = 'type_token_ratio'
fps = 12
file_list = glob.glob('kmeans_gif/text/*.png') # Get all the pngs in the current directory
list.sort(file_list, key=lambda x: int(x.split('_')[2].split('_')[1]))
clip = mpy.ImageSequenceClip(file_list, fps=fps)
clip.write_gif('{}.gif'.format(gif_name), fps=fps)
