import yt_dlp

class YouTubeVideo:
    def __init__(self, url, quality="best"):
        self.url = url
        self.quality = quality

    def download(self, output_path):
        format_code = "bestvideo*+bestaudio/best" if self.quality == "high" else "worst"

        ydl_opts = {
            'format': format_code,
            'outtmpl': f'{output_path}/%(title).70s.%(ext)s',  # tronque nom à 70 caractères
            'quiet': True,
            'noplaylist': True,
            'merge_output_format': 'mp4',
            'ignoreerrors': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.url])

    def get_title(self):
        ydl_opts = {'quiet': True, 'skip_download': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(self.url, download=False)
            return info.get("title", self.url)
