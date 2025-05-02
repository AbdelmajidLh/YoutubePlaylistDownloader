import os
import time

class Downloader:
    def __init__(self, config, playlist, logger):
        self.config = config
        self.playlist = playlist
        self.logger = logger

    def run(self):
        path = self.config.get_download_path()
        os.makedirs(path, exist_ok=True)
        for video in self.playlist.get_videos():
            try:
                
                title = video.get_title()
                self.logger.info(f"Téléchargement : {title}")
                video.download(path)
                time.sleep(1)
            except Exception as e:
                self.logger.error(f"Échec pour {video.url} : {e}")
