import time
import os
from pathlib import Path
import sys
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
from main.logger_config import log

work_dir = Path(__file__).resolve().parent


class ThemeChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith(".scss"):
            log.info(f"Detected change in {event.src_path}. Running compiler.py...")
            try:
                # Use sys.executable to ensure the current Python interpreter is used
                build_py_path = os.path.join(work_dir, "build.py")
                log.info(f"Builder path: {build_py_path}")
                subprocess.run([sys.executable, build_py_path], check=True)
                src = os.path.join(work_dir, "style", "icons")
                dest = os.path.join(
                    work_dir,
                    "ui",
                    "icons",
                )
                log.info(f"Copying icons from {src} to {dest}...")
                if not os.path.exists(dest):
                    os.makedirs(dest)
                shutil.copytree(src, dest, dirs_exist_ok=True)
                log.info(f"Copied {src} to {dest}")
            except Exception as e:
                log.error(f"Error: {e}")


def monitor():
    style_folder = Path(work_dir, "style")
    if not style_folder.exists():
        print(f"Theme directory {style_folder} does not exist.")
        return

    event_handler = ThemeChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, str(style_folder), recursive=True)

    log.info(f"Watching for changes in {style_folder}...")
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    monitor()
