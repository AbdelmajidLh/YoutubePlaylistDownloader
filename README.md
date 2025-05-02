# 🎬 YoutubePlaylistDownloader

Outil Python en ligne de commande pour télécharger automatiquement des **playlists YouTube** complètes, avec gestion de la qualité, configuration personnalisable, journalisation et structure modulaire.

> ✅ Basé sur [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) — puissant, moderne et maintenu.

---

## 🚀 Fonctionnalités

- 🔽 Télécharge une **playlist YouTube complète**
- 🎚️ Téléchargement en **haute** ou **basse** qualité (`high` / `low`)
- 📁 Sauvegarde dans un dossier configurable
- 🧠 Structure Python **OOP et modulaire**
- 📜 Logging automatique dans `app.log`
- ⚙️ Configurable via `config.json`
- 💡 Fonctionne sous Windows, Linux et macOS
- 📦 Installation simple via `pyproject.toml`

---

## 🧱 Structure du projet

```
YoutubePlaylistDownloader/
├── main.py
├── config.json
├── pyproject.toml
├── README.md
├── .gitignore
├── youtube_downloader/
│   ├── config.py
│   ├── downloader.py
│   ├── logger.py
│   ├── playlist.py
│   ├── video.py
├── scripts/
│   ├── run.sh
│   └── run.bat
```

---

## ⚙️ Configuration utilisateur

Fichier `config.json` :

```json
{
  "quality": "high",
  "download_path": "./downloads"
}
```

- `quality`: `"high"` ou `"low"`
- `download_path`: dossier cible

---

## 📦 Installation

### Prérequis :
- Python ≥ 3.7
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) (installé automatiquement)
- (Recommandé) [ffmpeg](https://ffmpeg.org/download.html) pour fusionner audio/vidéo

### Étapes :

#### 🖥️ Linux / macOS
```bash
git clone https://github.com/<ton_user>/YoutubePlaylistDownloader.git
cd YoutubePlaylistDownloader
chmod +x scripts/run.sh
./scripts/run.sh
```

#### 🪟 Windows
```bat
git clone https://github.com/<ton_user>/YoutubePlaylistDownloader.git
cd YoutubePlaylistDownloader
scripts\run.bat
```

---

## 🧪 Utilisation

1. Lancer le script via `main.py` ou la commande `yt-download` si installée.
2. Saisir l’URL de la playlist YouTube (format : `https://www.youtube.com/playlist?list=...`).
3. Les vidéos seront téléchargées dans le dossier défini.

---

## 🧰 Dépendances principales

- [`yt-dlp`](https://github.com/yt-dlp/yt-dlp)
- Python standard library
- `ffmpeg` (facultatif mais recommandé)

---

## 📜 Licence

Ce projet est sous licence **MIT**. Voir [LICENSE](LICENSE).

---

## 🔍 Mots-clés (SEO)

```
youtube downloader, yt-dlp, playlist downloader, python project, video download, cli, mp4, audio, open source, script youtube, batch youtube, ffmpeg, OOP
```

---

## 👤 Auteur

Développé par **Abdelmajid** – [GitHub](https://github.com/<ton_user>)

---

## 🌟 Contributions

Les PR sont les bienvenues. Si vous avez une amélioration, ouvrez une *issue* ou soumettez un *pull request*.
