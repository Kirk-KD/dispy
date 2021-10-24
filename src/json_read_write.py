import json


class JSONReadWrite:
    def __init__(self, save_dir: str):
        self.data = {}
        self.save_dir = save_dir

    def save(self):
        with open(self.save_dir, "w") as f:
            json.dump(self.data, f, indent=4)

    def add_event(self, event):
        self.data[hash(event)] = event.json()
        self.save()
