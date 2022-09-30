import tkinter as tk
from tkinter import ttk
from pytube import YouTube


# root window
root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title('YouTube Video Downloader')

SAVE_PATH = os.path.expanduser("~/Desktop/Video")

# store email address and password
link = tk.StringVar()


def on_progress(vid, chunk, bytes_remaining):
    total_size = vid.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    totalsz = (total_size/1024)/1024
    totalsz = round(totalsz,1)
    remain = (bytes_remaining / 1024) / 1024
    remain = round(remain, 1)
    dwnd = (bytes_downloaded / 1024) / 1024
    dwnd = round(dwnd, 1)
    percentage_of_completion = round(percentage_of_completion,2)
    print(f'Download Progress: {percentage_of_completion}%, Total Size:{totalsz} MB, Downloaded: {dwnd} MB, Remaining:{remain} MB')


def login_clicked():
    global video
    """ callback when the login button clicked
    """
    yt = YouTube(link.get(), on_progress_callback=on_progress)
    video = yt.streams.get_highest_resolution()
    video.download(SAVE_PATH)


# Sign in frame
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10, fill='x', expand=True)


# email
email_label = ttk.Label(frame, text="Video Link")
email_label.pack(fill='x', expand=True)

email_entry = ttk.Entry(frame, textvariable=link)
email_entry.pack(fill='x', expand=True)


# login button
download_button = ttk.Button(frame, text="Download", command=login_clicked)
download_button.pack(fill='x', expand=True, pady=10)


root.mainloop()
