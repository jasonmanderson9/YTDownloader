from pytube import YouTube
from tqdm import tqdm


class BColors:
    textcolor = '\033[94m'


print(BColors.textcolor, (("""\

 __     __         _         _            _____                      _                 _           
 \ \   / /        | |       | |          |  __ \                    | |               | |          
  \ \_/ /__  _   _| |_ _   _| |__   ___  | |  | | _____      ___ __ | | ___   __ _  __| | ___ _ __ 
   \   / _ \| | | | __| | | | '_ \ / _ \ | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
    | | (_) | |_| | |_| |_| | |_) |  __/ | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   
    |_|\___/ \__,_|\__|\__,_|_.__/ \___| |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   
    
""")))

video_url = input("Enter The URL of A Youtube Video: ")
yt = YouTube(str(video_url))
views = ('{:,}'.format(yt.views))
print("Title: " + "'" + yt.title + '\n' + "Autor: " + str(yt.author) + '\n' + "Views: " + str(views) + '\n\n' + "Would you like to download the video?" + '\n' + "1.) Yes" + '\n' + "2.) No")

option = input("Please choose an option: ")

if int(option) == 1:
    print('\n'"Downloading Video..."'\n')
    for i in tqdm(range(100), colour="blue"):
        ys = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
        ys.download()
    print('\n'"Video Download Completed!!")
else:
    exit(0)
