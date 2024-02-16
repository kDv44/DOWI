import os

from rgbprint import Color, gradient_print
from pytube import YouTube, Playlist


def downloader_song(song_link: str):
    try:
        yt = YouTube(song_link)

        video = yt.streams.filter(only_audio=True).first()
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
        print("\nSomething Went Wrong Please Try Again.\n")
        print(excep)


def download_playlist(playlist_link: str):
    playlist = Playlist(playlist_link)

    try:
        if playlist.title.__str__() not in os.listdir():
            os.mkdir(playlist.title)

            for video in playlist.videos:
                video = video.streams.filter(only_audio=True).first()
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
        print("\nSomething Went Wrong Please Try Again.\n")
        print(excep)


def main():
    gradient_print(
        """
     ========================================================================   
    |          :::::::::       ::::::::     :::       :::       :::::::::::  |
    |         :+:    :+:     :+:    :+:    :+:       :+:           :+:       |
    |        +:+    +:+     +:+    +:+    +:+       +:+           +:+        |
    |       +#+    +:+     +#+    +:+    +#+  +:+  +#+           +#+         |
    |      +#+    +#+     +#+    +#+    +#+ +#+#+ +#+           +#+          |
    |     #+#    #+#     #+#    #+#     #+#+# #+#+#            #+#           |
    |    #########       ########       ###   ###         ###########        |
     ========================================================================    
    """,
        start_color=Color.pale_violet_red,
        end_color=Color.medium_purple,
    )

    while True:
        gradient_print(
            "Choose option:\n1. Download Playlist\n2. Download Single Song\n3. Exit",
            start_color=Color.pale_violet_red,
            end_color=Color.pale_violet_red,
        )
        choice = input()

        if choice == "1":
            gradient_print(
                "Enter Playlist URL: ",
                start_color=Color.pale_violet_red,
                end_color=Color.pale_violet_red,
            )
            playlist_url = input()
            download_playlist(playlist_url)

        elif choice == "2":
            gradient_print(
                "Enter song URL: ",
                start_color=Color.pale_violet_red,
                end_color=Color.pale_violet_red,
            )
            song_url = input()
            downloader_song(song_url)

        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
