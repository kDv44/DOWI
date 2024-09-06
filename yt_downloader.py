import os
from pytubefix import YouTube, Playlist


def download_song(song_link: str):
    """Download a single song from YouTube."""
    try:
        yt = YouTube(song_link)
        video = yt.streams.filter(only_audio=True).first()
        if not video:
            raise ValueError("No audio stream available.")
        out_file = video.download()
        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp3"

        if os.path.exists(new_file):
            print(f"File '{new_file}' already exists.")
            os.remove(out_file)
        else:
            os.rename(out_file, new_file)
            print(f"Downloaded: '{video.title}'")

    except Exception as excep:
        print(f"Error downloading song: {excep}")


def download_playlist(playlist_link: str):
    """Download all songs from a YouTube playlist."""
    try:
        playlist = Playlist(playlist_link)

        if playlist.title not in os.listdir():
            os.mkdir(playlist.title)

            for video in playlist.videos:
                video = video.streams.filter(only_audio=True).first()
                if not video:
                    print(f"No audio stream available for {video.title}. Skipping.")
                    continue
                out_file = video.download(f"{playlist.title}")
                base, ext = os.path.splitext(out_file)
                new_file = base + ".mp3"

                if os.path.exists(new_file):
                    print(f"File '{base}' already exists.")
                    os.remove(out_file)
                else:
                    os.rename(out_file, new_file)
                    print(f"Downloaded: {video.title}")

        else:
            print(f"Directory '{playlist.title}' already exists.")

    except Exception as excep:
        print(f"Error downloading playlist: {excep}")
