import os
from rgbprint import Color, gradient_print
from simple_term_menu import TerminalMenu

from yt_downloader import download_song as yt_song, download_playlist as yt_playlist
from sc_downloader import download_track as sc_track, download_playlist as sc_playlist


def main_menu():
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
            "Choose an option:",
            start_color=Color.pale_violet_red,
            end_color=Color.pale_violet_red,
        )

        options = [
            "Download YouTube Playlist",
            "Download YouTube Track",
            "Download SoundCloud Track",
            "Download SoundCloud Playlist",
            "Exit",
        ]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        if menu_entry_index == 0:
            download_menu(yt_playlist, "YouTube Playlist")

        elif menu_entry_index == 1:
            download_menu(yt_song, "YouTube Song")

        elif menu_entry_index == 2:
            download_menu(lambda url: sc_track(url, os.getcwd()), "SoundCloud Track")

        elif menu_entry_index == 3:
            download_menu(sc_playlist, "SoundCloud Playlist")

        elif menu_entry_index == 4:
            break

        else:
            print("Invalid choice. Please try again.")


def download_menu(download_function, type_name):
    while True:
        gradient_print(
            f"Enter {type_name} URL or choose an option:",
            start_color=Color.pale_violet_red,
            end_color=Color.pale_violet_red,
        )

        options = ["Enter URL", "Back"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        if menu_entry_index == 0:
            gradient_print(
                f"Enter {type_name} URL: ",
                start_color=Color.pale_violet_red,
                end_color=Color.pale_violet_red,
            )
            url = input()
            try:
                download_function(url)
            except Exception as e:
                print(f"Failed to download {type_name.lower()}: {e}")

        elif menu_entry_index == 1:
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
