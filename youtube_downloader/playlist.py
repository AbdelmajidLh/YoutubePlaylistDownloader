import yt_dlp

from youtube_downloader.video import YouTubeVideo

class YouTubePlaylist:
    def __init__(self, playlist_url, quality):
        self.playlist_url = playlist_url
        self.quality = quality
        self.video_urls = self._extract_urls()

    def _extract_urls(self):
        ydl_opts = {'quiet': True, 'extract_flat': True, 'dump_single_json': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(self.playlist_url, download=False)
            return [entry['url'] for entry in info['entries']]

    def get_videos(self):
        return [YouTubeVideo(url, self.quality) for url in self.video_urls]
