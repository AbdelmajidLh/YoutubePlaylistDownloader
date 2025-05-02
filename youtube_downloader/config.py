import json

class UserConfig:
    def __init__(self, path="config.json"):
        self.path = path
        self.data = self.load()

    def load(self):
        with open(self.path, "r") as f:
            return json.load(f)

    def get_quality(self):
        return self.data.get("quality", "high")

    def get_download_path(self):
        return self.data.get("download_path", "./downloads")
