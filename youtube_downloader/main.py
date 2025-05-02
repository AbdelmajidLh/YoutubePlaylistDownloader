from youtube_downloader.config import UserConfig
from youtube_downloader.playlist import YouTubePlaylist
from youtube_downloader.downloader import Downloader
from youtube_downloader.logger import setup_logger

def main():
    logger = setup_logger()
    logger.info("Lancement du téléchargement de playlist YouTube")
    config = UserConfig()
    url = input("URL de la playlist YouTube : ").strip()
    # Supprime les paramètres inutiles (feature=shared, etc.)
    if "&" in url:
        url = url.split("&")[0]
    playlist = YouTubePlaylist(url, config.get_quality())
    downloader = Downloader(config, playlist, logger)
    downloader.run()
    logger.info("Téléchargement terminé.")

if __name__ == "__main__":
    main()
