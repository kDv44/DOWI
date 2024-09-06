import os
import yt_dlp as ytdlp
from pydub import AudioSegment


def convert_to_mp3(file_path: str):
    mp3_path = os.path.splitext(file_path)[0] + '.mp3'
    try:
        audio = AudioSegment.from_file(file_path)
        audio.export(mp3_path, format='mp3')
        os.remove(file_path)
        print(f"Converted '{file_path}' to MP3.")
    except Exception as e:
        print(f"Error converting file to MP3: {e}")


def download_track(track_url: str, output_path: str):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'quiet': False
        }

        with ytdlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(track_url, download=True)
            file_path = ydl.prepare_filename(info_dict)

            if not file_path.endswith('.mp3'):
                print(f"Converting '{file_path}' to MP3...")
                convert_to_mp3(file_path)
            else:
                print(f"Downloaded '{info_dict.get('title')}' as MP3.")

    except Exception as excep:
        print(f"Error downloading track: {excep}")


def download_playlist(playlist_url: str):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'quiet': False
        }

        with ytdlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(playlist_url, download=False)
            if 'entries' in info_dict:
                playlist_title = info_dict.get('title', 'playlist')

                playlist_dir = playlist_title
                if not os.path.exists(playlist_dir):
                    os.mkdir(playlist_dir)

                ydl_opts['outtmpl'] = os.path.join(playlist_dir, '%(title)s.%(ext)s')

                ydl_opts['quiet'] = False
                with ytdlp.YoutubeDL(ydl_opts):
                    entries = info_dict['entries']
                    for entry in entries:
                        track_url = entry['url']
                        download_track(track_url, playlist_dir)

                print(f"Downloaded and processed all tracks in playlist '{playlist_title}'.")

    except Exception as excep:
        print(f"Error downloading playlist: {excep}")
