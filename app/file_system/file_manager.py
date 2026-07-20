from pathlib import Path
import shutil


class FileManager:
    """
    Handles basic file and folder operations.
    """

    def exists(self, path: str):

        return Path(path).exists()

    def create_folder(self, path: str):

        Path(path).mkdir(parents=True, exist_ok=True)

        return f"Folder created: {path}"

    def delete(self, path: str):

        p = Path(path)

        if not p.exists():

            return f"{path} does not exist."

        if p.is_file():

            p.unlink()

        else:

            shutil.rmtree(p)

        return f"Deleted: {path}"

    def rename(self, old_path: str, new_path: str):

        Path(old_path).rename(new_path)

        return f"Renamed to {new_path}"

    def copy(self, source: str, destination: str):

        shutil.copy2(source, destination)

        return f"Copied to {destination}"

    def move(self, source: str, destination: str):

        shutil.move(source, destination)

        return f"Moved to {destination}"