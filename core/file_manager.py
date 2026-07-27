from pathlib import Path
# from datetime import datetime


class FileManager:
    def __init__(self):
        self.base_path = Path(__file__).resolve().parent.parent
        self.folders = [
            self.base_path / "logs",
            self.base_path / "config",
            self.base_path / "reports",
        ]

    def create_structure(self):
        """
        Create the necessary folder structure for the application if not exists
        """
        for folder in self.folders:
            folder.mkdir(parents=True, exist_ok=True)

    def get_path(self, folder: str) -> Path:
        try:
            if folder not in self.folders:
                raise ValueError(f"Folder '{folder}' is not a valid folder.")
            return self.base_path / folder
        except ValueError as error:
            """
            To-do: Implement logging for this exception.
            """
            print(error)
            return None

    def create_path():
        pass


if __name__ == "__main__":
    test = FileManager()
    test.get_path("logsss")
