import json
import glob


class SaveSystem:
    def __init__(self, game):
        self.game = game

    def save(self, save_name):
        if save_name == "list":
            print("Save name 'list' is reserved, please choose a different save name.")
            return
        pass

    def load(self, save_name):
        pass

    @staticmethod
    def get_save_names(self):
        return [name.split(".")[0] for name in glob.glob("*.json")]
