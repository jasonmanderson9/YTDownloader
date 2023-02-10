import tkinter
from tkinter import *
import sv_ttk
from tkinter import ttk
from pytube import YouTube

# GUI Properties
win = Tk()
win.iconbitmap('download.ico')
sv_ttk.set_theme("light")
win.minsize(400, 120)
win.maxsize(400, 120)
win.geometry("400x120")
win.eval('tk::PlaceWindow . center')
win.wm_title("Youtube Downloader")


# Delete temp text in form
def temp_text(e):
    video_url.delete(0, "end")


# Missing URL Error
def missing_url():
    top = Toplevel(win)
    top.iconbitmap('error.ico')
    top.minsize(400, 120)
    top.maxsize(400, 120)
    top.geometry("400x120")
    top.title("ERROR!")
    Label(top, text="ERROR: Missing Youtube URL.", font=('Arial', 12)).pack()
    ttk.Button(top, text="OK", command=top.destroy).pack(pady=20)


# Download vide function
def download_video():
    if len(video_url.get()) == 0 or video_url.get() == "Enter Youtube Video URL: ":
        missing_url()
    else:
        # Start Download
        top = Toplevel(win)
        top.title("Downloading Video...")
        top.geometry("400x200+1100+550")
        Label(top, text="Downloading Video...", font=('Arial', 12)).pack()
        yt = YouTube(video_url.get())
        ys = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
        ys.download()
        complete_label = Label(top, text="\n\nDownload Completed!!", font=('Arial', 12))
        complete_label.pack(pady=0)


# Get video URL
var = StringVar()
video_url = Entry(win, width=50, textvariable=var)
video_url.insert(0, 'Enter Youtube Video URL: ')
video_url.pack(pady=20)
video_url.bind("<FocusIn>", temp_text)

# Download Button
ttk.Button(win, text="Download", command=download_video).pack(pady=10)

win.mainloop()
